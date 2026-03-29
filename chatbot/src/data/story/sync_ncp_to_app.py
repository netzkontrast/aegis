#!/usr/bin/env python3
"""
Syncs the Narrative Coherence Protocol (NCP) data and manuscript content
to the Chatbot application's data directory.

This script performs two main tasks:
1. Copies the master NCP JSON to `chatbot/src/data/story/ncp_full.json`.
2. Parses manuscript files (Markdown with YAML frontmatter) and generates per-chapter JSON snippets in `chatbot/src/data/story/snippets/`.
"""

import os
import json
import re
import shutil
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).parent.parent.parent.parent
NCP_SOURCE = REPO_ROOT / "skills/narrative_design/ncp/kohaerenz_protokoll.ncp.json"
MANUSCRIPT_ROOT = REPO_ROOT / "kohaerenz_protokoll/manuscript"
APP_DATA_DIR = REPO_ROOT / "chatbot/src/data/story"
SNIPPETS_DIR = APP_DATA_DIR / "snippets"

def parse_frontmatter(content):
    """
    Parses YAML frontmatter from a markdown string using regex.
    Returns a dictionary of metadata and the remaining content.
    """
    frontmatter_regex = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
    match = frontmatter_regex.match(content)

    metadata = {}
    body = content

    if match:
        yaml_block = match.group(1)
        body = content[match.end():]

        # Simple line-by-line parsing for key: value
        for line in yaml_block.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip().strip('"').strip("'")

    return metadata, body.strip()

def sync_ncp_json():
    """Copies the master NCP JSON to the app data directory."""
    if not NCP_SOURCE.exists():
        print(f"Error: NCP source file not found at {NCP_SOURCE}")
        return

    APP_DATA_DIR.mkdir(parents=True, exist_ok=True)
    destination = APP_DATA_DIR / "ncp_full.json"

    try:
        shutil.copy2(NCP_SOURCE, destination)
        print(f"Successfully copied NCP JSON to {destination}")
    except Exception as e:
        print(f"Failed to copy NCP JSON: {e}")

def generate_chapter_snippets():
    """Scans manuscript files and generates per-chapter JSON snippets."""
    SNIPPETS_DIR.mkdir(parents=True, exist_ok=True)

    chapters = {}

    # Iterate through act directories
    for act_dir in sorted(MANUSCRIPT_ROOT.glob("act_*")):
        if not act_dir.is_dir():
            continue

        print(f"Processing {act_dir.name}...")

        for md_file in sorted(act_dir.glob("*.md")):
            try:
                content = md_file.read_text(encoding='utf-8')
                metadata, body = parse_frontmatter(content)

                # Extract chapter/scene info from filename if not in metadata
                # Filename format: chapter_XX_scene_YY.md
                match = re.match(r"chapter_(\d+)_scene_(\d+)", md_file.stem)

                chapter_num = metadata.get('chapter')
                scene_id = metadata.get('scene_id')

                if match:
                    if not chapter_num:
                        chapter_num = int(match.group(1))
                    if not scene_id:
                        scene_id = match.group(2)

                if chapter_num is None:
                    print(f"Warning: Could not determine chapter for {md_file.name}")
                    continue

                chapter_key = f"chapter_{int(chapter_num):02d}"

                if chapter_key not in chapters:
                    chapters[chapter_key] = {
                        "chapter": int(chapter_num),
                        "scenes": []
                    }

                chapters[chapter_key]["scenes"].append({
                    "scene_id": scene_id,
                    "title": metadata.get('title', 'Untitled'),
                    "content": body,
                    "metadata": metadata
                })

            except Exception as e:
                print(f"Error processing {md_file.name}: {e}")

    # Write chapter JSONs
    for chapter_key, data in chapters.items():
        # Sort scenes by ID
        data["scenes"].sort(key=lambda x: x["scene_id"] if x["scene_id"] else "")

        output_file = SNIPPETS_DIR / f"{chapter_key}.json"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Generated {output_file.name}")
        except Exception as e:
            print(f"Failed to write {output_file.name}: {e}")

def main():
    print("Starting data synchronization...")
    sync_ncp_json()
    generate_chapter_snippets()
    print("Synchronization complete.")

if __name__ == "__main__":
    main()
