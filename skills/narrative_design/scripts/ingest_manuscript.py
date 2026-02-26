import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional
import yaml  # PyYAML

DEFAULT_NCP_PATH = Path(__file__).parent.parent / 'ncp' / 'kohaerenz_protokoll.ncp.json'
MANUSCRIPT_ROOT = Path('kohaerenz_protokoll/manuscript')

# Regex for standard scene filenames: chapter_XX_scene_YY.md
SCENE_PATTERN = re.compile(r'chapter_(\d+)_scene_(\d+)(?:_(.+))?\.md')

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Updated {path}")

def parse_frontmatter(content):
    if content.startswith('---'):
        try:
            parts = content.split('---', 2)
            if len(parts) >= 3:
                return yaml.safe_load(parts[1])
        except Exception as e:
            print(f"Error parsing frontmatter: {e}")
    return {}

def scan_manuscript(root: Path):
    found_scenes = []

    for root_dir, _, files in os.walk(root):
        for file in files:
            if not file.endswith('.md'):
                continue

            match = SCENE_PATTERN.match(file)
            if match:
                chapter_num = int(match.group(1))
                scene_num = int(match.group(2)) # Keep as int for logic, but ID is string
                suffix = match.group(3)

                # Construct ID
                scene_id = f"{chapter_num}.{scene_num}" # e.g. 1.1
                # If scene number is > 9 in file but < 10, typically 01 -> 1
                # But ID format in JSON might be 1.1 or 1.01. Let's assume X.Y

                file_path = Path(root_dir) / file

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                meta = parse_frontmatter(content)

                # Fallback to filename info if meta missing
                chapter = meta.get('chapter', chapter_num)
                # Ensure chapter matches filename

                title = meta.get('title', 'Untitled')
                location = meta.get('location', '')
                pov = meta.get('pov', '')

                scene_data = {
                    "scene_id": scene_id,
                    "chapter": chapter,
                    "title": title,
                    "location": location,
                    "pov_character": pov,
                    "file_path": str(file_path),
                    "active_alters": meta.get('active_alters', []),
                    "suffix": suffix
                }
                found_scenes.append(scene_data)

    return found_scenes

def update_ncp(ncp_path: Path, scanned_scenes: List[Dict]):
    data = load_json(ncp_path)

    if 'structural_framework' not in data:
        data['structural_framework'] = {}
    if 'scenes' not in data['structural_framework']:
        data['structural_framework']['scenes'] = []

    ncp_scenes = data['structural_framework']['scenes']

    # Helper to find existing scene
    def find_scene(sid):
        for s in ncp_scenes:
            if s.get('scene_id') == sid:
                return s
        return None

    changes_count = 0

    for item in scanned_scenes:
        sid = item['scene_id']
        suffix = item.get('suffix')

        existing = find_scene(sid)

        if suffix:
            # It's a branch or variant
            if not existing:
                print(f"Warning: Found branch file {item['file_path']} but no main scene {sid} in NCP. Skipping branch logic until main scene exists.")
                # Could create main scene, but risky.
                continue

            # Add to branches
            if 'branches' not in existing:
                existing['branches'] = []

            # Check if branch exists
            branch_name = suffix
            found_branch = False
            for b in existing['branches']:
                if b.get('branch_name') == branch_name:
                    b['file_path'] = item['file_path']
                    # Could update description from meta if available
                    found_branch = True
                    break

            if not found_branch:
                existing['branches'].append({
                    "branch_name": branch_name,
                    "description": f"Variant found in {item['file_path']}",
                    "outcome": "Unknown",
                    "file_path": item['file_path'],
                    "status": "Draft"
                })
                print(f"Added new branch '{branch_name}' to scene {sid}")
                changes_count += 1

        else:
            # Main scene
            if existing:
                # Update fields
                existing['title'] = item['title']
                existing['location'] = item['location']
                existing['pov_character'] = item['pov_character']
                existing['file_path'] = item['file_path']
                if item['active_alters']:
                    existing['active_alters'] = item['active_alters']
                # Don't overwrite goal/conflict/outcome if they exist in JSON but not file
            else:
                # Create new
                new_scene = {
                    "scene_id": sid,
                    "chapter": item['chapter'],
                    "title": item['title'],
                    "location": item['location'],
                    "pov_character": item['pov_character'],
                    "active_alters": item['active_alters'],
                    "goal": "",
                    "conflict": "",
                    "outcome": "",
                    "prose_style": "",
                    "branches": [],
                    "file_path": item['file_path']
                }
                ncp_scenes.append(new_scene)
                print(f"Added new scene {sid}: {item['title']}")
                changes_count += 1

    # Sort scenes
    ncp_scenes.sort(key=lambda x: (x.get('chapter', 0), float(x.get('scene_id', 0))))

    if changes_count > 0:
        save_json(ncp_path, data)
    else:
        print("No changes needed.")

def main():
    parser = argparse.ArgumentParser(description="Ingest manuscript files into NCP")
    parser.add_argument('--ncp', type=Path, default=DEFAULT_NCP_PATH)
    parser.add_argument('--root', type=Path, default=MANUSCRIPT_ROOT)
    parser.add_argument('--scan', action='store_true', help="Execute scan")

    args = parser.parse_args()

    if not args.scan:
        parser.print_help()
        return

    print(f"Scanning {args.root}...")
    scenes = scan_manuscript(args.root)
    print(f"Found {len(scenes)} files.")

    print(f"Updating {args.ncp}...")
    update_ncp(args.ncp, scenes)

if __name__ == "__main__":
    main()
