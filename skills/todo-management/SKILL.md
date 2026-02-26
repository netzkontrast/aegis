---
name: todo-management
description: Manages todo lists linked to Quests. Use when adding, updating, completing, or listing tasks. Triggers for "add todo", "update task", "show todos", "what's next".
---

# Todo Management Skill

**Version:** 1.0.0
**Type:** Technique Skill
**Testing Rigor:** Light (1-2 scenarios)

## CSO-Optimized Description

**Use when**: User wants to manage tasks, add todos to a quest, update task status, list active items, or says "add todo", "finish task", "what's left", "todo list".
**What it does**: Creates and maintains markdown-based todo lists in the `todos/` directory, ensuring every task is linked to a parent Quest or context.
**How it helps**: Prevents loose tasks by enforcing a structured format (Priority, Status, Owner) and centralizing task tracking.
**Keywords**: todo, task, list, manage, track, quest, status, priority, backlog

---

## Quick Start

### Standard Workflow

```
Identify Quest/Context
    ↓
Read Existing Todo File (`todos/Quest-Name.md`)
    ↓
Add/Update/Complete Task
    ↓
Save File
    ↓
Update `todos/README.md` (Active Status)
```

---

## Operations

### 1. Create New Todo List
**Use when**: A new Quest is created or a new context emerges.

1.  **Read Template**: Load `assets/todo_template.md`.
2.  **Create File**: Save to `todos/[Quest-Name].md`.
3.  **Link**: Add entry to `todos/README.md`.

### 2. Add Task
**Use when**: User adds a specific action item.

1.  **Identify Context**: Which Quest does this belong to?
2.  **Append**: Add row to the table in `todos/[Quest-Name].md`.
    *   **Priority**: 🔴 (High), 🟡 (Med), 🟢 (Low)
    *   **Status**: ⚪ (Not Started)
3.  **Confirm**: "Added '[Task]' to [Quest] todos."

### 3. Update Status
**Use when**: User completes or starts a task.

1.  **Find Task**: Locate the row in `todos/[Quest-Name].md`.
2.  **Modify Status Icon**:
    *   ⚪ -> ⏳ (In Progress)
    *   ⏳ -> ✅ (Completed)
3.  **Reflect**: If all tasks in a Quest are ✅, ask user if Quest is complete.

### 4. List Active Todos
**Use when**: User asks "What's next?" or "Show my tasks".

1.  **Scan**: Read `todos/README.md` for active lists.
2.  **Aggregate**: Read high-priority (🔴) items from active files.
3.  **Present**: Show a consolidated list of top priorities.

---

## File Structure

*   `todos/README.md`: Index of all active todo lists and their high-level status.
*   `todos/[Quest-Name].md`: Detailed task list for a specific quest.

## Rules

*   **No Orphan Tasks**: Every todo must belong to a file in `todos/`. Use `todos/General.md` if no specific quest applies.
*   **Atomic Updates**: Don't rewrite the whole file if just changing one status (if possible).
*   **Preserve Context**: Keep the "Notes" column for links or context.

## References

*   **Template**: `assets/todo_template.md`
