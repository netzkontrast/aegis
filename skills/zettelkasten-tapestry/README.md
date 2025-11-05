# Zettelkasten-Tapestry Integration

**Version**: 1.0.0
**Status**: Production Ready
**Type**: Technique Skill

## Overview

The Zettelkasten-Tapestry skill enables **progressive learning** by integrating three powerful systems:

1. **Tapestry** - Content extraction from any URL (YouTube, articles, PDFs)
2. **Ship-Learn-Next** - Action planning with 5-rep progressive iterations
3. **Zettelkasten** - Knowledge graph building with atomic notes

## What Problem Does This Solve?

**Without integration:**
- Each learning cycle is isolated
- Knowledge doesn't compound over time
- You repeat learning the same concepts
- Hard to see connections between topics
- Learning feels fragmented

**With Zettelkasten-Tapestry:**
- Every learning session builds on previous knowledge
- Automatic connection discovery across topics
- Progressive complexity based on what you already know
- Learning continuity across weeks and months
- Knowledge compounds exponentially

## How It Works

### The Progressive Learning Loop

```
1. Extract content from URL (Tapestry)
   ↓
2. Create 5-rep action plan (Ship-Learn-Next)
   ↓
3. Capture as Source Note (Zettelkasten)
   ↓
4. Process into atomic concepts (3-7 Zettel notes)
   ↓
5. Create Learning Quest MOC
   ↓
6. Connect to existing knowledge graph
   ↓
7. Ship Rep 1 → Learn → Update knowledge
   ↓
8. Generate next learning path (based on knowledge graph)
   ↓
9. Repeat with new content (building on previous)
```

### Key Components

#### Source Notes (SRC)
- Entry point for new content
- Captures raw/minimally processed information
- Status: `unprocessed → processing → processed`
- Links to content files and action plans

#### Zettel Notes (ZTL)
- Atomic concepts (one idea per note)
- Declarative titles (state claims, not topics)
- Self-contained but highly connected
- Include practical applications

#### Maps of Content (MOC)
- Navigation for collections of notes
- Organized around learning quests
- Integrate Ship-Learn-Next rep structure
- Track progress and connections

## Usage

### Via Slash Command

```bash
# In Claude Code
/zettelkasten-tapestry https://youtube.com/watch?v=example
```

### Via Natural Language

Say any of these to Claude:
- "tapestry [URL] and save to zettelkasten"
- "progressive learning from [URL]"
- "build knowledge base from [URL]"
- "zettelkasten tapestry [URL]"
- "learn and connect to existing knowledge [URL]"

### Manual Invocation

Reference the skill directly:
```
I want to use the zettelkasten-tapestry skill to process this URL: [URL]
```

## File Structure

```
skills/zettelkasten-tapestry/
├── SKILL.md                           # Main skill (682 lines)
├── README.md                          # This file
└── reference/
    ├── zettelkasten-note-types.md     # Deep dive on SRC, ZTL, MOC
    └── integration-workflows.md       # Technical implementation

.claude/commands/
└── zettelkasten-tapestry.md           # Slash command

zettelkasten_agent/vault/              # Knowledge base
├── _INDEX.md                          # Master index
├── _LOG.md                            # Action log
├── SRC-*.md                           # Source notes
├── ZTL-*.md                           # Atomic concept notes
└── MOC-*.md                           # Maps of content
```

## Example Workflow

### First Learning Quest

```
User: /zettelkasten-tapestry https://youtube.com/watch?v=build-in-public

Claude:
🧵 Running Zettelkasten-Tapestry Workflow...

Phase 1: Extract & Plan
✓ Detected: YouTube video
✓ Extracted: "How to Build in Public.txt"
✓ Created: "Ship-Learn-Next Plan - Build in Public.md"

Phase 2: Create Source Note
✓ Created: SRC-20250115-1430-Build-in-Public.md
✓ Status: unprocessed → processing

Phase 3: Extract Atomic Concepts
✓ Identified 5 core concepts:
  1. ZTL-Public-Building-Increases-Accountability
  2. ZTL-Sharing-Progress-Attracts-Collaborators
  3. ZTL-Small-Updates-Beat-Big-Reveals
  4. ZTL-Community-Feedback-Guides-Development
  5. ZTL-Consistency-Matters-More-Than-Perfection

Phase 4: Create Learning Quest
✓ Created: MOC-Build-in-Public-Quest.md
✓ Linked 5 Zettel notes + Ship-Learn-Next plan

Phase 5: Connect Knowledge
🔗 Connections found: 0 (first quest - connections will grow!)
✓ Updated _INDEX.md

✅ Zettelkasten-Tapestry Complete!

📚 Knowledge Captured:
  - 1 Source Note
  - 5 Zettel Notes (atomic concepts)
  - 1 Learning Quest MOC

🎯 Your Quest: Build in Public for 5 Weeks
Rep 1 (This Week): Ship 3 small updates publicly

When will you ship Rep 1?
```

### Second Quest (Building on Knowledge)

```
User: /zettelkasten-tapestry https://article.com/mvp-development

Claude:
🧵 Running Zettelkasten-Tapestry Workflow...

Phase 1-4: [Similar to above]

Phase 5: Connect Knowledge
🔗 Connections found: 3
  - "Small scope" → Links to [[ZTL-Small-Updates-Beat-Big-Reveals]]
  - "Fast iteration" → Connects to [[ZTL-Consistency-Matters]]
  - "Public testing" → Builds on [[MOC-Build-in-Public-Quest]]

✓ Updated existing notes with bidirectional links

✅ Zettelkasten-Tapestry Complete!

🔗 Knowledge Connections:
  - 3 links to previous learning quest
  - Building on "Build in Public" concepts

🎯 Progressive Learning Path:
This quest naturally builds on your "Build in Public" knowledge!
Your MVP can be built in public using those principles.

🎯 Your Quest: Build 5 MVPs in 5 Weeks
Rep 1: Ship one-feature MVP by Friday
```

## CSO Optimization

**For Claude to discover this skill, it needs:**

### Primary Keywords
- zettelkasten
- tapestry
- progressive learning
- knowledge graph
- knowledge building

### Secondary Keywords
- atomic notes
- learning continuity
- connected learning
- MOC (maps of content)
- learning quests
- knowledge synthesis

### Trigger Phrases
- "learn progressively from [URL]"
- "build knowledge base"
- "connect my learning"
- "zettelkasten tapestry"
- "save to knowledge graph"

## Integration Points

### With Tapestry
- Uses tapestry workflow for content extraction
- Supports YouTube, articles, PDFs
- Preserves content files for reference

### With Ship-Learn-Next
- Integrates 5-rep action plan into MOC
- Links concepts to specific reps
- Captures learnings after each rep as new Zettel notes

### With Zettelkasten Agent
- Uses vault structure (`/home/user/aegis/zettelkasten_agent/vault/`)
- Follows note taxonomy (SRC, ZTL, MOC)
- Implements cognitive processing loop

## Best Practices

### Note Creation
✅ Create atomic notes (one concept per note)
✅ Use declarative titles (state claims)
✅ Include practical applications
✅ Link bidirectionally
✅ Keep notes self-contained but connected

❌ Don't dump entire content into one note
❌ Don't use vague topic-based titles
❌ Don't create orphan notes (no connections)
❌ Don't skip the reflection step

### Knowledge Building
✅ Process content into concepts, not just storage
✅ Connect new to existing knowledge
✅ Update understanding as you learn
✅ Use MOCs to zoom out and see patterns
✅ Review connections regularly

❌ Don't just archive content without processing
❌ Don't create isolated knowledge islands
❌ Don't let MOCs become dumping grounds
❌ Don't forget to update after shipping reps

### Progressive Learning
✅ Build on existing knowledge graph
✅ Suggest natural progressions
✅ Allow for exploration of related domains
✅ Adjust learning paths based on experience
✅ Celebrate connections discovered

❌ Don't force linear progression
❌ Don't ignore unexpected connections
❌ Don't plan too far ahead without shipping
❌ Don't let perfect be the enemy of shipped

## Success Metrics

A successful Zettelkasten-Tapestry cycle produces:

- ✅ 1 Source Note with complete metadata
- ✅ 3-7 Zettel notes with declarative titles
- ✅ 1 Quest MOC integrating Ship-Learn-Next plan
- ✅ Connections to existing knowledge (grows over time)
- ✅ Clear Rep 1 goal and timeline
- ✅ Reflection captured after each rep completion
- ✅ Progressive learning path suggestions

## Testing Scenarios

### Scenario 1: First Learning Quest (No Existing Knowledge)
**Input**: URL to educational content
**Expected**:
- Content extracted successfully
- 3-7 atomic concepts identified
- Source note, Zettel notes, and MOC created
- Zero connections (normal for first quest)
- Clear Rep 1 goal presented

### Scenario 2: Second Quest (Building on Knowledge)
**Input**: URL to related content
**Expected**:
- Content extracted successfully
- 3-7 atomic concepts identified
- All notes created
- 1+ connections discovered to first quest
- Progressive path suggested

### Scenario 3: Rep Completion (Learning Capture)
**Input**: User ships Rep 1 and provides reflection
**Expected**:
- Learnings extracted as new Zettel notes
- MOC updated with completion status
- Connections made to original concepts
- Rep 2 plan adjusted based on learnings

### Scenario 4: Cross-Domain Learning
**Input**: URL from unrelated domain
**Expected**:
- Content processed normally
- Unexpected connections may be discovered
- New domain section added to _INDEX.md
- Progressive paths show both domain options

### Scenario 5: Quest Completion
**Input**: User completes all 5 reps
**Expected**:
- MOC marked complete
- 3 next quest suggestions generated
- Knowledge graph statistics shown
- Celebration of progress

## Troubleshooting

### Issue: Vault doesn't exist
**Solution**: Skill will auto-create vault structure at `/home/user/aegis/zettelkasten_agent/vault/`

### Issue: Tapestry extraction failed
**Solution**: Check URL accessibility, provide content file manually if needed

### Issue: Too many Zettel notes created
**Solution**: Focus on 3-7 core concepts. More is not better. Atomic ≠ fragmentary

### Issue: No connections found
**Solution**: Normal for first few quests. Connections emerge over time. Continue building.

### Issue: MOC becoming cluttered
**Solution**: Review and restructure. MOCs are living documents. Split if needed.

## Maintenance

### Weekly
- Update rep status in MOCs
- Add learnings as Zettel notes
- Check for new connections

### Monthly
- Review MOC structure
- Consolidate related notes if needed
- Update _INDEX.md
- Identify knowledge gaps

### Quarterly
- Deep review of all notes
- Refactor MOCs if needed
- Archive completed quests
- Plan next learning trajectory

## Version History

### v1.0.0 (2025-01-15)
- Initial release
- Complete integration of Tapestry, Ship-Learn-Next, and Zettelkasten
- Full documentation with examples
- CSO optimization
- Slash command support

## Contributing

To enhance this skill:

1. **Add examples**: Real-world usage examples are valuable
2. **Improve workflows**: Suggest optimizations to the process
3. **Add tools**: Integration with additional knowledge tools
4. **Share patterns**: Novel connection patterns discovered

## Philosophy

> "You're not just saving content. You're building a knowledge graph that grows with each learning cycle. Every new quest connects to and builds on what you've learned before. This is progressive learning."

The goal is **knowledge that compounds**, not content that accumulates.

## License

Part of the Aegis project.

## See Also

- [Skill Authoring Guide](/home/user/aegis/skills/skill-authoring/SKILL.md)
- [Tapestry Command](/home/user/aegis/.claude/commands/tapestry.md)
- [Ship-Learn-Next Command](/home/user/aegis/.claude/commands/ship-learn-next.md)
- [Zettelkasten Agent](/home/user/aegis/zettelkasten_agent/)

---

**Let's weave your learning into lasting knowledge.** 🧵🧠
