import os
import re
import glob

ACT_1_PATH = "kohaerenz_protokoll/manuscript/act_1/*.md"
OUTPUT_REPORT = "kohaerenz_protokoll/narrative_design/NCP_V2_ACT_1_LOG_AUDIT.md"

# Strict Syntax Regex (approximate based on the template)
# [AEGIS v{X.X} // LOG_{0xHEX}]
STRICT_START_PATTERN = re.compile(r"\[AEGIS v\d+\.\d+ // LOG_0x[0-9A-F]+\]")
STRICT_END_PATTERN = re.compile(r"\[ENDE LOG\]")

# Loose patterns to find potential logs that need fixing
LOOSE_PATTERNS = [
    re.compile(r"\*\*LOG ENTRY", re.IGNORECASE),
    re.compile(r"LOGGING FAILURE", re.IGNORECASE),
    re.compile(r"INCIDENT LOG", re.IGNORECASE),
    re.compile(r"SYSTEM_KAEL", re.IGNORECASE), # Should be in strict, but good to catch standalone
    re.compile(r"ZEITSTEMPEL", re.IGNORECASE),
    re.compile(r"PARADOX_INDEX", re.IGNORECASE),
    re.compile(r"> \*\*UNIT DESIGNATION\*\*", re.IGNORECASE), # From Chapter 3 snippet
    re.compile(r"SECURITY ALERT", re.IGNORECASE),
]

def audit_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    filename = os.path.basename(filepath)
    issues = []
    strict_logs_found = 0

    in_strict_log = False

    for i, line in enumerate(lines):
        line = line.strip()

        # Check for Strict Log Start
        if STRICT_START_PATTERN.search(line):
            in_strict_log = True
            strict_logs_found += 1
            continue

        # Check for Strict Log End
        if STRICT_END_PATTERN.search(line):
            in_strict_log = False
            continue

        # If not in a strict log, check for loose patterns
        if not in_strict_log:
            for pattern in LOOSE_PATTERNS:
                if pattern.search(line):
                    issues.append({
                        "line": i + 1,
                        "content": line,
                        "pattern": pattern.pattern
                    })
                    break # Avoid duplicate hits for same line

    return {
        "filename": filename,
        "strict_count": strict_logs_found,
        "issues": issues
    }

def main():
    files = sorted(glob.glob(ACT_1_PATH))
    results = []

    for filepath in files:
        results.append(audit_file(filepath))

    # Generate Report
    with open(OUTPUT_REPORT, 'w', encoding='utf-8') as f:
        f.write("# AEGIS Log Audit Report: Act 1\n\n")
        f.write("**Status:** Automated Audit Generated\n")
        f.write("**Target Syntax:** Strict AEGIS Log Format (see `quests/aegis.md`)\n\n")

        total_strict = sum(r['strict_count'] for r in results)
        total_issues = sum(len(r['issues']) for r in results)

        f.write(f"## Summary\n")
        f.write(f"- **Files Scanned:** {len(files)}\n")
        f.write(f"- **Compliant Logs Found:** {total_strict}\n")
        f.write(f"- **Potential Issues / Non-Compliant Logs:** {total_issues}\n\n")

        f.write("## Detailed Findings\n\n")

        for r in results:
            if r['strict_count'] == 0 and len(r['issues']) == 0:
                continue

            f.write(f"### {r['filename']}\n")
            if r['strict_count'] > 0:
                f.write(f"- ✅ **Compliant Logs:** {r['strict_count']}\n")

            if r['issues']:
                f.write("- ⚠️ **Potential Non-Compliant Content:**\n")
                f.write("| Line | Content Snippet | Trigger |\n")
                f.write("|---|---|---|\n")
                for issue in r['issues']:
                    # Escape pipe characters in content to avoid breaking markdown table
                    content = issue['content'].replace("|", "\\|")
                    # Truncate long lines
                    if len(content) > 60:
                        content = content[:57] + "..."
                    f.write(f"| {issue['line']} | `{content}` | `{issue['pattern']}` |\n")
            f.write("\n")

    print(f"Audit complete. Report generated at {OUTPUT_REPORT}")

if __name__ == "__main__":
    main()
