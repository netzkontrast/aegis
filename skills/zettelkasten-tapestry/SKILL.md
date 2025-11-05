# Zettelkasten-Tapestry: Progressive Learning System

**Version:** 1.0.0
**Type:** Technique Skill
**Testing Rigor:** Moderate (3-5 scenarios)

## CSO-Optimized Description

**Use when**: User wants progressive learning, knowledge building from content, connecting learning cycles, building on previous knowledge, synthesizing insights across learning quests, or says "learn progressively", "build knowledge base", "connect my learning", "zettelkasten tapestry".

**What it does**: Integrates Tapestry content extraction with Zettelkasten knowledge management to create a progressive learning system where each learning cycle builds on previous knowledge.

**How it helps**: Transforms isolated learning sessions into a growing knowledge graph, enables discovery of connections between topics, suggests progressive learning paths based on existing knowledge, and maintains learning continuity across time.

**Keywords**: zettelkasten, tapestry, progressive learning, knowledge graph, atomic notes, learning continuity, knowledge synthesis, connected learning, MOC, learning quests

---

## Quick Start (Read This First)

### What Is This?

A unified workflow that combines:
- **Tapestry**: Extract content from any URL (YouTube, articles, PDFs)
- **Ship-Learn-Next**: Create actionable 5-rep learning plans
- **Zettelkasten**: Build a progressive knowledge graph that grows with each learning cycle

### The Progressive Learning Loop

```
Extract Content (Tapestry)
    ↓
Create Action Plan (Ship-Learn-Next)
    ↓
Capture as Source Note (Zettelkasten)
    ↓
Process into Atomic Concepts (ZTL notes)
    ↓
Create Learning Quest MOC
    ↓
Connect to Existing Knowledge
    ↓
Ship Rep 1 → Learn → Update Knowledge
    ↓
Generate Next Learning Path (based on knowledge graph)
    ↓
Repeat with New Content
```

### Why This Matters

**Without this integration:**
- Each learning cycle is isolated
- Knowledge doesn't compound
- You repeat learning the same concepts
- Hard to see connections between topics

**With this integration:**
- Every learning session builds on previous knowledge
- Automatic connection discovery
- Progressive complexity based on what you know
- Learning continuity across weeks/months

### When to Use This Skill

Activate when user:
- Says "tapestry [URL] and save to zettelkasten"
- Says "progressive learning from [URL]"
- Says "build knowledge base from this content"
- Says "connect this to my previous learning"
- Wants to maintain learning continuity across multiple sessions
- Asks to "synthesize insights across learning quests"
- Mentions "zettelkasten tapestry" or "knowledge building"

---

## Complete Workflow

### Phase 1: Extract & Plan (Tapestry + Ship-Learn-Next)

**Step 1**: Run the standard tapestry workflow:

```bash
# User provides URL
tapestry https://example.com/article

# This creates:
# - content.txt (extracted content)
# - Ship-Learn-Next Plan - [Title].md (action plan)
```

**Step 2**: Verify files were created:
- Content file exists and has content
- Ship-Learn-Next plan was generated
- Files are in current working directory

### Phase 2: Capture as Source Note (Zettelkasten)

**Step 3**: Create a Source Note (SRC) in the Zettelkasten vault:

```markdown
# SRC-YYYYMMDD-HHMM-[Brief-Title]

## Metadata
- **Type**: Source Note
- **Status**: unprocessed
- **Source**: [Original URL]
- **Extracted**: [Date/Time]
- **Quest**: [[MOC-Quest-Title]]
- **Content File**: [path to content.txt]
- **Action Plan**: [path to Ship-Learn-Next plan]

## Source Context

[Brief description of what this source is about]

## Raw Content

[Full extracted content OR link to content file]

## Initial Observations

[Quick notes while extracting - optional]

## Processing Log

- [ ] Identify atomic concepts
- [ ] Create Zettel notes (ZTL)
- [ ] Link to existing knowledge
- [ ] Create/update MOC
- [ ] Update quest plan

---

## Cognitive Processing

[This section filled during processing phase]

### Factual Analysis
[Key facts, data, explicit claims]

### Inferential Analysis
[Patterns, relationships, implicit meanings]

### Generative Synthesis
[New insights, connections, applications]
```

**Step 4**: Save the Source Note to:
```
/home/user/aegis/zettelkasten_agent/vault/SRC-[YYYYMMDD-HHMM]-[Title].md
```

### Phase 3: Process into Atomic Concepts (Cognitive Loop)

**Step 5**: Run the Zettelkasten cognitive loop to extract atomic concepts:

For each core concept in the content, create a Zettel note (ZTL):

```markdown
# ZTL-YYYYMMDD-HHMM-[Declarative-Title]

## Concept

[Single, self-contained idea with declarative title]

Example titles:
- "Spaced repetition increases long-term retention"
- "Progressive overload drives skill development"
- "Small batch sizes enable faster iteration"

## Explanation

[2-4 paragraphs explaining the concept clearly]

## Source

- **From**: [[SRC-YYYYMMDD-Title]]
- **Original**: [URL or reference]
- **Quest**: [[MOC-Quest-Title]]

## Connections

- **Builds on**: [[ZTL-Previous-Related-Concept]]
- **Contradicts**: [[ZTL-Alternative-View]]
- **Applies to**: [[ZTL-Application-Domain]]
- **Example**: [[ZTL-Case-Study]]

## Practical Application

[How to actually use this concept - action-oriented]

## Questions & Extensions

- [Open question 1]
- [Extension idea 1]

## Tags

#concept #domain #technique
```

**Step 6**: Save each Zettel note to:
```
/home/user/aegis/zettelkasten_agent/vault/ZTL-[YYYYMMDD-HHMM]-[Title].md
```

**Extraction guidelines:**
- **Atomic**: One concept per note (can split if needed)
- **Declarative**: Title states a claim/principle, not just a topic
- **Self-contained**: Readable without reading the source
- **Connected**: Link to related notes in vault
- **Actionable**: Include practical application

### Phase 4: Create Learning Quest MOC

**Step 7**: Create a Map of Content (MOC) for the learning quest:

```markdown
# MOC-[Quest-Title]

## Quest Overview

- **Goal**: [From Ship-Learn-Next plan]
- **Timeline**: [4-8 weeks typically]
- **Status**: 🟢 Active / 🟡 Paused / ✅ Complete
- **Current Rep**: Rep X of 5

## Source Material

- [[SRC-YYYYMMDD-Title-1]] - [Brief description]
- [[SRC-YYYYMMDD-Title-2]] - [Brief description]

## Core Concepts (Zettel Notes)

### Foundational Concepts
- [[ZTL-Concept-1]] - [One-line summary]
- [[ZTL-Concept-2]] - [One-line summary]

### Advanced Concepts
- [[ZTL-Concept-3]] - [One-line summary]
- [[ZTL-Concept-4]] - [One-line summary]

### Practical Applications
- [[ZTL-Application-1]] - [One-line summary]
- [[ZTL-Application-2]] - [One-line summary]

## Learning Progression

### Rep 1: [Title] - ✅ Complete
- **Shipped**: [What was created]
- **Learned**: [Key learnings]
- **New Zettel**: [[ZTL-Learning-From-Rep-1]]

### Rep 2: [Title] - 🟢 In Progress
- **Goal**: [Current focus]
- **Concepts needed**: [[ZTL-X]], [[ZTL-Y]]

### Rep 3-5: [Planned]
[Brief overview]

## Connections to Other Quests

- [[MOC-Related-Quest-1]] - [How they connect]
- [[MOC-Related-Quest-2]] - [How they connect]

## Progressive Learning Path

**Based on this quest, next quests could explore:**
1. [[MOC-Suggested-Next-Quest-1]] - [Why this follows naturally]
2. [[MOC-Suggested-Next-Quest-2]] - [Alternative direction]

## Resources

- Action Plan: [path to Ship-Learn-Next plan]
- Content Files: [paths]

## Reflection

[Add reflection after each rep completion]

---

**Last Updated**: [Date]
```

**Step 8**: Save the MOC to:
```
/home/user/aegis/zettelkasten_agent/vault/MOC-[Quest-Title].md
```

### Phase 5: Connect to Existing Knowledge

**Step 9**: Search the Zettelkasten vault for related concepts:

```python
# Search for related notes by:
# 1. Similar keywords/tags
# 2. Related domains
# 3. Analogous concepts
# 4. Contradictory ideas
```

**Step 10**: Add bidirectional links:
- Update new Zettel notes with links to existing notes
- Update existing notes with links to new Zettel notes
- Update relevant MOCs with new connections

**Step 11**: Update the master index (`_INDEX.md`):
- Add new MOC to appropriate section
- Update MOC relationships
- Maintain hierarchical structure

### Phase 6: Update After Each Rep

**After Rep 1 completion:**

**Step 12**: User ships Rep 1 and reflects on learnings

**Step 13**: Extract learnings as new Zettel notes:
```markdown
# ZTL-YYYYMMDD-[Learning-From-Rep-1]

## Concept
[What was learned by doing]

## Source
- **From**: Rep 1 of [[MOC-Quest-Title]]
- **Shipped**: [What was created]
- **Date**: [Completion date]

## Explanation
[What actually happened vs expectations]
[Specific insights from shipping]

## Connections
- **Validates**: [[ZTL-Original-Concept]]
- **Contradicts**: [[ZTL-Previous-Assumption]]
- **Discovered**: [[ZTL-New-Related-Concept]]

## Practical Application
[How this learning applies to future work]
```

**Step 14**: Update the MOC:
- Mark Rep 1 as complete
- Add learned concepts
- Update Rep 2 plan based on learnings
- Adjust future reps if needed

**Step 15**: Update Source Note status:
```
Status: processing → processed
```

**Repeat Steps 12-15 for each rep completion**

### Phase 7: Generate Progressive Learning Path

**After quest completion or mid-quest:**

**Step 16**: Analyze the knowledge graph:
```python
# Look for:
# 1. Concepts mentioned but not learned
# 2. Related domains in existing notes
# 3. Natural progressions (foundational → advanced)
# 4. Gaps in knowledge
# 5. Complementary skills
```

**Step 17**: Suggest next learning quest:

Present to user:
```
✅ Quest Progress Update

Current Quest: [Quest Title]
Rep: X of 5
Knowledge Captured: Y Zettel notes

🔗 Discovered Connections:
- [New concept] connects to [[Previous-Concept]]
- [Learning] validates [[Previous-Learning]]

🎯 Progressive Learning Paths:

Option 1: [Next Quest Title]
- **Why**: Builds directly on [[ZTL-Current-Concepts]]
- **New Skills**: [What you'll learn next]
- **Complexity**: +1 level
- **Suggested Source**: [URL or topic]

Option 2: [Alternative Quest]
- **Why**: Explores related domain [[Related-MOC]]
- **New Skills**: [What you'll learn]
- **Complexity**: Same level, different direction

What would you like to explore next?
```

---

## Implementation Checklist

When user requests zettelkasten-tapestry integration:

### Initial Setup
- [ ] Verify Zettelkasten vault exists at `/home/user/aegis/zettelkasten_agent/vault/`
- [ ] Check for `_INDEX.md` and `_LOG.md`
- [ ] Verify tapestry and ship-learn-next workflows are available

### Phase 1: Extract & Plan
- [ ] Run tapestry workflow on provided URL
- [ ] Verify content file created
- [ ] Verify Ship-Learn-Next plan created
- [ ] Extract key metadata (title, URL, date)

### Phase 2: Create Source Note
- [ ] Generate SRC note with proper format
- [ ] Include all metadata
- [ ] Link to content and plan files
- [ ] Save to vault with proper naming
- [ ] Mark status as "unprocessed"

### Phase 3: Process to Zettel Notes
- [ ] Read and analyze content deeply
- [ ] Identify 3-7 atomic concepts
- [ ] Create ZTL note for each concept
- [ ] Use declarative titles
- [ ] Include practical applications
- [ ] Add initial connections (may be empty for new domains)
- [ ] Save all ZTL notes to vault

### Phase 4: Create Quest MOC
- [ ] Create MOC based on Ship-Learn-Next plan
- [ ] Link to source note
- [ ] Link to all Zettel notes
- [ ] Include rep progression structure
- [ ] Add space for future reflections
- [ ] Save to vault

### Phase 5: Connect Knowledge
- [ ] Search vault for related concepts
- [ ] Add bidirectional links
- [ ] Update existing MOCs if relevant
- [ ] Update `_INDEX.md` with new MOC

### Phase 6: Present to User
- [ ] Show summary of created notes
- [ ] Display connections found
- [ ] Highlight Rep 1 from plan
- [ ] Ask when they'll ship Rep 1

### Phase 7: After Rep Completion
- [ ] Create learning Zettel from reflection
- [ ] Update MOC with learnings
- [ ] Mark rep complete
- [ ] Suggest next steps

---

## Best Practices

### Note Creation
✅ **DO:**
- Create atomic notes (one concept per note)
- Use declarative titles that state claims
- Include practical applications
- Link bidirectionally
- Update existing notes with new connections
- Keep notes self-contained but connected

❌ **DON'T:**
- Dump entire content into one note
- Use vague topic-based titles
- Create orphan notes (no connections)
- Copy-paste without synthesis
- Skip the reflection step

### Knowledge Building
✅ **DO:**
- Process content into concepts, not just storage
- Connect new to existing knowledge
- Update understanding as you learn
- Use MOCs to zoom out and see patterns
- Review connections regularly

❌ **DON'T:**
- Just archive content without processing
- Create isolated knowledge islands
- Let MOCs become dumping grounds
- Forget to update after shipping reps

### Progressive Learning
✅ **DO:**
- Build on existing knowledge graph
- Suggest natural progressions
- Allow for exploration of related domains
- Adjust learning paths based on experience
- Celebrate connections discovered

❌ **DON'T:**
- Force linear progression
- Ignore unexpected connections
- Plan too far ahead without shipping
- Let perfect be the enemy of shipped

---

## Example Usage

### Example 1: First Learning Quest

```
User: tapestry https://youtube.com/watch?v=example and save to zettelkasten

Claude:
🧵 Running Zettelkasten-Tapestry Workflow...

Phase 1: Extract & Plan
✓ Detected: YouTube video
✓ Extracted transcript: "How to Build in Public.txt"
✓ Created action plan: "Ship-Learn-Next Plan - Build in Public.md"

Phase 2: Create Source Note
✓ Created: SRC-20250115-1430-Build-in-Public.md
✓ Status: unprocessed → processing

Phase 3: Extract Atomic Concepts
✓ Identified 5 core concepts:
  1. ZTL-20250115-1431-Public-Building-Increases-Accountability.md
  2. ZTL-20250115-1432-Sharing-Progress-Attracts-Collaborators.md
  3. ZTL-20250115-1433-Small-Updates-Beat-Big-Reveals.md
  4. ZTL-20250115-1434-Community-Feedback-Guides-Development.md
  5. ZTL-20250115-1435-Consistency-Matters-More-Than-Perfection.md

Phase 4: Create Learning Quest
✓ Created: MOC-Build-in-Public-Quest.md
✓ Linked to 5 Zettel notes
✓ Integrated Ship-Learn-Next plan

Phase 5: Connect Knowledge
🔗 Connections found: 0 (this is your first quest!)
✓ Updated _INDEX.md with new MOC

✅ Zettelkasten-Tapestry Complete!

📚 Knowledge Captured:
  - 1 Source Note
  - 5 Zettel Notes (atomic concepts)
  - 1 Learning Quest MOC

🎯 Your Quest: Build in Public for 5 Weeks
Rep 1 (This Week): Ship 3 small updates publicly

When will you ship Rep 1?
```

### Example 2: Second Quest (Building on Knowledge)

```
User: tapestry https://example.com/article-on-mvps and save to zettelkasten

Claude:
🧵 Running Zettelkasten-Tapestry Workflow...

Phase 1: Extract & Plan
✓ Detected: Article
✓ Extracted: "How to Build MVPs Fast.txt"
✓ Created plan: "Ship-Learn-Next Plan - MVP Development.md"

Phase 2: Create Source Note
✓ Created: SRC-20250122-0930-MVP-Development.md

Phase 3: Extract Atomic Concepts
✓ Identified 6 core concepts:
  1. ZTL-20250122-0931-MVPs-Test-Assumptions-Not-Features.md
  2. ZTL-20250122-0932-Smaller-Scope-Enables-Faster-Learning.md
  ... [4 more]

Phase 4: Create Learning Quest
✓ Created: MOC-MVP-Development-Quest.md

Phase 5: Connect Knowledge
🔗 Connections found: 3
  - "Small scope" → Links to [[ZTL-Small-Updates-Beat-Big-Reveals]]
  - "Fast iteration" → Connects to [[ZTL-Consistency-Matters]]
  - "Public testing" → Builds on [[MOC-Build-in-Public-Quest]]

✓ Updated existing notes with bidirectional links
✓ Updated _INDEX.md

✅ Zettelkasten-Tapestry Complete!

📚 Knowledge Captured:
  - 1 Source Note
  - 6 Zettel Notes
  - 1 Learning Quest MOC

🔗 Knowledge Connections:
  - 3 links to previous learning quest
  - Building on "Build in Public" concepts

🎯 Progressive Learning Path:
This quest naturally builds on your "Build in Public" knowledge!
Your MVP can be built in public using those principles.

🎯 Your Quest: Build 5 MVPs in 5 Weeks
Rep 1: Ship one-feature MVP by Friday

When will you ship Rep 1?
```

---

## Persuasion & Engagement

**Authority** (Moderate): "Research shows knowledge compounds when connected, not just stored."

**Unity** (Primary): "Let's build your personal knowledge graph together, one learning quest at a time."

**Commitment**:
- Use checklists for each phase
- Ask "When will you ship Rep 1?" (locks in commitment)
- Track rep completions in MOC

**Social Proof**: "Zettelkasten practitioners report better retention when learning builds on previous knowledge rather than isolated study sessions."

---

## Troubleshooting

### Issue: Vault doesn't exist
**Solution**: Check path or create vault structure:
```bash
mkdir -p /home/user/aegis/zettelkasten_agent/vault/
touch /home/user/aegis/zettelkasten_agent/vault/_INDEX.md
touch /home/user/aegis/zettelkasten_agent/vault/_LOG.md
```

### Issue: Too many Zettel notes created
**Solution**: Focus on 3-7 core concepts per source. More is not better. Atomic doesn't mean fragmentary.

### Issue: No connections found
**Solution**: This is normal for first few quests. Connections emerge over time. Continue building.

### Issue: MOC becoming cluttered
**Solution**: Review and restructure. MOCs are living documents. Split into multiple MOCs if needed.

### Issue: User skipping reflections
**Solution**: Emphasize learnings compound when captured. Offer to extract learnings from their shipped work.

---

## Success Metrics

A successful Zettelkasten-Tapestry cycle has:

✅ Source Note with complete metadata
✅ 3-7 atomic Zettel notes with declarative titles
✅ Quest MOC integrating Ship-Learn-Next plan
✅ Connections to existing knowledge (grows over time)
✅ Clear Rep 1 goal and timeline
✅ Reflection after each rep completion
✅ Progressive learning path suggestions

---

## See Also

- [Zettelkasten Note Types](/home/user/aegis/skills/zettelkasten-tapestry/reference/zettelkasten-note-types.md) - Deep dive into SRC, ZTL, MOC structures
- [Integration Workflows](/home/user/aegis/skills/zettelkasten-tapestry/reference/integration-workflows.md) - Step-by-step technical implementation
- [Tapestry Command](/home/user/aegis/.claude/commands/tapestry.md) - Content extraction workflow
- [Ship-Learn-Next Command](/home/user/aegis/.claude/commands/ship-learn-next.md) - Action planning framework
- [Zettelkasten Agent](/home/user/aegis/zettelkasten_agent/) - Core Zettelkasten implementation

---

**Remember**: You're not just saving content. You're building a knowledge graph that grows with each learning cycle. Every new quest connects to and builds on what you've learned before. This is progressive learning.

Let's weave your learning into lasting knowledge.
