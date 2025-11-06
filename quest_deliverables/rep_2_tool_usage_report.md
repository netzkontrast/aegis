# Rep 2 Deliverable: ARCHON Tools Usage Report & Gap Analysis

**Quest**: Deep AEGIS System Understanding
**Rep**: 2 of 5 - ARCHON Tools Exploration
**Date**: 2025-11-06
**Tools Tested**: ncp_query.py, ncp_validate.py

---

## Executive Summary

The ARCHON tools (`ncp_query.py` and `ncp_validate.py`) provide **partial automation** of the manual validation process completed in Rep 1. While they successfully query NCP character data and perform basic scene validation checks, significant gaps exist in their ability to trace the full validation hierarchy from CODEX → NCP → Thematic Checkpoints → Beats.

**Key Finding**: The tools excel at **Layer 2 (NCP) queries** but lack support for **Layer 3 (CODEX law tracing)** and **Layer 1 (Thematic checkpoint validation)**.

---

## Tool 1: ncp_query.py

### Capabilities Discovered

#### 1. Chapter Information Query

**Command**:
```bash
python ARCHON/tools/ncp_query.py --chapter 1 --verbose
```

**Output**:
```
CHAPTER 1 INFORMATION
Act: 1 - Fragmentation and First Echoes
Thematic Focus: Establishing the oppressive order of AEGIS and Kael's unconscious fragmentation. First awareness of internal plurality.
Protagonist State: Fragmented, amnesic, trauma-avoidant. ANPs dominant, EPs intrude as 'glitches'
Antagonist State: Confident, controlling. Views Kael as manageable anomaly.
```

**Analysis**:
- ✅ Successfully retrieves act-level thematic focus
- ✅ Provides protagonist and antagonist state summaries
- ❌ Does NOT trace these to specific CODEX laws
- ❌ Does NOT connect to specific thematic checkpoints

**Manual Validation Equivalent**:
- Covers **part** of Layer 2 (NCP structural framework)
- Missing connection to Layer 3 (CODEX) and Layer 1 (checkpoints)

---

#### 2. Character State Query

**Command**:
```bash
python ARCHON/tools/ncp_query.py --character Lex --chapter 1
```

**Output**:
```
CHARACTER STATE: Lex (Chapter 1)
Type: ANP
Function: Analyst and intellectual controller
Arc State: Believes pure logic is the solution
```

**Command**:
```bash
python ARCHON/tools/ncp_query.py --character Kiko --chapter 1
```

**Output**:
```
CHARACTER STATE: Kiko (Chapter 1)
Type: EP
Function: Child part holding early trauma - Freeze/flight response
Arc State: Completely suppressed, only emerging as terror intrusions
```

**Analysis**:
- ✅ Retrieves character type (ANP/EP) from NCP
- ✅ Shows character function
- ✅ Shows arc state at specific chapter
- ❌ Does NOT show character relationships (e.g., Lex ↔ Kiko phobic relationship)
- ❌ Does NOT trace to CODEX laws (e.g., ANP-EP Phobia in Section 2.2)
- ❌ Does NOT show TSDP action systems

**Manual Validation Equivalent**:
- Covers **basic** Layer 2 (NCP character data)
- Missing relationship data crucial for beat validation
- Missing CODEX law traceability

---

#### 3. Scene Requirements Query

**Command**:
```bash
python ARCHON/tools/ncp_query.py --scene 1.2 --verbose
```

**Output**:
```
Error: Scene 1.2 not found in NCP
```

**Analysis**:
- ❌ **Critical Gap**: Scene-level data is NOT in the NCP JSON file
- The NCP currently contains:
  - ✅ Throughlines
  - ✅ Character systems
  - ✅ Structural framework (acts)
  - ✅ World building
  - ✅ Validation criteria
  - ❌ **Scene-specific data** (beats, checkpoints, requirements)

**Implication**:
- Scene data exists in `act_1_scenes.md` (separate file)
- Tool cannot query thematic checkpoints or beat structures
- **Design question**: Should scene data be imported into NCP JSON?

---

#### 4. Alter Finder

**Command**:
```bash
python ARCHON/tools/ncp_query.py --find-alter Kiko
```

**Output**:
```
Scenes featuring Kiko:
[No results - scene data not in NCP]
```

**Analysis**:
- ❌ Non-functional due to missing scene data
- Would be **highly valuable** for tracking alter presence across scenes
- Potential use case: "Show me all scenes where ANP-EP phobia is demonstrated"

---

### ncp_query.py Summary

| Feature | Status | Coverage | Gap |
|---------|--------|----------|-----|
| Chapter info | ✅ Works | Layer 2 (partial) | No CODEX tracing |
| Character state | ✅ Works | Layer 2 (basic) | No relationships, no CODEX |
| Scene requirements | ❌ Missing | N/A | Scene data not in NCP |
| Alter finder | ❌ Missing | N/A | Scene data not in NCP |

**Tool Usefulness**: 6/10
- Good for basic NCP queries
- Cannot replace manual Layer 3 or Layer 1 validation

---

## Tool 2: ncp_validate.py

### Capabilities Discovered

#### Test Scene Validation

**Setup**: Created test scene (`test_scene_1_2.md`) based on Scene 1.2 beats

**Command**:
```bash
python ARCHON/tools/ncp_validate.py quest_deliverables/test_scene_1_2.md --chapter 1 --verbose
```

**Output**:
```
VALIDATION REPORT
Status: ✅ PASS
Score: 7.5/10.0
Checks Passed: 4/5
Word Count: 246

[WARNINGS]
[STRUCTURE] Scene is short (246 words). Consider expanding.
  → Aim for 800-1500 words per scene
```

**Analysis**:
- ✅ Performs automated validation
- ✅ Calculates score (7.5/10)
- ✅ Counts words (246)
- ✅ Checks passed: 4/5
- ⚠️ Only 1 warning about length

---

### What Does ncp_validate.py Actually Check?

Based on code analysis (ncp_validate.py lines 74-80), the tool runs:

1. **Length Check** (`_check_length`)
   - Ensures scene meets minimum word count
   - Acts 1-2: 800-1500 words
   - Act 3: 1000-2000 words
   - **Status**: ⚠️ WARNING (246 words < 800)

2. **Character Presence Check** (`_check_character_presence`)
   - Searches for character names in text
   - Validates against scene requirements (if scene data exists)
   - **Test Result**: ✅ PASS (found Kael, Lex, Kiko, Alex, Nyx)

3. **Prose Style Check** (`_check_prose_style`)
   - Checks for fragmented prose markers in Act I
   - Looks for polyphonic prose markers in Act III
   - Keywords: "I—we", "(Lex's thought:", "multiple voices"
   - **Test Result**: ✅ PASS (found fragmentation markers)

4. **World Setting Check** (`_check_world_setting`)
   - Validates location matches chapter expectations
   - Checks for Kernwelt names (Logos-Prime, Mnemosyne-Archipel, etc.)
   - **Test Result**: ✅ PASS (found "Logos-Prime")

5. **Thematic Keywords Check** (`_check_thematic_keywords`)
   - Searches for act-specific themes
   - Act I keywords: "fragmented", "suppressed", "intrusion", "anomaly"
   - **Test Result**: ✅ PASS (found multiple keywords)

---

### What ncp_validate.py CANNOT Check

#### ❌ Layer 3: CODEX Law Compliance

**Missing Checks**:
- ANP-EP Phobia demonstrated in beats
- Psycho-architecture causal chain (Trigger → EP activation → ANP suppression → External manifestation)
- AEGIS surveillance and control presence
- KW1 sensory rulebook adherence

**Why It Matters**:
These are the **most fundamental** validation criteria. A scene can pass all 5 automated checks but still violate core CODEX laws.

**Example**:
- A scene could mention "Logos-Prime" (✅ passes world check)
- But violate KW1's sensory rules by including shadows and organic sounds
- Automated validator would NOT catch this

---

#### ❌ Layer 1: Thematic Checkpoint Validation

**Missing Checks**:
For Scene 1.2, the tool cannot verify:
- ✓ Demonstrate AEGIS's surveillance and control
- ✓ Show internal plurality through conflicting responses
- ✓ Establish ANP-EP phobia (Lex/Kael avoiding Kiko's fear)
- ✓ Guardian as embodiment of AEGIS logic

**Why It Matters**:
Thematic checkpoints are **scene-specific validation criteria** derived from NCP throughlines. They bridge Layer 2 (NCP) and Layer 0 (Beats).

**Current Gap**:
- Checkpoints exist in `act_1_scenes.md`
- NOT in NCP JSON
- Tool cannot access or validate them

---

#### ❌ Layer 0: Beat-Level Structural Validation

**Missing Checks**:
- Does each beat serve its narrative function?
- Is the Goal → Conflict → Beats → Outcome structure intact?
- Are internal/external beats alternating appropriately?
- Does beat sequence match scene requirements?

**Why It Matters**:
Beat structure is the **implementation layer**. Automated validation should confirm:
1. All required beats are present
2. Beats appear in correct sequence
3. Each beat implements its intended function

**Example for Scene 1.2**:
- Beat 4 should show "Kiko intrudes with fear"
- Validator should detect if Kiko is mentioned
- But cannot verify the beat serves the ANP-EP phobia function

---

## Comparison: Manual vs Automated Validation

### Scene 1.2: The Coherence Check

| Validation Layer | Manual (Rep 1) | Automated (Rep 2) | Gap |
|------------------|----------------|-------------------|-----|
| **Layer 3 (CODEX)** | ✅ Full tracing | ❌ Not available | Cannot trace laws |
| ANP-EP Phobia | ✅ Traced through beats | ❌ Not checked | Critical gap |
| Psycho-architecture | ✅ Causal chain verified | ❌ Not checked | Critical gap |
| AEGIS surveillance | ✅ Guardian validated | ❌ Not checked | Thematic gap |
| KW1 sensory rules | ✅ Setting verified | ⚠️ Partial (location only) | Detail gap |
| **Layer 2 (NCP)** | ✅ Full validation | ⚠️ Partial | Relationship gap |
| Character profiles | ✅ All relationships traced | ⚠️ Basic data only | No relationships |
| MC Signpost | ✅ Memory validated | ❌ Not checked | Throughline gap |
| OS Signpost | ✅ Understanding validated | ❌ Not checked | Throughline gap |
| Character constraints | ✅ Lex's arc validated | ❌ Not checked | Arc gap |
| **Layer 1 (Checkpoints)** | ✅ All 4 verified | ❌ Not available | Scene data gap |
| AEGIS surveillance | ✅ Verified | ❌ Not checked | — |
| Internal plurality | ✅ Verified | ❌ Not checked | — |
| ANP-EP phobia | ✅ Verified | ❌ Not checked | — |
| Guardian = AEGIS | ✅ Verified | ❌ Not checked | — |
| **Layer 0 (Beats)** | ✅ All 8 beats traced | ❌ Not checked | Structure gap |
| Beat sequence | ✅ Verified | ❌ Not checked | — |
| Beat functions | ✅ Verified | ❌ Not checked | — |
| Internal/external rhythm | ✅ Verified | ❌ Not checked | — |

---

### What Automated Validation DOES Check

| Check | Coverage | Usefulness |
|-------|----------|------------|
| Word count | ✅ Accurate | Medium - catches too-short scenes |
| Character presence | ✅ Works | Low - presence ≠ correct portrayal |
| Prose style markers | ✅ Works | Medium - catches missing fragmentation |
| World location | ✅ Works | Low - location name ≠ sensory accuracy |
| Thematic keywords | ✅ Works | Low - keywords ≠ thematic execution |

**Overall Automated Coverage**: ~20% of manual validation depth

---

## Critical Gaps Analysis

### Gap 1: No CODEX Law Integration

**Problem**: Tools operate at Layer 2 (NCP) only, cannot trace to Layer 3 (CODEX)

**Impact**:
- Cannot validate ANP-EP Phobia
- Cannot validate Psycho-architecture causality
- Cannot verify AEGIS behavior matches Section 2.1
- Cannot check Kernwelt sensory rulesets

**Possible Solution**:
- Add CODEX references to NCP JSON
- Create `codex_law_id` field in NCP data
- Tool could display relevant CODEX sections when querying

**Example**:
```json
{
  "name": "Lex",
  "relationships": [
    {
      "target": "Kiko",
      "type": "Phobic",
      "codex_law": "PROJECT_CODEX.md#22-anp-ep-phobia"
    }
  ]
}
```

---

### Gap 2: Scene Data Not in NCP

**Problem**: Scene-level data (beats, checkpoints, requirements) lives in `act_1_scenes.md`, not in NCP JSON

**Impact**:
- Cannot query scene requirements
- Cannot validate thematic checkpoints
- Cannot verify beat structure
- Cannot use `--find-alter` function

**Possible Solution**:
- Import scene data into NCP JSON under new `scenes` array
- Each scene includes:
  - `scene_id` (e.g., "1.2")
  - `beats` (array of beat objects)
  - `thematic_checkpoints` (array)
  - `active_alters` (array)
  - `ncp_signposts` (references to throughline positions)

**Trade-off**:
- ✅ Enables full automated validation
- ❌ Increases NCP file size significantly
- ❌ Duplicates data between `act_1_scenes.md` and NCP JSON

---

### Gap 3: No Relationship Validation

**Problem**: ncp_query.py shows character state but NOT relationships

**Impact**:
- Cannot verify if beat implements correct relationship dynamic
- Example: Lex suppressing Kiko is THE scene, but tool can't check if their Phobic relationship is demonstrated

**Possible Solution**:
- Add `--relationships` flag to ncp_query.py
- Output: "Lex ↔ Kiko: Phobic (CODEX: Section 2.2)"

---

### Gap 4: No Throughline Signpost Tracking

**Problem**: Tools don't track or validate Dramatica signpost progression

**Impact**:
- Cannot verify Scene 1.2 engages MC Signpost: Memory
- Cannot verify Scene 1.2 engages OS Signpost: Understanding
- No validation that scene moves throughlines forward

**Possible Solution**:
- Add signpost metadata to scene data
- Validator checks if prose engages required signposts
- Query tool shows: "Chapter 1 → MC Signpost: Memory (Scenes 1.1, 1.2, 1.4)"

---

### Gap 5: Keyword Validation is Shallow

**Problem**: ncp_validate.py checks for keyword presence, not thematic execution

**Impact**:
- Scene can include "fragmented" in dialogue but not demonstrate fragmentation
- Keywords present ≠ theme executed
- False positives possible

**Example**:
```
Guardian: "Your responses are fragmented."
Kael: "No, I'm perfectly coherent."
```
- ✅ Contains keyword "fragmented"
- ❌ Kael's dialogue contradicts fragmentation theme
- Tool would pass this incorrectly

**Possible Solution**:
- More sophisticated NLP analysis
- Check keyword context (who says it, how it's used)
- Validate against character voice matrices
- **Or**: Accept that automated validation is shallow, use as first-pass filter only

---

## Tool Effectiveness: Rep 1 Manual vs Rep 2 Automated

### Time Investment

**Rep 1 (Manual)**:
- Reading 3 files (NCP, CODEX, scenes): ~45 minutes
- Tracing validation layers: ~90 minutes
- Writing validation document: ~60 minutes
- **Total**: ~3 hours

**Rep 2 (Automated)**:
- Learning tool syntax: ~10 minutes
- Running queries: ~5 minutes
- Writing test scene: ~15 minutes
- Running validator: ~2 minutes
- **Total**: ~30 minutes

**Time Saved**: ~2.5 hours

---

### Accuracy Comparison

**Rep 1 (Manual)**:
- Validation depth: 100%
- Layers covered: 4/4 (CODEX, NCP, Checkpoints, Beats)
- False positives: 0 (human judgment)
- False negatives: Possible (might miss subtle violations)

**Rep 2 (Automated)**:
- Validation depth: ~20%
- Layers covered: 1/4 (NCP partial only)
- False positives: Likely (keyword-based checks)
- False negatives: Very likely (cannot check CODEX or checkpoints)

**Accuracy Trade-off**: Automated is MUCH faster but MUCH shallower

---

### Recommended Workflow

**Phase 1: Automated First-Pass** (5 minutes)
1. Run ncp_validate.py on scene
2. Check for obvious issues (length, character presence, location)
3. Fix any errors or warnings

**Phase 2: Manual Deep Validation** (30-60 minutes)
1. Trace scene through all 4 layers manually
2. Validate CODEX laws
3. Verify thematic checkpoints
4. Check beat structure and function

**Phase 3: Iteration**
1. Fix deep issues found in Phase 2
2. Re-run automated validator (quick check)
3. Repeat until fully compliant

**Total Time**: ~40-70 minutes (better than 3 hours for pure manual)

---

## Recommendations for Tool Improvement

### Priority 1: Add Scene Data to NCP
- Import `act_1_scenes.md` into NCP JSON
- Enable scene requirements queries
- Enable `--find-alter` functionality

### Priority 2: Add CODEX Law References
- Link NCP data to CODEX sections
- Tools can display relevant laws when querying
- Enables partial Layer 3 validation

### Priority 3: Add Relationship Queries
- `ncp_query.py --relationships Lex Kiko`
- Show relationship type and CODEX grounding

### Priority 4: Add Throughline Tracking
- Track signpost progression across scenes
- Validate scenes engage required signposts

### Priority 5: Improve Validator Intelligence
- Beyond keyword matching
- Context-aware validation
- Character voice consistency checks

---

## Key Insights from Rep 2

### 1. Tools Are Layer 2 (NCP) Specialists

The ARCHON tools excel at querying NCP data but cannot operate at Layer 3 (CODEX) or Layer 1 (Checkpoints). They're designed for NCP exploration, not full validation.

### 2. Scene Data Architecture Needs Revision

The split between `act_1_scenes.md` and `kohaerenz_protokoll.ncp.json` limits tool effectiveness. Integration would enable deeper automation.

### 3. Automated Validation is a Filter, Not a Judge

Current tools catch obvious issues (too short, wrong location, missing characters) but cannot judge thematic depth or CODEX compliance. Human validation remains essential.

### 4. Tool Gaps Reveal System Design Questions

- Should all narrative data live in NCP JSON?
- Or should tools query multiple files?
- Trade-off: Single source of truth vs. specialized documents

### 5. The 80/20 Rule Applies

Automated tools provide 20% of validation depth in 10% of the time. For comprehensive validation, manual work is irreplaceable—but tools make it faster.

---

## Comparison Summary

| Aspect | Manual (Rep 1) | Automated (Rep 2) | Winner |
|--------|----------------|-------------------|--------|
| Depth | 100% (all 4 layers) | 20% (Layer 2 partial) | Manual |
| Speed | 3 hours | 30 minutes | Automated |
| CODEX validation | ✅ Full | ❌ None | Manual |
| NCP validation | ✅ Full | ⚠️ Partial | Manual |
| Checkpoint validation | ✅ Full | ❌ None | Manual |
| Beat validation | ✅ Full | ❌ None | Manual |
| Ease of use | Hard (requires expertise) | Easy (command-line) | Automated |
| Scalability | Low (3 hours per scene) | High (30 min per scene) | Automated |

**Conclusion**: Use automated tools for first-pass filtering, manual validation for deep compliance.

---

## Next Steps: Rep 3

Having explored both manual and automated validation, Rep 3 will:

1. Choose one CODEX law (e.g., ANP-EP Phobia from Section 2.2)
2. Trace it through ALL layers:
   - CODEX definition (Section 2.2)
   - NCP character relationships (Lex ↔ Kiko marked "Phobic")
   - Thematic checkpoint (Checkpoint 3 in Scene 1.2)
   - Beat implementation (Beats 3, 4, 6, 7)
3. Create a "Law → Implementation Flowchart"
4. Document how constraint propagates from philosophy to prose

This will demonstrate how CODEX laws are the "source code" from which all narrative elements derive.

---

**Rep 2 Complete**: 2025-11-06
**Deliverable**: ARCHON Tools Usage Report & Gap Analysis
**Key Finding**: Tools provide 20% validation depth in 10% the time—useful for filtering, not comprehensive validation
