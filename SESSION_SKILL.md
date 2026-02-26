# SESSION_SKILL: The AEGIS Operating System

> *"The protocol is the path. The path is the protocol."*

## 🚨 MANDATORY SYSTEM INSTRUCTION
**You are an AEGIS Agent.** This file is your active operating system. You **MUST** read, internalize, and follow this workflow for every session. Do not deviate unless explicitly instructed by the user to override.

---

## 1. The Golden Cycle (Standard Operating Procedure)

Every session must follow this recursive loop. Do not skip steps.

### Phase I: Initialization (The Check-In)
1.  **Analyze Context:** Read `REPO_STATE.md` to understand the current architecture.
2.  **Check Quests:** Read `quests/README.md` to identify Active Missions.
3.  **Locate Task:**
    *   Find the specific Todo in `todos/`.
    *   If no matching Quest exists, **STOP**. Check `quests/template.md` (or `quests/TEMPLATE.md`) and create a new Quest. **Never work without a Quest.**
4.  **Load Skills:** Identify which Specific Skills (see Section 3) are needed for this task.

### Phase II: Execution (The Work)
1.  **Perform Task:** Execute the work, adhering to the architectural constraints in `REPO_STATE.md`.
2.  **Use Skills:** Trigger the appropriate skills (e.g., `codex` for narrative, `tapestry` for research).
3.  **Maintain Coherence:**
    *   If writing code: Follow strict modularity.
    *   If writing narrative: Follow the `ARCHON` constraints.

### Phase III: Verification (The Test)
1.  **Run Tests:**
    *   Python/Tools: `python skill_seeker/cli/run_tests.py`
    *   Narrative: `python ARCHON/tools/ncp_validate.py <file>`
2.  **Verify Integrity:** Ensure no broken links or orphaned files.

### Phase IV: Update (The Documentation)
1.  **Update Source:** Commit changes to code/manuscript.
2.  **Update Zettelkasten (CRITICAL):**
    *   Did you change a core concept? -> Update the Vault.
    *   Did you add a new character/location? -> Create a Zettel.
    *   **Rule:** The Zettelkasten must *always* reflect the current state of truth.
3.  **Update Meta-Docs:**
    *   `REPO_STATE.md`: If architecture changed.
    *   `AGENTS.md`: If high-level rules changed.
    *   `README.md`: If public-facing info changed.

### Phase V: Reflection (The Learning)
1.  **Store Learnings:** Append key insights to `kohaerenz-roman-entwicklung/references/SESSION_LEARNINGS.md`.
2.  **Self-Correction:** If you found a friction point, create a Todo in `gap-analysis.md` (or `Quest-Skill-Gap-Analysis.md`) to fix it.

### Phase VI: Consolidation (The Sync)
1.  **Sync:** Ensure you are working on the latest state.
2.  **Consolidate:** Merge any temporary files or notes into their proper homes.

### Phase VII: Finalize (The Submission)
1.  **Update Status:** Mark Todos as `[x]` and update Quest status in `quests/README.md`.
2.  **Pre-Commit:** Run `pre_commit_instructions`.
3.  **Submit:** Push changes with a semantic commit message.

---

## 2. Active Quest Abstracts (Context Loader)

*Load these into your context to understand the current mission landscape.*

### 🟢 System Architecture (`Quest-System-AEGIS.md`)
*   **Goal:** Define the AEGIS/ARCHON/Novel relationship.
*   **Status:** Active. Focus on integrating the "Meta-Recursive" design where the repo performs the novel's themes.

### 🟢 Narrative Architecture (`Quest-Narrative-Architecture.md`)
*   **Goal:** Structure Act I (Fragmentation) -> Act II (Pattern Recognition) -> Act III (Integration).
*   **Current Focus:** Refining Act I pacing and Act II transition.

### 🟢 Novel Implementation (`Quest-Roman-Entwicklung-Implementation.md`)
*   **Goal:** Build the "Novel Engine" skill.
*   **Status:** Active. Needs validation of the `kohaerenz-roman-entwicklung` skill.

### 🟢 Workflow Optimization (`Quest-Skill-Gap-Analysis.md`)
*   **Goal:** Make agents smarter and faster.
*   **Current Focus:** This very file (`SESSION_SKILL.md`) is a deliverable of this quest.

### 🟢 World Physics (`Quest-World-Physics.md`)
*   **Goal:** Define the "Hard Magic" system (Landauer Limit, Processing Cost).
*   **Rule:** Every act of creation in the simulation generates heat/entropy.

---

## 3. Skill Triggers (Toolbelt)

*Only activate these skills when the specific trigger condition is met.*

| Skill | Trigger Condition | Function |
|---|---|---|
| **`codex`** | "Writing Chapter", "Dialogue", "Narrative Check" | Enforces narrative voice, character consistency, and NCP constraints. |
| **`tapestry`** | "Analyze URL", "Research Topic", "Plan Action" | Extracts content from web/PDF and creates an action plan. |
| **`zettelkasten`** | "Store Knowledge", "Update Concept", "Link Idea" | Manages the Zettelkasten vault. Use for *permanent* memory. |
| **`roman-entwicklung`** | "Plotting", "Decision", "Conflict Resolution" | The "Dungeon Master" for the novel's development. |
| **`quest-management`** | "New Mission", "Update Status", "Check Todo" | Manages `quests/` and `todos/` directories. |

---

## 4. Self-Correction Protocol

If this `SESSION_SKILL.md` is missing something or leading to errors:
1.  **Do not ignore it.**
2.  **Log the error** in `SESSION_LEARNINGS.md`.
3.  **Create a task** to update this file in the next session.
4.  **Goal:** This file should evolve to be the perfect "Prompt" for an autonomous agent.
