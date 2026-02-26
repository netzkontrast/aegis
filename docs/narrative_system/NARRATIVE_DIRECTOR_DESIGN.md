# Narrative Director Agent: Design Specification (Phase 1)

**Quest:** [[narrative-system.md]]
**Objective:** Design the "Narrative Director" agent to guide narrative flow and validate coherence.

## 1. Core Purpose
The Narrative Director is not a writer; it is an **Editor-in-Chief**. It does not generate prose; it generates **instructions**. It ensures that the *Novel* adheres to the *AEGIS Framework*.

## 2. Architecture (Input/Output)

### Input
- **Current Scene Context:** `chapter_XX_scene_YY.md`
- **Active Quest Context:** `quests/*.md`
- **NCP Constraints:** `aegis/ncp/kohaerenz_protokoll_v2.ncp.json`
- **Triadic Currency State:** `ACT_1_CURRENCY_CHECK.md`

### Output
- **Scene Instructions:** "Increase Tension. Reduce Empathy. Current POV is Kael (ANP)."
- **Validation Report:** "Violation: Kael used metaphor in Scene 3 (ANP violation)."
- **Gap Analysis:** "Scene 4 connects poorly to Scene 5. Missing logical bridge."

## 3. Key Components

### A. The Context Loader
- Reads `REPO_STATE.md` and `quests/narrative.md`.
- Understands where in the "Golden Cycle" the user is.

### B. The Constraint Checker
- Verifies adherence to:
    - **Voice:** (Dual-Voice Protocol)
    - **Physics:** (Landauer Limit)
    - **Philosophy:** (Coherence vs. Correspondence)

### C. The Instruction Generator
- Generates a prompt for the `Codex` skill (the writer).
- Example: *"Write Scene 6. Focus on 'Curiosity'. POV: Lex. Constraints: No contractions."*

## 4. Implementation Plan (Phase 1)
1. **Define Schema:** Create `narrative_director_schema.json` for I/O.
2. **Build Tool:** Create `aegis/tools/narrative_director.py`.
3. **Integrate:** Hook into `aegis/SKILL.md` workflow.

---

## Next Steps
- Implement `aegis/tools/narrative_director.py` in the next session.
- Define the prompt templates for the Director.
