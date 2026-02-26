# Coherence Enforcer: Usage Examples

This document demonstrates practical applications of the Coherence Enforcer skill through real AEGIS scenarios.

---

## Example 1: Monthly Coherence Audit

**Scenario:** It's been a month since the last audit. Time for routine maintenance.

### User Request
```
Run a coherence audit on the AEGIS project
```

### Assistant Response (Using Skill)

**Phase 1: Audit**

```bash
# Step 1: Check for command duplication
echo "=== Checking Commands ==="
ls -la .claude/commands/*.md | wc -l
# Output: 5 command files

# Step 2: Analyze command descriptions
grep "description:" .claude/commands/*.md
```

**Findings:**
```
.claude/commands/tapestry.md:description: Extract content + Plan
.claude/commands/ship-learn-next.md:description: Create action plans
.claude/commands/zettelkasten-tapestry.md:description: Extract + Plan + Save
.claude/commands/learn.md:description: Unified learning workflow
```

**Analysis:**
- Potential overlap detected between `tapestry` and `learn`
- Need to investigate implementation similarity

```bash
# Step 3: Check for unreferenced files
echo "=== Checking for Dead Code ==="
for file in $(find skill_seeker/cli -name "*.py" -not -name "__init__.py"); do
  module=$(basename "$file" .py)
  refs=$(grep -r "import.*$module" --exclude="$file" skill_seeker/ 2>/dev/null | wc -l)
  echo "$file: $refs references"
done
```

**Findings:**
```
skill_seeker/cli/doc_scraper.py: 3 references ✅
skill_seeker/cli/unified_scraper.py: 2 references ✅
skill_seeker/cli/enhance_skill.py: 1 reference ✅
skill_seeker/cli/enhance_skill_local.py: 1 reference ✅
skill_seeker/cli/package_skill.py: 0 references ⚠️
```

**Analysis:**
- `package_skill.py` has 0 imports - check git history before archiving

```bash
# Step 4: Check git activity for package_skill.py
git log --since="6 months ago" --oneline -- skill_seeker/cli/package_skill.py | wc -l
# Output: 5 commits

# Recent activity! This is active development, keep it.
```

**Phase 2: Generate Report**

```markdown
# AEGIS Coherence Audit Report
**Date:** 2025-11-06

## Findings

### MEDIUM: Command System Transition Incomplete
- **Status:** `/learn` command created but not activated
- **Issue:** Old commands (tapestry, ship-learn-next) still primary
- **Impact:** Users uncertain which command to use
- **Recommendation:** Complete migration per REFACTORING_PROPOSAL
- **Priority:** 🟡 P1

### LOW: Package Skill Unreferenced (False Positive)
- **Status:** package_skill.py has 0 imports
- **Analysis:** Recent commits (5 in 6 months) indicate active dev
- **Conclusion:** CLI tool, not library - import check doesn't apply
- **Action:** None (working as intended)

## Recommendations

1. Activate `/learn` command deprecation notices
2. Update docs to recommend `/learn` over old commands
3. Create timeline for removing old commands (1 month notice)

## Health Score: 🟡 7/10 (Good, minor improvements needed)
```

**Phase 3: Get Approval & Execute**

"I've found that the command consolidation started but isn't complete. Should I:
1. Add deprecation notices to old commands?
2. Update documentation to recommend `/learn`?
3. Set a timeline for removing old commands?"

---

## Example 2: Pre-Release Coherence Check

**Scenario:** About to create a PR. Want to ensure no regressions or fragmentation.

### User Request
```
I'm about to create a PR for the zettelkasten agent. Check coherence first.
```

### Assistant Response (Using Skill)

**Phase 1: Focused Audit**

```bash
# Check integration with existing commands
echo "=== Checking Zettelkasten Integration ==="
grep -r "zettelkasten" .claude/commands/

# Check for documentation about the new feature
grep -r "zettelkasten_agent" docs/
grep -r "zettelkasten_agent" README.md
```

**Findings:**
```
.claude/commands/zettelkasten-tapestry.md: References zettelkasten workflow
skills/zettelkasten-tapestry/: Contains skill wrapper

README.md: No mention of zettelkasten_agent
docs/: No integration documentation
```

**Analysis:**
- ✅ Command integration exists
- ❌ Missing documentation
- ⚠️ Unclear relationship between `zettelkasten_agent/` (Python) and commands (markdown)

**Phase 2: Documentation Verification**

```bash
# Check if zettelkasten_agent has README
cat zettelkasten_agent/README.md | head -20
```

**Findings:**
- ✅ zettelkasten_agent/README.md exists (343 lines)
- ❌ Not linked from main README.md
- ❌ Not explained in .claude/README.md

**Phase 3: Recommendations**

```markdown
# Pre-Release Coherence Check: Zettelkasten Agent

## Status: 🟡 Ready with Minor Improvements

### REQUIRED (Before PR):

1. **Link from main README**
   ```markdown
   ### Tools
   - **Zettelkasten Agent** - Knowledge management system
     - [Documentation](zettelkasten_agent/README.md)
     - [MCP Server](zettelkasten_agent/mcp/)
     - Related: [Zettelkasten-Tapestry command](.claude/commands/zettelkasten-tapestry.md)
   ```

2. **Clarify relationship in docs**
   Create `zettelkasten_agent/INTEGRATION.md`:
   ```markdown
   # How Zettelkasten Agent Integrates

   - **Python Agent**: Core knowledge management (this directory)
   - **Slash Command**: Workflow wrapper (.claude/commands/zettelkasten-tapestry.md)
   - **Skill**: Reusable module (skills/zettelkasten-tapestry/)

   Use command/skill for convenience, use agent directly for advanced workflows.
   ```

### OPTIONAL (Nice to have):

3. **Add to Documentation Index** (docs/INDEX.md)
4. **Cross-reference from knowledge-extraction docs**

### Validation:
- ✅ Code works (tests passing)
- ✅ Documentation exists (README complete)
- 🟡 Integration documented (needs linking)
- 🟡 Navigation clear (needs INDEX update)

**Recommendation:** Make required changes, then PR is ready.
```

**User approves → Execute → Validate → Create PR**

---

## Example 3: Investigating Duplication

**Scenario:** About to add a new feature but suspect similar code exists.

### User Request
```
I want to add a PDF scraper. Do we already have something like that?
```

### Assistant Response (Using Skill)

**Phase 1: Search for Existing Implementation**

```bash
# Search for PDF-related code
echo "=== Searching for PDF functionality ==="
grep -r "pdf" --include="*.py" --include="*.md" . | grep -i "scrap\|extract\|parse"
```

**Findings:**
```
skill_seeker/cli/pdf_scraper.py: PDF scraping implementation
skill_seeker/docs/PDF_SCRAPER.md: Documentation
skill_seeker/README.md: Mentions PDF support
```

**Analysis:**
✅ **PDF scraper already exists!** Don't duplicate.

**Phase 2: Review Existing Implementation**

```bash
# Check what pdf_scraper.py provides
head -50 skill_seeker/cli/pdf_scraper.py
```

**Capabilities found:**
- Text extraction (pdftotext)
- Image extraction (pdfimages)
- Table extraction (tabula-py)
- OCR support (tesseract)
- Multi-page handling

**Phase 3: Integration Recommendation**

```markdown
# Duplication Prevention: PDF Scraper

## Finding
✅ PDF scraper already exists in `skill_seeker/cli/pdf_scraper.py`

## Capabilities
- Text, images, tables extraction
- OCR support
- Production-ready (used in unified_scraper)

## Recommendation: DON'T CREATE NEW IMPLEMENTATION

### Instead, integrate existing tool:

**Option 1: Use directly**
```python
from skill_seeker.cli.pdf_scraper import PDFScraper

scraper = PDFScraper(config)
content = scraper.extract("document.pdf")
```

**Option 2: Enhance existing**
If current implementation is missing features:
1. Add to `skill_seeker/cli/pdf_scraper.py`
2. Write tests in `skill_seeker/tests/`
3. Update `skill_seeker/docs/PDF_SCRAPER.md`

**Option 3: Wrap for convenience**
If you need simpler interface:
```python
# utils/pdf_helper.py
from skill_seeker.cli.pdf_scraper import PDFScraper

def extract_pdf_text(filepath):
    """Simple wrapper for common use case"""
    scraper = PDFScraper({'mode': 'text'})
    return scraper.extract(filepath)
```

## Next Steps
1. Read skill_seeker/docs/PDF_SCRAPER.md
2. Identify if existing tool meets your needs
3. Enhance if needed, wrap if convenient
4. **DON'T duplicate the core logic**
```

**Result:** Prevented 500+ lines of duplication!

---

## Example 4: Documentation Drift Detection

**Scenario:** User reports that a command doesn't work as documented.

### User Request
```
The /tapestry command docs say it can handle GitHub repos, but it fails when I try.
```

### Assistant Response (Using Skill)

**Phase 1: Investigate Claim vs Reality**

```bash
# Check what tapestry.md claims
grep -A10 "GitHub" .claude/commands/tapestry.md
```

**Finding:**
```markdown
## Supported Sources
- YouTube videos
- Web articles
- PDFs
- **GitHub repositories** ← CLAIMED
```

**Check implementation:**
```bash
# Search for GitHub handling in tapestry.md
grep -n "github\|GitHub" .claude/commands/tapestry.md | tail -20
```

**Finding:**
```
Line 45: "- GitHub repositories"
Line 120: "# GitHub support not yet implemented (See Quest-Zettelkasten-Tapestry)"
```

**Analysis:**
🔴 **DOCUMENTATION DRIFT DETECTED**
- Docs claim GitHub is supported
- Implementation has TODO comment
- User expectation ≠ Reality

**Phase 2: Check for Existing GitHub Support**

```bash
# Maybe GitHub support exists elsewhere?
grep -r "github" skill_seeker/cli/*.py | grep -i "scrap\|extract"
```

**Finding:**
```
skill_seeker/cli/github_scraper.py: Full GitHub scraping implementation
skill_seeker/cli/unified_scraper.py: Uses github_scraper.py
```

**Analysis:**
- GitHub scraper EXISTS in skill_seeker
- tapestry.md doesn't integrate it
- disconnection between command and tool

**Phase 3: Fix Documentation Drift**

```markdown
# Documentation Drift Fix: Tapestry GitHub Support

## Issue
- **Claimed:** Tapestry supports GitHub repositories
- **Reality:** GitHub support not implemented in tapestry.md
- **Impact:** User confusion, broken workflows

## Root Cause
- skill_seeker has github_scraper.py (working)
- tapestry.md doesn't integrate it
- Docs were aspirational, not factual

## Fix Options

### Option A: Remove claim (Quick fix)
```markdown
## Supported Sources
- YouTube videos
- Web articles
- PDFs
- ~~GitHub repositories~~ ← REMOVE

**Coming soon:** GitHub repository support
```

### Option B: Implement integration (Complete fix)
Add to tapestry.md:
```bash
if [[ "$URL" =~ github.com ]]; then
  echo "GitHub repository detected..."
  python skill_seeker/cli/github_scraper.py "$URL" > extracted_content.md
fi
```

## Recommendation: Option B (1-2 hours)
- Leverage existing tool
- Meet user expectations
- Complete the feature properly

## Validation
After fix:
1. Test: /tapestry https://github.com/anthropics/claude-code
2. Verify: Extraction works
3. Update docs: Mark as implemented
```

**User approves Option B → Implement → Validate → Fix drift**

**Update (2025-11-06):** GitHub support has since been implemented in the `/learn` command, which replaces `tapestry`. The example above is preserved for historical context on detecting drift.

---

## Example 5: Safe Dead Code Archival

**Scenario:** Found a file that seems unused, want to remove it safely.

### User Request
```
Can we delete skill_seeker/cli/old_scraper.py? I don't think it's used anymore.
```

### Assistant Response (Using Skill)

**Phase 1: Verify "Dead" Status**

```bash
# Check for imports
echo "=== Checking References ==="
grep -r "old_scraper" --exclude="old_scraper.py" .

# Check git history
echo "=== Checking Git History ==="
git log --since="6 months ago" --oneline -- skill_seeker/cli/old_scraper.py | wc -l
```

**Findings:**
```
References: 0
Recent commits: 0
Last modified: 2024-03-15 (8 months ago)
```

**Analysis:**
- No imports found ✅
- No recent activity ✅
- Likely safe to remove

**Phase 2: Deeper Investigation**

```bash
# Check git blame to understand original purpose
git log --follow --all -- skill_seeker/cli/old_scraper.py | head -20

# Check if it's mentioned in docs
grep -r "old_scraper" docs/ README.md
```

**Findings:**
```
Git history: "feat: Add old_scraper.py for legacy docs format"
Last commit: "fix: Handle edge case in old_scraper"
Docs: No mentions
```

**Analysis:**
- Was created for legacy format support
- Had bug fixes (was used seriously)
- Now superseded by unified_scraper.py

**Phase 3: Safe Archival (NOT Deletion)**

```markdown
# Safe Removal: old_scraper.py

## Status: SAFE TO ARCHIVE

### Verification
- ✅ No references in code (0 imports)
- ✅ No recent activity (8 months dormant)
- ✅ Superseded by unified_scraper.py
- ✅ Not documented as active

### Archival Process (Reversible)

**Step 1: Create archive**
```bash
mkdir -p .archive/removed-2025-11-06/skill_seeker/cli/
```

**Step 2: Move (don't delete)**
```bash
git mv skill_seeker/cli/old_scraper.py \
        .archive/removed-2025-11-06/skill_seeker/cli/old_scraper.py
```

**Step 3: Document removal**
```bash
cat > .archive/removed-2025-11-06/REMOVAL_LOG.md <<'EOF'
# Files Archived: 2025-11-06

## old_scraper.py
- **Original location:** skill_seeker/cli/old_scraper.py
- **Last modified:** 2024-03-15
- **Reason:** No references, superseded by unified_scraper.py
- **Restore command:**
  ```
  git mv .archive/removed-2025-11-06/skill_seeker/cli/old_scraper.py \
         skill_seeker/cli/old_scraper.py
  ```
EOF
```

**Step 4: Commit**
```bash
git add .archive/
git commit -m "archive: Move old_scraper.py to .archive/

Superseded by unified_scraper.py. Can be restored if needed.
See .archive/removed-2025-11-06/REMOVAL_LOG.md"
```

### Benefits
- ✅ Reversible (not deleted)
- ✅ Documented (why removed, how to restore)
- ✅ Tracked in git
- ✅ Clean codebase
```

**Result:** Code archived safely, can be restored in 10 seconds if needed.

---

## Example 6: Integration Gap Detection

**Scenario:** Two systems that should work together don't.

### User Request
```
Why doesn't the Codex skill use the ARCHON validation tools?
```

### Assistant Response (Using Skill)

**Phase 1: Verify Disconnection**

```bash
# Check if Codex mentions ARCHON tools
grep -n "ncp_validate\|ncp_query" .claude/skills/codex.md
```

**Finding:**
```
(no results)
```

**Check if tools exist:**
```bash
ls -la ARCHON/tools/*.py
```

**Finding:**
```
-rwxr-xr-x ncp_query.py
-rwxr-xr-x ncp_validate.py
-rwxr-xr-x ncp_assist.py (planned, not implemented)
```

**Analysis:**
🔴 **INTEGRATION GAP**
- ARCHON tools exist and work
- Codex skill doesn't use them
- Manual validation only (error-prone)

**Phase 2: Understand Why**

```bash
# Check when each was created
git log --reverse --oneline -- .claude/skills/codex.md | head -1
git log --reverse --oneline -- ARCHON/tools/ncp_validate.py | head -1
```

**Finding:**
```
codex.md: Created 2025-10-15
ncp_validate.py: Created 2025-11-01
```

**Analysis:**
- Codex created first
- ARCHON tools added later
- Never integrated (oversight, not intentional)

**Phase 3: Design Integration**

```markdown
# Integration Fix: Codex + ARCHON Tools

## Current State
- Codex skill: Manual validation checklists
- ARCHON tools: Automated NCP validation
- Connection: None

## Proposed Integration

### Add to Codex Workflow 1 (Validating a Scene)

**Step 4: Automated Validation (NEW)**
```bash
# Query NCP for canonical constraints
python ARCHON/tools/ncp_query.py \
  --chapter "$CHAPTER" \
  --aspect "characters,kernwelt,integration"

# Validate scene against NCP
python ARCHON/tools/ncp_validate.py \
  --scene "$SCENE_FILE" \
  --chapter "$CHAPTER" \
  --verbose
```

**Step 5: Review Results**
```
VALIDATION REPORT:
✅ Kernwelt: KW2 sensory signature applied
✅ Characters: Alter TSDP profiles correct
❌ Integration: "we"-voice in Act I (should be fragmented)

Recommendation: Fix integration level
```

### Benefits
- ✅ Automated detection of violations
- ✅ Canonical NCP as source of truth
- ✅ Faster feedback loop
- ✅ Consistent validation (not interpretation-dependent)

### Implementation
1. Edit .claude/skills/codex.md
2. Add Workflow 1.5 (Automated Validation)
3. Update examples to show tool usage
4. Test with actual scene file

**Time estimate:** 1-2 hours
```

**User approves → Implement → Validate → Gap closed**

---

## Anti-Pattern Examples

### ❌ WRONG: Delete First, Ask Later

```
User: "This file looks old, I'll delete it"

# DON'T DO THIS
rm skill_seeker/cli/old_scraper.py
git commit -m "cleanup"
```

**Why wrong:**
- Irreversible (harder to restore)
- No documentation of why
- May break hidden dependencies

### ✅ RIGHT: Archive with Documentation

```
User: "This file looks old, let me verify first"

# Check references, git history, verification
# If truly dead → archive to .archive/ with REMOVAL_LOG.md
# Commit with descriptive message
```

---

### ❌ WRONG: Copy-Paste to Add Feature

```
User: "I need email scraping. I'll copy pdf_scraper.py and modify it"

# DON'T DO THIS
cp skill_seeker/cli/pdf_scraper.py skill_seeker/cli/email_scraper.py
# Now you have 2,000 lines of duplicated logic
```

**Why wrong:**
- Duplicates common logic (URL fetching, caching, error handling)
- Bug fixes need to be applied twice
- Maintenance burden doubles

### ✅ RIGHT: Extract Common Logic, Inherit

```
User: "I need email scraping. Let me check for existing patterns"

# Review existing scrapers
# Identify common logic (BaseScraper pattern exists in REFACTORING_PROPOSAL)
# Create EmailScraper(BaseScraper) with only email-specific logic
# Result: 200 lines instead of 2,000
```

---

### ❌ WRONG: Document Aspirationally

```markdown
## Features
- PDF extraction ✅
- Web scraping ✅
- GitHub repos ✅ ← LYING (not implemented)
```

**Why wrong:**
- Creates false user expectations
- Documentation drift
- Breaks trust

### ✅ RIGHT: Document Reality, Plan Future

```markdown
## Features
- PDF extraction ✅
- Web scraping ✅

## Planned
- GitHub repos 🔜 (see issue #42)
```

---

## Key Takeaways

1. **Audit regularly** - Monthly checks prevent accumulation
2. **Verify before removing** - git history, references, documentation
3. **Archive, don't delete** - Reversibility is crucial
4. **Integrate, don't duplicate** - Check for existing implementations
5. **Document reality** - Aspirational docs create drift
6. **Connect systems** - Find and close integration gaps
7. **User approval** - Never refactor without confirmation

---

**These examples demonstrate the Coherence Enforcer skill in action. Use them as templates for your own coherence work.**
