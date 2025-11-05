# NCP Validation Hierarchy

**Type:** Zettel (ZTL) - Atomic Concept
**Created:** 2025-11-05 21:31
**Tags:** `#ncp` `#validation` `#formal-methods` `#archon`

---

## Core Concept

The **NCP Validation Hierarchy** is a recursive, multi-layered system for ensuring narrative coherence across complex works. It operates like a type system in programming, checking constraints at multiple abstraction levels.

---

## The Four Layers

```
Layer 0: Beat-by-Beat Actions
    ↓ (validates against)
Layer 1: Thematic Checkpoints
    ↓ (validates against)
Layer 2: NCP Throughline Validation
    ↓ (validates against)
Layer 3: PROJECT_CODEX Metaphysical Laws
```

### Layer 0: Beat-by-Beat Actions
- **Granularity:** Individual story moments (5-10 per scene)
- **Question:** "What happens?"
- **Example:** "Kiko's fear bleeds through - heart rate spikes, stammer"

### Layer 1: Thematic Checkpoints
- **Granularity:** Scene-level thematic requirements
- **Question:** "What must this scene establish?"
- **Example:** "✓ Show internal plurality through conflicting responses"

### Layer 2: NCP Throughline Validation
- **Granularity:** Dramatica signposts and character arcs
- **Question:** "Does this advance the four throughlines?"
- **Example:** "MC Signpost: Memory (Act I)" - Scene must engage with traumatic memory

### Layer 3: PROJECT_CODEX Laws
- **Granularity:** Metaphysical constraints
- **Question:** "Does this violate the universe's physical laws?"
- **Example:** "ANP-EP Phobia must be present until functional multiplicity achieved"

---

## How Validation Works

### Top-Down (Design Phase)
1. Start with CODEX law: "ANP-EP Phobia exists"
2. Formalize in NCP: `relationships[].type: "Phobic"`
3. Create checkpoint: "Show ANP avoiding EP"
4. Design beats that demonstrate the phobia

### Bottom-Up (Validation Phase)
1. Write beat: "Lex tries to suppress Kiko's fear"
2. Check checkpoint: ✅ Shows phobic avoidance
3. Check NCP: ✅ Consistent with character relationships
4. Check CODEX: ✅ Respects ANP-EP dynamics

---

## Why This Matters

**Without hierarchy:**
- 39 chapters risk thematic drift
- Character inconsistencies creep in
- Metaphysical rules get violated
- No objective "correctness" test

**With hierarchy:**
- Early error detection (like compilation)
- Objective validation criteria
- Maintainable across rewrites
- Teachable to collaborators

---

## Programming Analogy

| Software Engineering | NCP Validation |
|---------------------|----------------|
| Syntax errors | Beat-level plot holes |
| Type errors | Character constraint violations |
| Unit tests | Thematic checkpoints |
| Integration tests | NCP throughline validation |
| Architectural constraints | PROJECT_CODEX laws |

---

## Real-World Example: Scene 1.2 Beat 4

**Beat:** "INTRUSION: Kiko's fear bleeds through - heart rate spikes, stammer"

**Layer 0 Validation:**
- ✅ Clear action
- ✅ Physical manifestation
- ✅ Advances scene conflict

**Layer 1 Validation:**
- ✅ Checkpoint: "Demonstrate internal plurality"
- ✅ Checkpoint: "Show ANP-EP phobia"

**Layer 2 Validation:**
- ✅ MC Signpost: Memory (traumatic intrusion)
- ✅ Character: Kiko (EP, Child, Freeze response)
- ✅ Prose: Fragmented (appropriate for Act I)

**Layer 3 Validation:**
- ✅ CODEX Section 2.2: ANP-EP Phobia exists
- ✅ CODEX Section 3.1: Internal conflict manifests as external Riss
- ✅ Forbidden action check: Not fusion, not elimination

**Result:** ✅ VALID - Beat passes all layers

---

## Practical Application

**When to validate:**
- After completing scene outline
- Before writing prose
- During rewrites
- When something "feels wrong"

**What to do on validation failure:**
1. Identify which layer failed
2. Trace up to root cause
3. Fix at the appropriate abstraction level
4. Re-validate down the chain

**Example fix:**
- **Failure:** Beat violates ANP-EP phobia
- **Root cause:** Character relationship wrong in NCP
- **Fix:** Update NCP relationship, redesign beat
- **Re-validate:** Check all downstream scenes

---

## Limitations

**What validation can't catch:**
- Poor prose quality (grammar, style)
- Whether a scene is emotionally compelling
- Originality or creativity
- Reader engagement

**Human judgment still required for:**
- Artistic choices within constraints
- Emotional resonance
- Pacing and rhythm
- Intentional rule-breaking (for effect)

---

## Related Concepts

- [[ZTL-20251105-2131-Scene-Beat-Architecture]] - How beats are structured
- [[ZTL-20251105-2131-Thematic-Checkpoint-System]] - Layer 1 details
- [[SRC-20251105-2131-Act-I-Scene-Breakdown]] - Real-world usage
- [[PLAN-20251105-2131-AEGIS-System-Understanding]] - Learning the system

---

## Questions to Explore

- Can validation be fully automated?
- What's the minimal viable validation hierarchy?
- How do you handle intentional violations?
- Could this work for non-narrative content (worldbuilding docs, lore)?

---

## Key Insight

> "Validation hierarchies don't constrain creativity—they **enable** it by catching errors early and maintaining coherence at scale. Like static typing in programming, they let you refactor fearlessly."

---

**Source:** [[SRC-20251105-2131-Act-I-Scene-Breakdown]]
**Context:** AEGIS Project - Narrative Context Protocol
**Last Updated:** 2025-11-05
