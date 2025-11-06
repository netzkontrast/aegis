# Rep 5 Deliverable: Using NCP for Narrative Coherence - A Complete Guide

**Quest**: Deep AEGIS System Understanding
**Rep**: 5 of 5 - Synthesis & Complete Guide
**Date**: 2025-11-06
**Status**: Quest Complete ✅

---

## Table of Contents

1. [Introduction](#introduction)
2. [The Four-Layer Validation Hierarchy](#the-four-layer-validation-hierarchy)
3. [Understanding the Architecture](#understanding-the-architecture)
4. [Workflow 1: Validating Existing Scenes](#workflow-1-validating-existing-scenes)
5. [Workflow 2: Designing New Scenes](#workflow-2-designing-new-scenes)
6. [Using ARCHON Tools](#using-archon-tools)
7. [Common Pitfalls and Solutions](#common-pitfalls-and-solutions)
8. [Advanced Techniques](#advanced-techniques)
9. [Quick Reference](#quick-reference)

---

## Introduction

### What Is the NCP Validation System?

The **Narrative Context Protocol (NCP)** validation system is a four-layer hierarchy that ensures narrative coherence in the Kohärenz Protokoll project. It transforms abstract philosophical principles (CODEX laws) into concrete, validated prose through a systematic cascade of constraints.

**Core Principle**: Every narrative element—from a single beat to an entire character arc—can be traced through four validation layers, ensuring nothing is arbitrary and everything serves the thematic and philosophical foundation.

### Why Use This System?

**Without NCP**:
- Scenes might contradict character arcs
- Thematic coherence is accidental, not structural
- World physics rules become inconsistent
- No way to validate if a scene serves the story

**With NCP**:
- Every beat traces to a thematic checkpoint
- Every checkpoint traces to NCP data
- Every NCP element traces to a CODEX law
- **Nothing is arbitrary**

### What You'll Learn

This guide teaches you to:
1. **Validate** existing scenes against all four layers (analysis)
2. **Design** new scenes using the hierarchy (synthesis)
3. **Use** ARCHON tools to automate basic queries
4. **Avoid** common validation pitfalls
5. **Master** the relationship between CODEX, NCP, and prose

---

## The Four-Layer Validation Hierarchy

### Overview

```
Layer 3: CODEX (Philosophical Foundation)
    ↓ Formalization
Layer 2: NCP (Formal Specification)
    ↓ Scene Requirements
Layer 1: Thematic Checkpoints (Scene Constraints)
    ↓ Implementation
Layer 0: Beats (Concrete Prose)
```

### Layer 3: CODEX (Philosophical Foundation)

**Location**: `PROJECT_CODEX.md`

**Function**: Defines immutable laws of the Kohärenz Protokoll universe

**Key Sections**:
- Section 1.0: Philosophical & Metaphysical Foundation
- Section 2.2: ANP-EP Phobia (central psychological conflict)
- Section 2.3: Juna/V as Exiled Core
- Section 3.1: Psycho-Architecture / Risse Causality
- Section 3.2: Kernwelten Sensory Rulesets

**Authority**: ⭐⭐⭐⭐⭐ (Highest - Immutable)

**Example Law** (Section 2.2):
> *"The central psychological conflict is the 'ANP-EP Phobia'—the phobic avoidance between the 'Apparently Normal Parts' (ANPs), who manage daily life, and the 'Emotional Parts' (EPs), who hold unprocessed trauma."*

**What to Look For**:
- Universal principles (apply to ALL scenes)
- Character system rules
- World physics laws
- Thematic mandates

---

### Layer 2: NCP (Formal Specification)

**Location**: `kohaerenz_protokoll.ncp.json`

**Function**: Translates CODEX laws into machine-readable data structures

**Key Data**:
- **Throughlines**: Dramatica structure (MC, IC, OS, SS)
- **Character Systems**: All 11 alters with types, functions, relationships, arcs
- **Structural Framework**: 39 chapters, 3 acts, narrative models
- **World Building**: Kernwelten definitions, ontological layers
- **Validation Criteria**: Forbidden actions, character constraints

**Authority**: ⭐⭐⭐⭐ (High - Formal Specification)

**Example Data** (Lex → Kiko relationship):
```json
{
  "name": "Lex",
  "type": "ANP",
  "relationships": [
    {
      "target": "All EPs",
      "type": "Phobic",
      "description": "Views emotional parts as threats to stability"
    }
  ]
}
```

**What to Look For**:
- Character types (ANP, EP, ISH)
- Relationship metadata (Phobic, Cooperative, Conflicted)
- Arc states (initial, midpoint, final)
- Throughline signposts

---

### Layer 1: Thematic Checkpoints (Scene Constraints)

**Location**: `act_1_scenes.md` (and similar scene outlines)

**Function**: Defines scene-specific requirements derived from NCP

**Format**:
```
**Thematic Checkpoints**:
- ✓ Demonstrate AEGIS's surveillance and control
- ✓ Show internal plurality through conflicting responses
- ✓ Establish ANP-EP phobia (Lex/Kael avoiding Kiko's fear)
- ✓ Guardian as embodiment of AEGIS logic
```

**Authority**: ⭐⭐⭐ (Medium-High - Scene Constraint)

**Purpose**: Bridges abstract NCP data and concrete beats

**What to Look For**:
- Scene-specific validation criteria
- Required character dynamics
- World physics requirements
- Throughline engagement

---

### Layer 0: Beats (Concrete Implementation)

**Location**: Scene outlines (beat structure) and manuscript prose

**Function**: Physical execution of thematic checkpoints

**Format**:
```
**Beat 4**: **INTRUSION**: Kiko's fear bleeds through - heart rate spikes, stammer
```

**Authority**: ⭐⭐ (Medium - Implementation)

**Purpose**: The actual prose that implements all higher layers

**What to Look For**:
- Beat count (typically 6-10 per scene)
- Internal/External rhythm
- Goal → Conflict → Outcome structure
- Character consistency
- Prose style matching act/chapter

---

## Understanding the Architecture

### The Cascade Mechanism

**How Laws Become Prose**:

1. **CODEX defines a law** (e.g., "ANP-EP Phobia exists")
2. **NCP formalizes it** (e.g., `{"type": "Phobic"}` in relationships)
3. **Checkpoints require it** (e.g., "Show Lex avoiding Kiko's fear")
4. **Beats implement it** (e.g., Beat 4: Kiko intrudes, Lex suppresses)

**Key Insight**: Each layer CONSTRAINS the layer below it.

---

### Load-Bearing vs. Arbitrary Elements

**Load-Bearing** (cannot be changed without breaking validation):
- ANP-EP Phobia (removes central conflict)
- Character types (ANP vs EP distinction)
- TSDP action systems (defines Riss types)
- Kernwelt physics (defines world rules)

**Arbitrary** (can be changed freely):
- Guardian unit numbers (734 vs 619)
- Specific location names (within Kernwelt type)
- Surface details (clothing, minor props)
- Exact word choices (as long as voice/style match)

**Test**: If removing an element breaks the validation cascade, it's load-bearing.

---

### Traceability

**Every valid element has a clear ancestry**:

```
Beat 4 (Kiko intrudes)
    ↑
Checkpoint 3 (Show ANP-EP phobia)
    ↑
NCP (Lex → Kiko: Phobic relationship)
    ↑
CODEX Section 2.2 (ANP-EP Phobia law)
```

**If you can't trace an element upward, it may be non-canonical.**

---

## Workflow 1: Validating Existing Scenes

### Step-by-Step Process

#### Phase 1: Preparation (5 minutes)

**Open three files side-by-side**:
1. `PROJECT_CODEX.md`
2. `kohaerenz_protokoll.ncp.json`
3. `act_X_scenes.md` (for the chapter)

**Identify the scene**:
- Scene ID (e.g., 1.2)
- Chapter number
- Act number

---

#### Phase 2: Layer 0 Analysis (15 minutes)

**Read the beat outline**:
- Count beats (should be 6-10)
- Identify Internal vs External beats
- Map Goal → Conflict → Outcome structure

**Questions to ask**:
- Is the beat count appropriate?
- Do beats serve clear narrative functions?
- Is there I/E rhythm?
- Does prose style match act/chapter expectations?

**Document findings** in validation table.

---

#### Phase 3: Layer 1 Validation (20 minutes)

**Check thematic checkpoints**:
- List all checkpoints for the scene
- For each checkpoint, identify which beats satisfy it
- Mark checkpoints as ✅ PASS or ❌ FAIL

**Example**:
```
Checkpoint 3: "Establish ANP-EP phobia"
- Beat 3: Lex tries logical control ✅
- Beat 4: Kiko intrudes ✅
- Beat 6: ANPs suppress EPs ✅
→ Checkpoint 3: ✅ SATISFIED
```

**Document findings** in validation table.

---

#### Phase 4: Layer 2 Validation (30 minutes)

**Query NCP data**:

**Character Validation**:
- For each active alter in scene, read their NCP profile
- Check: Type (ANP/EP), Function, Arc State, Relationships
- Verify beat behavior matches NCP profile

**Throughline Validation**:
- Identify relevant signposts (MC, OS, IC, SS)
- Verify scene engages required signposts
- Check if throughline progression is shown

**Example**:
```
Lex (Beat 3: tries logical evasion)
NCP Profile:
- Type: ANP ✅
- Function: "Analyst and intellectual controller" ✅
- Core Fear: "Chaos, emotion overwhelming logic" ✅
  (Kiko's intrusion IS his fear realized)
→ Character: ✅ COMPLIANT
```

**Document findings** in validation table.

---

#### Phase 5: Layer 3 Validation (30 minutes)

**Identify relevant CODEX laws**:
- Which laws does this scene engage?
- Are they demonstrated explicitly?

**Trace cascade**:
- Beat → Checkpoint → NCP → CODEX
- Verify each link is unbroken

**Example**:
```
Beat 4 (Kiko intrudes)
    ↑ implements
Checkpoint 3 (Show ANP-EP phobia)
    ↑ requires
NCP Line 163 (Kiko → Lex: Phobic)
    ↑ formalizes
CODEX Section 2.2 (ANP-EP Phobia law)
→ Cascade: ✅ UNBROKEN
```

**Document findings** in validation table.

---

#### Phase 6: Report Generation (15 minutes)

**Create validation summary**:

| Layer | Element | Status | Notes |
|-------|---------|--------|-------|
| Layer 3 | ANP-EP Phobia | ✅ PASS | Beats 3-4-6-7 demonstrate |
| Layer 2 | Lex profile | ✅ PASS | Matches NCP function/arc |
| Layer 2 | Kiko profile | ✅ PASS | Freeze response shown |
| Layer 1 | Checkpoint 3 | ✅ PASS | All requirements met |
| Layer 0 | Beat structure | ✅ PASS | 8 beats, clear I/E rhythm |

**Overall Status**: ✅ FULLY VALIDATED or ❌ ISSUES FOUND

**Total Time**: ~2 hours for thorough manual validation

---

### Using ARCHON Tools for Faster Validation

**Step 1: Query Chapter Info**
```bash
python ARCHON/tools/ncp_query.py --chapter 1 --verbose
```
→ Get act, thematic focus, protagonist/antagonist state

**Step 2: Query Character States**
```bash
python ARCHON/tools/ncp_query.py --character Lex --chapter 1
```
→ Get type, function, arc state

**Step 3: Validate Scene File** (if prose exists)
```bash
python ARCHON/tools/ncp_validate.py manuscript/scene.md --chapter 1 --verbose
```
→ Get automated score, warnings, issues

**Note**: Tools cover ~20% of manual validation depth. Use for first-pass filtering, then manually validate deeply.

---

## Workflow 2: Designing New Scenes

### Step-by-Step Process

#### Phase 1: Choose CODEX Law (10 minutes)

**Questions**:
- Which CODEX law do I want to demonstrate?
- Which chapter/act is this scene in?
- What narrative goal does this scene serve?

**Example**:
- Law: Psycho-Architecture / Risse Causality (Section 3.1)
- Chapter: 4
- Goal: Show Kael learning to deliberately trigger Risse

---

#### Phase 2: Select NCP Elements (20 minutes)

**Character Selection**:
- Which alters must be active to demonstrate the law?
- What are their NCP profiles (type, function, relationships, arc states)?

**Example**:
- Kael (Host, ANP) - decision-maker
- Lex (Analyst, ANP) - proposes hypothesis
- Rhys (Caregiver, ANP) - provides safety
- Kiko (Child EP, Freeze) - holds trauma → triggers temporal Riss

**Throughline Engagement**:
- Which signposts should this scene engage?
- MC: Memory (confronting traumatic memory)
- OS: Doing (AEGIS escalates surveillance)

---

#### Phase 3: Create Thematic Checkpoints (20 minutes)

**Derive scene requirements from CODEX + NCP**:

**Example Checkpoints**:
1. ✓ Demonstrate all 4 steps of psycho-architecture causality
2. ✓ Show Kael's growing agency (makes conscious choice)
3. ✓ Establish Riss-navigation as possibility (exits by healing internal state)
4. ✓ AEGIS detection and escalation

**Validation**: Each checkpoint must be traceable to NCP/CODEX.

---

#### Phase 4: Design Beat Structure (30 minutes)

**Create 6-10 beats implementing checkpoints**:

**Example**:
1. Beat 1 (I): Kael proposes hypothesis
2. Beat 2 (E): Finds trigger object
3. Beat 3 (I): Kiko activates (Freeze)
4. Beat 4 (E): Temporal Riss manifests
5. Beat 5 (I): Lex vs Rhys conflict
6. Beat 6 (I): Rhys comforts Kiko
7. Beat 7 (E): Riss collapses
8. Beat 8 (E): AEGIS detects anomaly

**Check**:
- Does each beat serve a function?
- Is there I/E rhythm?
- Does sequence satisfy all checkpoints?

---

#### Phase 5: Write Prose (60 minutes)

**Execute beats as prose**:
- Use appropriate POV (Kael System for polyphonic)
- Match prose style to act/chapter
- Include internal voice markers for polyphonic sections
- Provide sensory detail for world physics

**Example**:
```
*Lex (analytical): "The pattern is clear. Emotional intrusions precede
spatial-temporal anomalies. If we could deliberately trigger one—"*
```

---

#### Phase 6: Validate Through All Layers (30 minutes)

**Reverse validate**:
- Layer 0: Check beat structure ✅
- Layer 1: Verify all checkpoints satisfied ✅
- Layer 2: Confirm NCP character compliance ✅
- Layer 3: Trace to CODEX laws ✅

**Create validation table** (same format as Workflow 1).

**Total Time**: ~3 hours from concept to validated scene

---

## Using ARCHON Tools

### Tool 1: ncp_query.py

**Purpose**: Query NCP data without manually parsing JSON

**Common Commands**:

```bash
# Get chapter information
python ARCHON/tools/ncp_query.py --chapter 4

# Get character state at specific chapter
python ARCHON/tools/ncp_query.py --character Lex --chapter 4

# Verbose output
python ARCHON/tools/ncp_query.py --chapter 4 --verbose

# JSON output (for scripting)
python ARCHON/tools/ncp_query.py --character Kiko --json
```

**Limitations**:
- ❌ Cannot query scene data (not in NCP JSON yet)
- ❌ Cannot query relationships
- ❌ Cannot trace to CODEX laws
- ❌ Cannot show throughline signposts

---

### Tool 2: ncp_validate.py

**Purpose**: Automated scene validation (basic checks)

**Common Commands**:

```bash
# Validate a scene file
python ARCHON/tools/ncp_validate.py manuscript/scene.md

# Specify chapter for context
python ARCHON/tools/ncp_validate.py scene.md --chapter 4

# Verbose output (show all issues)
python ARCHON/tools/ncp_validate.py scene.md --verbose
```

**What It Checks**:
1. Length (word count vs act expectations)
2. Character presence (searches for names)
3. Prose style markers (fragmentation, polyphony)
4. World setting (Kernwelt names)
5. Thematic keywords (act-specific themes)

**Limitations**:
- ❌ Cannot check CODEX law compliance
- ❌ Cannot validate thematic checkpoints
- ❌ Cannot verify beat structure/function
- ❌ Keyword-based (shallow analysis)

**Best Practice**: Use tools for first-pass filtering, then manual validation for depth.

---

## Common Pitfalls and Solutions

### Pitfall 1: Confusing Character Types

**Problem**: Treating ANP and EP parts as interchangeable

**Example**:
- ❌ "Kiko (EP) provides logical analysis" (violates her function)
- ✅ "Lex (ANP) provides logical analysis" (matches function)

**Solution**: Always check NCP character type and function before assigning behavior.

---

### Pitfall 2: Ignoring Relationship Metadata

**Problem**: Characters interact in ways that contradict NCP relationships

**Example**:
- ❌ Lex and Kiko cooperate easily in Beat 3 (violates Phobic relationship)
- ✅ Lex tries to suppress Kiko, Rhys mediates (respects relationships)

**Solution**: Map character relationships before designing beats.

---

### Pitfall 3: Arbitrary Riss Types

**Problem**: Choosing glitch type without considering TSDP action system

**Example**:
- ❌ Kiko (Freeze) causes kinetic explosion (wrong system)
- ✅ Kiko (Freeze) causes temporal slowdown (matches Freeze)

**Solution**: CODEX Section 3.1 specifies Riss type = TSDP action system.

---

### Pitfall 4: Skipping Checkpoints

**Problem**: Writing beats that don't satisfy any thematic checkpoints

**Example**:
- Scene has 8 beats about Kael's daily routine
- No ANP-EP conflict shown
- No CODEX laws demonstrated
- ❌ Scene fails validation

**Solution**: Create checkpoints BEFORE writing beats. Each beat must serve a checkpoint.

---

### Pitfall 5: Bypassing Character Arcs

**Problem**: Character behaves at midpoint/final state when still in initial state

**Example**:
- Chapter 1: Lex immediately accepts emotion (violates arc)
- NCP: Lex's initial state is "Believes pure logic is the solution"
- ❌ Breaks character constraint

**Solution**: Check character arc state for current chapter. Behavior must match.

---

### Pitfall 6: Trusting Automated Validation Alone

**Problem**: Relying on ncp_validate.py score without manual verification

**Example**:
- Scene scores 8.5/10 from validator
- But violates ANP-EP Phobia law
- Automated checks miss deep issues
- ❌ False positive

**Solution**: Use tools for first pass, always manually validate Layers 3-1.

---

## Advanced Techniques

### Technique 1: Multi-Law Scenes

**Concept**: Design scenes that demonstrate multiple CODEX laws simultaneously

**Example** (Scene 1.2):
- ANP-EP Phobia (Section 2.2)
- Psycho-Architecture Causality (Section 3.1)
- AEGIS Surveillance (Section 2.1)
- KW1 Sensory Rules (Section 3.2)

**Benefit**: Maximizes thematic density, creates richer validation cascades

---

### Technique 2: Relationship Mapping

**Process**:
1. List all active alters in scene
2. Create relationship matrix from NCP

**Example**:
```
       Kael  Lex   Kiko  Nyx
Kael   —     Dep   Phob  Phob
Lex    Coop  —     Phob  Phob
Kiko   Phob  Phob  —     Dep
Nyx    Conf  Conf  Prot  —
```

**Use**: Predict interaction dynamics before writing beats

---

### Technique 3: Signpost Tracking

**Process**:
1. Create signpost progression chart for throughlines
2. Mark which scenes engage which signposts
3. Ensure even distribution across act

**Example** (MC Throughline - Act I):
- Memory: Scenes 1.1, 1.2, 1.4
- Conscious: Scenes 1.5, 1.7, 1.8
- (Ensuring progression, not repetition)

---

### Technique 4: TSDP Action System Matrix

**Process**:
1. List all EPs and their TSDP systems
2. Map expected Riss types

**Example**:
| EP | TSDP System | Riss Type |
|----|-------------|-----------|
| Kiko | Freeze | Temporal |
| Nyx | Fight | Kinetic |
| Lia | Flight | Spatial |
| Moros | Collapse | Existential void |

**Use**: Ensures Riss consistency across scenes

---

### Technique 5: Constraint-Driven Creativity

**Process**:
1. Instead of "What happens next?"
2. Ask "How does [CODEX law] manifest here?"

**Example**:
- Instead of: "Kael fights a Guardian"
- Ask: "How does ANP-EP Phobia create problems during Guardian encounter?"
- Result: Internal conflict DURING external threat (Scene 1.2)

---

## Quick Reference

### Validation Checklist

**Layer 3 (CODEX)**:
- [ ] Scene demonstrates at least one CODEX law
- [ ] Character behavior matches type (ANP/EP/ISH)
- [ ] World physics consistent with Kernwelt rules
- [ ] No forbidden actions violated

**Layer 2 (NCP)**:
- [ ] Character profiles consulted and respected
- [ ] Relationships enacted correctly
- [ ] Character arc states match chapter
- [ ] Throughline signposts engaged
- [ ] Character constraints honored

**Layer 1 (Checkpoints)**:
- [ ] All thematic checkpoints identified
- [ ] Each checkpoint mapped to specific beats
- [ ] All checkpoints satisfied

**Layer 0 (Beats)**:
- [ ] 6-10 beats present
- [ ] Goal → Conflict → Outcome structure clear
- [ ] Internal/External rhythm maintained
- [ ] Prose style matches act/chapter
- [ ] Each beat serves narrative function

---

### File Locations

| Resource | Path |
|----------|------|
| CODEX | `/PROJECT_CODEX.md` |
| NCP JSON | `/ARCHON/ncp/kohaerenz_protokoll.ncp.json` |
| Scene Outlines | `/kohaerenz_protokoll/narrative_design/act_X_scenes.md` |
| ncp_query.py | `/ARCHON/tools/ncp_query.py` |
| ncp_validate.py | `/ARCHON/tools/ncp_validate.py` |

---

### Common NCP Queries

```bash
# Chapter info
python ARCHON/tools/ncp_query.py --chapter X

# Character at chapter
python ARCHON/tools/ncp_query.py --character NAME --chapter X

# Validate scene
python ARCHON/tools/ncp_validate.py path/to/scene.md --chapter X --verbose
```

---

### Authority Hierarchy

When conflicts arise:

1. **PROJECT_CODEX.md** (highest authority)
2. **Strategic SRC notes** (framework decisions)
3. **kohaerenz_protokoll.ncp.json**
4. **MOCs** (Maps of Content)
5. **ZTL notes** (atomic principles)
6. **Character profiles**
7. **Scene outlines and manuscript**

---

## Conclusion

### What You've Learned

**Analysis (Reps 1-3)**:
- How to validate existing scenes through all four layers
- How to trace CODEX laws through NCP → Checkpoints → Beats
- How to use ARCHON tools for automated queries

**Synthesis (Rep 4)**:
- How to design new scenes using the validation hierarchy
- How to create thematic checkpoints from CODEX laws
- How to ensure coherence from concept to execution

**System Mastery (Rep 5)**:
- The relationship between CODEX, NCP, and prose
- When to use automated vs. manual validation
- Common pitfalls and how to avoid them

---

### Core Principles to Remember

1. **Nothing is arbitrary** - Every element traces to CODEX
2. **Constraints enable creativity** - Framework focuses, not limits
3. **Relationships are physics** - NCP metadata defines behavior
4. **Laws are fractal** - Same principles at all scales
5. **Validation is traceability** - If you can't trace it, question it

---

### Next Steps

**Immediate**:
- Practice validating 2-3 more scenes from Act I
- Design 1-2 original scenes for later chapters
- Create relationship matrices for key alter groups

**Medium-Term**:
- Contribute scene data to NCP JSON (enables tool queries)
- Enhance ARCHON tools (add relationship queries, CODEX tracing)
- Build scene templates for common patterns

**Long-Term**:
- Apply framework to Acts II and III
- Document edge cases and exceptions
- Share learnings with other project contributors

---

### Final Thoughts

The NCP validation system is not just a quality control mechanism—it's a **creative engine**. By providing clear constraints derived from philosophical principles, it transforms the overwhelming question "What should happen next?" into the focused question "How do these laws manifest here?"

This framework ensures that every scene, every beat, every line of dialogue serves the deeper thematic and philosophical architecture of Kohärenz Protokoll. It's the difference between writing a story about dissociation and writing a story that **performs** dissociation through its very structure.

Use it well.

---

**Rep 5 Complete**: 2025-11-06
**Quest Status**: ✅ **COMPLETE**
**Total Quest Time**: ~6 hours across 5 reps
**Deliverables Created**: 6 comprehensive documents (Reps 1-5 + this guide)
**Outcome**: Deep mastery of AEGIS validation hierarchy demonstrated through analysis, synthesis, and teaching

---

## Appendix: Case Study References

**Rep 1**: Manual Validation of Scene 1.2
- File: `rep_1_validation_chain_scene_1_2.md`
- Focus: Comprehensive 4-layer validation
- Key Learning: How to trace beats through all layers

**Rep 2**: ARCHON Tools Exploration
- File: `rep_2_tool_usage_report.md`
- Focus: Automated vs. manual validation comparison
- Key Learning: Tools provide 20% depth in 10% time

**Rep 3**: ANP-EP Phobia Law Tracing
- File: `rep_3_law_implementation_flowchart.md`
- Focus: Single law cascade from CODEX → Prose
- Key Learning: Constraint propagation mechanism

**Rep 4**: Scene 4.3 Design
- File: `rep_4_scene_design_4_3.md`
- Focus: Generative use of validation hierarchy
- Key Learning: Framework as creative tool

---

*"The story of coherence is not written by eliminating contradiction, but by integrating it into a greater truth."*

**— The Codex Authority**
