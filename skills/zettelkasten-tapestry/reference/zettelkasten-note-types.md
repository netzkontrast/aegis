# Zettelkasten Note Types - Deep Dive

This document provides comprehensive details on the three core note types used in the Zettelkasten-Tapestry integration.

---

## Source Notes (SRC)

### Purpose
Source notes are the entry point for new content. They capture raw or minimally processed information from external sources.

### Naming Convention
```
SRC-YYYYMMDD-HHMM-[Brief-Title].md
```

**Examples:**
- `SRC-20250115-1430-Build-in-Public.md`
- `SRC-20250122-0930-MVP-Development.md`
- `SRC-20250201-1615-React-Performance-Optimization.md`

### Status Lifecycle

```
unprocessed → processing → processed
```

**unprocessed**: Just created, not yet analyzed
**processing**: Currently being analyzed and converted to Zettel notes
**processed**: All concepts extracted, Zettel notes created

### Complete Template

```markdown
# SRC-YYYYMMDD-HHMM-[Brief-Title]

## Metadata
- **Type**: Source Note
- **Status**: [unprocessed | processing | processed]
- **Source**: [Original URL or reference]
- **Extracted**: [Date/Time]
- **Quest**: [[MOC-Quest-Title]]
- **Content File**: [path to extracted content file]
- **Action Plan**: [path to Ship-Learn-Next plan]
- **Processing Date**: [When converted to Zettel notes]

## Source Context

[1-2 paragraph description]
- What is this source about?
- Who created it?
- Why is it relevant to your learning?
- What format (video, article, PDF)?

## Raw Content

### Option 1: Inline (for shorter content)
[Paste full extracted content here]

### Option 2: Reference (for longer content)
Content stored in: [path/to/content-file.txt]

**Preview** (first 500 words):
[Paste preview here]

## Initial Observations

[Quick notes captured during extraction]
- Initial reaction
- Key themes noticed
- Questions that arise
- Connections to existing knowledge

---

## Cognitive Processing

### Factual Analysis

**Key Facts:**
- [Fact 1]
- [Fact 2]
- [Fact 3]

**Data Points:**
- [Specific numbers, statistics]
- [Research citations]
- [Case study results]

**Explicit Claims:**
- [Claim 1]: [Supporting evidence]
- [Claim 2]: [Supporting evidence]

### Inferential Analysis

**Patterns Identified:**
- [Pattern 1]: [Description]
- [Pattern 2]: [Description]

**Implicit Relationships:**
- [Relationship 1]
- [Relationship 2]

**Underlying Assumptions:**
- [Assumption 1]
- [Assumption 2]

**Contextual Factors:**
- [Factor 1]: [How it affects interpretation]
- [Factor 2]: [How it affects interpretation]

### Generative Synthesis

**Novel Insights:**
1. [Insight 1] - [Why this is new/interesting]
2. [Insight 2] - [Why this is new/interesting]

**Connections to Existing Knowledge:**
- Confirms: [[ZTL-Existing-Concept]]
- Contradicts: [[ZTL-Different-View]]
- Extends: [[ZTL-Related-Concept]]

**Practical Applications:**
1. [Application 1] - [How to use this]
2. [Application 2] - [How to use this]

**Open Questions:**
- [Question 1]
- [Question 2]

---

## Extracted Zettel Notes

- [[ZTL-YYYYMMDD-HHMM-Concept-1]]
- [[ZTL-YYYYMMDD-HHMM-Concept-2]]
- [[ZTL-YYYYMMDD-HHMM-Concept-3]]
- [[ZTL-YYYYMMDD-HHMM-Concept-4]]
- [[ZTL-YYYYMMDD-HHMM-Concept-5]]

Total: X Zettel notes created

---

## Learning Quest Integration

**Quest**: [[MOC-Quest-Title]]
**Rep Phase**: Rep X of 5
**Concepts Needed For**:
- Rep 1: [[ZTL-A]], [[ZTL-B]]
- Rep 2: [[ZTL-C]], [[ZTL-D]]

---

## Processing Log

- [x] Read through entire content
- [x] Complete factual analysis
- [x] Complete inferential analysis
- [x] Complete generative synthesis
- [x] Extract atomic concepts
- [x] Create Zettel notes (X created)
- [x] Link to existing knowledge (Y connections)
- [x] Update Quest MOC
- [x] Update _INDEX.md
- [x] Status changed to: processed

**Processing Time**: [e.g., "~45 minutes"]
**Processed By**: [Claude | User | Collaborative]

---

## Review & Maintenance

**Last Reviewed**: [Date]
**Review Notes**:
- [Note from review]

**Future Processing**:
- [ ] Re-read after Rep 3 completion
- [ ] Extract additional concepts if new connections emerge
```

### Best Practices for Source Notes

**DO:**
- Create immediately after Tapestry extraction
- Include all metadata fields
- Link to both content file AND action plan
- Process within 24-48 hours of creation
- Update status as you work
- Be thorough in cognitive processing

**DON'T:**
- Let source notes accumulate unprocessed
- Skip the cognitive processing sections
- Create Zettel notes without deep analysis
- Delete the source note after processing (keep for reference)

---

## Zettel Notes (ZTL)

### Purpose
Zettel notes capture single, atomic concepts in a self-contained way. They are the building blocks of your knowledge graph.

### Naming Convention
```
ZTL-YYYYMMDD-HHMM-[Declarative-Title].md
```

**Key: Use DECLARATIVE titles (state a claim/principle)**

**Good examples:**
- `ZTL-20250115-1431-Public-Building-Increases-Accountability.md`
- `ZTL-20250122-0932-Smaller-Scope-Enables-Faster-Learning.md`
- `ZTL-20250201-1120-React-Memoization-Prevents-Unnecessary-Rerenders.md`

**Bad examples:**
- `ZTL-20250115-1431-Public-Building.md` (not declarative)
- `ZTL-20250122-0932-Scope.md` (too vague)
- `ZTL-20250201-1120-React-Optimization-Techniques.md` (too broad, multiple concepts)

### Atomicity Principle

**One concept = One note**

If you find yourself writing "and" or "also" frequently, you probably have multiple concepts. Split them.

**Example - Too Broad:**
```
# ZTL - Progressive Learning and Knowledge Building

This note covers progressive learning, knowledge building,
spaced repetition, and active recall...
```

**Better - Atomic:**
```
# ZTL - Progressive Learning Builds On Prior Knowledge

[One focused concept]

Related: [[ZTL - Spaced Repetition Increases Retention]]
Related: [[ZTL - Active Recall Strengthens Memory]]
```

### Complete Template

```markdown
# ZTL-YYYYMMDD-HHMM-[Declarative-Title]

## Concept

[1-2 sentence statement of the core idea]

This is the "headline" - what someone would remember.

## Explanation

[2-4 paragraphs explaining the concept in depth]

**What it is:**
[Clear definition]

**Why it matters:**
[Significance and implications]

**How it works:**
[Mechanism or process]

**When to use it:**
[Context and conditions]

## Source

- **From**: [[SRC-YYYYMMDD-Title]]
- **Original**: [URL or reference]
- **Quest**: [[MOC-Quest-Title]]
- **Created**: [Date/Time]
- **Type**: [Concept | Principle | Technique | Pattern | Case Study]

## Connections

### Builds On
- [[ZTL-Foundational-Concept-1]] - [Why this is foundational]
- [[ZTL-Foundational-Concept-2]] - [Why this is foundational]

### Extends
- [[ZTL-Related-Concept-1]] - [How they relate]

### Contradicts
- [[ZTL-Alternative-View-1]] - [Nature of contradiction]

### Applies To
- [[ZTL-Application-Domain-1]] - [How it applies]
- [[ZTL-Application-Domain-2]] - [How it applies]

### Examples
- [[ZTL-Case-Study-1]] - [Specific example]
- [[ZTL-Real-World-Example]] - [Real application]

### Part Of
- [[MOC-Domain-Map]] - [Which domain this belongs to]

## Practical Application

### How to Use This

[Step-by-step guide or principles for applying this concept]

1. [Action step 1]
2. [Action step 2]
3. [Action step 3]

### Example Implementation

[Concrete example of using this concept]

**Context**: [Situation]
**Application**: [How concept was used]
**Result**: [Outcome]

### Common Pitfalls

- ⚠️ [Pitfall 1]: [How to avoid]
- ⚠️ [Pitfall 2]: [How to avoid]

## Evidence & Support

**Research:**
- [Research finding 1]
- [Research finding 2]

**Case Studies:**
- [Example 1]
- [Example 2]

**Personal Experience:**
- [Your experience with this concept]

## Questions & Extensions

**Open Questions:**
- [Question 1]
- [Question 2]

**Future Explorations:**
- [Area to explore further]
- [Related concept to investigate]

**Hypothesis:**
- [Testable hypothesis related to this concept]

## Tags

#concept #domain #subdomain #technique #principle

## Revision History

- **v1.0** (YYYY-MM-DD): Initial creation from [[SRC-Title]]
- **v1.1** (YYYY-MM-DD): Added connection to [[ZTL-New-Related-Concept]]
- **v1.2** (YYYY-MM-DD): Updated practical application based on Rep 2 learning
```

### Connection Types Explained

**Builds On**: Prerequisites - concepts you need to understand first
**Extends**: Takes a concept further or adds nuance
**Contradicts**: Alternative or opposing viewpoints
**Applies To**: Domains where this concept is relevant
**Examples**: Specific instances or case studies
**Part Of**: Higher-level maps or categories

### Best Practices for Zettel Notes

**DO:**
- Use declarative titles (state a claim)
- Keep notes atomic (one concept)
- Make notes self-contained
- Include practical applications
- Link bidirectionally
- Update as understanding evolves

**DON'T:**
- Use vague topic titles
- Combine multiple concepts
- Copy-paste without synthesis
- Create orphan notes (no connections)
- Leave notes static (they should evolve)

---

## Maps of Content (MOC)

### Purpose
MOCs provide structure and navigation for collections of related Zettel notes. They are "zoom out" views that help you see patterns and relationships.

### Types of MOCs

**Quest MOCs**: Organized around a learning quest
**Domain MOCs**: Organized around a knowledge domain
**Project MOCs**: Organized around a specific project
**Theme MOCs**: Organized around a conceptual theme

### Naming Convention

```
MOC-[Title].md
```

**Examples:**
- `MOC-Build-in-Public-Quest.md` (Quest MOC)
- `MOC-React-Performance.md` (Domain MOC)
- `MOC-MVP-Builder-Project.md` (Project MOC)
- `MOC-Progressive-Learning.md` (Theme MOC)

### Quest MOC Template (Primary for Zettelkasten-Tapestry)

```markdown
# MOC-[Quest-Title]

## Quest Overview

- **Goal**: [From Ship-Learn-Next plan - specific and measurable]
- **Timeline**: [Start date] → [Target end date] (typically 4-8 weeks)
- **Status**: [🟢 Active | 🟡 Paused | ✅ Complete | 🔴 Cancelled]
- **Current Rep**: Rep X of 5
- **Completion**: [X%] complete

## Why This Quest

[1-2 paragraphs]
- What motivated this learning quest?
- How does it connect to larger goals?
- What problem does it solve?

## Source Material

### Primary Sources
- [[SRC-YYYYMMDD-Title-1]] - [Brief description] - [Status]
- [[SRC-YYYYMMDD-Title-2]] - [Brief description] - [Status]

### Additional References
- [External URL 1] - [Description]
- [Book/Paper reference]

## Core Concepts (Zettel Notes)

### Foundational Concepts (Must Know)
- [[ZTL-Concept-1]] - [One-line summary]
- [[ZTL-Concept-2]] - [One-line summary]
- [[ZTL-Concept-3]] - [One-line summary]

### Supporting Concepts (Should Know)
- [[ZTL-Concept-4]] - [One-line summary]
- [[ZTL-Concept-5]] - [One-line summary]

### Advanced Concepts (Nice to Know)
- [[ZTL-Concept-6]] - [One-line summary]
- [[ZTL-Concept-7]] - [One-line summary]

### Practical Applications
- [[ZTL-Application-1]] - [One-line summary]
- [[ZTL-Application-2]] - [One-line summary]

## Learning Progression (Ship-Learn-Next Integration)

### Rep 1: [Specific Goal] - [Status Icon]

**Ship Goal**: [What will be created/shipped]

**Timeline**: [Start date] → [End date]

**Success Criteria**:
- [x] [Criterion 1]
- [x] [Criterion 2]
- [x] [Criterion 3]

**Concepts Applied**:
- [[ZTL-Concept-A]] - [How used]
- [[ZTL-Concept-B]] - [How used]

**What Was Shipped**: [Description + link/path]

**Key Learnings**:
1. [Learning 1] → [[ZTL-Learning-From-Rep-1]]
2. [Learning 2] → [[ZTL-Learning-2-From-Rep-1]]

**Reflection** (from Ship-Learn-Next):
- **What happened**: [Actual vs expected]
- **What worked**: [Successes]
- **What didn't**: [Failures/challenges]
- **Surprises**: [Unexpected outcomes]
- **Rating**: [X/10]

### Rep 2: [Specific Goal] - [Status Icon]

**Ship Goal**: [What will be created/shipped]

**Builds On**: Learnings from Rep 1

**New Challenge**: [One new element added]

**Timeline**: [Start date] → [End date]

**Success Criteria**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

**Concepts Applied**:
- [[ZTL-Concept-C]] - [How used]
- [[ZTL-Concept-D]] - [How used]

[Fill in after completion]

### Rep 3: [Specific Goal] - [Status Icon]

[Similar structure, more advanced]

### Rep 4: [Specific Goal] - [Status Icon]

[Similar structure, more advanced]

### Rep 5: [Specific Goal] - [Status Icon]

[Similar structure, most advanced]

## Overall Quest Progress

**Timeline**:
```
Rep 1: ✅ (Week 1)
Rep 2: ✅ (Week 2)
Rep 3: 🟢 (Week 3)
Rep 4: ⏳ (Week 4)
Rep 5: ⏳ (Week 5)
```

**Velocity**: [How quickly progressing vs plan]

**Adjustments Made**:
- [Change 1]: [Reason]
- [Change 2]: [Reason]

## Knowledge Graph

### Connections to Other Quests

- [[MOC-Related-Quest-1]] - [How they connect]
  - Shared concepts: [[ZTL-X]], [[ZTL-Y]]
  - Builds on: [What from that quest]

- [[MOC-Related-Quest-2]] - [How they connect]

### Emergent Themes

[Themes/patterns noticed across reps]
1. [Theme 1]
2. [Theme 2]

## Progressive Learning Path

**What This Quest Unlocks:**

### Immediate Next Steps (After Rep 5)
1. [[MOC-Suggested-Next-Quest-1]]
   - **Why**: [Natural progression]
   - **Builds on**: [[ZTL-X]], [[ZTL-Y]]
   - **New skills**: [What you'll learn]
   - **Complexity**: +1 level

2. [[MOC-Suggested-Next-Quest-2]]
   - **Why**: [Alternative direction]
   - **Builds on**: [[ZTL-A]], [[ZTL-B]]
   - **New skills**: [What you'll learn]
   - **Complexity**: Same level, different domain

### Long-Term Trajectory (3-6 months)
- [Longer-term goal that this quest contributes to]
- [Skills tree visualization]

## Resources

**Action Plan**: [path to Ship-Learn-Next plan file]

**Content Files**:
- [path to content file 1]
- [path to content file 2]

**Shipped Artifacts**:
- Rep 1: [link/path]
- Rep 2: [link/path]
- [etc.]

**External References**:
- [URL 1]
- [URL 2]

## Metrics & Analytics

**Total Time Invested**: [X hours across Y weeks]
**Zettel Notes Created**: [X notes]
**Connections Made**: [Y connections to existing knowledge]
**Artifacts Shipped**: [Z concrete outputs]
**Knowledge Density**: [New concepts learned / time invested]

## Quest Reflection (After Completion)

**Overall Rating**: [X/10]

**What Worked Well**:
- [Success 1]
- [Success 2]

**What Could Be Improved**:
- [Improvement 1]
- [Improvement 2]

**Most Valuable Learning**:
[1-2 paragraphs on the most important takeaway]

**Unexpected Outcomes**:
[Surprises, serendipitous discoveries]

**Would I Recommend This Quest?**
[Yes/No + why]

**Advice for Future Self**:
[What to remember if revisiting this domain]

---

**Created**: [Date]
**Last Updated**: [Date]
**Status**: [Active/Complete]
```

### Best Practices for MOCs

**DO:**
- Update after each rep completion
- Capture learnings as new Zettel notes
- Adjust future reps based on experience
- Link related quests
- Suggest progressive paths
- Review and reflect regularly

**DON'T:**
- Let MOCs become cluttered dumping grounds
- Create rigid structures that don't evolve
- Plan all 5 reps in perfect detail upfront
- Skip the reflection steps
- Forget to update status

---

## Index Structure (_INDEX.md)

The master index provides top-level navigation for all MOCs.

### Template

```markdown
# Knowledge Base Index

## Active Learning Quests

- [[MOC-Quest-1]] - Rep X/5 - [One-line description]
- [[MOC-Quest-2]] - Rep Y/5 - [One-line description]

## Completed Quests

- [[MOC-Completed-Quest-1]] - ✅ [Date] - [One-line description]
- [[MOC-Completed-Quest-2]] - ✅ [Date] - [One-line description]

## Domain Maps

### Software Development
- [[MOC-React-Performance]] - [X notes]
- [[MOC-System-Design]] - [Y notes]

### Learning & Meta-Skills
- [[MOC-Progressive-Learning]] - [X notes]
- [[MOC-Knowledge-Building]] - [Y notes]

### Business & Product
- [[MOC-MVPs]] - [X notes]
- [[MOC-Build-in-Public]] - [Y notes]

## Theme Maps

- [[MOC-Shipping-Mindset]] - [Description]
- [[MOC-Iteration-Strategies]] - [Description]

## Statistics

- **Total Zettel Notes**: [X]
- **Total Source Notes**: [Y]
- **Total MOCs**: [Z]
- **Active Quests**: [A]
- **Completed Quests**: [B]
- **Knowledge Connections**: [Estimate based on links]

**Last Updated**: [Date]
```

---

## Note Relationships & Linking

### Bidirectional Linking

When you create a link from Note A to Note B, ALWAYS update Note B to link back to Note A.

**Example:**

**ZTL-Note-A.md**:
```markdown
## Connections
- **Builds on**: [[ZTL-Note-B]]
```

**ZTL-Note-B.md** (update this):
```markdown
## Connections
- **Extended by**: [[ZTL-Note-A]]
```

### Link Types & Semantics

Use specific relationship labels:

- **Builds on / Foundational to**
- **Extends / Extended by**
- **Contradicts / Alternative to**
- **Applies to / Application of**
- **Example of / Exemplified by**
- **Part of / Contains**
- **Similar to / Related to**
- **Precedes / Follows** (temporal)

### Network Effects

As your vault grows:
- More connections emerge naturally
- Patterns become visible
- Unexpected relationships surface
- Knowledge compounds exponentially

**Target**: Each new Zettel should connect to 2-5 existing notes.

---

## Maintenance & Evolution

### Regular Reviews

**Weekly** (during active quest):
- Update rep status in MOC
- Add learnings as Zettel notes
- Check for new connections

**Monthly**:
- Review MOC structure
- Consolidate related notes if needed
- Update _INDEX.md
- Identify knowledge gaps

**Quarterly**:
- Deep review of all notes
- Refactor MOCs if needed
- Archive completed quests
- Plan next learning trajectory

### When to Update Notes

**Update existing Zettel when:**
- New evidence confirms/contradicts
- Personal experience validates/refutes
- New connections discovered
- Understanding deepens

**Don't update when:**
- It's truly a different concept (create new note instead)
- Just adding more examples (link to example note instead)
- Making it less atomic (split instead)

### Version Control

Track significant updates in the revision history section of each note.

---

## Summary

**Three Note Types:**
1. **SRC** - Entry point, raw content, cognitive processing
2. **ZTL** - Atomic concepts, self-contained, highly connected
3. **MOC** - Navigation, structure, quest tracking

**Key Principles:**
- **Atomic**: One concept per Zettel
- **Declarative**: State claims, not topics
- **Connected**: Bidirectional links
- **Self-contained**: Readable without source
- **Evolving**: Update as understanding grows

**The Goal:**
Build a knowledge graph that compounds over time, where each new learning cycle connects to and builds on previous knowledge.
