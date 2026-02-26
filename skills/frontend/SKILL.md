# SKILL: Frontend Builder (Dynamic UI)

**Version:** 1.0.0
**Status:** Alpha
**Owner:** Jules (Agent)

## 🎯 Purpose
This skill enables the AEGIS Console (`vercel-prototype`) to dynamically generate its user interface based on the repository's capabilities. Instead of hardcoding forms and buttons, the frontend reads JSON schemas derived from markdown command files (`.claude/commands/*.md`).

## 🛠️ Capabilities

### 1. Spec Generation (`generate_ui_spec.py`)
- **Input:** `.claude/commands/` directory.
- **Process:** Scans all `.md` files for YAML frontmatter defining UI components.
- **Output:** A unified `console-config.json` that the Next.js app consumes.

### 2. UI Schema Definition
Defines standard components available to the frontend:
- `CommandForm`: A form with inputs (text, select, boolean).
- `DataVisualizer`: A chart or graph (e.g., Knowledge Graph).
- `TerminalOutput`: A streaming text view.

## 📝 Usage

### Adding UI to a Command
To expose a command in the Console, add a YAML frontmatter block to its definition file (e.g., `.claude/commands/learn.md`):

```yaml
---
ui:
  component: "CommandForm"
  title: "Learn New Skill"
  description: "Extract knowledge from a URL or file."
  inputs:
    - name: "url"
      type: "text"
      label: "Source URL"
      placeholder: "https://example.com/article"
      required: true
    - name: "save"
      type: "boolean"
      label: "Save to Zettelkasten"
      default: false
---
```

## 🔗 Dependencies
- Python 3.x (for parsing)
- PyYAML
