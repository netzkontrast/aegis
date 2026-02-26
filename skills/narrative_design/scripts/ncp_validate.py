#!/usr/bin/env python3
"""
NCP Scene Validator - MVP Implementation

Validates written prose against NCP constraints using rule-based checks.

Usage:
    python ncp_validate.py manuscript/act_1/chapter_01_scene_01.md
    python ncp_validate.py scene.md --chapter 1 --verbose
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass
import argparse

# Import NCP Manager from ncp_query
sys.path.insert(0, str(Path(__file__).parent))
from ncp_query import NCPManager


@dataclass
class ValidationIssue:
    """A single validation issue"""
    severity: str  # ERROR, WARNING, INFO
    category: str  # character, theme, prose, world, continuity
    message: str
    line_number: int = None
    suggestion: str = None


@dataclass
class ValidationResult:
    """Complete validation result"""
    valid: bool
    score: float  # 0-10
    issues: List[ValidationIssue]
    checks_passed: int
    checks_total: int
    word_count: int


class SceneValidator:
    """Validates scenes against NCP constraints"""

    def __init__(self, ncp: NCPManager):
        self.ncp = ncp

    def validate_scene(
        self,
        scene_text: str,
        chapter: int,
        scene_id: str = None,
        verbose: bool = False
    ) -> ValidationResult:
        """Run all validation checks on a scene"""

        issues = []
        checks_passed = 0
        checks_total = 0

        # Word count
        word_count = len(scene_text.split())

        # Get NCP requirements
        chapter_info = self.ncp.get_chapter_info(chapter)
        scene_req = None
        if scene_id:
            scene_req = self.ncp.get_scene_requirements(scene_id)

        # Run checks
        checks = [
            self._check_length(scene_text, chapter),
            self._check_character_presence(scene_text, chapter, scene_req),
            self._check_prose_style(scene_text, chapter),
            self._check_world_setting(scene_text, chapter, scene_req),
            self._check_thematic_keywords(scene_text, chapter, scene_req),
        ]

        for check_issues, passed in checks:
            issues.extend(check_issues)
            checks_total += 1
            if passed:
                checks_passed += 1

        # Calculate score
        base_score = (checks_passed / checks_total) * 10

        # Deduct for errors
        error_penalty = sum(2.0 for i in issues if i.severity == "ERROR")
        warning_penalty = sum(0.5 for i in issues if i.severity == "WARNING")

        score = max(0.0, base_score - error_penalty - warning_penalty)

        # Valid if score >= 7.0 and no errors
        has_errors = any(i.severity == "ERROR" for i in issues)
        valid = score >= 7.0 and not has_errors

        return ValidationResult(
            valid=valid,
            score=score,
            issues=issues,
            checks_passed=checks_passed,
            checks_total=checks_total,
            word_count=word_count
        )

    def _check_length(self, text: str, chapter: int) -> Tuple[List[ValidationIssue], bool]:
        """Check scene length is reasonable"""
        issues = []
        word_count = len(text.split())

        if word_count < 500:
            issues.append(ValidationIssue(
                severity="WARNING",
                category="structure",
                message=f"Scene is short ({word_count} words). Consider expanding.",
                suggestion="Aim for 800-1500 words per scene"
            ))
            return issues, False

        if word_count > 3000:
            issues.append(ValidationIssue(
                severity="WARNING",
                category="structure",
                message=f"Scene is long ({word_count} words). Consider splitting.",
                suggestion="Scenes over 2500 words may lose focus"
            ))
            return issues, True  # Not a failure

        return issues, True

    def _check_character_presence(
        self,
        text: str,
        chapter: int,
        scene_req
    ) -> Tuple[List[ValidationIssue], bool]:
        """Check that expected characters appear"""
        issues = []
        passed = True

        # Check protagonist is named
        if chapter == 1 and "Kael" not in text:
            issues.append(ValidationIssue(
                severity="ERROR",
                category="character",
                message="Protagonist 'Kael' not mentioned in opening chapter",
                suggestion="Establish protagonist identity early"
            ))
            passed = False

        # If we have scene requirements, check active alters
        if scene_req and scene_req.active_alters:
            for alter in scene_req.active_alters:
                alter_name = alter.split()[0]  # "Lex (background)" -> "Lex"

                # Exception: background alters don't need explicit mention
                if "background" in alter.lower():
                    continue

                if alter_name not in text:
                    # Check if it's an intrusion/echo (those are OK to be subtle)
                    if "echo" in alter.lower() or "intrusion" in alter.lower():
                        continue

                    issues.append(ValidationIssue(
                        severity="WARNING",
                        category="character",
                        message=f"Active alter '{alter_name}' not found in scene",
                        suggestion=f"Ensure {alter_name} has presence/dialogue/internal voice"
                    ))

        return issues, passed

    def _check_prose_style(
        self,
        text: str,
        chapter: int
    ) -> Tuple[List[ValidationIssue], bool]:
        """Check prose style matches expected integration level"""
        issues = []

        # Calculate metrics
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        if not sentences:
            return issues, True

        avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences)

        # Count fragments (sentences starting with lowercase or very short)
        fragments = sum(1 for s in sentences if len(s.split()) < 5 or (s and s[0].islower()))
        fragment_ratio = fragments / len(sentences)

        # Count parenthetical intrusions
        intrusions = text.count('(')

        # Act I (Chapters 1-13): Should be fragmented
        if chapter <= 13:
            if avg_sentence_length > 25:
                issues.append(ValidationIssue(
                    severity="WARNING",
                    category="prose",
                    message=f"Act I prose should be fragmented (avg {avg_sentence_length:.1f} words/sentence)",
                    suggestion="Use shorter sentences, more fragments, interruptions"
                ))

            if intrusions < 5:
                issues.append(ValidationIssue(
                    severity="INFO",
                    category="prose",
                    message=f"Few intrusive thoughts detected ({intrusions})",
                    suggestion="Consider more parenthetical intrusions from other alters"
                ))

        # Act II (Chapters 14-26): Transitional
        elif chapter <= 26:
            if avg_sentence_length < 10 or avg_sentence_length > 30:
                issues.append(ValidationIssue(
                    severity="INFO",
                    category="prose",
                    message=f"Act II prose should be transitional (avg {avg_sentence_length:.1f})",
                    suggestion="Balance fragmentation with emerging cooperation"
                ))

        # Act III (Chapters 27-39): Polyphonic
        else:
            if avg_sentence_length < 15:
                issues.append(ValidationIssue(
                    severity="WARNING",
                    category="prose",
                    message="Act III prose should be polyphonic, not fragmented",
                    suggestion="Use complex sentences holding multiple perspectives"
                ))

            # Check for "we" usage
            if text.lower().count(' we ') < 3:
                issues.append(ValidationIssue(
                    severity="INFO",
                    category="prose",
                    message="Act III should use collective 'we' voice",
                    suggestion="Integrate alter perspectives into unified voice"
                ))

        return issues, True  # Prose style is advisory, not pass/fail

    def _check_world_setting(
        self,
        text: str,
        chapter: int,
        scene_req
    ) -> Tuple[List[ValidationIssue], bool]:
        """Check world physics and setting consistency"""
        issues = []
        passed = True

        if not scene_req:
            return issues, True

        location = scene_req.location.lower()

        # KW1 (Logos-Prime) - Logic and order
        if "logos-prime" in location or "kw1" in location:
            kw1_keywords = ["sterile", "geometric", "angle", "perfect", "order", "logic"]
            found_keywords = sum(1 for kw in kw1_keywords if kw in text.lower())

            if found_keywords < 2:
                issues.append(ValidationIssue(
                    severity="WARNING",
                    category="world",
                    message="KW1 (Logos-Prime) setting not strongly established",
                    suggestion="Emphasize: sterile perfection, geometric order, shadowless light"
                ))

        # KW2 (Mnemosyne-Archipel) - Emotion and memory
        elif "mnemosyne" in location or "kw2" in location:
            kw2_keywords = ["memory", "emotion", "water", "mist", "island", "echo"]
            found_keywords = sum(1 for kw in kw2_keywords if kw in text.lower())

            if found_keywords < 2:
                issues.append(ValidationIssue(
                    severity="WARNING",
                    category="world",
                    message="KW2 (Mnemosyne) setting not strongly established",
                    suggestion="Emphasize: fluid landscape, emotional resonance, memory islands"
                ))

        # KW3 (Cerberus-Labyrinth) - Defense and fear
        elif "cerberus" in location or "kw3" in location:
            kw3_keywords = ["fortress", "wall", "defense", "paranoid", "concrete", "steel"]
            found_keywords = sum(1 for kw in kw3_keywords if kw in text.lower())

            if found_keywords < 2:
                issues.append(ValidationIssue(
                    severity="WARNING",
                    category="world",
                    message="KW3 (Cerberus) setting not strongly established",
                    suggestion="Emphasize: brutalist architecture, defensive structures, paranoia"
                ))

        # KW4 (Kairos-Potentialis) - Potential and creativity
        elif "kairos" in location or "kw4" in location:
            kw4_keywords = ["growth", "garden", "potential", "emerge", "fractal", "possibility"]
            found_keywords = sum(1 for kw in kw4_keywords if kw in text.lower())

            if found_keywords < 2:
                issues.append(ValidationIssue(
                    severity="WARNING",
                    category="world",
                    message="KW4 (Kairos) setting not strongly established",
                    suggestion="Emphasize: organic growth, creative chaos, emergent patterns"
                ))

        return issues, passed

    def _check_thematic_keywords(
        self,
        text: str,
        chapter: int,
        scene_req
    ) -> Tuple[List[ValidationIssue], bool]:
        """Check for thematic checkpoint keywords"""
        issues = []

        if not scene_req or not scene_req.thematic_checkpoints:
            return issues, True

        text_lower = text.lower()

        for checkpoint in scene_req.thematic_checkpoints:
            checkpoint_name = checkpoint.get('checkpoint', '')

            # Extract key themes from checkpoint
            if "trauma" in checkpoint_name.lower():
                if not any(kw in text_lower for kw in ["fear", "terror", "pain", "overwhelm"]):
                    issues.append(ValidationIssue(
                        severity="INFO",
                        category="theme",
                        message=f"Checkpoint '{checkpoint_name}' - trauma language sparse",
                        suggestion="Consider stronger emotional vocabulary"
                    ))

            if "phobia" in checkpoint_name.lower() and "anp" in checkpoint_name.lower():
                if "avoid" not in text_lower and "flee" not in text_lower:
                    issues.append(ValidationIssue(
                        severity="INFO",
                        category="theme",
                        message=f"Checkpoint '{checkpoint_name}' - avoidance behavior not shown",
                        suggestion="Show ANP actively avoiding EP emotional content"
                    ))

            if "glitch" in checkpoint_name.lower() or "riss" in checkpoint_name.lower():
                if not any(kw in text_lower for kw in ["flicker", "error", "wrong", "crack", "break"]):
                    issues.append(ValidationIssue(
                        severity="WARNING",
                        category="theme",
                        message=f"Checkpoint '{checkpoint_name}' - glitch/rift not apparent",
                        suggestion="Show reality instability or system errors"
                    ))

        return issues, True  # Thematic checks are advisory


def print_validation_result(result: ValidationResult, verbose: bool = False):
    """Print validation result in human-readable format"""

    # Header
    print(f"\n{'='*60}")
    print(f"VALIDATION REPORT")
    print(f"{'='*60}")

    # Status
    status_icon = "✅" if result.valid else "❌"
    status_text = "PASS" if result.valid else "FAIL"
    print(f"\nStatus: {status_icon} {status_text}")
    print(f"Score: {result.score:.1f}/10.0")
    print(f"Checks Passed: {result.checks_passed}/{result.checks_total}")
    print(f"Word Count: {result.word_count}")

    # Issues by severity
    errors = [i for i in result.issues if i.severity == "ERROR"]
    warnings = [i for i in result.issues if i.severity == "WARNING"]
    info = [i for i in result.issues if i.severity == "INFO"]

    if errors:
        print(f"\n{'─'*60}")
        print(f"❌ ERRORS ({len(errors)})")
        print(f"{'─'*60}")
        for issue in errors:
            print(f"\n[{issue.category.upper()}] {issue.message}")
            if issue.suggestion:
                print(f"  → {issue.suggestion}")

    if warnings:
        print(f"\n{'─'*60}")
        print(f"⚠️  WARNINGS ({len(warnings)})")
        print(f"{'─'*60}")
        for issue in warnings:
            print(f"\n[{issue.category.upper()}] {issue.message}")
            if verbose and issue.suggestion:
                print(f"  → {issue.suggestion}")

    if info and verbose:
        print(f"\n{'─'*60}")
        print(f"ℹ️  INFO ({len(info)})")
        print(f"{'─'*60}")
        for issue in info:
            print(f"\n[{issue.category.upper()}] {issue.message}")
            if issue.suggestion:
                print(f"  → {issue.suggestion}")

    if not result.issues:
        print(f"\n✨ No issues found! Scene is excellent.")

    print(f"\n{'='*60}\n")


def extract_metadata_from_scene(scene_text: str) -> Dict:
    """Extract metadata from scene markdown frontmatter"""
    metadata = {}

    # Look for YAML frontmatter
    if scene_text.startswith('---'):
        parts = scene_text.split('---', 2)
        if len(parts) >= 2:
            frontmatter = parts[1]
            for line in frontmatter.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip().strip('"')

    return metadata


def main():
    parser = argparse.ArgumentParser(
        description='Validate scene against NCP constraints',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate a scene file
  python ncp_validate.py manuscript/act_1/chapter_01_scene_01.md

  # Specify chapter explicitly
  python ncp_validate.py scene.md --chapter 1

  # Verbose output with all issues
  python ncp_validate.py scene.md --verbose

  # Specify scene ID for detailed checks
  python ncp_validate.py scene.md --scene 1.1
        """
    )

    parser.add_argument('scene_file', type=Path, help='Scene file to validate')
    parser.add_argument('--ncp', type=Path,
                        default=Path(__file__).parent.parent / 'ncp' / 'kohaerenz_protokoll.ncp.json',
                        help='Path to NCP JSON file')
    parser.add_argument('--chapter', type=int, help='Chapter number')
    parser.add_argument('--scene', type=str, help='Scene ID (e.g., 1.1)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show all issues including INFO')

    args = parser.parse_args()

    # Load scene
    if not args.scene_file.exists():
        print(f"Error: Scene file not found: {args.scene_file}", file=sys.stderr)
        sys.exit(1)

    with open(args.scene_file, 'r', encoding='utf-8') as f:
        scene_text = f.read()

    # Try to extract metadata
    metadata = extract_metadata_from_scene(scene_text)

    chapter = args.chapter or int(metadata.get('chapter', 1))
    scene_id = args.scene or metadata.get('scene_id')

    # Load NCP
    try:
        ncp = NCPManager(args.ncp)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Validate
    validator = SceneValidator(ncp)
    result = validator.validate_scene(scene_text, chapter, scene_id, args.verbose)

    # Print results
    print_validation_result(result, args.verbose)

    # Exit code
    sys.exit(0 if result.valid else 1)


if __name__ == '__main__':
    main()
