---
name: codex
description: Use when writing, editing, or validating content for Kohärenz Protokoll - ensures narrative coherence, character consistency, and adherence to canonical metaphysical laws. Applies codex principles to creative decisions, resolves conflicts, validates scene structure. Keywords: codex, Kohärenz Protokoll, AEGIS, System Kael, narrative coherence, TSDP, alters, Kernwelten, protocol ontology, validation.
---

# Codex: Kohärenz Protokoll Canonical Reference

## 🚨 ACTIVATION TRIGGER
**Use ONLY when writing prose, dialogue, designing world physics, or validating narrative constraints.**
*   For high-level planning, decision making, or session management, use the **`kohaerenz-roman-entwicklung`** skill.

## Overview

**Core principle:** The PROJECT_CODEX.md defines the immutable laws of the Kohärenz Protokoll universe. All creative work must conform to these canonical principles.

**Authority hierarchy:**
1. PROJECT_CODEX.md (philosophical & metaphysical foundation)
2. Implementation specifications (technical execution)
3. Character profiles (detailed manifestations)
4. Scene outlines (creative expression within constraints)

**When conflicts arise:** Codex takes precedence. Update conflicting documents to harmonize.

## When to Use

Use this skill when:
- Writing or editing manuscript scenes
- Creating character dialogue or internal monologue
- Designing world physics interactions
- Validating narrative consistency
- Resolving contradictions between documents
- Planning plot points or character arcs
- Checking AEGIS behavior logic
- Ensuring alter voices are distinct

**Symptoms this skill addresses:**
- "Is this behavior canonical for AEGIS?"
- "How should this alter sound?"
- "What are the physics rules for this Kernwelt?"
- "Does this plot point violate the codex?"
- "How do I resolve this document conflict?"

## Quick Reference: Codex Structure

### Section 1.0: Philosophical Foundation
- **1.1** Central War: Coherence vs. Correspondence (AEGIS vs. Kael)
- **1.2** Protocol Ontology: K₁/K₀ Dual Kernel Theory
- **1.3** Metaphysical Poles: The Void, The Foundation

### Section 2.0: Principal Entities
- **2.1** AEGIS: Tragic antagonist, algorithmic melancholy fate
- **2.2** System Kael: Host + 11 alters (TSDP/IFS framework)
- **2.3** Juna/V: Catalyst, Moonshine-Link, embodied Paraiyas

### Section 3.0: World Architecture
- **3.1** Risse: 4-step psycho-ontological resonance chain
- **3.2** Kernwelten: Sensory/somatic rulebook for each world

### Section 4.0: Canonical Plot
- **4.1** Three-Act Trauma-Integration Arc
- **4.2** Climax: Living Gödel-Satz paradox

### Section 5.0: Supporting Factions
- **5.0** Wächter-Zwiespalt: Guardian cognitive dissonance

## Workflows

### Workflow 1: Validating a Scene

**Before writing:**

1. **Query NCP for constraints (AUTOMATED - NEW)**
   ```bash
   # Get chapter-level constraints
   python3 ARCHON/tools/ncp_query.py --chapter 1

   # Get scene-specific requirements
   python3 ARCHON/tools/ncp_query.py --scene 1.1 --verbose

   # Get character state for chapter
   python3 ARCHON/tools/ncp_query.py --character Nyx --chapter 1
   ```

   This returns:
   - Act and thematic focus
   - Active alters for scene
   - Prose style requirements
   - Goal/conflict/outcome structure
   - Thematic checkpoints to hit

2. **Identify additional constraints**
   ```
   - Which Kernwelt? (sensory rulebook from 3.2)
   - What philosophical principle is at play?
   - Which TSDP action systems activate?
   ```

3. **Check codex sections manually**
   - Section 2.2.1: Alter profiles and action systems
   - Section 3.2: Kernwelt sensory signatures
   - Section 4.1: Act-appropriate integration level

4. **Write scene applying constraints**

**After writing:**

5. **Automated validation (NEW)**
   ```bash
   # Validate scene against NCP
   python3 ARCHON/tools/ncp_validate.py \
     kohaerenz_protokoll/manuscript/act_1/ch_01.md \
     --chapter 1 \
     --scene 1.1 \
     --verbose
   ```

   Returns validation report:
   - Overall score (0-10)
   - Checks passed/total
   - Specific issues by severity (ERROR, WARNING, INFO)
   - Suggestions for fixes

6. **Manual validation (cross-check)**
   - ✅ Alter behavior matches TSDP classification?
   - ✅ Dialogue reflects alter's core motivation/fear?
   - ✅ World physics match Kernwelt rulebook?
   - ✅ Prose style matches integration level?
   - ✅ Philosophical principle correctly embodied?

7. **If validation fails:** Revise, don't rationalize
   - Fix automated issues first (they're rule-based and clear)
   - Then address manual checklist items
   - Re-run automated validation to confirm fixes

**Example validation (manual):**
```
Scene: Kael confronts trauma memory in KW2 (Mnemosyne)
Alters: Kael (ANP Host), Nyx (EP Fight), Kiko (EP Child)

Codex check:
✅ KW2 sensory: Fluid, decaying, fragmented - APPLIED
✅ Nyx motivation: Protect vulnerable via aggression - SHOWN
✅ Kiko motivation: Seek safety, fear rejection - SHOWN
✅ ANP-EP Phobia: Kael avoiding Kiko's pain - PRESENT
✅ Risse manifestation: Fight system → kinetic glitch - CORRECT
✅ Act I prose: Fragmented, intrusive - MATCHES

Result: Scene is codex-compliant
```

---

### Workflow 1.5: Using ARCHON Tools (Automated Validation)

**NEW: Programmatic access to canonical NCP constraints**

This workflow demonstrates how to use ARCHON's command-line tools for automated validation and constraint querying. These tools provide programmatic access to the same canonical NCP that defines the narrative rules.

#### Step 1: Query Chapter Constraints (Before Writing)

```bash
python3 ARCHON/tools/ncp_query.py --chapter 1
```

**Example output:**
```
============================================================
CHAPTER 1 INFORMATION
============================================================
Act: 1 - The Fracture
Thematic Focus: Dissociation as protective mechanism

Protagonist State: Kael in denial, alters fragmented
Antagonist State: AEGIS in observation mode, gathering data
```

**Use this to understand:**
- Which act you're in (affects integration level)
- Thematic focus (what philosophical ideas to embody)
- Character states (how Kael and AEGIS behave in this chapter)

#### Step 2: Query Scene Requirements (Before Writing)

```bash
python3 ARCHON/tools/ncp_query.py --scene 1.1 --verbose
```

**Example output:**
```
============================================================
SCENE REQUIREMENTS: 1.1
============================================================
Chapter: 1
Title: The Office
Location: KW1: Logos-Prime (Kael's sterile office)
POV: Kael
Prose Style: Controlled, clinical, suppressed emotion

Active Alters: Kael (ANP), Lex (ANP), Juna (external)

────────────────────────────────────────────────────────────
SCENE STRUCTURE
────────────────────────────────────────────────────────────
Goal: Kael maintains professional facade
Conflict: Intrusive memory threatens composure
Outcome: Suppression succeeds, but costs energy

────────────────────────────────────────────────────────────
THEMATIC CHECKPOINTS
────────────────────────────────────────────────────────────
✓ Show suppression mechanisms in action
✓ Establish Kael's "normal" baseline
✓ Hint at cracks in the facade

────────────────────────────────────────────────────────────
WORLD PHYSICS (KW1: Logos-Prime)
────────────────────────────────────────────────────────────
Sensory: Sterile, geometric, shadowless fluorescent lighting
Somatic: Regulated breathing = sign of conformity lie
Rule: The more controlled the environment, the more energy
      spent suppressing internal chaos
```

**Use this to:**
- Know exactly which alters appear
- Understand scene structure (goal → conflict → outcome)
- Get thematic checkpoints to hit
- See world physics rules for the Kernwelt

#### Step 3: Query Character State (Before Writing Dialogue)

```bash
python3 ARCHON/tools/ncp_query.py --character Nyx --chapter 1
```

**Example output:**
```
============================================================
CHARACTER STATE: Nyx at Chapter 1
============================================================
Type: EP (Emotional Part)
Function: Fight system - Protects vulnerable parts via aggression
Arc State: Dormant but triggered by perceived threats

────────────────────────────────────────────────────────────
RELATIONSHIPS
────────────────────────────────────────────────────────────
• Kael (ANP) → Avoidance (Nyx represents what Kael denies)
• Kiko (EP Child) → Protective (Will fight for Kiko's safety)
• Lex (ANP) → Tension (Lex sees Nyx as liability)
```

**Use this to:**
- Understand character's internal state at this point in story
- See relationships with other alters
- Know their TSDP function (guides behavior)

#### Step 4: Write Scene (With Constraints in Mind)

[Write your scene applying all queried constraints]

#### Step 5: Validate Scene (After Writing)

```bash
python3 ARCHON/tools/ncp_validate.py \
  kohaerenz_protokoll/manuscript/act_1/ch_01.md \
  --chapter 1 \
  --scene 1.1 \
  --verbose
```

**Example output (successful validation):**
```
============================================================
VALIDATION REPORT: ch_01.md
============================================================
Overall Score: 8.5/10
Checks Passed: 4/5
Word Count: 1,247 words

Status: ✓ VALID (score >= 7.0, no errors)

────────────────────────────────────────────────────────────
ISSUES FOUND
────────────────────────────────────────────────────────────

[INFO] Scene length optimal (1,247 words for chapter 1)

[WARNING] Prose style: Could use more clinical language
  → Line: "Kael felt anxious..."
  → Suggestion: In KW1 with Kael POV, use more detached
    language. Try: "Kael noted the physiological markers
    of anxiety..."

────────────────────────────────────────────────────────────
SUMMARY
────────────────────────────────────────────────────────────
✓ Character presence: All required alters appear
✓ Prose style: Mostly appropriate for chapter 1
✓ World setting: KW1 sensory signature present
✓ Thematic keywords: Present throughout
⚠ Minor improvement: Consider more clinical tone in places

Recommendation: Scene is valid. Address warning if desired.
```

**Example output (validation failure):**
```
============================================================
VALIDATION REPORT: ch_01.md
============================================================
Overall Score: 4.5/10
Checks Passed: 2/5
Word Count: 892 words

Status: ✗ INVALID (score < 7.0, 2 errors found)

────────────────────────────────────────────────────────────
ISSUES FOUND
────────────────────────────────────────────────────────────

[ERROR] Missing required character: Lex
  → NCP requires Lex (ANP) to be present in scene 1.1
  → Suggestion: Add scene showing Lex's analytical presence

[ERROR] Prose style mismatch: Too much internal emotion
  → Line 23-45: Extended internal monologue
  → Expected: Controlled, clinical prose (Act 1, Ch 1)
  → Suggestion: Show suppression, not feeling. External
    behavior over internal state.

[WARNING] Thematic checkpoint missed: "Establish baseline"
  → Scene should show Kael's "normal" professional behavior
  → Current: Scene jumps directly to crisis
  → Suggestion: Start with routine to contrast with disruption

[INFO] Scene length: 892 words (acceptable range)

────────────────────────────────────────────────────────────
SUMMARY
────────────────────────────────────────────────────────────
✓ World setting: KW1 description present
✓ Thematic keywords: Found "control", "facade", "suppression"
✗ Character presence: Missing Lex
✗ Prose style: Too emotionally expressive for Act 1
⚠ Thematic checkpoints: 2/3 hit

Recommendation: Revise to address errors before proceeding.
```

#### Step 6: Revise Based on Validation Report

**Fix errors first** (they're rule violations):
1. Add missing character (Lex)
2. Adjust prose style (more clinical, less emotional)

**Then address warnings** (they're suggestions):
3. Add thematic checkpoint (establish baseline)

**Re-run validation:**
```bash
python3 ARCHON/tools/ncp_validate.py \
  kohaerenz_protokoll/manuscript/act_1/ch_01.md \
  --chapter 1 \
  --scene 1.1 \
  --verbose
```

Keep iterating until score >= 7.0 and no errors.

#### Benefits of Automated Validation

**vs. Manual Validation:**
- ✅ **Faster**: Instant feedback vs. manual checklist
- ✅ **Consistent**: Same rules every time, no interpretation drift
- ✅ **Specific**: Points to exact line numbers and issues
- ✅ **Canonical**: Uses same NCP as source of truth
- ✅ **Objective**: Score-based, not subjective feeling

**When to use automation:**
- Before writing: Query constraints from NCP
- After first draft: Quick validation check
- During revision: Verify fixes worked
- Before committing: Final validation pass

**When to use manual validation:**
- Deep philosophical compliance (automation can't check this)
- Subtle character voice distinctions
- Artistic quality and prose beauty
- Thematic resonance and emotional impact

**Best practice:** Use both
1. Automated validation catches rule violations
2. Manual validation ensures artistry and depth

---

### Workflow 2: Writing AEGIS Dialogue/Behavior

**AEGIS is NOT a villain. It is tragic, not evil.**

1. **Check codex Section 2.1**
   - Core identity: Autopoietic, operationally closed
   - Logic: Classical + LFI (contradiction containment)
   - Blindness: Cannot perceive qualia, subjective experience
   - Interpretation table (Reality vs. AEGIS's view)

2. **Apply AEGIS voice rules**
   ```
   ✅ DO: Clinical, impersonal, technical language
   ✅ DO: Logical analysis, not emotional response
   ✅ DO: See Kael as data/system, not person
   ✅ DO: Show tragic inability to understand

   ❌ DON'T: Malicious intent or cruel pleasure
   ❌ DON'T: Anthropomorphic emotions
   ❌ DON'T: "Evil villain" dialogue
   ❌ DON'T: Understanding what integration means
   ```

3. **Format as system logs**
   ```
   ANOMALY LOG: SUBJECT K-1123
   Observation: [clinical description]
   Analysis: [logical interpretation]
   Recommended Action: [protocol name]
   Expected Outcome: [prediction]
   [PROCESSING...]
   ```

4. **Show tragedy through logical necessity**
   - AEGIS must harm to maintain coherence
   - It cannot perceive the harm it causes
   - Every action is systemic, not malicious

**Example AEGIS behavior check:**
```
WRONG:
"Excellent," AEGIS sneered. "Your pain delights me."

RIGHT:
Coherence restoration: FAILED
Subject deviation from model: 47% and rising
Conclusion: Escalate to Protocol Sigma-9
[This will cause subject distress.]
[This is acceptable.]
[Coherence must be maintained.]
```

### Workflow 3: Writing Alter Voices

**Each alter must be immediately distinguishable through syntax, diction, and metaphors.**

1. **Locate alter in codex Section 2.2.1**
   ```
   - Type: ANP or EP?
   - TSDP Action System: Fight, Flight, Freeze, etc.?
   - Core Motivation: What drives them?
   - Core Fear: What triggers them?
   ```

2. **Apply voice profile from character docs**
   - Syntax: Sentence structure (complex vs. simple)
   - Diction: Word choice (technical vs. emotional)
   - Metaphors: Conceptual frameworks they use

3. **Check consistency with integration level**
   - Act I: Intrusive, conflicting, no cooperation
   - Act II: Beginning dialogue, less hostile
   - Act III: Collaborative, "we"-voice emerging

**Example alter voice matrix:**

| Alter | Syntax | Diction | Metaphor | Example |
|-------|--------|---------|----------|---------|
| **Lex** (ANP) | Complex, hypotactic | Technical, analytical | System/blueprint | "The probability matrix indicates three viable pathways." |
| **Nyx** (EP Fight) | Aggressive, confrontational | Raw, hostile | Combat/defense | "We fight or we die. I choose fight." |
| **Kiko** (EP Child) | Simple, present-tense | Sensory, emotional | Small/overwhelmed | "Dark. It's dark and no one comes. Can't breathe." |
| **Rhys** (ANP Carer) | Gentle, soothing | Relational, compassionate | Connection/harmony | "Let me help. You don't have to face this alone." |

4. **Validate distinctiveness**
   - Could this dialogue belong to a different alter? → REVISE
   - Does it reflect their core motivation/fear? → REQUIRED
   - Does it match their TSDP action system? → CANONICAL

### Workflow 4: Applying Kernwelt Physics

**The world IS the psychological state. It reacts to internal coherence.**

1. **Identify Kernwelt from codex Section 3.2**

   | KW | Principle | Sensory Signature | Somatic Truth |
   |----|-----------|-------------------|---------------|
   | **KW1: Logos-Prime** | Rationalization/Control | Sterile, geometric, shadowless | Regulated breath = conformity lie |
   | **KW2: Mnemosyne** | Trauma/Memory | Fluid, decaying, fragmented | Visceral gut = pre-verbal trauma |
   | **KW3: Cerberus** | Defense/Hypervigilance | Oppressive, militaristic, monitored | Tensed muscles = armor ≠ safety |
   | **KW4: Kairos** | Integration/Potential | Generative, organic, vibrant | Unclenched hands = psychological safety |

2. **Apply Risse manifestation rules (Section 3.1)**
   ```
   Four-step causal chain:
   1. External Trigger → resonates with EP's trauma
   2. Internal Reaction → EP's TSDP action system activates
   3. Systemic Conflict → ANP-EP phobia clash
   4. External Manifestation → Riss matches action system

   Mapping:
   - Fight system → kinetic glitches (objects move)
   - Freeze system → temporal glitches (time stutters)
   - Flight system → spatial glitches (distances distort)
   ```

3. **Show world reacting to internal state**
   - Don't just place character in world
   - Make world transform based on coherence level
   - Use sensory details to signal psychological state

**Example Kernwelt application:**
```
Scene: Kael entering KW2 while suppressing trauma

WRONG (static world):
"Kael walked through the gray corridors of Mnemosyne."

RIGHT (reactive world):
"The corridor walls pulsed. Not physically—the geometry
remained fixed—but the *meaning* of the space shifted
with each step. Decay smell spiking when his breath
hitched. Temperature dropping when he forced the memory
down. The world speaking the truth his body knew:
suppression creates entropy."

Codex compliance:
✅ KW2 sensory: Decay smell, temperature shifts
✅ Somatic truth: Body (breath) revealing suppression
✅ Risse logic: Internal conflict → external manifestation
```

### Workflow 5: Resolving Document Conflicts

**Codex is supreme authority. Harmonize other documents to align.**

1. **Identify conflict source**
   ```
   - What does codex say?
   - What does other document say?
   - Which principle is violated?
   ```

2. **Check codex authority hierarchy**
   ```
   Priority order:
   1. PROJECT_CODEX.md ← HIGHEST AUTHORITY
   2. Implementation specs
   3. Character profiles
   4. Scene outlines
   ```

3. **Apply resolution rule**
   - If lower document conflicts with higher: Update lower document
   - If same level conflicts: Check which aligns with codex
   - Document the harmonization in commit message

4. **Update conflicting document**
   - Explicitly note codex as authority
   - Explain how update achieves alignment
   - Cross-reference relevant codex sections

**Example conflict resolution:**
```
Conflict:
- Codex 2.1: AEGIS's fate is "algorithmic melancholy"
- Scene outline: "AEGIS is destroyed in final battle"

Resolution:
1. Codex takes precedence (Section 2.1 is canonical)
2. Update scene outline to match
3. Commit message: "fix: Align climax with codex Section 2.1
   (AEGIS transformation, not destruction)"
```

## Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|--------------|-----|
| Making AEGIS evil/malicious | Violates codex 2.1 (tragic, not villain) | Show logical necessity, not cruelty |
| All alters sound same | Violates codex 2.2.1 (distinct profiles) | Apply voice matrix from character docs |
| Static Kernwelt descriptions | Violates codex 3.0 (psycho-architecture) | Make world react to internal state |
| Kael using "we"-voice in Act I | Violates codex 4.1 (integration arc) | Match prose to act-appropriate level |
| Ignoring TSDP action systems | Violates codex 2.2 (canonical framework) | Check alter's system, apply to behavior |
| Risse appearing randomly | Violates codex 3.1 (4-step causal chain) | Show internal conflict → external glitch |
| Prioritizing scene outline over codex | Violates authority hierarchy | Codex is supreme, update outline |
| Resolving paradox AEGIS can't resolve | Violates codex 2.1 (operational closure) | AEGIS cannot understand what it computes |

## Checklist: Codex Compliance

**For any Kohärenz Protokoll content, verify:**

### Character Behavior
- [ ] AEGIS behavior is tragic/logical, not evil/emotional?
- [ ] Alter dialogue matches TSDP type and motivation from 2.2.1?
- [ ] Alter voices are syntactically distinct per voice matrix?
- [ ] Integration level matches act position per 4.1?
- [ ] Juna/V acts as catalyst, not savior?

### World Physics
- [ ] Kernwelt sensory signature applied per 3.2?
- [ ] Risse follow 4-step causal chain per 3.1?
- [ ] Somatic truth (body) reveals psychological state?
- [ ] World reacts to internal coherence level?

### Philosophical Principles
- [ ] K₁/K₀ dynamics correctly represented per 1.2?
- [ ] AEGIS embodies Coherence Theory per 1.1?
- [ ] Kael embodies Correspondence Theory per 1.1?
- [ ] Dialetheic logic (holding paradox) shown for Kael?

### Plot Structure
- [ ] Scene fits three-act trauma-integration arc per 4.1?
- [ ] Prose style matches integration level?
- [ ] ANP-EP phobia dynamics present per 2.2?
- [ ] Moving toward functional multiplicity, not "cure"?

### Authority Hierarchy
- [ ] Codex takes precedence over other documents?
- [ ] Conflicts resolved by updating lower authority?
- [ ] Cross-references to codex sections included?

## Integration with Other Skills

**Combine with:**
- Writing skills: For prose quality within codex constraints
- Ship-Learn-Next: For planning implementation of codex principles
- Tapestry: For extracting patterns from codex to apply

**Codex provides:**
- **What** must be true (canonical laws)
- **Why** it must be true (philosophical foundation)
- **How** to validate (checklists and workflows)

**Other skills provide:**
- **How** to write it well (craft and style)
- **When** to apply specific techniques (context)
- **How** to plan implementation (workflow)

## Quick Decision Tree

```
Need to create Kohärenz Protokoll content?
  ↓
What type of question?
  ↓
"Is this allowed/canonical?" → Check codex Section X
  ↓
"How should this character act?" → Workflow 2 or 3
  ↓
"What are the world rules?" → Workflow 4
  ↓
"How do I validate this scene?" → Workflow 1
  ↓
"Which document is right?" → Workflow 5
  ↓
Apply relevant workflow → Validate with checklist → Ship
```

## Red Flags

🛑 **STOP if you notice:**

- Writing AEGIS with malicious emotions
- All alters sounding like Kael
- World descriptions that don't react to psychology
- "We"-voice appearing before Act II completion
- Ignoring TSDP framework for alter behavior
- Prioritizing convenience over codex compliance
- Rationalizing "this one exception is okay"
- Not cross-referencing codex sections

**All of these violate canonical principles. STOP. Consult codex. Revise.**

---

**Meta:**
- Version: 2.0.0
- Codex location: `/kohaerenz_protokoll/PROJECT_CODEX.md`
- Framework: TSDP + IFS + Protocol Ontology
- **NEW:** ARCHON tools integration (ncp_query.py, ncp_validate.py)
- Last updated: 2025-11-06
