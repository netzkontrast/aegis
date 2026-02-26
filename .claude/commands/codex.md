---
name: codex
description: Access the Kohärenz Protokoll narrative authority. Manage canon, validate scenes, and sync documentation.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
ui:
  component: "CommandForm"
  title: "Codex Narrative Engine"
  description: "Interact with the narrative canon."
  inputs:
    - name: "action"
      type: "select"
      label: "Action"
      options:
        - label: "Show Summary"
          value: "summary"
        - label: "Sync Codex"
          value: "sync"
        - label: "Validate File"
          value: "validate"
        - label: "Assist Writing"
          value: "assist"
      default: "summary"
    - name: "target"
      type: "text"
      label: "Target File (for validate)"
      placeholder: "kohaerenz_protokoll/manuscript/..."
      required: false
---

# Codex Command - Narrative Authority

**The interface to the Kohärenz Protokoll narrative engine.**

Canon Management → Validation → Assistance

---

## Usage

```bash
/codex                            # Show Canon Summary
/codex sync                       # Update PROJECT_CODEX.md from ncp.json
/codex validate <file>            # Check a manuscript file for consistency
/codex assist                     # Start the AI writing assistant
```

---

## Implementation

### Step 1: Parse Action

```bash
ACTION="$1"
TARGET="$2"

if [ -z "$ACTION" ]; then
    ACTION="summary"
fi

echo "📖 Codex Command: $ACTION"
echo ""
```

### Step 2: Execute Workflow

#### Mode: Summary

```bash
if [ "$ACTION" = "summary" ]; then
    # Display key info from PROJECT_CODEX.md
    CODEX_FILE="kohaerenz_protokoll/PROJECT_CODEX.md"

    if [ ! -f "$CODEX_FILE" ]; then
        echo "❌ Error: Codex file not found. Run '/codex sync' first."
        exit 1
    fi

    echo "## 📜 Current Canon Status"
    echo ""
    # Extract Title and Version (approximate)
    grep -m 1 "Kohärenz Protokoll" "$CODEX_FILE"
    echo ""

    echo "### 🌌 Physics Engine"
    grep -A 5 "Dual Kernel Theory" "$CODEX_FILE" | grep -v "^--|^$"
    echo "..."
    echo ""

    echo "### 🎭 Active Systems"
    grep -A 10 "System Kael" "$CODEX_FILE" | grep "Functional Multiplicity"
    echo ""

    echo "👉 Use '/codex help' for more options."
fi
```

#### Mode: Sync

```bash
if [ "$ACTION" = "sync" ]; then
    echo "🔄 Syncing Codex from Single Source of Truth..."
    python3 skills/narrative_design/scripts/sync_codex.py

    if [ $? -eq 0 ]; then
        echo "✅ PROJECT_CODEX.md updated successfully."
    else
        echo "❌ Sync failed."
    fi
fi
```

#### Mode: Validate

```bash
if [ "$ACTION" = "validate" ]; then
    if [ -z "$TARGET" ]; then
        echo "❌ Error: Please specify a file to validate."
        echo "Usage: /codex validate <path/to/scene.md>"
        exit 1
    fi

    echo "🕵️‍♀️ Validating $TARGET..."
    python3 skills/narrative_design/scripts/ncp_validate.py "$TARGET"
fi
```

#### Mode: Assist

```bash
if [ "$ACTION" = "assist" ]; then
    echo "🤖 Launching Narrative Assistant..."
    python3 skills/narrative_design/scripts/ncp_assist.py
fi
```
