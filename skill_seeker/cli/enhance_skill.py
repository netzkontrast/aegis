#!/usr/bin/env python3
"""
SKILL.md Enhancement Script
Uses Claude API to improve SKILL.md by analyzing reference documentation.

Usage:
    python3 cli/enhance_skill.py output/steam-inventory/
    python3 cli/enhance_skill.py output/react/
    python3 cli/enhance_skill.py output/godot/ --api-key YOUR_API_KEY
"""

import os
import sys
import argparse
from pathlib import Path

# Add parent directory to path for imports when run as script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cli.skill_enhancer import create_enhancer

def main():
    parser = argparse.ArgumentParser(
        description='Enhance SKILL.md using Claude API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Using ANTHROPIC_API_KEY environment variable
  export ANTHROPIC_API_KEY=sk-ant-...
  python3 cli/enhance_skill.py output/steam-inventory/

  # Providing API key directly
  python3 cli/enhance_skill.py output/react/ --api-key sk-ant-...
"""
    )

    parser.add_argument('skill_dir', type=str,
                       help='Path to skill directory (e.g., output/steam-inventory/)')
    parser.add_argument('--api-key', type=str,
                       help='Anthropic API key (or set ANTHROPIC_API_KEY env var)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without calling API')

    args = parser.parse_args()

    # Validate skill directory
    skill_dir = Path(args.skill_dir)
    if not skill_dir.exists():
        print(f"❌ Error: Directory not found: {skill_dir}")
        sys.exit(1)

    if not skill_dir.is_dir():
        print(f"❌ Error: Not a directory: {skill_dir}")
        sys.exit(1)

    # Dry run mode
    if args.dry_run:
        print(f"🔍 DRY RUN MODE")
        print(f"   Would enhance: {skill_dir}")
        print(f"   References: {skill_dir / 'references'}")
        print(f"   SKILL.md: {skill_dir / 'SKILL.md'}")
        return

    # Create enhancer and run
    try:
        api_key = args.api_key or os.environ.get('ANTHROPIC_API_KEY')
        enhancer = create_enhancer('api', skill_dir, api_key=api_key)
        success = enhancer.run()
        sys.exit(0 if success else 1)

    except ValueError as e:
        print(f"❌ Error: {e}")
        print("\nSet your API key:")
        print("  export ANTHROPIC_API_KEY=sk-ant-...")
        print("Or provide it directly:")
        print(f"  python3 cli/enhance_skill.py {skill_dir} --api-key sk-ant-...")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
