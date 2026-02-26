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

## Quick Start

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

### When to Use This Skill

Activate when user:
- Says "tapestry [URL] and save to zettelkasten"
- Says "progressive learning from [URL]"
- Says "build knowledge base from this content"
- Wants to maintain learning continuity across multiple sessions

---

## Complete Workflow

### Phase 1: Extract & Plan (Tapestry + Ship-Learn-Next)

**Step 1**: Run the standard tapestry workflow:
`tapestry https://example.com/article`

**Step 2**: Verify `content.txt` and Ship-Learn-Next plan were created.

### Phase 2: Capture as Source Note (Zettelkasten)

**Step 3**: Create a Source Note (SRC) in the Zettelkasten vault:
- See `reference/zettelkasten-note-types.md` for template.
- Link to content file and action plan.

**Step 4**: Save to `/home/user/aegis/zettelkasten_agent/vault/SRC-[YYYYMMDD-HHMM]-[Title].md`.

### Phase 3: Process into Atomic Concepts (Cognitive Loop)

**Step 5**: Run the Zettelkasten cognitive loop to extract atomic concepts:
- Create 3-7 Zettel notes (ZTL).
- See `reference/zettelkasten-note-types.md` for template.

**Step 6**: Save each Zettel note to `/home/user/aegis/zettelkasten_agent/vault/ZTL-[YYYYMMDD-HHMM]-[Title].md`.

### Phase 4: Create Learning Quest MOC

**Step 7**: Create a Map of Content (MOC) for the learning quest:
- Integrate Ship-Learn-Next plan.
- Link to Source Note and Zettel notes.
- See `reference/zettelkasten-note-types.md` for template.

**Step 8**: Save to `/home/user/aegis/zettelkasten_agent/vault/MOC-[Quest-Title].md`.

### Phase 5: Connect to Existing Knowledge

**Step 9**: Search the Zettelkasten vault for related concepts.

**Step 10**: Add bidirectional links (New <-> Existing).

**Step 11**: Update the master index (`_INDEX.md`).

### Phase 6: Update After Each Rep

**Step 12**: After user ships Rep 1, extract learnings as new Zettel notes.

**Step 13**: Update the MOC with learnings and mark Rep 1 as complete.

**Step 14**: Update Source Note status to `processed`.

### Phase 7: Generate Progressive Learning Path

**Step 15**: Analyze the knowledge graph for gaps and next steps.

**Step 16**: Present "Quest Progress Update" to user with 2 progressive path options.

---

## Implementation Checklist

- [ ] Verify Zettelkasten vault structure
- [ ] Run tapestry workflow
- [ ] Generate SRC note
- [ ] Create atomic ZTL notes
- [ ] Create Quest MOC
- [ ] Connect to existing knowledge
- [ ] Present summary and Rep 1 commitment to user

---

## References & Resources

- **Examples**: See [reference/examples.md](reference/examples.md)
- **Best Practices**: See [reference/best-practices.md](reference/best-practices.md)
- **Troubleshooting**: See [reference/troubleshooting.md](reference/troubleshooting.md)
- **Note Types**: See [reference/zettelkasten-note-types.md](reference/zettelkasten-note-types.md)
- **Integration Details**: See [reference/integration-workflows.md](reference/integration-workflows.md)

---

## Persuasion & Engagement

**Authority** (Moderate): "Research shows knowledge compounds when connected, not just stored."
**Unity** (Primary): "Let's build your personal knowledge graph together."
**Commitment**: Ask "When will you ship Rep 1?" to lock in action.
