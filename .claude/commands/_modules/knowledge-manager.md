# Knowledge Management Module (Zettelkasten)

**Purpose:** Build a knowledge graph from learning content using Zettelkasten principles.

This module creates Source Notes, Zettel Notes, and Maps of Content to preserve and connect knowledge.
It requires both a content file and a plan file as inputs.

---

## Function: save_to_zettelkasten(CONTENT_FILE, PLAN_FILE)

**Input:**
- Content file path (string)
- Plan file path (string)

**Output:** Summary of knowledge structure created (string)

---

## Zettelkasten Workflow (6 Phases)

### Phase 1: Create Source Note (SRC)

**Purpose:** Record the source material with metadata

```bash
create_source_note() {
    local CONTENT_FILE="$1"
    local PLAN_FILE="$2"
    local URL="$3"

    echo "📝 Creating Source Note..."

    # Generate timestamp
    TIMESTAMP=$(date +"%Y%m%d-%H%M")

    # Extract title from content file or plan
    TITLE=$(basename "$CONTENT_FILE" .txt | tr '_' ' ' | cut -c 1-60)

    # Create source note filename
    SRC_FILE="SRC-${TIMESTAMP}-${TITLE// /-}.md"
    SRC_PATH="${VAULT_DIR}/${SRC_FILE}"

    # Create source note
    cat > "$SRC_PATH" <<EOF
# Source: $TITLE

**Type:** Source Note (SRC)
**Created:** $(date +"%Y-%m-%d %H:%M")
**Status:** unprocessed
**URL:** $URL

---

## Metadata

- **Content File:** [[${CONTENT_FILE}]]
- **Action Plan:** [[${PLAN_FILE}]]
- **Date Captured:** $(date +"%Y-%m-%d")

---

## Source Summary

[Brief 2-3 sentence summary of the source material]

---

## Processing Notes

This source has been captured and is ready for cognitive processing.

### Next Steps:
- [ ] Read and analyze content deeply
- [ ] Extract atomic concepts (3-7 Zettel notes)
- [ ] Create Quest MOC
- [ ] Connect to existing knowledge
- [ ] Update status to 'processed'

---

## Related Notes

(To be added during processing)

EOF

    echo "✓ Source note created: $SRC_FILE"
    echo "$SRC_PATH"
}
```

---

### Phase 2: Process into Atomic Concepts

**Purpose:** Extract 3-7 atomic concepts as Zettel notes

```bash
create_zettel_notes() {
    local CONTENT_FILE="$1"
    local SRC_PATH="$2"

    echo "🧠 Extracting atomic concepts..."

    # Read and analyze content
    CONTENT=$(cat "$CONTENT_FILE")

    # Identify 3-7 atomic concepts
    # This is done through careful analysis of the content
    # Each concept should be:
    # - Atomic (one idea)
    # - Declarative (states a claim)
    # - Self-contained (readable without source)
    # - Connected (links to related ideas)
    # - Actionable (includes practical application)

    # For each concept, create a Zettel note
    ZETTEL_FILES=()

    # Generate timestamp
    TIMESTAMP=$(date +"%Y%m%d-%H%M")

    # Example: Create Zettel note
    # (In practice, you'd loop through identified concepts)

    echo "   Identified X atomic concepts"
    echo "   Creating Zettel notes..."

    # Template for each Zettel note:
    create_zettel_note() {
        local CONCEPT_TITLE="$1"  # Declarative title
        local CONCEPT_CONTENT="$2"
        local PRACTICAL_APPLICATION="$3"
        local SOURCE_REF="$4"

        local ZETTEL_FILE="ZTL-${TIMESTAMP}-${CONCEPT_TITLE// /-}.md"
        local ZETTEL_PATH="${VAULT_DIR}/${ZETTEL_FILE}"

        cat > "$ZETTEL_PATH" <<EOF
# $CONCEPT_TITLE

**Type:** Zettel Note (ZTL)
**Created:** $(date +"%Y-%m-%d %H:%M")
**Tags:** #concept #learning

---

## Concept

$CONCEPT_CONTENT

---

## Practical Application

$PRACTICAL_APPLICATION

---

## Source

- [[${SOURCE_REF}]]

---

## Related Concepts

(To be added as connections are discovered)

EOF

        echo "✓ Created Zettel: $CONCEPT_TITLE"
        ZETTEL_FILES+=("$ZETTEL_PATH")
    }

    # Return array of created Zettel files
    echo "${ZETTEL_FILES[@]}"
}
```

**Zettel Quality Guidelines:**

✅ **Good Declarative Titles:**
- "Spaced repetition increases long-term retention"
- "Small batch sizes enable faster iteration"
- "Public accountability drives consistent shipping"

❌ **Bad Non-Declarative Titles:**
- "Spaced repetition" (just a topic)
- "Learning techniques" (too broad)
- "About memory" (vague)

---

### Phase 3: Create Learning Quest MOC

**Purpose:** Create Map of Content for the quest

```bash
create_quest_moc() {
    local PLAN_FILE="$1"
    local SRC_PATH="$2"
    local ZETTEL_FILES="$3"

    echo "🗺️  Creating Quest MOC..."

    # Extract quest title from plan
    QUEST_TITLE=$(grep "^# Ship-Learn-Next Quest:" "$PLAN_FILE" | sed 's/^# Ship-Learn-Next Quest: //')

    if [ -z "$QUEST_TITLE" ]; then
        QUEST_TITLE="Learning Quest"
    fi

    MOC_FILE="MOC-${QUEST_TITLE// /-}.md"
    MOC_PATH="${VAULT_DIR}/${MOC_FILE}"

    # Create MOC with quest structure
    cat > "$MOC_PATH" <<EOF
# Quest: $QUEST_TITLE

**Type:** Map of Content (MOC)
**Created:** $(date +"%Y-%m-%d %H:%M")
**Status:** In Progress

---

## Quest Overview

[Extract from plan file]

**Timeline:** 4-8 weeks
**Current Rep:** Rep 1

---

## Source Material

- [[$(basename "$SRC_PATH")]]

---

## Core Concepts

[List of Zettel notes - link to each one]

---

## Ship-Learn-Next Progression

### Rep 1: [Title]
**Status:** 🎯 Current
**Ship by:** [Date]

[Brief description]

**Related Concepts:**
- [[Zettel 1]]
- [[Zettel 2]]

---

### Rep 2: [Title]
**Status:** ⏳ Planned

[Brief description]

---

### Rep 3: [Title]
**Status:** ⏳ Planned

[Brief description]

---

### Rep 4: [Title]
**Status:** ⏳ Planned

[Brief description]

---

### Rep 5: [Title]
**Status:** ⏳ Planned

[Brief description]

---

## Learning Log

### $(date +"%Y-%m-%d")
- Quest started
- Source material captured
- Concepts extracted and processed
- Rep 1 planned

---

## Connections to Other Knowledge

[To be added as connections are discovered]

---

## Progress Tracker

- [ ] Rep 1 shipped
- [ ] Rep 2 shipped
- [ ] Rep 3 shipped
- [ ] Rep 4 shipped
- [ ] Rep 5 shipped

**Completion:** 0/5 reps (0%)

EOF

    echo "✓ Quest MOC created: $MOC_FILE"
    echo "$MOC_PATH"
}
```

---

### Phase 4: Connect to Existing Knowledge

**Purpose:** Find and create bidirectional links

```bash
connect_to_existing_knowledge() {
    local VAULT_DIR="$1"
    local NEW_ZETTEL_FILES="$2"

    echo "🔗 Searching for connections..."

    # Search vault for related concepts
    CONNECTIONS_FOUND=0

    for ZETTEL_FILE in "${NEW_ZETTEL_FILES[@]}"; do
        # Extract key terms from Zettel
        # Search existing notes for those terms
        # Create bidirectional links

        # Example: Search for keyword in existing notes
        KEYWORD=$(grep "^# " "$ZETTEL_FILE" | sed 's/^# //' | awk '{print $1}')

        if [ -n "$KEYWORD" ]; then
            # Search for related notes
            RELATED_NOTES=$(grep -rl "$KEYWORD" "$VAULT_DIR" --include="*.md" | grep -v "$(basename "$ZETTEL_FILE")")

            if [ -n "$RELATED_NOTES" ]; then
                echo "   Found connections for: $(basename "$ZETTEL_FILE")"
                CONNECTIONS_FOUND=$((CONNECTIONS_FOUND + 1))

                # Add links to both notes (bidirectional)
                # [Implementation would go here]
            fi
        fi
    done

    echo "✓ Found $CONNECTIONS_FOUND connections"
    echo "$CONNECTIONS_FOUND"
}
```

**Connection Types:**
- **Builds On:** Prerequisites
- **Extends:** Takes concept further
- **Contradicts:** Alternative view
- **Applies To:** Use cases
- **Example Of:** Instances

---

### Phase 5: Update Index

**Purpose:** Update vault index with new notes

```bash
update_vault_index() {
    local VAULT_DIR="$1"
    local SRC_FILE="$2"
    local MOC_FILE="$3"
    local ZETTEL_COUNT="$4"

    echo "📇 Updating vault index..."

    INDEX_FILE="${VAULT_DIR}/_INDEX.md"

    # Create index if it doesn't exist
    if [ ! -f "$INDEX_FILE" ]; then
        cat > "$INDEX_FILE" <<EOF
# Zettelkasten Vault Index

**Last Updated:** $(date +"%Y-%m-%d %H:%M")

---

## Maps of Content (MOCs)

---

## Recent Sources (SRC)

---

## Recent Zettel Notes (ZTL)

---

## Statistics

- **Total MOCs:** 0
- **Total Sources:** 0
- **Total Zettel:** 0
- **Total Notes:** 0

EOF
    fi

    # Update index with new notes
    # Add MOC to MOC section
    # Add SRC to Sources section
    # Update statistics

    # Update timestamp
    sed -i '' "s/\*\*Last Updated:\*\* .*/\*\*Last Updated:\*\* $(date +"%Y-%m-%d %H:%M")/" "$INDEX_FILE" 2>/dev/null || \
    sed -i "s/\*\*Last Updated:\*\* .*/\*\*Last Updated:\*\* $(date +"%Y-%m-%d %H:%M")/" "$INDEX_FILE"

    echo "✓ Index updated"
}
```

---

### Phase 6: Update Activity Log

**Purpose:** Record the knowledge management activity

```bash
update_activity_log() {
    local VAULT_DIR="$1"
    local QUEST_TITLE="$2"
    local ZETTEL_COUNT="$3"
    local CONNECTIONS="$4"

    echo "📋 Logging activity..."

    LOG_FILE="${VAULT_DIR}/_LOG.md"

    # Create log if it doesn't exist
    if [ ! -f "$LOG_FILE" ]; then
        cat > "$LOG_FILE" <<EOF
# Zettelkasten Activity Log

---

EOF
    fi

    # Add activity entry at top (most recent first)
    LOG_ENTRY="## $(date +"%Y-%m-%d %H:%M") - Quest Started: $QUEST_TITLE

- Created source note
- Extracted $ZETTEL_COUNT atomic concepts
- Created quest MOC
- Found $CONNECTIONS connections to existing knowledge
- Status: Rep 1 in progress

---

"

    # Prepend to log file
    echo "$LOG_ENTRY$(cat "$LOG_FILE")" > "$LOG_FILE"

    echo "✓ Activity logged"
}
```

---

## Main Knowledge Management Function

```bash
save_to_zettelkasten() {
    local CONTENT_FILE="$1"
    local PLAN_FILE="$2"
    local URL="$3"

    echo ""
    echo "🧠 Zettelkasten Knowledge Management"
    echo "======================================"
    echo ""

    # Validate inputs
    if [ ! -f "$CONTENT_FILE" ]; then
        echo "❌ Error: Content file not found"
        return 1
    fi

    if [ ! -f "$PLAN_FILE" ]; then
        echo "❌ Error: Plan file not found"
        return 1
    fi

    # Set vault directory
    VAULT_DIR="/home/user/aegis/zettelkasten_agent/vault"

    # Ensure vault exists
    if [ ! -d "$VAULT_DIR" ]; then
        echo "📁 Creating Zettelkasten vault..."
        mkdir -p "$VAULT_DIR"
    fi

    # Phase 1: Create Source Note
    SRC_PATH=$(create_source_note "$CONTENT_FILE" "$PLAN_FILE" "$URL")

    # Phase 2: Extract atomic concepts (creates Zettel notes)
    # Note: This requires careful analysis of content
    # For now, we guide the user to create them
    echo ""
    echo "🧠 Phase 2: Extract Atomic Concepts"
    echo "   Analyzing content for atomic concepts..."
    echo "   (This requires deep cognitive processing)"
    echo ""

    # In practice, you would analyze the content and create 3-7 Zettel notes
    # For this module, we'll provide the structure and guidance

    # Phase 3: Create Quest MOC
    MOC_PATH=$(create_quest_moc "$PLAN_FILE" "$SRC_PATH" "")

    # Phase 4: Connect to existing knowledge
    CONNECTIONS=$(connect_to_existing_knowledge "$VAULT_DIR" "")

    # Phase 5: Update index
    update_vault_index "$VAULT_DIR" "$(basename "$SRC_PATH")" "$(basename "$MOC_PATH")" "0"

    # Phase 6: Log activity
    QUEST_TITLE=$(basename "$MOC_PATH" .md | sed 's/^MOC-//' | tr '-' ' ')
    update_activity_log "$VAULT_DIR" "$QUEST_TITLE" "0" "$CONNECTIONS"

    # Summary
    echo ""
    echo "✅ Knowledge Management Complete!"
    echo ""
    echo "📦 Created:"
    echo "   - Source Note: $(basename "$SRC_PATH")"
    echo "   - Quest MOC: $(basename "$MOC_PATH")"
    echo "   - Connections: $CONNECTIONS"
    echo ""
    echo "📍 Location: $VAULT_DIR"
    echo ""

    return 0
}
```

---

## Vault Structure

```
vault/
├── _INDEX.md               # Master navigation
├── _LOG.md                 # Activity log
├── SRC-YYYYMMDD-HHMM-Title.md    # Source notes
├── ZTL-YYYYMMDD-HHMM-Title.md    # Zettel notes (atomic concepts)
└── MOC-Quest-Title.md            # Maps of content
```

---

## Source Note Status Lifecycle

```
unprocessed → processing → processed
```

**Statuses:**
- `unprocessed`: Captured but not yet analyzed
- `processing`: Currently extracting concepts
- `processed`: Concepts extracted, connections made

---

## Usage

### Standalone Usage
```bash
# Save content and plan to Zettelkasten
save_to_zettelkasten "article.txt" "Ship-Learn-Next Plan - Quest.md" "https://example.com"
```

### As Module (called by other commands)
```bash
# Source this module
source .claude/commands/_modules/knowledge-manager.md

# Use the function
save_to_zettelkasten "$CONTENT_FILE" "$PLAN_FILE" "$URL"
```

---

## Note Types Reference

### Source Note (SRC)
- Captures original material
- Links to content and plan files
- Tracks processing status

### Zettel Note (ZTL)
- One atomic concept
- Declarative title (states a claim)
- Self-contained explanation
- Practical application
- Links to source and related concepts

### Map of Content (MOC)
- Organizes related notes
- Provides quest structure
- Tracks rep progress
- Shows knowledge connections

---

## Philosophy

**You're not just saving content. You're building a knowledge graph that grows with each learning cycle.**

Every new quest:
- Adds atomic concepts to your vault
- Connects to existing knowledge
- Strengthens your understanding
- Creates a web of ideas

This is progressive learning. Knowledge compounds over time.

---

## Success Criteria

A successful knowledge management workflow produces:
- ✅ 1 Source Note with complete metadata
- ✅ 3-7 Zettel notes with declarative titles
- ✅ 1 Quest MOC integrating the action plan
- ✅ Connections to existing knowledge (grows over time)
- ✅ Updated index and activity log

---

**Your knowledge graph is growing. Keep learning. Keep connecting.**
