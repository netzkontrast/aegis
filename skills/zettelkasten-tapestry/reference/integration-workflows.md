# Integration Workflows - Technical Implementation

This document provides detailed technical workflows for integrating Tapestry, Ship-Learn-Next, and Zettelkasten.

---

## Workflow 1: Initial Quest Creation

### Input
User provides: `tapestry [URL] and save to zettelkasten`

### Complete Step-by-Step Process

#### Step 1: Run Tapestry Extraction

```bash
# Detect URL type
URL="$1"

if [[ "$URL" =~ youtube\.com|youtu\.be ]]; then
    TYPE="youtube"
elif [[ "$URL" =~ \.pdf$ ]]; then
    TYPE="pdf"
else
    TYPE="article"
fi

# Extract content (see tapestry.md for details)
# Result: content-file.txt
```

**Output:**
- Content file: `[Title].txt`
- Path stored in: `$CONTENT_FILE`

#### Step 2: Create Ship-Learn-Next Plan

```bash
# Run ship-learn-next workflow on extracted content
# See ship-learn-next.md for details

# Result: Ship-Learn-Next Plan - [Quest Title].md
```

**Output:**
- Plan file: `Ship-Learn-Next Plan - [Quest Title].md`
- Path stored in: `$PLAN_FILE`

#### Step 3: Generate Timestamps and Names

```bash
# Generate timestamp
TIMESTAMP=$(date +%Y%m%d-%H%M)

# Extract quest title from plan file
QUEST_TITLE=$(head -n 1 "$PLAN_FILE" | sed 's/# Your Ship-Learn-Next Quest: //' | tr ' ' '-' | tr '[:upper:]' '[:lower:]')

# Create safe filenames
SRC_FILENAME="SRC-${TIMESTAMP}-${QUEST_TITLE}.md"
MOC_FILENAME="MOC-${QUEST_TITLE}.md"

# Vault path
VAULT_PATH="/home/user/aegis/zettelkasten_agent/vault"
```

#### Step 4: Create Source Note

```bash
# Read content for preview
CONTENT=$(cat "$CONTENT_FILE")
WORD_COUNT=$(echo "$CONTENT" | wc -w)

# Create SRC note
cat > "${VAULT_PATH}/${SRC_FILENAME}" << 'EOF'
# SRC-${TIMESTAMP}-${QUEST_TITLE}

## Metadata
- **Type**: Source Note
- **Status**: unprocessed
- **Source**: ${URL}
- **Extracted**: $(date '+%Y-%m-%d %H:%M')
- **Quest**: [[MOC-${QUEST_TITLE}]]
- **Content File**: ${CONTENT_FILE}
- **Action Plan**: ${PLAN_FILE}
- **Word Count**: ${WORD_COUNT}

## Source Context

[Content extracted from: ${TYPE}]

## Raw Content

${CONTENT}

## Initial Observations

[To be filled during processing]

---

## Cognitive Processing

[Status: unprocessed]

### Factual Analysis
[To be completed]

### Inferential Analysis
[To be completed]

### Generative Synthesis
[To be completed]

---

## Extracted Zettel Notes

[To be created during processing]

---

## Processing Log

- [ ] Read through entire content
- [ ] Complete factual analysis
- [ ] Complete inferential analysis
- [ ] Complete generative synthesis
- [ ] Extract atomic concepts
- [ ] Create Zettel notes
- [ ] Link to existing knowledge
- [ ] Update Quest MOC
- [ ] Update _INDEX.md
- [ ] Status changed to: processed

EOF
```

#### Step 5: Cognitive Processing (Extract Atomic Concepts)

**This is the CRITICAL step where content becomes knowledge.**

```python
# Pseudo-code for concept extraction

def extract_atomic_concepts(content):
    """
    Analyze content and extract 3-7 atomic concepts
    """
    concepts = []

    # Read and analyze content
    # Look for:
    # - Core principles stated
    # - Techniques described
    # - Patterns identified
    # - Advice given
    # - Case studies presented

    # For each potential concept:
    for potential_concept in content:
        # Test if atomic (single idea)
        if is_atomic(potential_concept):
            # Create declarative title
            title = create_declarative_title(potential_concept)

            # Extract explanation
            explanation = extract_explanation(potential_concept)

            # Identify source location
            source_ref = locate_in_source(potential_concept)

            # Add to concepts
            concepts.append({
                'title': title,
                'explanation': explanation,
                'source_ref': source_ref,
                'timestamp': generate_timestamp()
            })

    return concepts

# Run extraction
concepts = extract_atomic_concepts(content)
```

**Manual Process (Claude-assisted):**

1. **Read the entire content carefully**
2. **Identify 3-7 core concepts** (not more, not less)
3. **For each concept, ask:**
   - Is this a single idea? (atomic test)
   - Can I state it as a claim? (declarative test)
   - Is it actionable or insightful? (value test)
4. **Create declarative titles**
5. **Write clear explanations**
6. **Identify practical applications**

#### Step 6: Create Zettel Notes

```bash
# For each extracted concept
for concept in "${concepts[@]}"; do
    # Generate timestamp (increment by 1 minute for each note)
    ZTL_TIMESTAMP=$(date -d "+${i} minutes" +%Y%m%d-%H%M)

    # Create safe filename from title
    TITLE_SAFE=$(echo "$concept_title" | tr ' ' '-' | tr '[:upper:]' '[:lower:]')
    ZTL_FILENAME="ZTL-${ZTL_TIMESTAMP}-${TITLE_SAFE}.md"

    # Create Zettel note
    cat > "${VAULT_PATH}/${ZTL_FILENAME}" << EOF
# ZTL-${ZTL_TIMESTAMP}-${concept_title}

## Concept

${concept_summary}

## Explanation

${concept_explanation}

## Source

- **From**: [[SRC-${TIMESTAMP}-${QUEST_TITLE}]]
- **Original**: ${URL}
- **Quest**: [[MOC-${QUEST_TITLE}]]
- **Created**: $(date '+%Y-%m-%d %H:%M')
- **Type**: ${concept_type}

## Connections

### Builds On
[To be filled - search vault for related concepts]

### Extends
[To be filled]

### Applies To
[To be filled]

## Practical Application

${concept_application}

## Questions & Extensions

${concept_questions}

## Tags

${concept_tags}

## Revision History

- **v1.0** ($(date '+%Y-%m-%d')): Initial creation from [[SRC-${TIMESTAMP}-${QUEST_TITLE}]]

EOF

    # Add to concepts list
    ZTL_NOTES+=("$ZTL_FILENAME")

    ((i++))
done
```

#### Step 7: Search for Existing Connections

```bash
# For each new Zettel note
for ztl_note in "${ZTL_NOTES[@]}"; do
    # Extract key terms from the note
    KEY_TERMS=$(grep "^## Concept" "${VAULT_PATH}/${ztl_note}" | extract_keywords)

    # Search vault for related notes
    RELATED_NOTES=$(grep -l "$KEY_TERMS" "${VAULT_PATH}"/ZTL-*.md | grep -v "$ztl_note")

    # For each related note found
    for related in "${RELATED_NOTES[@]}"; do
        # Determine relationship type
        RELATIONSHIP=$(determine_relationship "$ztl_note" "$related")

        # Add bidirectional links
        add_connection "$ztl_note" "$related" "$RELATIONSHIP"
        add_connection "$related" "$ztl_note" "$(reverse_relationship $RELATIONSHIP)"
    done
done
```

**Connection Discovery Algorithm:**

```python
def find_connections(new_note, vault):
    """
    Find connections between new note and existing notes
    """
    connections = []

    # Extract key concepts from new note
    new_concepts = extract_concepts(new_note)

    # Search existing notes
    for existing_note in vault:
        # Skip if same note
        if existing_note.id == new_note.id:
            continue

        # Calculate semantic similarity
        similarity = calculate_similarity(new_concepts, existing_note.concepts)

        if similarity > THRESHOLD:
            # Determine relationship type
            relationship = classify_relationship(new_note, existing_note)

            connections.append({
                'note': existing_note,
                'relationship': relationship,
                'strength': similarity
            })

    return connections

def classify_relationship(note_a, note_b):
    """
    Determine the type of relationship
    """
    # Check for foundational relationship
    if is_prerequisite(note_b, note_a):
        return 'builds_on'

    # Check for extension relationship
    if extends_concept(note_a, note_b):
        return 'extends'

    # Check for contradiction
    if contradicts(note_a, note_b):
        return 'contradicts'

    # Check for application
    if applies_to(note_a, note_b):
        return 'applies_to'

    # Default: related
    return 'related_to'
```

#### Step 8: Create Quest MOC

```bash
# Extract rep details from Ship-Learn-Next plan
REP1_GOAL=$(grep -A 5 "## Rep 1:" "$PLAN_FILE" | grep "Ship Goal" | sed 's/\*\*Ship Goal\*\*: //')

# Create MOC
cat > "${VAULT_PATH}/${MOC_FILENAME}" << EOF
# MOC-${QUEST_TITLE}

## Quest Overview

- **Goal**: ${quest_goal}
- **Timeline**: $(date '+%Y-%m-%d') → $(date -d '+8 weeks' '+%Y-%m-%d')
- **Status**: 🟢 Active
- **Current Rep**: Rep 1 of 5
- **Completion**: 0%

## Why This Quest

${quest_motivation}

## Source Material

### Primary Sources
- [[SRC-${TIMESTAMP}-${QUEST_TITLE}]] - ${content_description} - unprocessed

## Core Concepts (Zettel Notes)

### Foundational Concepts
$(for note in "${ZTL_NOTES[@]}"; do
    echo "- [[${note%.md}]] - ${note_summary}"
done)

## Learning Progression (Ship-Learn-Next Integration)

### Rep 1: ${REP1_GOAL} - ⏳ Not Started

**Ship Goal**: ${REP1_GOAL}

**Timeline**: $(date '+%Y-%m-%d') → $(date -d '+1 week' '+%Y-%m-%d')

**Success Criteria**:
${rep1_criteria}

**Concepts Applied**:
${rep1_concepts}

**What Was Shipped**: [To be filled]

**Key Learnings**: [To be filled after completion]

**Reflection**: [To be filled after completion]

### Rep 2-5: [To be detailed after Rep 1]

${remaining_reps_summary}

## Connections to Other Quests

[None yet - first quest]

## Progressive Learning Path

**What This Quest Unlocks:**

[To be identified after Rep 2-3 completion]

## Resources

**Action Plan**: ${PLAN_FILE}
**Content Files**: ${CONTENT_FILE}

## Metrics & Analytics

**Total Time Invested**: 0 hours
**Zettel Notes Created**: ${#ZTL_NOTES[@]}
**Connections Made**: ${connection_count}
**Artifacts Shipped**: 0

---

**Created**: $(date '+%Y-%m-%d')
**Last Updated**: $(date '+%Y-%m-%d')
**Status**: Active

EOF
```

#### Step 9: Update Master Index

```bash
# Check if _INDEX.md exists
if [ ! -f "${VAULT_PATH}/_INDEX.md" ]; then
    # Create new index
    cat > "${VAULT_PATH}/_INDEX.md" << EOF
# Knowledge Base Index

## Active Learning Quests

## Completed Quests

## Domain Maps

## Statistics

**Last Updated**: $(date '+%Y-%m-%d')
EOF
fi

# Add new MOC to index
sed -i "/## Active Learning Quests/a - [[MOC-${QUEST_TITLE}]] - Rep 1/5 - ${quest_summary}" "${VAULT_PATH}/_INDEX.md"

# Update statistics
TOTAL_ZTL=$(ls "${VAULT_PATH}"/ZTL-*.md 2>/dev/null | wc -l)
TOTAL_SRC=$(ls "${VAULT_PATH}"/SRC-*.md 2>/dev/null | wc -l)
TOTAL_MOC=$(ls "${VAULT_PATH}"/MOC-*.md 2>/dev/null | wc -l)

# Update stats in index
sed -i "s/\*\*Total Zettel Notes\*\*: .*/\*\*Total Zettel Notes\*\*: ${TOTAL_ZTL}/" "${VAULT_PATH}/_INDEX.md"
sed -i "s/\*\*Total Source Notes\*\*: .*/\*\*Total Source Notes\*\*: ${TOTAL_SRC}/" "${VAULT_PATH}/_INDEX.md"
sed -i "s/\*\*Total MOCs\*\*: .*/\*\*Total MOCs\*\*: ${TOTAL_MOC}/" "${VAULT_PATH}/_INDEX.md"
```

#### Step 10: Update Source Note with Processing Results

```bash
# Update SRC note with created Zettel notes
cat >> "${VAULT_PATH}/${SRC_FILENAME}" << EOF

## Extracted Zettel Notes

$(for note in "${ZTL_NOTES[@]}"; do
    echo "- [[${note%.md}]]"
done)

Total: ${#ZTL_NOTES[@]} Zettel notes created

---

## Processing Log

- [x] Read through entire content
- [x] Complete factual analysis
- [x] Complete inferential analysis
- [x] Complete generative synthesis
- [x] Extract atomic concepts
- [x] Create Zettel notes (${#ZTL_NOTES[@]} created)
- [x] Link to existing knowledge (${connection_count} connections)
- [x] Update Quest MOC
- [x] Update _INDEX.md
- [x] Status changed to: processed

**Processing Time**: $(($SECONDS / 60)) minutes
**Processed By**: Claude + User

EOF

# Update status in metadata
sed -i 's/Status: unprocessed/Status: processed/' "${VAULT_PATH}/${SRC_FILENAME}"
```

#### Step 11: Present Summary to User

```bash
cat << EOF

✅ Zettelkasten-Tapestry Workflow Complete!

📥 Content Extracted:
   ✓ ${TYPE}: ${original_title}
   ✓ Saved to: ${CONTENT_FILE}
   ✓ ${WORD_COUNT} words extracted

📋 Action Plan Created:
   ✓ Quest: ${QUEST_TITLE}
   ✓ Saved to: ${PLAN_FILE}

🧠 Knowledge Captured:
   ✓ Source Note: ${SRC_FILENAME}
   ✓ Zettel Notes: ${#ZTL_NOTES[@]} atomic concepts
   ✓ Quest MOC: ${MOC_FILENAME}

🔗 Knowledge Connections:
   ✓ ${connection_count} connections found
   $(if [ $connection_count -eq 0 ]; then
       echo "   (This is your first quest - connections will grow over time!)"
   fi)

📊 Vault Statistics:
   ✓ Total Zettel Notes: ${TOTAL_ZTL}
   ✓ Total Source Notes: ${TOTAL_SRC}
   ✓ Total MOCs: ${TOTAL_MOC}

🎯 Your Quest: ${quest_goal}

📍 Rep 1 (This Week): ${REP1_GOAL}

When will you ship Rep 1?

EOF
```

---

## Workflow 2: Rep Completion & Learning Capture

### Input
User completes a rep and reports learnings

### Process

#### Step 1: User Ships Rep & Reflects

User provides:
- What was shipped (artifact/link/description)
- Reflection answers (from Ship-Learn-Next plan)

#### Step 2: Extract Learnings as Zettel Notes

```python
def extract_learnings_from_rep(reflection):
    """
    Convert rep reflections into atomic learnings
    """
    learnings = []

    # Analyze reflection
    # Look for:
    # - Unexpected outcomes
    # - Validated assumptions
    # - Invalidated assumptions
    # - New techniques discovered
    # - Practical insights

    # For each learning:
    for learning in identified_learnings:
        # Create declarative title
        title = "Learning: " + create_claim(learning)

        # Add context about what was done
        context = {
            'rep': rep_number,
            'shipped': artifact_description,
            'expected': expectation,
            'actual': reality,
            'insight': core_learning
        }

        learnings.append({
            'title': title,
            'context': context,
            'type': 'experiential'
        })

    return learnings
```

#### Step 3: Create Learning Zettel Notes

```bash
# For each learning extracted
for learning in "${learnings[@]}"; do
    TIMESTAMP=$(date -d "+${i} minutes" +%Y%m%d-%H%M)
    TITLE_SAFE=$(echo "$learning_title" | tr ' ' '-')
    ZTL_FILENAME="ZTL-${TIMESTAMP}-${TITLE_SAFE}.md"

    cat > "${VAULT_PATH}/${ZTL_FILENAME}" << EOF
# ZTL-${TIMESTAMP}-${learning_title}

## Concept

${learning_statement}

## Explanation

**Context**: ${rep_context}

**What Happened**: ${actual_outcome}

**Expected**: ${expected_outcome}

**Key Insight**: ${core_learning}

## Source

- **From**: Rep ${rep_number} of [[MOC-${QUEST_TITLE}]]
- **Shipped**: ${artifact_description}
- **Date**: $(date '+%Y-%m-%d')
- **Type**: Experiential Learning

## Connections

### Validates
- [[ZTL-Original-Concept]] - [How this confirms it]

### Contradicts
- [[ZTL-Previous-Assumption]] - [How this refutes it]

### Extends
- [[ZTL-Related-Concept]] - [How this builds on it]

## Practical Application

**How to use this learning**:

${practical_application}

**When this matters**:
${context_for_use}

## Questions & Extensions

- ${follow_up_question_1}
- ${follow_up_question_2}

## Tags

#learning #rep${rep_number} #experiential #${quest_tag}

## Revision History

- **v1.0** ($(date '+%Y-%m-%d')): Created from Rep ${rep_number} reflection

EOF

    LEARNING_NOTES+=("$ZTL_FILENAME")
    ((i++))
done
```

#### Step 4: Update Quest MOC

```bash
# Find the MOC file
MOC_FILE="${VAULT_PATH}/MOC-${QUEST_TITLE}.md"

# Update rep section with completion info
sed -i "/### Rep ${rep_number}:/,/### Rep $((rep_number + 1))/ {
    s/Status.*$/✅ Complete/
    /\*\*What Was Shipped\*\*:/c\*\*What Was Shipped\*\*: ${artifact_description}
}" "$MOC_FILE"

# Add learnings section
cat >> "$MOC_FILE" << EOF

**Key Learnings**:
$(for note in "${LEARNING_NOTES[@]}"; do
    echo "- [[${note%.md}]] - ${learning_summary}"
done)

**Reflection**:
- **What happened**: ${reflection_actual}
- **What worked**: ${reflection_worked}
- **What didn't**: ${reflection_didnt_work}
- **Surprises**: ${reflection_surprises}
- **Rating**: ${reflection_rating}/10

EOF

# Update completion percentage
COMPLETION=$(( (rep_number * 100) / 5 ))
sed -i "s/\*\*Completion\*\*: .*%/\*\*Completion\*\*: ${COMPLETION}%/" "$MOC_FILE"

# Update current rep
sed -i "s/\*\*Current Rep\*\*: Rep .*/\*\*Current Rep\*\*: Rep $((rep_number + 1)) of 5/" "$MOC_FILE"
```

#### Step 5: Connect Learning Notes

```bash
# For each learning note
for learning_note in "${LEARNING_NOTES[@]}"; do
    # Find original concept that was tested
    ORIGINAL_CONCEPT=$(extract_tested_concept "$learning_note")

    if [ -n "$ORIGINAL_CONCEPT" ]; then
        # Add validation/contradiction link
        if validates_concept "$learning_note" "$ORIGINAL_CONCEPT"; then
            add_bidirectional_link "$learning_note" "$ORIGINAL_CONCEPT" "validates" "validated_by"
        elif contradicts_concept "$learning_note" "$ORIGINAL_CONCEPT"; then
            add_bidirectional_link "$learning_note" "$ORIGINAL_CONCEPT" "contradicts" "contradicted_by"
        fi
    fi

    # Search for related concepts
    find_and_connect "$learning_note"
done
```

#### Step 6: Adjust Future Reps

```bash
# Based on learnings, update future rep plans in MOC

# Example: If learning revealed a gap
if [ "$learning_reveals_gap" = true ]; then
    # Add new concept to Rep N plan
    sed -i "/### Rep $((rep_number + 1)):/a \*\*Additional Concept\*\*: [[ZTL-New-Concept]] - ${gap_description}" "$MOC_FILE"
fi

# Example: If learning suggests change in approach
if [ "$learning_suggests_change" = true ]; then
    # Add note to next rep
    sed -i "/### Rep $((rep_number + 1)):/a \*\*Adjustment\*\*: ${approach_change}" "$MOC_FILE"
fi
```

#### Step 7: Generate Progress Update

```bash
cat << EOF

✅ Rep ${rep_number} Captured!

🚢 Shipped:
   ${artifact_description}

📚 Learnings Captured:
   $(for note in "${LEARNING_NOTES[@]}"; do
       echo "✓ ${learning_summary}"
   done)

🔗 Connections Updated:
   ✓ ${new_connections} new connections
   ✓ ${validated_concepts} concepts validated
   ✓ ${contradicted_concepts} concepts refined

📊 Quest Progress:
   ✓ Rep ${rep_number}/5 complete (${COMPLETION}%)
   ✓ Total Zettel: ${total_zettel_for_quest}
   ✓ Knowledge density: ${knowledge_per_rep}

🎯 Next: Rep $((rep_number + 1))
   ${next_rep_goal}

Ready to plan Rep $((rep_number + 1))?

EOF
```

---

## Workflow 3: Progressive Path Discovery

### Input
User completes quest or asks for next learning path

### Process

#### Step 1: Analyze Knowledge Graph

```python
def discover_progressive_paths(quest_moc, vault):
    """
    Analyze completed quest and suggest next learning paths
    """
    paths = []

    # Extract concepts from completed quest
    quest_concepts = extract_concepts(quest_moc)

    # Analyze each concept
    for concept in quest_concepts:
        # Find related concepts in vault
        related = find_related_concepts(concept, vault)

        # Identify natural progressions
        progressions = identify_progressions(concept, related)

        for progression in progressions:
            paths.append({
                'next_concept': progression,
                'builds_on': concept,
                'complexity_increase': calculate_complexity_delta(concept, progression),
                'rationale': explain_progression(concept, progression)
            })

    # Find concepts mentioned but not learned
    mentioned_not_learned = find_knowledge_gaps(quest_moc, vault)

    for gap in mentioned_not_learned:
        paths.append({
            'next_concept': gap,
            'fills_gap': True,
            'rationale': f"This was mentioned in {quest_moc} but not deeply explored"
        })

    # Find related domains
    related_domains = find_related_domains(quest_concepts, vault)

    for domain in related_domains:
        paths.append({
            'next_domain': domain,
            'connection_type': 'related',
            'rationale': explain_domain_connection(quest_moc, domain)
        })

    # Rank by learning value
    ranked_paths = rank_by_value(paths)

    return ranked_paths[:3]  # Top 3 suggestions
```

#### Step 2: Generate Quest Suggestions

```bash
# Get top 3 progressive paths
PATHS=$(discover_progressive_paths "$MOC_FILE" "$VAULT_PATH")

# For each path, create a suggested quest outline
for path in "${PATHS[@]}"; do
    SUGGESTED_TITLE=$(echo "$path" | jq -r '.title')
    BUILDS_ON=$(echo "$path" | jq -r '.builds_on[]')
    NEW_CONCEPTS=$(echo "$path" | jq -r '.new_concepts[]')
    COMPLEXITY=$(echo "$path" | jq -r '.complexity_level')

    # Create suggestion document
    cat << EOF

## Option $((i+1)): ${SUGGESTED_TITLE}

**Why This Next**:
${path_rationale}

**Builds On** (from ${QUEST_TITLE}):
$(for concept in "${BUILDS_ON[@]}"; do
    echo "- [[${concept}]]"
done)

**New Concepts You'll Learn**:
$(for concept in "${NEW_CONCEPTS[@]}"; do
    echo "- ${concept}"
done)

**Complexity**: ${COMPLEXITY} (+${complexity_delta} from current)

**Suggested Source Material**:
${suggested_resources}

**Estimated Timeline**: ${estimated_weeks} weeks

EOF

    ((i++))
done
```

#### Step 3: Present Options to User

```bash
cat << EOF

🎯 Quest "${QUEST_TITLE}" Complete! Congratulations! 🎉

📊 Quest Summary:
   ✓ All 5 reps shipped
   ✓ ${total_zettel} Zettel notes created
   ✓ ${total_connections} knowledge connections
   ✓ ${artifacts_shipped} artifacts shipped

🧠 Knowledge Graph Growth:
   ✓ Vault now contains ${vault_total_zettel} Zettel notes
   ✓ ${new_connections} connections discovered during this quest

---

🚀 Progressive Learning Paths

Based on your knowledge graph, here are three natural next quests:

$(display_quest_suggestions)

---

Which path interests you? Or would you like to explore something different?

EOF
```

---

## Workflow 4: Cross-Quest Connection Discovery

### Trigger
When processing a new quest and existing knowledge exists

### Process

#### Step 1: Extract Concepts from New Source

```python
def extract_and_connect_new_quest(new_source, existing_vault):
    """
    Process new quest while actively connecting to existing knowledge
    """
    # Extract concepts from new source
    new_concepts = extract_atomic_concepts(new_source)

    connections = []

    # For each new concept
    for new_concept in new_concepts:
        # Search existing vault
        similar_notes = semantic_search(new_concept, existing_vault)

        for similar in similar_notes:
            # Calculate similarity
            similarity = calculate_similarity(new_concept, similar)

            if similarity > THRESHOLD:
                # Determine relationship
                relationship = classify_relationship(new_concept, similar)

                # Create connection
                connections.append({
                    'new': new_concept,
                    'existing': similar,
                    'relationship': relationship,
                    'strength': similarity,
                    'insight': generate_connection_insight(new_concept, similar)
                })

    return connections
```

#### Step 2: Highlight Cross-Quest Insights

```bash
# When creating new Zettel notes for Quest B
# and connections to Quest A are found

cat << EOF

🔗 Cross-Quest Connection Discovered!

**New Concept** (Quest B): [[ZTL-New-Concept]]
"${new_concept_title}"

**Connects To** (Quest A): [[ZTL-Existing-Concept]]
"${existing_concept_title}"

**Relationship**: ${relationship_type}

**Insight**: ${connection_insight}

This connection reveals: ${meta_insight}

EOF

# Update both MOCs
echo "- Connected to [[MOC-Quest-B]] via [[ZTL-New-Concept]]" >> "$MOC_QUEST_A"
echo "- Connected to [[MOC-Quest-A]] via [[ZTL-Existing-Concept]]" >> "$MOC_QUEST_B"
```

#### Step 3: Update Knowledge Graph Visualization

```bash
# Update INDEX with cross-quest relationships

cat >> "${VAULT_PATH}/_INDEX.md" << EOF

## Quest Relationships

- [[MOC-Quest-A]] ←→ [[MOC-Quest-B]]
  - Shared concepts: [[ZTL-X]], [[ZTL-Y]]
  - Connection type: ${relationship}

EOF
```

---

## Workflow 5: Knowledge Maintenance

### Weekly Review

```bash
#!/bin/bash
# weekly-review.sh

VAULT_PATH="/home/user/aegis/zettelkasten_agent/vault"

echo "=== Weekly Knowledge Review ==="
echo ""

# Check active quests
ACTIVE_QUESTS=$(grep -l "Status.*Active" "$VAULT_PATH"/MOC-*.md)

echo "📋 Active Quests:"
for quest in $ACTIVE_QUESTS; do
    QUEST_NAME=$(basename "$quest" .md)
    CURRENT_REP=$(grep "Current Rep" "$quest" | sed 's/.*Rep \([0-9]\).*/\1/')
    echo "  - $QUEST_NAME (Rep $CURRENT_REP/5)"
done
echo ""

# Check unprocessed sources
UNPROCESSED=$(grep -l "Status: unprocessed" "$VAULT_PATH"/SRC-*.md)

if [ -n "$UNPROCESSED" ]; then
    echo "⚠️  Unprocessed Sources:"
    for src in $UNPROCESSED; do
        echo "  - $(basename "$src" .md)"
    done
    echo "  Action: Process these into Zettel notes"
    echo ""
fi

# Recent connections
echo "🔗 Recent Connections (last 7 days):"
find "$VAULT_PATH" -name "ZTL-*.md" -mtime -7 -exec grep -l "Revision History" {} \; | head -5
echo ""

# Suggest review candidates
echo "📚 Suggested for Review:"
# Notes created >30 days ago with no recent updates
find "$VAULT_PATH" -name "ZTL-*.md" -mtime +30 ! -mtime -7 | head -3
echo ""

echo "Next review: $(date -d '+7 days' '+%Y-%m-%d')"
```

### Monthly Maintenance

```bash
#!/bin/bash
# monthly-maintenance.sh

VAULT_PATH="/home/user/aegis/zettelkasten_agent/vault"

echo "=== Monthly Knowledge Maintenance ==="
echo ""

# Orphan detection
echo "🔍 Checking for orphan notes..."
ORPHANS=$(find "$VAULT_PATH" -name "ZTL-*.md" -exec grep -L "\[\[ZTL-" {} \;)

if [ -n "$ORPHANS" ]; then
    echo "⚠️  Found $(echo "$ORPHANS" | wc -l) orphan notes"
    echo "  Action: Connect these to knowledge graph"
fi
echo ""

# MOC health check
echo "📊 MOC Health Check:"
for moc in "$VAULT_PATH"/MOC-*.md; do
    NOTE_COUNT=$(grep -c "\[\[ZTL-" "$moc")
    echo "  - $(basename "$moc" .md): $NOTE_COUNT notes"
done
echo ""

# Suggest consolidation
echo "🔄 Consolidation Opportunities:"
# Find similar concepts that might need merging
# (This would be a more complex script in practice)
echo ""

# Update statistics
echo "📈 Vault Statistics:"
TOTAL_ZTL=$(ls "$VAULT_PATH"/ZTL-*.md 2>/dev/null | wc -l)
TOTAL_SRC=$(ls "$VAULT_PATH"/SRC-*.md 2>/dev/null | wc -l)
TOTAL_MOC=$(ls "$VAULT_PATH"/MOC-*.md 2>/dev/null | wc -l)
TOTAL_CONNECTIONS=$(grep -oh "\[\[ZTL-" "$VAULT_PATH"/*.md | wc -l)

echo "  Zettel Notes: $TOTAL_ZTL"
echo "  Source Notes: $TOTAL_SRC"
echo "  MOCs: $TOTAL_MOC"
echo "  Total Connections: $TOTAL_CONNECTIONS"
echo "  Avg Connections/Note: $((TOTAL_CONNECTIONS / TOTAL_ZTL))"
echo ""

echo "Next maintenance: $(date -d '+30 days' '+%Y-%m-%d')"
```

---

## Error Handling

### Common Issues & Solutions

#### Issue 1: Vault Path Not Found

```bash
if [ ! -d "$VAULT_PATH" ]; then
    echo "⚠️  Zettelkasten vault not found at: $VAULT_PATH"
    echo ""
    echo "Creating vault structure..."
    mkdir -p "$VAULT_PATH"

    # Create _INDEX.md
    cat > "$VAULT_PATH/_INDEX.md" << EOF
# Knowledge Base Index

## Active Learning Quests

## Completed Quests

## Domain Maps

## Statistics

**Last Updated**: $(date '+%Y-%m-%d')
EOF

    # Create _LOG.md
    cat > "$VAULT_PATH/_LOG.md" << EOF
# Zettelkasten Action Log

## $(date '+%Y-%m-%d')

- Vault initialized
- Created master index

EOF

    echo "✓ Vault structure created"
fi
```

#### Issue 2: Tapestry Extraction Failed

```bash
if [ ! -f "$CONTENT_FILE" ] || [ ! -s "$CONTENT_FILE" ]; then
    echo "⚠️  Content extraction failed"
    echo ""
    echo "Possible causes:"
    echo "  - URL is not accessible"
    echo "  - Content requires authentication"
    echo "  - Extraction tool not installed"
    echo ""
    echo "Action: Check URL and retry, or provide content file manually"
    exit 1
fi
```

#### Issue 3: No Concepts Extracted

```bash
if [ ${#concepts[@]} -eq 0 ]; then
    echo "⚠️  No concepts extracted from content"
    echo ""
    echo "Possible causes:"
    echo "  - Content is too short/vague"
    echo "  - Content is not educational/actionable"
    echo ""
    echo "Action: Review content and identify 3-7 core concepts manually"
    exit 1
fi
```

#### Issue 4: Connection Discovery Fails

```bash
# Gracefully handle no connections found
if [ $connection_count -eq 0 ]; then
    echo "ℹ️  No connections found (yet)"
    echo ""
    echo "This is normal for:"
    echo "  - First learning quest"
    echo "  - New domains not related to previous learning"
    echo ""
    echo "Connections will emerge as you build more knowledge"
fi
```

---

## Performance Optimization

### Batch Processing

When processing multiple sources:

```bash
# Process multiple URLs in one session
for url in "${urls[@]}"; do
    # Extract all content first (parallel)
    tapestry "$url" &
    PIDS+=($!)
done

# Wait for all extractions
for pid in "${PIDS[@]}"; do
    wait "$pid"
done

# Then process into Zettelkasten sequentially
for content_file in *.txt; do
    process_to_zettelkasten "$content_file"
done
```

### Caching

```bash
# Cache semantic similarity calculations
CACHE_DIR="$HOME/.zettelkasten-cache"
mkdir -p "$CACHE_DIR"

# Before calculating similarity
CACHE_KEY="${note1_hash}-${note2_hash}"
if [ -f "$CACHE_DIR/$CACHE_KEY" ]; then
    SIMILARITY=$(cat "$CACHE_DIR/$CACHE_KEY")
else
    SIMILARITY=$(calculate_similarity "$note1" "$note2")
    echo "$SIMILARITY" > "$CACHE_DIR/$CACHE_KEY"
fi
```

---

## Summary

This document covers the technical implementation of five key workflows:

1. **Initial Quest Creation**: Tapestry → Zettelkasten integration
2. **Rep Completion**: Capture learnings from shipping
3. **Progressive Path Discovery**: Suggest next learning quests
4. **Cross-Quest Connections**: Link knowledge across quests
5. **Knowledge Maintenance**: Keep vault healthy

All workflows follow the principle: **Extract → Process → Connect → Build**
