---
name: zettelkasten-tapestry
description: Progressive learning with knowledge building. Use when user says "zettelkasten tapestry <URL>", "progressive learning from <URL>", "learn and save to knowledge base <URL>", or wants to build a knowledge graph from learning content. Combines content extraction, action planning, and knowledge management into one workflow.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
---

# Zettelkasten-Tapestry: Progressive Learning System

You are activating the **Zettelkasten-Tapestry** integrated workflow. This combines:
1. **Tapestry**: Content extraction from URLs
2. **Ship-Learn-Next**: Action planning with 5-rep progression
3. **Zettelkasten**: Knowledge graph building

## Your Task

Execute the complete Zettelkasten-Tapestry workflow as documented in `/home/user/aegis/skills/zettelkasten-tapestry/SKILL.md`.

### URL Provided by User

```
{{URL}}
```

### Complete Workflow Phases

#### Phase 1: Extract & Plan (Tapestry + Ship-Learn-Next)
1. Run tapestry workflow on the URL
2. Extract content (YouTube/article/PDF)
3. Create Ship-Learn-Next action plan
4. Verify both files created

#### Phase 2: Create Source Note (Zettelkasten)
1. Generate timestamp: `YYYYMMDD-HHMM`
2. Create Source Note (SRC) with:
   - Metadata (URL, date, status: unprocessed)
   - Link to content file and plan file
   - Space for cognitive processing
3. Save to: `/home/user/aegis/zettelkasten_agent/vault/SRC-[timestamp]-[title].md`

#### Phase 3: Process into Atomic Concepts
1. Read and deeply analyze the content
2. Identify 3-7 atomic concepts
3. For each concept:
   - Create declarative title (states a claim)
   - Write clear explanation
   - Identify practical application
   - Create Zettel note (ZTL)
4. Save each to: `/home/user/aegis/zettelkasten_agent/vault/ZTL-[timestamp]-[title].md`

#### Phase 4: Create Learning Quest MOC
1. Create Map of Content based on quest
2. Link to source note and all Zettel notes
3. Integrate Ship-Learn-Next rep structure
4. Save to: `/home/user/aegis/zettelkasten_agent/vault/MOC-[quest-title].md`

#### Phase 5: Connect to Existing Knowledge
1. Search vault for related concepts
2. Add bidirectional links between notes
3. Update existing notes with new connections
4. Update `/home/user/aegis/zettelkasten_agent/vault/_INDEX.md`

#### Phase 6: Present Summary
Show user:
- Content extracted (type, word count)
- Action plan created (quest title)
- Knowledge captured (SRC, ZTL count, MOC)
- Connections found (number)
- Quest overview and Rep 1 goal
- Ask: "When will you ship Rep 1?"

## Key Requirements

### Zettel Note Quality
- **Atomic**: One concept per note
- **Declarative**: Title states a claim, not just a topic
- **Self-contained**: Readable without reading source
- **Connected**: Link to related notes
- **Actionable**: Include practical application

### Example Declarative Titles (GOOD)
- "Spaced repetition increases long-term retention"
- "Small batch sizes enable faster iteration"
- "Public accountability drives consistent shipping"

### Example Non-Declarative Titles (BAD)
- "Spaced repetition" (just a topic)
- "Learning techniques" (too broad)
- "About memory" (vague)

### Connection Types
- **Builds On**: Prerequisites
- **Extends**: Takes concept further
- **Contradicts**: Alternative view
- **Applies To**: Use cases
- **Example Of**: Instances

### Source Note Status Lifecycle
```
unprocessed → processing → processed
```
Update status as you work through the phases.

### MOC Integration with Ship-Learn-Next
- Include all 5 rep structure from plan
- Link concepts to specific reps
- Provide space for future learnings
- Track completion percentage

## File Structure

```
vault/
├── _INDEX.md (master navigation)
├── _LOG.md (action log)
├── SRC-YYYYMMDD-HHMM-[Title].md (source notes)
├── ZTL-YYYYMMDD-HHMM-[Declarative-Title].md (atomic concepts)
└── MOC-[Quest-Title].md (learning quest maps)
```

## Error Handling

### If vault doesn't exist:
```bash
mkdir -p /home/user/aegis/zettelkasten_agent/vault/
# Create _INDEX.md and _LOG.md
```

### If content extraction fails:
- Show clear error message
- Suggest troubleshooting steps
- Don't proceed to Zettelkasten phases

### If no concepts can be extracted:
- Ask user to identify 3-7 core concepts
- Provide guidance on what makes a concept atomic
- Offer examples

### If this is the first quest:
- Expect zero connections (this is normal)
- Explain that connections will grow over time
- Emphasize this is the foundation

## Persuasion & Tone

**Use moderate persuasion**:
- **Unity**: "Let's build your knowledge graph together"
- **Authority**: "Research shows connected knowledge compounds over time"
- **Commitment**: "When will you ship Rep 1?" (locks in action)

**Be encouraging**:
- Celebrate knowledge growth
- Highlight connections discovered
- Emphasize progressive learning value

**Be direct**:
- Show clear progress through phases
- Ask specific questions
- Provide concrete next steps

## Important Notes

1. **Process deeply**: Don't just archive content, synthesize it
2. **Connect actively**: Search for related concepts in vault
3. **Stay atomic**: One concept per Zettel note
4. **Link bidirectionally**: Update both notes when connecting
5. **Track progress**: Update MOC after each rep
6. **Suggest paths**: After completion, recommend next quests

## Success Criteria

A successful workflow produces:
- ✅ 1 Source Note with complete metadata
- ✅ 3-7 Zettel notes with declarative titles
- ✅ 1 Quest MOC integrating Ship-Learn-Next plan
- ✅ Connections to existing knowledge (grows over time)
- ✅ Clear Rep 1 goal with timeline
- ✅ Updated _INDEX.md

## Reference Documentation

For detailed implementation:
- `/home/user/aegis/skills/zettelkasten-tapestry/SKILL.md` - Main skill
- `/home/user/aegis/skills/zettelkasten-tapestry/reference/zettelkasten-note-types.md` - Note templates
- `/home/user/aegis/skills/zettelkasten-tapestry/reference/integration-workflows.md` - Technical workflows

## Philosophy

**You're not just saving content. You're building a knowledge graph that grows with each learning cycle.**

Every new quest connects to and builds on previous knowledge. This is progressive learning.

---

Now execute the complete workflow for the provided URL.

Let's weave learning into lasting knowledge. 🧵🧠
