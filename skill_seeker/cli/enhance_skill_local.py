#!/usr/bin/env python3
"""
SKILL.md Enhancement Script (Local - Using Claude Code)
Uses local Claude CLI to enhance SKILL.md.
No API key needed (uses Claude Code session).

Usage:
    python3 cli/enhance_skill_local.py output/steam-inventory/
    python3 cli/enhance_skill_local.py output/react/
"""

import os
import sys
import argparse
from pathlib import Path

# Add parent directory to path for imports when run as script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cli.skill_enhancer import create_enhancer

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 cli/enhance_skill_local.py <skill_directory>")
        print()
        print("Examples:")
        print("  python3 cli/enhance_skill_local.py output/steam-inventory/")
        print("  python3 cli/enhance_skill_local.py output/react/")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])

    # Validate skill directory
    if not skill_dir.exists():
        print(f"❌ Error: Directory not found: {skill_dir}")
        sys.exit(1)

    try:
        enhancer = create_enhancer('local', skill_dir)
        success = enhancer.run()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
