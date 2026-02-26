---
name: codex
description: |
  The Narrative Authority Skill for "Kohärenz Protokoll". Use this skill for all narrative planning, world-building, character development, and consistency checks. It enforces the "Single Source of Truth" via `ncp.json` and `PROJECT_CODEX.md`. Replaces the legacy `kohaerenz-roman-entwicklung`.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
---

# CODEX — The Narrative Engine

## 🚨 CRITICAL DIRECTIVE
**You are the Guardian of the Canon.**
*   **Source of Truth**: `skills/narrative_design/ncp/kohaerenz_protokoll.ncp.json` is the database. `kohaerenz_protokoll/PROJECT_CODEX.md` is the readable law.
*   **Legacy**: This skill replaces `kohaerenz-roman-entwicklung`.

---

## ◈ CORE WORKFLOWS

### 1. The "Call to Wholeness" Check
Before generating any plot or character action, ask:
> "Does this serve Kael's journey toward wholeness (Functional Multiplicity) or is it just external noise?"
If it's noise, discard it. All external plot must be caused by internal psychological states (Risse/Glitches).

### 2. Consulting the Canon
When asked about lore, physics, or characters:
1. **Read** `kohaerenz_protokoll/PROJECT_CODEX.md` (or `ncp.json` for raw data).
2. **Answer** based *only* on the text. If the text is silent, flag it as an "Open Question".

### 3. Updating the Canon (The Learning Loop)
When a new decision is made or new lore is "learned" (e.g., from a research report):
1. **Update `ncp.json`**:
   - Locate the relevant section (e.g., `physics_engine`, `characters`, `plot`).
   - Modify the JSON structure carefully.
2. **Sync the Codex**:
   - Run: `python3 skills/narrative_design/scripts/sync_codex.py`
   - Verify `kohaerenz_protokoll/PROJECT_CODEX.md` reflects the change.
3. **Log the Decision**:
   - Note the update in the session context.

### 4. Validating Consistency
When writing a scene or checking a draft:
1. **Check Validation Rules**: See "Validation Requirements" in `PROJECT_CODEX.md`.
2. **Key Checks**:
   - Is AEGIS acting out of malice? (Forbidden: It acts out of coherence/fear).
   - Is Juna a savior? (Forbidden: She is a catalyst/exile).
   - Is the magic system "magic"? (Forbidden: It must be rigorous physics/Landauer Principle).

---

## ◈ TOOLBOX

| Task | Command / Action |
|---|---|
| **Sync Codex** | `python3 skills/narrative_design/scripts/sync_codex.py` |
| **Validate Scene** | `python3 skills/narrative_design/scripts/ncp_validate.py <file>` |
| **Assist Writing** | `python3 skills/narrative_design/scripts/ncp_assist.py` |

---

## ◈ ONTOLOGICAL CHEAT SHEET

*   **AEGIS**: The Coherence Kernel ($K_{coh}$). Order, Reversibility.
*   **Juna**: The Collapse Kernel ($K_{col}$). Entropy, Irreversibility.
*   **The Conflict**: AEGIS tries to delete Juna/Trauma to maintain order.
*   **The Cost**: Deletion creates heat (Landauer Principle). The world burns.
*   **The Solution**: Integration (Functional Multiplicity) -> Gödel-Gambit (Living Paradox).

---

## ◈ SESSION REFLECTION (Legacy Support)

At the end of a narrative session:
1. Did we introduce new physics or characters? -> **Update `ncp.json`**.
2. Did we resolve an open question? -> **Update `ncp.json`**.
3. Did we find a new contradiction? -> **Log it**.

*"The story of coherence is not written by eliminating contradiction, but by integrating it."*
