---
name: quest-management
description: Manages high-level narrative and development quests. Use when creating new quests, tracking project progress, managing large workflows, or resolving complex narrative blocks. Triggers for "new quest", "update quest", "quest status", "what are we working on".
---

# Quest Management Skill

**Version:** 1.0.0
**Type:** Technique Skill
**Testing Rigor:** Moderate (3-5 scenarios)

## CSO-Optimized Description

**Use when**: User wants to define a new mission, track progress on a major feature/narrative arc, update the status of a quest, or view all active quests.
**What it does**: Creates and maintains structured markdown files in `quests/`, ensuring alignment with `AGENTS.md` and triggering associated todo lists.
**How it helps**: Provide a high-level view of project goals, consolidated knowledge, and execution plans, preventing loss of context.
**Keywords**: quest, project management, tracking, mission, narrative arc, workflow, status, goal

---

## Quick Start

### Standard Workflow

```
Identify Mission/Goal
    ↓
Check `quests/README.md` and `quests/*.md` (Is it already covered?)
    ↓
Merge/Update if exists OR Create New Quest File (`quests/Quest-Name.md`)
    ↓
Generate Todo List (via `todo-management`)
    ↓
Update `AGENTS.md` (Quest Index)
```

---

## Operations

### 1. Create New Quest
**Use when**: A new major goal is identified (e.g., "Fix Plot Hole X", "Implement Feature Y").

1.  **Pre-Flight Check**:
    *   Read `quests/README.md`.
    *   List files in `quests/`.
    *   **CRITICAL**: If a similar quest exists, UPDATE or MERGE it. Do not create duplicates.
2.  **Read Template**: Load `quests/TEMPLATE.md`.
3.  **Populate**: Fill in Title, Focus, Challenge, Goal, and "Related Quests".
4.  **Save**: Save to `quests/Quest-[Name].md`.
5.  **Link**: Add entry to `quests/README.md` and `AGENTS.md`.
6.  **Trigger**: Ask user if they want to populate specific todos immediately.

### 2. Update Quest Status
**Use when**: Progress is made or a quest is completed.

1.  **Find Quest**: Locate `quests/Quest-[Name].md`.
2.  **Update Metadata**: Change **Status** (⚪ -> 🟡 -> ✅).
3.  **Update Content**: Mark steps as complete `[x]`, add notes to "Next Steps".
4.  **Reflect**: If ✅, ask user for a brief "Retrospective" or "Learnings" note to append.

### 3. List Active Quests
**Use when**: User asks "What are we working on?" or "Show quests".

1.  **Scan**: Read `quests/README.md`.
2.  **Filter**: Show only 🟡 Active quests.
3.  **Summarize**: Display Title + Focus + Current Status.

---

## File Structure

*   `quests/README.md`: Index of all quests (Active, Completed, Backlog).
*   `quests/Quest-[Name].md`: Detailed mission document.

## Rules

*   **One Quest, One File**: Keep quests atomic. If too big, split into sub-quests.
*   **Link to Truth**: Always reference canonical docs (e.g., `PROJECT_CODEX.md`) in the "Consolidated Knowledge" section.
*   **Sync with Todos**: A Quest without todos is just a wish. Trigger `todo-management` to operationalize.

## References

*   **Template**: `assets/quest_template.md`
