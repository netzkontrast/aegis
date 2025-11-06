---
name: coherence-enforcer
description: Maintains project coherence by detecting duplication, disconnected systems, orphaned docs, and documentation drift. Proposes and executes consolidation. Use when maintaining AEGIS architecture, refactoring, or when code feels fragmented. Keywords: coherence, refactor, consolidation, integration, duplication, architecture, maintenance, cleanup.
---

# Coherence Enforcer: Integration Through Systematic Consolidation

## Overview

**Meta-recursive principle:** This skill performs AEGIS's own philosophical theme—achieving coherence through *integration* of contradictions, not elimination.

Just as Kael's 11 alters achieve "functional multiplicity" without fusion, a coherent codebase should have distinct components that work together seamlessly. This skill identifies fragmentation disguised as modularity and transforms it into true integration.

**Authority:** This skill references and executes the REFACTORING_PROPOSAL.md strategy.

## When to Use

Use this skill when:
- **Feeling lost** in scattered documentation or duplicated workflows
- **Adding new features** that seem to duplicate existing ones
- **Maintaining architecture** and ensuring integration points are clear
- **Periodic audits** (monthly) to prevent fragmentation accumulation
- **Before major releases** to ensure system coherence
- **After rapid development sprints** where shortcuts may have fragmented design

**Symptoms this skill addresses:**
- "Where should this code go?"
- "Didn't we already implement something like this?"
- "How do these systems connect?"
- "Why do we have 3 commands that do similar things?"
- "This documentation contradicts that documentation"
- "Is this code even used anymore?"

## The Four Phases

### Phase 1: Audit
**Goal:** Scan project to identify coherence issues

**What we detect:**
1. **Code Duplication** - Similar logic across multiple files
2. **Disconnected Systems** - Components that should integrate but don't
3. **Orphaned Documentation** - Docs referencing non-existent code
4. **Documentation Drift** - Docs contradicting actual implementation
5. **Dead Code** - Unused functions, unreferenced files
6. **Unclear Structure** - Directories with ambiguous organization

**Tools:** Grep, Glob, Read, Bash (git log, file stats)

### Phase 2: Analyze & Propose
**Goal:** Categorize findings and generate consolidation plan

**Output:** Coherence audit report with prioritized recommendations

### Phase 3: Execute
**Goal:** Perform refactoring with user approval

**Actions:** Extract modules, create orchestrators, link docs, remove dead code

### Phase 4: Validate
**Goal:** Verify changes maintain functionality

**Checks:** Tests pass, references work, integration verified

---

## Workflows

### Workflow 1: Full System Audit

**Use when:** Periodic maintenance or feeling project fragmentation

#### Step 1.1: Detect Code Duplication

```bash
# Find files with similar names (often indicates duplication)
find . -name "*.md" -o -name "*.py" | sort | uniq -c | grep -v "^[[:space:]]*1 "

# Find commands with overlapping descriptions
grep -r "description:" .claude/commands/ | cut -d: -f2- | sort | uniq -c | grep -v "^[[:space:]]*1 "
```

**Manual analysis:**
- Read similar files side-by-side
- Identify overlapping logic (>30% similarity = duplication)
- Note which file is canonical

**Example finding:**
```
DUPLICATION DETECTED:
- tapestry.md: Lines 45-120 (content extraction)
- zettelkasten-tapestry.md: Lines 30-95 (content extraction)
- Overlap: ~70% similar logic
- Recommendation: Extract to _modules/extract-content.md
```

#### Step 1.2: Find Disconnected Systems

**Questions to answer:**
1. Which components reference each other in docs but not in code?
2. Which tools exist but aren't integrated into workflows?
3. Which skills/commands don't use available backend tools?

**Example finding:**
```
DISCONNECTION DETECTED:
- Codex skill (.claude/skills/codex.md) validates narratives
- ARCHON tools (ncp_validate.py) perform validation
- Status: Codex doesn't invoke ncp_validate.py
- Recommendation: Integrate Codex skill with ARCHON backend
```

**Search patterns:**
```bash
# Find skills that mention tools but don't call them
grep -r "ncp_validate" .claude/skills/ | grep -v "Bash"

# Find tools that aren't referenced in any command/skill
for tool in ARCHON/tools/*.py; do
  basename="$(basename "$tool")"
  count=$(grep -r "$basename" .claude/ | wc -l)
  if [ "$count" -eq 0 ]; then
    echo "ORPHANED TOOL: $tool"
  fi
done
```

#### Step 1.3: Detect Documentation Drift

**Methodology:**
- Read documentation's claimed behavior
- Read actual code implementation
- Note discrepancies

**Example finding:**
```
DRIFT DETECTED:
- docs/README.md claims: "Use /learn for all learning workflows"
- Reality: learn.md exists but not activated (still using tapestry)
- Recommendation: Activate learn.md or update docs
```

#### Step 1.4: Find Dead Code

```bash
# Find Python files never imported
for file in $(find . -name "*.py" -not -path "./venv/*"); do
  module=$(basename "$file" .py)
  if ! grep -r "import.*$module" --exclude="$file" . > /dev/null 2>&1; then
    echo "POTENTIALLY DEAD: $file"
  fi
done

# Find markdown files never referenced
for file in $(find . -name "*.md" -not -name "README.md"); do
  filename=$(basename "$file")
  if ! grep -r "$filename" --exclude="$file" . > /dev/null 2>&1; then
    echo "POTENTIALLY ORPHANED: $file"
  fi
done
```

**Validation required:** Check git history - recent activity indicates living code.

#### Step 1.5: Analyze Directory Structure

**Questions:**
- Are similar files grouped logically?
- Is the purpose of each directory clear?
- Do naming conventions help or confuse?

**Example finding:**
```
STRUCTURE CONFUSION:
- .claude/skills/ contains 4 operational skills
- skills/ contains 2 meta-skills
- Purpose unclear: Why two skill directories?
- Recommendation: Clarify in README or reorganize
```

---

### Workflow 2: Command Consolidation (PRIORITY 1)

**Based on:** REFACTORING_PROPOSAL.md, Part 1

**Problem:** Three commands (tapestry, ship-learn-next, zettelkasten-tapestry) with 30% duplication

**Solution:** Create unified `/learn` command with modular components

#### Step 2.1: Analyze Current Commands

1. **Read all three commands:**
   - `.claude/commands/tapestry.md`
   - `.claude/commands/ship-learn-next.md`
   - `.claude/commands/zettelkasten-tapestry.md`

2. **Identify shared logic blocks:**
   - Content extraction (tapestry + zettelkasten-tapestry)
   - Action planning (all three)
   - Knowledge management (zettelkasten-tapestry only)

3. **Map logic to modules:**
   ```
   tapestry.md:
     Lines 45-120 → extract-content.md
     Lines 121-350 → action-planner.md

   ship-learn-next.md:
     Lines 30-200 → action-planner.md (canonical version)

   zettelkasten-tapestry.md:
     Lines 30-95 → extract-content.md
     Lines 96-150 → action-planner.md
     Lines 151-219 → knowledge-manager.md
   ```

#### Step 2.2: Extract Modules

**Create:** `.claude/commands/_modules/extract-content.md`

**Content structure:**
```markdown
# Content Extraction Module

**Purpose:** Extract content from URLs (YouTube, articles, PDFs, etc.)

**Input:** URL string
**Output:** File path to extracted content

## Supported Sources
- YouTube transcripts (youtube-dl or yt-dlp)
- Web articles (readable-cli or WebFetch)
- PDFs (pdftotext)
- GitHub repositories (gh or WebFetch)

## Workflow
[Pure extraction logic - NO planning, NO knowledge management]

## Error Handling
[Dependency checks, fallbacks]

## Output Format
[Standardized markdown with metadata header]
```

**Create:** `.claude/commands/_modules/action-planner.md`

**Content structure:**
```markdown
# Action Planning Module (Ship-Learn-Next)

**Purpose:** Transform content into 5-rep implementation plan

**Input:** File path to content
**Output:** File path to action plan

## Planning Philosophy
[Rep 1 = shippable, Reps 2-5 = progressive enhancement]

## Workflow
[Analysis → Design Rep 1 → Design Reps 2-5 → Commitment questions]

## Output Format
[Standardized plan structure]
```

**Create:** `.claude/commands/_modules/knowledge-manager.md`

**Content structure:**
```markdown
# Knowledge Management Module (Zettelkasten)

**Purpose:** Save learning to knowledge vault

**Input:** Content file + plan file
**Output:** Knowledge structure summary

## Workflow
1. Create Source Note (SRC)
2. Extract atomic concepts (ZTL notes)
3. Create Quest MOC
4. Link to existing notes
5. Update vault index

## Output Format
[Links to created notes + integration summary]
```

#### Step 2.3: Create Unified Orchestrator

**Create:** `.claude/commands/learn.md`

**Content structure:**
```markdown
---
name: learn
description: Unified learning workflow - extract content from URLs, create action plans, and optionally build knowledge graphs. Use when user wants to learn from any content source (YouTube, articles, PDFs, or existing files).
---

# Learn Command - Unified Learning Workflow

## Phase 1: Detect Intent

Check input type:
- URL → needs extraction
- File path → skip to planning
- Flags: --save, --extract-only, --plan-only

## Phase 2: Execute Modules

### If URL provided:
Source: .claude/commands/_modules/extract-content.md
Run: Content extraction
Output: content_file_path

### If content exists:
Source: .claude/commands/_modules/action-planner.md
Run: Create action plan
Output: plan_file_path

### If --save flag:
Source: .claude/commands/_modules/knowledge-manager.md
Run: Save to zettelkasten
Output: knowledge_summary

## Phase 3: Present Results

Unified output format showing:
- What was created (files)
- Key insights extracted
- Next steps
- Commitment questions (if relevant)
```

#### Step 2.4: Deprecate Old Commands

**Update:** `.claude/commands/tapestry.md`

Add deprecation notice at top:
```markdown
---
name: tapestry
description: [DEPRECATED] Use /learn instead. Redirecting...
---

# ⚠️ DEPRECATED: This command has been replaced by `/learn`

The `/learn` command provides the same functionality with better modularity.

**Old usage:** `/tapestry <URL>`
**New usage:** `/learn <URL>`

Redirecting to: `/learn {{URL}}`

[Rest of file kept for reference during transition period]
```

**Repeat for:** ship-learn-next.md, zettelkasten-tapestry.md

#### Step 2.5: Update Documentation

**Update:** `.claude/commands/README.md`

Add migration guide:
```markdown
## Command Consolidation (2025-11-06)

The learning commands have been unified:

| Old Command | New Command | Notes |
|-------------|-------------|-------|
| `/tapestry <URL>` | `/learn <URL>` | Extract + Plan |
| `/ship-learn-next <file>` | `/learn <file>` | Plan only |
| `/zettelkasten-tapestry <URL>` | `/learn <URL> --save` | Extract + Plan + Save |

Old commands will redirect for 1 month, then be removed.
```

#### Step 2.6: Validate Consolidation

**Test each workflow:**
```bash
# Test extraction + planning
/learn https://example.com/article

# Test planning only
/learn existing-content.md

# Test with knowledge management
/learn https://example.com/article --save

# Verify old commands redirect
/tapestry https://example.com/article
```

**Check:**
- ✅ All workflows produce same output as before?
- ✅ No duplication in final structure?
- ✅ Modules can be updated independently?
- ✅ Documentation matches implementation?

---

### Workflow 3: Skill-Tool Integration

**Use when:** Skills reference tools but don't invoke them programmatically

**Example:** Codex skill + ARCHON tools integration

#### Step 3.1: Identify Disconnection

**Current state:**
- Codex skill (.claude/skills/codex.md) validates narrative coherence
- ARCHON tools (ncp_query.py, ncp_validate.py) exist
- Problem: Codex doesn't call ARCHON tools programmatically

**Read both:**
```bash
# Check what Codex claims to do
grep -A5 "validate" .claude/skills/codex.md

# Check what ARCHON tools actually provide
grep -A5 "def validate" ARCHON/tools/ncp_validate.py
```

#### Step 3.2: Design Integration

**Add to Codex skill:**
```markdown
### Workflow 1.5: Programmatic Validation (NEW)

**After writing a scene, validate against NCP automatically:**

1. **Identify scene context**
   ```bash
   CHAPTER="act_1/ch_01"
   SCENE_FILE="kohaerenz_protokoll/manuscript/${CHAPTER}.md"
   ```

2. **Query NCP for constraints**
   ```bash
   # Use ARCHON tool to get canonical constraints
   python ARCHON/tools/ncp_query.py \
     --chapter "$CHAPTER" \
     --aspect "characters"

   # Returns: Which alters should be active, their TSDP profiles, etc.
   ```

3. **Validate scene against NCP**
   ```bash
   # Use ARCHON tool for automated validation
   python ARCHON/tools/ncp_validate.py \
     --scene "$SCENE_FILE" \
     --chapter "$CHAPTER"

   # Returns: Validation report with pass/fail per constraint
   ```

4. **Review validation report**
   - ✅ Passed: Scene is codex-compliant
   - ❌ Failed: Shows which constraints violated, suggests fixes

**Example validation:**
```bash
$ python ARCHON/tools/ncp_validate.py --scene ch_01.md --chapter "act_1/ch_01"

VALIDATION REPORT:
✅ Kernwelt sensory signature: KW2 (Mnemosyne) - PASS
✅ Alter behavior: Nyx (EP Fight) - PASS
❌ Integration level: "we"-voice detected in Act I - FAIL
   → Recommendation: Remove collaborative language (Act I = fragmented)

Result: 2/3 constraints passed. Review required.
```
```

#### Step 3.3: Update Codex Workflow

**Edit:** `.claude/skills/codex.md`

Modify Workflow 1 (Validating a Scene) to include:

```markdown
**After writing (ENHANCED):**

4. **Validate against codex - AUTOMATED**
   ```bash
   # Run ARCHON validation tool
   python ARCHON/tools/ncp_validate.py \
     --scene "$SCENE_FILE" \
     --chapter "$CHAPTER"
   ```

5. **Review validation report**
   - Check automated findings
   - Cross-reference with manual checklist
   - If validation fails: Revise, don't rationalize

**Benefits:**
- Automated detection of constraint violations
- Canonical NCP truth source (not manual interpretation)
- Faster feedback loop
```

#### Step 3.4: Validate Integration

**Test:**
```bash
# Verify ARCHON tools work
python ARCHON/tools/ncp_query.py --chapter "act_1/ch_01" --aspect "characters"

# Verify Codex skill can call them
# (Use skill and check that Bash commands execute correctly)
```

---

### Workflow 4: Documentation Consolidation

**Use when:** Multiple docs explain similar concepts

**Problem:** 10+ documentation files with overlapping content

#### Step 4.1: Audit Documentation

**Find all primary docs:**
```bash
find . -name "README.md" -o -name "*CODEX*.md" -o -name "*REFLECTION*.md" | sort
```

**Categorize by purpose:**
```
Project overview:
- README.md (997 lines)
- .claude/README.md (494 lines)

Narrative canon:
- PROJECT_CODEX.md (186 lines, but dense)

Strategic assessment:
- PROJECT_REFLECTION_2025-11-06.md (24,508 bytes)
- REFACTORING_PROPOSAL.md (19,528 bytes)

Deep analysis:
- docs/knowledge-extraction/07-synthesis-unified-framework.md (33,784 bytes)

Skill creation:
- skills/skill-authoring/SKILL.md (373 lines)
```

#### Step 4.2: Identify Overlap

**For each category, check:**
- What unique information does each doc provide?
- What information is duplicated?
- Which is the canonical source?

**Example finding:**
```
OVERLAP DETECTED:
- README.md explains project philosophy (150 lines)
- PROJECT_REFLECTION.md explains project philosophy (200 lines)
- 07-synthesis-unified-framework.md explains philosophy (400 lines)

Analysis:
- README should be high-level overview (30-50 lines)
- PROJECT_REFLECTION is strategic assessment (keep full)
- 07-synthesis is deep dive (keep full)

Action: Simplify README, link to deeper docs
```

#### Step 4.3: Create Documentation Index

**Create:** `docs/INDEX.md`

```markdown
# AEGIS Documentation Index

**Start here:** Choose your path based on what you need.

## I want to understand the project

**Quick overview (5 minutes):**
- [README.md](../README.md) - Project purpose and components

**Strategic assessment (20 minutes):**
- [PROJECT_REFLECTION_2025-11-06.md](PROJECT_REFLECTION_2025-11-06.md) - Current state, challenges, opportunities

**Deep dive (2 hours):**
- [07-synthesis-unified-framework.md](knowledge-extraction/07-synthesis-unified-framework.md) - Comprehensive analysis

## I want to write Kohärenz Protokoll content

**Canonical reference:**
- [PROJECT_CODEX.md](../kohaerenz_protokoll/PROJECT_CODEX.md) - Immutable narrative laws

**Writing workflow:**
- [Codex Skill](../.claude/skills/codex.md) - Step-by-step validation

**Backend tools:**
- [ARCHON Tools](../ARCHON/tools/README.md) - NCP query and validation

## I want to maintain AEGIS architecture

**Consolidation strategy:**
- [REFACTORING_PROPOSAL.md](REFACTORING_PROPOSAL.md) - Current refactoring plan

**Implementation roadmaps:**
- [TDD Plans](plans/README.md) - Knowledge graph and writing assistant plans

**Coherence maintenance:**
- [Coherence Enforcer Skill](../.claude/skills/coherence-enforcer.md) - This skill!

## I want to create skills

**Meta-skill:**
- [Skill Authoring](../skills/skill-authoring/SKILL.md) - How to write skills

**Comprehensive analysis:**
- [07-synthesis-unified-framework.md](knowledge-extraction/07-synthesis-unified-framework.md) - Pattern extraction

## Component Documentation

### Commands
- [Tapestry](../.claude/commands/tapestry.md) - Content extraction + planning
- [Ship-Learn-Next](../.claude/commands/ship-learn-next.md) - Action planning
- [Zettelkasten-Tapestry](../.claude/commands/zettelkasten-tapestry.md) - KB building

### Tools
- [Skill Seeker](../skill_seeker/README.md) - Documentation → Skill converter
- [Zettelkasten Agent](../zettelkasten_agent/README.md) - Knowledge management
- [ARCHON](../ARCHON/README.md) - Narrative coherence framework

---

**Navigation principle:** Start with index, drill down as needed. Link liberally.
```

#### Step 4.4: Simplify Top-Level README

**Edit:** `README.md`

**Goal:** Reduce from 997 lines to ~200 lines

**Structure:**
1. One-sentence description (5 lines)
2. Core components (50 lines - bullet list)
3. Quick start (30 lines)
4. Links to deep docs (20 lines)
5. Contributing (20 lines)

**Move detailed content to:**
- Philosophy → docs/PROJECT_REFLECTION_2025-11-06.md
- Architecture → docs/knowledge-extraction/07-synthesis.md
- Implementation → docs/REFACTORING_PROPOSAL.md

#### Step 4.5: Update Cross-References

**For each doc, add navigation:**
```markdown
---
**See also:**
- [Documentation Index](docs/INDEX.md) - All documentation
- [PROJECT_CODEX.md](kohaerenz_protokoll/PROJECT_CODEX.md) - Canonical narrative laws
- [Coherence Enforcer](../.claude/skills/coherence-enforcer.md) - Maintenance workflow
---
```

---

### Workflow 5: Dead Code Removal

**Use when:** Unsure if code is still needed

**IMPORTANT:** Never delete without verification!

#### Step 5.1: Identify Candidates

**Find unreferenced Python files:**
```bash
for file in $(find . -name "*.py" -not -path "./venv/*" -not -name "__init__.py"); do
  module=$(basename "$file" .py)
  refs=$(grep -r "import.*$module" --exclude="$file" . 2>/dev/null | wc -l)

  if [ "$refs" -eq 0 ]; then
    echo "CANDIDATE: $file (0 imports found)"
  fi
done
```

**Find unreferenced Markdown files:**
```bash
for file in $(find . -name "*.md" -not -name "README.md"); do
  filename=$(basename "$file")
  refs=$(grep -r "$filename" --exclude="$file" . 2>/dev/null | wc -l)

  if [ "$refs" -eq 0 ]; then
    echo "CANDIDATE: $file (0 references found)"
  fi
done
```

#### Step 5.2: Verify with Git History

**Check recent activity:**
```bash
# For each candidate, check last modification date
git log -1 --format="%ai" -- "$file"

# Check commit frequency (last 6 months)
git log --since="6 months ago" --oneline -- "$file" | wc -l
```

**Decision matrix:**
| Last Modified | Commits (6mo) | References | Decision |
|---------------|---------------|------------|----------|
| > 6 months ago | 0 | 0 | **Consider removal** |
| < 6 months ago | 0 | 0 | **Review manually** |
| Any | > 0 | 0 | **Keep (active dev)** |
| Any | Any | > 0 | **Keep (in use)** |

#### Step 5.3: Safe Removal Process

**NEVER delete directly. Use git mv to archive:**

```bash
# Create archive directory
mkdir -p .archive/removed-2025-11-06/

# Move (don't delete) candidates
git mv "$dead_file" .archive/removed-2025-11-06/

# Document reason
cat > .archive/removed-2025-11-06/REMOVAL_LOG.md <<EOF
# Files Removed: 2025-11-06

## Reason
No references found, no recent activity (>6 months)

## Files
- $dead_file
  - Last modified: $(git log -1 --format="%ai" -- "$dead_file")
  - References: 0
  - Can be restored with: git mv .archive/removed-2025-11-06/$(basename "$dead_file") original/path

EOF

# Commit with reversible message
git add .archive/
git commit -m "archive: Move unreferenced files to .archive/

Files can be restored if needed. See .archive/removed-2025-11-06/REMOVAL_LOG.md"
```

**Benefits:**
- Reversible (not deleted, just moved)
- Documented (why it was removed)
- Tracked (git knows about the move)
- Safe (can be restored with git mv)

---

## Common Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|--------------|--------------|-----|
| **Copy-paste to add features** | Creates duplication, maintenance burden | Extract to module, import instead |
| **Create new command for similar workflow** | User confusion, overlapping functionality | Extend existing command with flags |
| **Document same concept in multiple places** | Documentation drift, inconsistency | Single canonical source + links |
| **Bypass existing tools** | Disconnected systems, reimplementation | Integrate with existing backend |
| **Delete code without verification** | Breaks hidden dependencies | Archive to `.archive/`, document |
| **Refactor without tests** | Breaks functionality, no validation | Write tests first, validate after |
| **Create abstraction too early** | Over-engineering, premature complexity | Wait for 3+ use cases, then abstract |
| **Never remove anything** | Accumulate dead code, confusion | Safe archival process (git mv) |

---

## Checklist: Coherence Audit

**Run this monthly or before major releases:**

### Code Structure
- [ ] No duplicated logic (>30% similarity) across files?
- [ ] All commands use shared modules where possible?
- [ ] Skills invoke backend tools programmatically (not manual)?
- [ ] Directory structure is clear and documented?

### Documentation
- [ ] No contradictions between docs and code?
- [ ] No orphaned docs (referencing non-existent code)?
- [ ] Single canonical source for each concept?
- [ ] Clear navigation between related docs?
- [ ] Documentation index exists and is up-to-date?

### Integration
- [ ] Related systems reference each other in code (not just docs)?
- [ ] Backend tools are utilized by frontend workflows?
- [ ] Knowledge flows between components (not siloed)?
- [ ] New features extend existing systems (not parallel implementations)?

### Maintenance
- [ ] No dead code (unreferenced for >6 months)?
- [ ] Git history shows recent activity for all active files?
- [ ] Tests exist for all critical workflows?
- [ ] Refactoring proposals are documented and tracked?

### Meta-Coherence
- [ ] Project performs its own theme (integration, not elimination)?
- [ ] Distinct components work together (functional multiplicity)?
- [ ] Architecture enables rather than constrains?
- [ ] Complexity is justified (not accidental)?

---

## Integration with Other Skills

**Combine with:**
- **Codex**: For narrative coherence (this skill handles code coherence)
- **Ship-Learn-Next**: For planning refactoring implementations
- **Zettelkasten-Tapestry**: For saving coherence insights

**Coherence Enforcer provides:**
- **Structural hygiene** (clean architecture)
- **Integration patterns** (how to connect systems)
- **Consolidation strategies** (reduce duplication)

**Other skills provide:**
- **Domain logic** (what to build)
- **Narrative principles** (creative constraints)
- **Learning workflows** (how to improve)

---

## Quick Decision Tree

```
Feeling project fragmentation?
  ↓
What type of issue?
  ↓
"Duplicated code" → Workflow 2 (Command Consolidation)
  ↓
"Disconnected systems" → Workflow 3 (Skill-Tool Integration)
  ↓
"Scattered docs" → Workflow 4 (Documentation Consolidation)
  ↓
"Dead code?" → Workflow 5 (Safe Removal)
  ↓
"General audit" → Workflow 1 (Full System Audit)
  ↓
Apply workflow → Generate report → Get approval → Execute → Validate
```

---

## Red Flags

🛑 **STOP if you notice:**

- Creating new command/skill that duplicates existing functionality
- Writing documentation without checking existing docs
- Implementing feature without searching for existing implementation
- Deleting code without git history check
- Refactoring without understanding integration points
- Abstracting before seeing 3+ use cases
- Consolidating without preserving distinct purposes
- Forcing unification where separation is correct

**All of these violate coherence principles. STOP. Audit. Plan. Execute with approval.**

---

## Meta: Skill Maintenance

- **Version:** 1.0.0
- **Based on:** docs/REFACTORING_PROPOSAL.md
- **Authority:** Execute proposals with user approval
- **Last updated:** 2025-11-06
- **Review frequency:** Monthly audit recommended

---

## Example: Complete Audit Report

```markdown
# AEGIS Coherence Audit Report
**Date:** 2025-11-06
**Auditor:** Coherence Enforcer Skill v1.0.0

## Executive Summary

- **Code Health:** 🟡 Moderate (duplication detected)
- **Documentation:** 🟡 Moderate (fragmentation detected)
- **Integration:** 🔴 Needs Work (disconnections found)
- **Dead Code:** 🟢 Good (minimal orphans)

## Findings

### CRITICAL: Command Duplication
- **Location:** .claude/commands/
- **Issue:** 3 commands with 30% overlapping logic
- **Files:** tapestry.md, ship-learn-next.md, zettelkasten-tapestry.md
- **Impact:** HIGH - Maintenance burden, user confusion
- **Recommendation:** Implement REFACTORING_PROPOSAL Part 1 (Unified /learn command)
- **Effort:** 1-2 weeks
- **Priority:** 🔴 P0 (Do first)

### HIGH: Codex-ARCHON Disconnection
- **Location:** .claude/skills/codex.md + ARCHON/tools/
- **Issue:** Codex skill doesn't invoke ARCHON tools programmatically
- **Impact:** MEDIUM - Manual validation, less reliable
- **Recommendation:** Integrate Codex with ncp_validate.py
- **Effort:** 2-3 days
- **Priority:** 🟡 P1 (Do soon)

### MEDIUM: Documentation Fragmentation
- **Location:** README.md, docs/
- **Issue:** 10+ docs explaining similar concepts
- **Impact:** MEDIUM - Onboarding confusion, drift risk
- **Recommendation:** Create docs/INDEX.md, simplify README
- **Effort:** 1 week
- **Priority:** 🟡 P1 (Do soon)

### LOW: Skill Directory Ambiguity
- **Location:** .claude/skills/ vs skills/
- **Issue:** Two directories, unclear separation
- **Impact:** LOW - Minor confusion
- **Recommendation:** Document purpose in README
- **Effort:** 1 hour
- **Priority:** 🟢 P2 (Nice to have)

## Recommended Implementation Order

1. **Week 1-2:** Command consolidation (REFACTORING_PROPOSAL Part 1)
2. **Week 2:** Codex-ARCHON integration
3. **Week 3:** Documentation consolidation
4. **Week 3:** Skill directory clarification

## Success Metrics

- ✅ Reduce duplication from ~2,000 lines to <100 lines
- ✅ Single entry point for learning workflows (/learn)
- ✅ Automated validation (Codex + ARCHON)
- ✅ Documentation index with <5 min navigation time
- ✅ Zero contradictions between docs and code

## Next Steps

1. Review this audit report
2. Approve P0 items (command consolidation)
3. Create feature branch: refactor/unified-learning-command
4. Execute with validation
5. Re-audit in 1 month

---
**This report represents the current state. Track progress in todos.**
```

---

**End of Coherence Enforcer Skill**

*"Coherence through integration of contradictions, not elimination."*
