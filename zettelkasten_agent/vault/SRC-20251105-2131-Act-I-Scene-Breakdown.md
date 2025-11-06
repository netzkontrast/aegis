# Source: Act I Scene Breakdown - Kohärenz Protokoll

**Type:** Source Note (SRC)
**Created:** 2025-11-05 21:31
**Status:** processed
**Source File:** `kohaerenz_protokoll/narrative_design/act_1_scenes.md`

---

## Metadata

- **Content Type:** Narrative design document
- **Word Count:** ~2,200 words
- **Chapters Covered:** Chapters 1-13 (Act I)
- **Related Action Plan:** [[PLAN-20251105-2131-AEGIS-System-Understanding]]
- **Quest MOC:** [[MOC-20251105-2131-Deep-System-Understanding-Quest]]
- **Date Captured:** 2025-11-05

---

## Summary

This is the complete structural specification for Act I of the novel *Kohärenz Protokoll*. It demonstrates how the AEGIS project integrates multiple theoretical frameworks:

- **Dramatica Theory** → NCP Schema → Scene Validation
- **TSDP Psychology** → Character System → Alter Interactions
- **Project Codex Laws** → World Physics → Scene Constraints
- **Prose Evolution** → Fragmentation → Polyphony

The document is a masterclass in theory-driven narrative design, where every scene beat validates against formal constraints while maintaining creative freedom.

---

## Key Structural Elements

### Act I Overview
- **Structure:** Heroine's Journey (Internal discovery and acceptance)
- **Chapters:** 1-13
- **Kael's Arc:** Fragmented → Conscious plurality → First internal council
- **AEGIS's Arc:** Confident control → Recognizing threat
- **Prose Evolution:** Maximum fragmentation → Emerging polyphony

### 8 Major Scenes

1. **Scene 1.1: The Awakening** (Ch 1) - Disorientation in perfect world
2. **Scene 1.2: The Coherence Check** (Ch 1) - First polyphonic conflict
3. **Scene 1.3: The Anomaly** (Ch 1) - Active investigation begins
4. **Scene 1.4: The Drowning Pool** (Ch 2-3) - KW2 trauma immersion
5. **Scene 1.5: The Inner Bunker** (Ch 4-6) - KW3 defense mechanisms
6. **Scene 1.6: The Therapist's Office** (Ch 4-6) - AEGIS gaslighting
7. **Scene 1.7: The Overgrown Garden** (Ch 4-6) - KW4 hope glimpse
8. **Scene 1.8: The First Internal Council** (Ch 7-13) - Formation of functional multiplicity

---

## NCP Validation Pattern

Every scene follows this structure:

```
Goal → Conflict → Beats (7-10 actions)
  ↓
Thematic Checkpoints (4-6 validations)
  ↓
NCP Validation (MC/OS Signposts, Character Constraints, Prose Style)
  ↓
Outcome (State change + next goal)
```

This creates a **recursive validation chain**:
- **Level 0:** Beat-by-beat action
- **Level 1:** Thematic checkpoints
- **Level 2:** NCP throughline validation
- **Level 3:** PROJECT_CODEX law compliance

---

## Integration Points

### Theory → Practice Pipeline

1. **PROJECT_CODEX** defines metaphysical laws
   - Example: "ANP-EP Phobia is fundamental conflict"

2. **NCP Schema** formalizes the laws
   - `character_systems.protagonist_system.parts[].relationships[]`
   - Relationship type: "Phobic"

3. **Populated NCP** applies to specific characters
   - Kael → Kiko: "Phobic" relationship defined

4. **Scene Breakdown** implements the constraint
   - Scene 1.2, Beat 4: "INTRUSION: Kiko's fear bleeds through"
   - Beat 5: "Guardian registers emotional noise as anomaly"
   - Internal conflict: Lex tries to suppress, Alex manages crisis

5. **ARCHON Tools** validate the implementation
   - `ncp_query.py --scene 1.2` → Returns required beats
   - `ncp_validate.py manuscript/ch1.md` → Checks compliance

---

## Extracted Concepts

This source generated the following atomic notes:

- [[ZTL-20251105-2131-NCP-Validation-Hierarchy]] - The recursive validation system
- [[ZTL-20251105-2131-Scene-Beat-Architecture]] - Goal/Conflict/Outcome pattern
- [[ZTL-20251105-2131-Prose-Evolution-Tracking]] - Fragmentation → Polyphony
- [[ZTL-20251105-2131-Psycho-Architecture]] - Psychology as world physics
- [[ZTL-20251105-2131-ANP-EP-Phobia-Dynamics]] - Core internal conflict
- [[ZTL-20251105-2131-Four-Kernwelten-System]] - The nested simulation layers
- [[ZTL-20251105-2131-Thematic-Checkpoint-System]] - Validation at scene level

---

## Personal Insights

**What makes this remarkable:**

This isn't just a scene outline—it's a **formal specification** that treats narrative design as a branch of software engineering. The NCP system is essentially:

- **Type system** for characters (ANP/EP/ISH)
- **Constraint solver** for plot (validation criteria)
- **State machine** for arcs (initial → midpoint → final)
- **Compilation target** for prose (schema → scene → text)

The genius is that these formal constraints don't restrict creativity—they **enable** it by:
1. Catching logical errors early
2. Maintaining thematic coherence across 39 chapters
3. Allowing safe experimentation (validation catches drift)
4. Creating clear success criteria (did it validate?)

It's like **Test-Driven Development for narrative**.

---

## Questions to Explore

- How does `ncp_query.py` actually generate scene requirements from the JSON?
- Can the validation be automated end-to-end (prose → parse → validate)?
- What happens when a scene deliberately violates validation? (Planned breaks vs bugs)
- Could this system work for other genres/structures?
- Is there a "compile" step that generates prose scaffolding from NCP?

---

## Related Notes

### Direct Links
- [[ZTL-20251105-2131-NCP-Validation-Hierarchy]]
- [[ZTL-20251105-2131-Scene-Beat-Architecture]]
- [[PLAN-20251105-2131-AEGIS-System-Understanding]]
- [[MOC-20251105-2131-Deep-System-Understanding-Quest]]

### Contextual
- `ARCHON/ncp/schema.json` - The formal spec
- `ARCHON/ncp/kohaerenz_protokoll.ncp.json` - The populated data
- `kohaerenz_protokoll/PROJECT_CODEX.md` - The metaphysical foundation

---

## Tags

`#narrative-design` `#ncp` `#archon` `#validation-systems` `#scene-structure` `#dramatica` `#tsdp` `#formal-methods`
