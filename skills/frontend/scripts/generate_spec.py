#!/usr/bin/env python3
import os
import glob
import yaml
import json
import re

COMMANDS_DIR = ".claude/commands"
OUTPUT_FILE = "skills/console/specs/console-commands.json"

def parse_frontmatter(filepath):
    """Extracts YAML frontmatter from a markdown file."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Regex to find YAML frontmatter between --- lines at the start of the file
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError as e:
            print(f"Error parsing YAML in {filepath}: {e}")
            return None
    return None

def main():
    commands = []

    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    print(f"Scanning {COMMANDS_DIR} for UI specs...")

    for filepath in glob.glob(os.path.join(COMMANDS_DIR, "*.md")):
        filename = os.path.basename(filepath)
        command_name = os.path.splitext(filename)[0]

        frontmatter = parse_frontmatter(filepath)

        if frontmatter and 'ui' in frontmatter:
            print(f"  Found UI spec in {filename}")
            command_spec = {
                "id": command_name,
                "path": filepath,
                "ui": frontmatter['ui']
            }
            commands.append(command_spec)
        else:
            # print(f"  No UI spec in {filename}")
            pass

    output = {
        "version": "1.0",
        "generated_at": os.popen('date -u +"%Y-%m-%dT%H:%M:%SZ"').read().strip(),
        "commands": commands
    }

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"Generated spec with {len(commands)} commands to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
