# Zettelkasten Note Types & Templates

## 1. Source Note (SRC)

Use this template when processing a new content source (URL, PDF, Video).

**Filename:** `SRC-[YYYYMMDD-HHMM]-[Title].md`

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

## 2. Zettel Note (ZTL)

Use this template for atomic concepts extracted from sources.

**Filename:** `ZTL-[YYYYMMDD-HHMM]-[Declarative-Title].md`

```markdown
# ZTL-YYYYMMDD-HHMM-[Declarative-Title]

## Concept

[Single, self-contained idea with declarative title]

Example titles:
- "Spaced repetition increases long-term retention"
- "Progressive overload drives skill development"

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

## 3. Map of Content (MOC)

Use this template to organize a learning quest.

**Filename:** `MOC-[Quest-Title].md`

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
