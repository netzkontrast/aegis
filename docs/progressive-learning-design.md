# Progressive Learning with Zettelkasten: Design Document

## Overview

**Core Insight:** Learning is progressive - we start with surveys, focus on specifics, synthesize understanding, then connect to broader knowledge. Zettelkasten's structure naturally supports this progression.

**Tapestry Metaphor:** Knowledge is woven, not piled. Each thread (Zettel) connects to others, creating patterns (MOCs) that form a coherent whole (INDEX). Learning is following and creating threads.

## Learning Phases (The Progressive Journey)

### Phase 1: SURVEY (Wide, Shallow)
**Goal:** Get the lay of the land
**Method:** Navigate INDEX → Scan MOCs → Identify gaps
**Output:** Mental map of domain + questions

**Zettelkasten Pattern:**
- Read `_INDEX.md` (what exists?)
- Scan relevant MOC summaries (what are the main themes?)
- Note what's missing (knowledge gaps)

**Questions to ask:**
- What do I already know here?
- What's completely new?
- Where should I focus first?

### Phase 2: FOCUS (Narrow, Deep)
**Goal:** Master a specific sub-topic
**Method:** Deep-dive into specific Zettel + Create new notes
**Output:** Understanding of atomic concepts + connections

**Zettelkasten Pattern:**
- Pick one MOC from survey
- Read related Zettel in depth
- Create SRC notes from external sources
- Let agent synthesize into new ZTL notes
- Verify understanding by explaining in own words

**Questions to ask:**
- Can I explain this concept without looking?
- What examples illustrate this?
- What are the edge cases?

### Phase 3: SYNTHESIZE (Connect, Integrate)
**Goal:** Build mental models and frameworks
**Method:** Create connections between notes, identify patterns
**Output:** Personal synthesis notes + MOC refinements

**Zettelkasten Pattern:**
- Create "bridge notes" (ZTL) linking concepts from different MOCs
- Identify emergent patterns
- Create or update MOCs to reflect understanding
- Write synthesis notes in own voice

**Questions to ask:**
- How does X relate to Y?
- What pattern connects these ideas?
- What's my unique insight here?

### Phase 4: EXTEND (Apply, Teach)
**Goal:** Apply knowledge and deepen through teaching
**Method:** Use knowledge in practice, explain to others
**Output:** Application notes + teaching MOCs

**Zettelkasten Pattern:**
- Create application examples (code, designs, analyses)
- Write "teaching MOCs" (how would I explain this?)
- Link theory notes to practice notes
- Document failures and learnings

**Questions to ask:**
- Where can I apply this?
- How would I teach this to someone?
- What would I do differently next time?

## The Tapestry: How Knowledge Weaves

### Vertical Threads (Depth)
```
INDEX (Catalog)
  ↓
MOC (Theme: "Machine Learning")
  ↓
ZTL (Concept: "Gradient Descent")
  ↓
ZTL (Detail: "Learning Rate Selection")
```

**Learning path:** Start general, drill down to specifics

### Horizontal Threads (Breadth)
```
ZTL (Math: "Optimization")
  ↔
ZTL (ML: "Gradient Descent")
  ↔
ZTL (Econ: "Marginal Utility")
```

**Learning path:** See same concept in different contexts

### Diagonal Threads (Synthesis)
```
ZTL (Theory: "Information Theory")
    ↘
     MOC (Synthesis: "Compression & Learning")
    ↗
ZTL (Practice: "Neural Network Pruning")
```

**Learning path:** Build meta-frameworks connecting domains

## Progressive Complexity Patterns

### Pattern 1: Depth Ladder
Start with overview, build understanding layer by layer

**Rungs:**
1. **Survey:** Read MOC summary (2 min)
2. **Sample:** Read 2-3 representative Zettel (10 min)
3. **Study:** Read all related Zettel (30-60 min)
4. **Synthesize:** Create own summary note (20 min)
5. **Extend:** Apply or teach (variable)

**When to climb:** When previous rung feels solid

### Pattern 2: Breadth Spiral
Circle through related topics, each time going deeper

**Spiral:**
1. **Pass 1:** Survey all MOCs in domain (identify 5-7 key themes)
2. **Pass 2:** Study one note per theme (get foundation)
3. **Pass 3:** Deep-dive each theme sequentially
4. **Pass 4:** Create connections between themes
5. **Pass 5:** Build synthesis framework

**When to spiral:** When learning broad, interconnected domain

### Pattern 3: Question-Driven
Let questions guide the learning path

**Flow:**
1. **Question arises** from curiosity or need
2. **Search** existing notes (`find_notes`)
3. **Read** related content
4. **Answer emerges** or **new questions** appear
5. **Document** answer as new Zettel
6. **Link** back to question origin

**When to use:** For just-in-time learning, research

## Integration with Zettelkasten Agent

### Learning Workflow with Agent

**Step 1: Ingest (Agent-Assisted)**
```
You: Add source material → SRC note
Agent: Prioritizer identifies for processing
Agent: Analyzer extracts concepts (factual/inferential/generative)
```

**Step 2: Synthesis (Agent-Generated)**
```
Agent: Synthesizer creates 3-7 atomic ZTL notes
Agent: Integrator links to existing knowledge
You: Review and refine agent synthesis
```

**Step 3: Navigation (You-Driven)**
```
You: Read INDEX → Choose MOC → Read Zettel
You: Follow interesting links
You: Identify knowledge gaps
```

**Step 4: Extension (Collaborative)**
```
You: Create application notes or questions
Agent: Suggests connections to existing notes
You: Weave new understanding into tapestry
```

### Teaching the Agent Your Learning Style

**Customize synthesis by providing context:**

```markdown
# In _LOG.md, add:
Learning goal: Master gradient descent for implementation
Learning style: Need concrete examples before theory
Current level: Understand calculus, new to ML
Focus areas: Practical implementation > mathematical proofs
```

Agent's analyzer can adapt emphasis based on this context.

## Knowledge Gap Detection

### Manual Detection
**Questions that signal gaps:**
- "I don't understand how X relates to Y"
- "What's the opposite of this concept?"
- "When would I NOT use this?"
- "What are the edge cases?"

### Automated Detection (Future)
**Patterns that suggest gaps:**
- Zettel with no links (orphans)
- MOCs with < 3 notes (underexplored)
- High-level concepts without examples
- Examples without theory notes

## Success Metrics for Progressive Learning

**Phase 1 (Survey):**
- ✅ Can list 5-7 main themes in domain
- ✅ Can explain domain to complete beginner
- ✅ Identified 2-3 areas for focused study

**Phase 2 (Focus):**
- ✅ Can explain concepts without looking at notes
- ✅ Can generate own examples
- ✅ Can identify when concept applies vs. doesn't

**Phase 3 (Synthesize):**
- ✅ Can see connections between concepts
- ✅ Can create analogies across domains
- ✅ Can critique or extend existing frameworks

**Phase 4 (Extend):**
- ✅ Applied knowledge to real problem
- ✅ Taught concept to someone else
- ✅ Created original synthesis or insight

## Common Learning Anti-Patterns

| Anti-Pattern | Why It Fails | Progressive Alternative |
|--------------|--------------|------------------------|
| **Depth-first obsession** | Get lost in details, lose big picture | Survey first, then focus |
| **Breadth-only skimming** | No real understanding, just familiarity | Breadth spiral with depth passes |
| **Linear reading** | Miss connections, no synthesis | Question-driven exploration |
| **Passive consumption** | Read but don't create | Synthesis as active learning |
| **Isolated notes** | Knowledge silos, no integration | Weave connections actively |
| **Premature MOC creation** | Structure before understanding | Let MOCs emerge from notes (5-7+ threshold) |

## Example: Learning Machine Learning (Complete Workflow)

**Week 1: Survey Phase**
```
1. Read INDEX → Identify "Machine Learning" MOC
2. Scan MOC → See themes: supervised, unsupervised, optimization, evaluation
3. Quick read 2 notes per theme (8 notes, ~30 min)
4. Document gaps in _LOG.md: "Need more on optimization algorithms"
```

**Week 2-3: Focus Phase (Optimization)**
```
1. Deep-dive MOC-Optimization.md
2. Read all Zettel on gradient descent (5 notes, ~1 hour)
3. Add external tutorial as SRC note
4. Agent synthesizes → 4 new ZTL notes created
5. Create own example: "ZTL-GradientDescentOnQuadratic.md"
```

**Week 4: Synthesize Phase**
```
1. Create bridge note: "ZTL-OptimizationAsSearch.md" (connects optimization to search algorithms)
2. Update MOC-Optimization.md with new framework
3. Link optimization concepts to stats and calculus MOCs
4. Write synthesis: "What all optimization has in common"
```

**Week 5: Extend Phase**
```
1. Implement gradient descent in Python (SRC → code)
2. Document failure: learning rate too high
3. Create teaching MOC: "MOC-ExplainingGradientDescent.md"
4. Apply to neural network project
```

## Integration Points for Skill

**For the actual skill (SKILL.md), include:**

1. **Quick Start** - The 4 phases as simple checklist
2. **Workflows** - Depth Ladder, Breadth Spiral, Question-Driven patterns
3. **Quick Reference** - Phase → Zettelkasten pattern → Questions table
4. **Examples** - ML learning workflow (condensed)
5. **Common Mistakes** - Anti-patterns table

**For reference files:**
- `reference/learning-patterns.md` - Detailed patterns with variations
- `reference/agent-collaboration.md` - How to work with synthesis agent
- `reference/knowledge-gap-detection.md` - Systematic gap analysis

**For testing (3-5 scenarios):**
1. Complete beginner learning new domain (e.g., Rust programming)
2. Intermediate learner deepening knowledge (e.g., advancing in ML)
3. Expert exploring adjacent domain (e.g., ML researcher learning neuroscience)
4. Teaching/explaining workflow (e.g., creating course materials)
5. Research synthesis (e.g., literature review → novel insight)

---

**Next: Implement SKILL.md using this design**
