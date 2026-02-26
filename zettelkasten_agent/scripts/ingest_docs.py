import os
import sys
import yaml
import json
import time
from pathlib import Path
from datetime import datetime

# Add parent directory to path to import schemas
# This script is in zettelkasten_agent/scripts/ingest_docs.py
# We want to import from zettelkasten_agent/schemas/note_schemas.py
script_dir = Path(__file__).parent.absolute()
parent_dir = script_dir.parent
sys.path.append(str(parent_dir))

try:
    from schemas.note_schemas import (
        SourceNoteMetadata,
        MocNoteMetadata,
        Note,
        generate_note_id,
        generate_filename
    )
except ImportError as e:
    print(f"Error importing schemas: {e}")
    sys.exit(1)

# Configuration
REPO_ROOT = parent_dir.parent
DOCS_PATH = REPO_ROOT / "docs"
VAULT_PATH = parent_dir / "vault"
QUESTS_PATH = REPO_ROOT / "quests"

# Ensure vault exists
VAULT_PATH.mkdir(parents=True, exist_ok=True)

# Quest Keywords for Tagging
QUEST_TAG_MAP = {}

def load_quest_tags():
    print("Loading quests...")
    if not QUESTS_PATH.exists():
        print("Quests directory not found.")
        return

    count = 0
    for quest_file in QUESTS_PATH.glob("*.md"):
        if quest_file.name == "README.md" or quest_file.name == "TEMPLATE.md":
            continue

        # Extract tag from filename (e.g., Quest-Narrative-Architecture -> #quest/narrative-architecture)
        tag_name = quest_file.stem.replace("Quest-", "").lower()
        tag = f"#quest/{tag_name}"

        # simple keyword extraction from filename parts
        keywords = tag_name.split("-")

        QUEST_TAG_MAP[quest_file.stem] = {
            "tag": tag,
            "keywords": keywords
        }
        count += 1
    print(f"Loaded {count} quests for tagging.")

def get_tags_for_content(content, filename):
    tags = []
    content_lower = content.lower()
    filename_lower = filename.lower()

    for quest, data in QUEST_TAG_MAP.items():
        # Check if any keyword matches
        match = False
        for kw in data["keywords"]:
            if len(kw) > 3 and kw in content_lower: # avoid short words
                match = True
                break
            if kw in filename_lower:
                match = True
                break

        if match:
            tags.append(data["tag"])

    return list(set(tags))

def get_existing_src_notes():
    existing_notes = {}
    print(f"Scanning vault at {VAULT_PATH} for existing notes...")
    for note_file in VAULT_PATH.glob("SRC-*.md"):
        try:
            content = note_file.read_text(encoding="utf-8")
            # extract source_uri from yaml
            if "source_uri:" in content:
                # simple parse or yaml load
                parts = content.split("---")
                if len(parts) >= 3:
                    metadata = yaml.safe_load(parts[1])
                    if "source_uri" in metadata:
                        existing_notes[metadata["source_uri"]] = note_file
        except Exception as e:
            print(f"Error reading {note_file}: {e}")
    print(f"Found {len(existing_notes)} existing SRC notes.")
    return existing_notes

def is_story_content(content, filepath):
    keywords = [
        "Kael", "AEGIS", "Juna", "Act I", "Act II", "Act III", "Chapter",
        "Narrative", "Plot", "Character", "Setting", "Theme",
        "Triadic Currency", "Logos", "Mnemosyne", "Cerberus", "Kairos",
        "Story", "Novel", "Book", "Manuscript", "Scene", "Writing"
    ]

    filepath_str = str(filepath)
    # Always include files in writing/ or plans/
    if "writing/" in filepath_str or "plans/" in filepath_str:
        return True

    content_lower = content.lower()
    for kw in keywords:
        if kw.lower() in content_lower:
            return True

    return False

def ingest_docs():
    load_quest_tags()
    existing_notes = get_existing_src_notes()

    processed_count = 0
    skipped_count = 0

    # Track MOC structure
    # Key: directory path relative to docs (e.g. "docs", "docs/plans")
    # Value: list of note objects {id, title, path}
    moc_structure = {}

    for root, dirs, files in os.walk(DOCS_PATH):
        root_path = Path(root)
        try:
            rel_path = root_path.relative_to(DOCS_PATH)
        except ValueError:
            continue

        # Create MOC key for directory
        dir_key = str(rel_path)
        if dir_key == ".":
            dir_key = "docs"
        else:
            dir_key = f"docs/{dir_key}"

        if dir_key not in moc_structure:
            moc_structure[dir_key] = []

        for file in files:
            if not file.endswith(".md"):
                continue

            file_path = root_path / file
            rel_file_path = file_path.relative_to(REPO_ROOT) # relative to repo root for source_uri
            source_uri = str(rel_file_path)

            content = file_path.read_text(encoding="utf-8")

            if not is_story_content(content, file_path):
                # print(f"Skipping {file} (no story content)")
                skipped_count += 1
                continue

            print(f"Processing {file}...")

            # Metadata
            tags = ["#docs"]
            if "plans" in str(file_path): tags.append("#plans")
            if "writing" in str(file_path): tags.append("#writing")

            content_tags = get_tags_for_content(content, file)
            tags.extend(content_tags)

            # Prepare content
            body_content = content
            original_metadata = {}
            if content.startswith("---"):
                try:
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        # Attempt to parse existing frontmatter
                        try:
                            original_metadata = yaml.safe_load(parts[1])
                        except yaml.YAMLError:
                            pass

                        body_content = parts[2].strip()
                        # Add original metadata block to body for reference
                        # Use a quote block to preserve it without interfering with new frontmatter
                        body_content = f"> **Original Metadata**:\n> ```yaml\n> {parts[1].strip()}\n> ```\n\n{body_content}"
                except Exception:
                    pass

            # Determine Title
            title = None
            if isinstance(original_metadata, dict):
                 title = original_metadata.get("title")

            if not title:
                # Try to find first H1
                lines = body_content.splitlines()
                for line in lines:
                    if line.startswith("# "):
                        title = line[2:].strip()
                        break

            if not title:
                title = file_path.stem.replace("-", " ").replace("_", " ").title()

            # Check if exists
            note_id = None
            if source_uri in existing_notes:
                old_note_path = existing_notes[source_uri]
                # Extract ID from filename (SRC-timestamp.md)
                note_id = old_note_path.stem
                print(f"  Updating existing note: {note_id}")
            else:
                # Generate new ID
                # To prevent collision if running fast
                while True:
                    candidate_id = generate_note_id("SRC")
                    candidate_filename = generate_filename(candidate_id)
                    if not (VAULT_PATH / candidate_filename).exists():
                        note_id = candidate_id
                        break
                    time.sleep(1.1)
                print(f"  Creating new note: {note_id}")

            # Construct Note Metadata
            # Note: status is strictly typed Literal["unprocessed", "processing", "processed"]
            metadata_dict = {
                "id": note_id,
                "created": datetime.now().isoformat(),
                "note_type": "SRC",
                "source_uri": source_uri,
                "tags": tags,
                "status": "processed",
                "links": []
            }

            # Use Pydantic model for validation
            try:
                metadata = SourceNoteMetadata(**metadata_dict)
            except Exception as e:
                print(f"Error validating metadata for {file}: {e}")
                continue

            # Create Note object (validates content)
            try:
                # Ensure title is at top of content if not present
                final_content = body_content
                if not final_content.startswith(f"# {title}"):
                     final_content = f"# {title}\n\n{body_content}"

                note = Note(
                    metadata=metadata,
                    content=final_content
                )
            except Exception as e:
                print(f"Error creating note object for {file}: {e}")
                continue

            # Write Note
            filename = generate_filename(note_id)
            out_path = VAULT_PATH / filename

            # Dump with YAML frontmatter
            yaml_meta = yaml.dump(
                metadata.model_dump(exclude_none=True),
                default_flow_style=False,
                sort_keys=False
            )

            full_text = f"---\n{yaml_meta}---\n\n{note.content}"
            out_path.write_text(full_text, encoding="utf-8")

            processed_count += 1

            # Add to MOC structure
            moc_structure[dir_key].append({
                "id": note_id,
                "title": title,
                "path": filename
            })

    # Create MOCs
    print("Creating MOCs...")
    for dir_key, notes in moc_structure.items():
        if not notes and dir_key != "docs":
            continue

        # MOC Topic
        # docs -> Docs
        # docs/plans -> Docs Plans
        topic_parts = dir_key.split("/")
        topic = " ".join([p.capitalize() for p in topic_parts])

        # MOC ID
        # We need a stable ID if we want to update MOCs, but MOC schema uses topic for ID generation?
        # generate_note_id("MOC", topic="Docs Plans") -> MOC-Docs_Plans
        # Let's check if MOC already exists for this topic to avoid duplication
        # We can search by filename since MOC ID is deterministic from topic

        moc_id = generate_note_id("MOC", topic=topic)
        moc_filename = generate_filename(moc_id)
        moc_path = VAULT_PATH / moc_filename

        action = "Created"
        if moc_path.exists():
            action = "Updated"

        moc_content = f"# Map of Content: {topic}\n\n"
        moc_content += f"Source directory: `{dir_key}`\n\n"

        # Add links to Sub-MOCs
        # Iterate all keys to find direct children
        children_mocs = []
        for other_key in moc_structure.keys():
            if other_key.startswith(dir_key + "/"):
                # Check if direct child (no extra slashes)
                rest = other_key[len(dir_key)+1:]
                if "/" not in rest:
                    child_topic_parts = other_key.split("/")
                    child_topic = " ".join([p.capitalize() for p in child_topic_parts])
                    child_id = generate_note_id("MOC", topic=child_topic)
                    children_mocs.append((child_id, child_topic))

        if children_mocs:
             moc_content += "## Sub-Directories\n\n"
             for child_id, child_topic in sorted(children_mocs, key=lambda x: x[1]):
                 moc_content += f"- [[{child_id}]] **{child_topic}**\n"
             moc_content += "\n"

        moc_content += "## Notes\n\n"
        for note in sorted(notes, key=lambda x: x['title']):
            moc_content += f"- [[{note['id']}]] {note['title']}\n"

        metadata_dict = {
            "id": moc_id,
            "created": datetime.now().isoformat(),
            "note_type": "MOC",
            "topic": topic,
            "tags": ["#moc", "#docs"],
            "links": [n['id'] for n in notes] + [c[0] for c in children_mocs]
        }

        try:
            metadata = MocNoteMetadata(**metadata_dict)
            note = Note(metadata=metadata, content=moc_content)

            yaml_meta = yaml.dump(
                metadata.model_dump(exclude_none=True),
                default_flow_style=False,
                sort_keys=False
            )

            full_text = f"---\n{yaml_meta}---\n\n{note.content}"
            moc_path.write_text(full_text, encoding="utf-8")
            print(f"{action} MOC: {moc_id} ({topic})")

        except Exception as e:
            print(f"Error creating MOC {topic}: {e}")

    print(f"\nIngestion Complete.")
    print(f"Processed: {processed_count}")
    print(f"Skipped:   {skipped_count}")

if __name__ == "__main__":
    ingest_docs()
