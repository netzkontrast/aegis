from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any, Optional
import os
import sys
import tempfile
import subprocess

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cli.utils import read_reference_files
from cli.constants import API_CONTENT_LIMIT, API_PREVIEW_LIMIT, LOCAL_CONTENT_LIMIT, LOCAL_PREVIEW_LIMIT

class SkillEnhancer(ABC):
    """Abstract base for skill enhancement"""

    def __init__(self, skill_dir: Path):
        self.skill_dir = skill_dir
        self.references_dir = self.skill_dir / "references"
        self.skill_md_path = self.skill_dir / "SKILL.md"

    @abstractmethod
    def enhance(self) -> Optional[str]:
        """Enhance skill content. Returns content string or None if handled internally."""
        pass

    def run(self) -> bool:
        """Execute the enhancement workflow"""
        try:
            print(f"\n{'='*60}")
            print(f"ENHANCING SKILL: {self.skill_dir.name}")
            print(f"{'='*60}\n")

            content = self.enhance()

            # If content is returned, save it.
            # If None is returned, assume the enhancer handled saving (e.g. LocalEnhancer via Claude)
            if content:
                self.save_enhanced(content)
                print(f"\n✅ Enhancement complete!")
                return True

            # If None, we assume success if no exception was raised,
            # unless the enhancer returned None to signal "nothing done" or "failure handled".
            # But enhance() is expected to raise exception on failure.
            return True

        except Exception as e:
            print(f"❌ Enhancement failed: {e}")
            return False

    def prepare_prompt(self, references: Dict[str, str], current_skill_md: Optional[str]) -> str:
        """Common prompt preparation logic"""
        skill_name = self.skill_dir.name

        prompt = f"""You are enhancing a Claude skill's SKILL.md file. This skill is about: {skill_name}

I've scraped documentation and organized it into reference files. Your job is to create an EXCELLENT SKILL.md that will help Claude use this documentation effectively.

CURRENT SKILL.MD:
{'```markdown' if current_skill_md else '(none - create from scratch)'}
{current_skill_md or 'No existing SKILL.md'}
{'```' if current_skill_md else ''}

REFERENCE DOCUMENTATION:
"""

        for filename, content in references.items():
            # Limit content length per file to avoid huge prompts
            # Using slice for safety, though read_reference_files handles limits
            prompt += f"\n\n## {filename}\n```markdown\n{content[:30000]}\n```\n"

        prompt += f"""

YOUR TASK:
Create an enhanced SKILL.md that includes:

1. **Clear "When to Use This Skill" section** - Be specific about trigger conditions
2. **Excellent Quick Reference section** - Extract 5-10 of the BEST, most practical code examples from the reference docs
   - Choose SHORT, clear examples that demonstrate common tasks
   - Include both simple and intermediate examples
   - Annotate examples with clear descriptions
   - Use proper language tags (cpp, python, javascript, json, etc.)
3. **Detailed Reference Files description** - Explain what's in each reference file
4. **Practical "Working with This Skill" section** - Give users clear guidance on how to navigate the skill
5. **Key Concepts section** (if applicable) - Explain core concepts
6. **Keep the frontmatter** (---\\nname: ...\\n---) intact

IMPORTANT:
- Extract REAL examples from the reference docs, don't make them up
- Prioritize SHORT, clear examples (5-20 lines max)
- Make it actionable and practical
- Don't be too verbose - be concise but useful
- Maintain the markdown structure for Claude skills
- Keep code examples properly formatted with language tags

SAVE THE RESULT:
Save the complete enhanced SKILL.md to: {self.skill_md_path.absolute()}

First, backup the original to: {self.skill_md_path.with_suffix('.md.backup').absolute()}
"""
        return prompt

    def save_enhanced(self, enhanced_content: str) -> None:
        """Common save logic with backup"""
        if self.skill_md_path.exists():
            backup_path = self.skill_md_path.with_suffix('.md.backup')
            self.skill_md_path.rename(backup_path)
            print(f"  💾 Backed up original to: {backup_path.name}")

        self.skill_md_path.write_text(enhanced_content, encoding='utf-8')
        print(f"  ✅ Saved enhanced SKILL.md")

    def read_current_skill_md(self) -> Optional[str]:
        """Read existing SKILL.md"""
        if not self.skill_md_path.exists():
            return None
        return self.skill_md_path.read_text(encoding='utf-8')

    def get_references(self, limit_content=True) -> Dict[str, str]:
        """Read reference files"""
        if limit_content:
            return read_reference_files(
                self.skill_dir,
                max_chars=LOCAL_CONTENT_LIMIT,
                preview_limit=LOCAL_PREVIEW_LIMIT
            )
        else:
            # API mode might allow more
            return read_reference_files(
                self.skill_dir,
                max_chars=API_CONTENT_LIMIT,
                preview_limit=API_PREVIEW_LIMIT
            )


class APIEnhancer(SkillEnhancer):
    """Uses Anthropic API for enhancement"""

    def __init__(self, skill_dir: Path, api_key: str):
        super().__init__(skill_dir)
        self.api_key = api_key

    def enhance(self) -> Optional[str]:
        try:
            import anthropic
        except ImportError:
            raise ImportError("anthropic package not installed. Run: pip install anthropic")

        print("📖 Reading reference documentation...")
        references = self.get_references(limit_content=False)
        if not references:
            raise ValueError("No reference files found")

        print(f"  ✓ Read {len(references)} reference files")

        current_skill_md = self.read_current_skill_md()
        prompt = self.prepare_prompt(references, current_skill_md)

        client = anthropic.Anthropic(api_key=self.api_key)

        print("\n🤖 Asking Claude to enhance SKILL.md...")
        try:
            # Override prompt to request ONLY content, not saving (since API returns text)
            # We need to strip the "SAVE THE RESULT" part from the prompt for API mode
            # or just ignore it. But better to guide correctly.
            api_prompt = prompt.replace("SAVE THE RESULT:", "OUTPUT:")
            api_prompt = api_prompt.replace(f"Save the complete enhanced SKILL.md to: {self.skill_md_path.absolute()}", "Return ONLY the complete SKILL.md content.")

            message = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                temperature=0.3,
                messages=[{"role": "user", "content": api_prompt}]
            )
            return message.content[0].text
        except Exception as e:
            raise RuntimeError(f"Error calling Claude API: {e}")


class LocalEnhancer(SkillEnhancer):
    """Uses Claude Code (local) for enhancement"""

    def enhance(self) -> Optional[str]:
        print("📖 Reading reference documentation...")
        references = self.get_references(limit_content=True)
        if not references:
            raise ValueError("No reference files found")
        print(f"  ✓ Read {len(references)} reference files")

        current_skill_md = self.read_current_skill_md()

        # Use common prepare_prompt which includes "SAVE THE RESULT" instructions
        # This is perfect for Local/Agent mode
        prompt = self.prepare_prompt(references, current_skill_md)

        # Save prompt to temp file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
            prompt_file = f.name
            f.write(prompt)

        print(f"  ✓ Prompt saved ({len(prompt):,} characters)\n")

        # Launch Claude Code in new terminal
        print("🚀 Launching Claude Code in new terminal...")

        # Create a shell script to run in the terminal
        shell_script = f'''#!/bin/bash
claude {prompt_file}
echo ""
echo "✅ Enhancement complete!"
echo "Press any key to close..."
read -n 1
rm {prompt_file}
'''

        # Save shell script
        with tempfile.NamedTemporaryFile(mode='w', suffix='.sh', delete=False) as f:
            script_file = f.name
            f.write(shell_script)

        os.chmod(script_file, 0o755)

        # Launch in new terminal
        if sys.platform == 'darwin':
            # macOS
            try:
                subprocess.Popen(['open', '-a', 'Terminal', script_file])
                print("✅ New terminal launched with Claude Code!")
            except Exception as e:
                print(f"⚠️  Error launching terminal: {e}")
                print(f"\nManually run: {script_file}")
        else:
            # Linux/Other - Cannot reliably open new terminal window without knowing env (gnome-terminal, xterm, etc.)
            # Fallback to manual instructions
            print("⚠️  Auto-launch requires macOS Terminal")
            print(f"\nManually run this command in a new terminal:")
            print(f"  {script_file}")
            print(f"\n(This script will run 'claude {prompt_file}' and then cleanup)")

        print()
        print("⏳ Wait for Claude Code to finish in the other terminal...")
        print("   (Usually takes 30-60 seconds)")
        print()

        # Return None because we don't have the content, the agent writes it to disk
        return None


def create_enhancer(mode: str, skill_dir: Path, **kwargs) -> SkillEnhancer:
    """Factory function to create appropriate enhancer"""

    if mode == 'api':
        api_key = kwargs.get('api_key')
        if not api_key:
            raise ValueError("API key required for API mode")
        return APIEnhancer(skill_dir, api_key)

    elif mode == 'local':
        return LocalEnhancer(skill_dir)

    else:
        raise ValueError(f"Unknown enhancer mode: {mode}")
