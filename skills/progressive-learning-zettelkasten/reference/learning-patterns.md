# Learning Patterns: Detailed Variations

## Overview

This document provides detailed variations of the 3 core learning patterns: Depth Ladder, Breadth Spiral, and Question-Driven.

## Pattern 1: Depth Ladder (Detailed)

### Standard Ladder (5 Rungs)

**Use when:** Learning single, well-defined concept

| Rung | Activity | Duration | Deliverable |
|------|----------|----------|-------------|
| 1 | Read MOC summary | 2 min | Mental outline |
| 2 | Sample 2-3 Zettel | 10 min | Basic understanding |
| 3 | Study all Zettel | 30-60 min | Comprehensive knowledge |
| 4 | Synthesize summary | 20 min | Own synthesis note |
| 5 | Apply/teach | Variable | Application or teaching MOC |

### Accelerated Ladder (3 Rungs)

**Use when:** Time-constrained, just-in-time learning

| Rung | Activity | Duration |
|------|----------|----------|
| 1 | Scan MOC | 5 min |
| 2 | Study key Zettel | 20 min |
| 3 | Quick application | 30 min |

### Deep Research Ladder (7 Rungs)

**Use when:** Academic research, thesis work

| Rung | Activity | Duration |
|------|----------|----------|
| 1 | Survey literature (MOCs) | 1 hour |
| 2 | Sample key papers (Zettel) | 2 hours |
| 3 | Deep study primary sources | 1 week |
| 4 | Critical analysis | 3 days |
| 5 | Synthesis framework | 2 days |
| 6 | Original contribution | 1-2 weeks |
| 7 | Peer feedback loop | Ongoing |

## Pattern 2: Breadth Spiral (Detailed)

### 5-Pass Spiral

**Use when:** Learning broad, interconnected domain (e.g., Machine Learning)

**Pass 1: Survey (Wide, Shallow)**
- Time: 2 hours
- Action: Scan all MOCs in domain
- Deliverable: List of 5-7 key themes
- Example: "ML themes: supervised, unsupervised, optimization, evaluation, deployment, ethics, theory"

**Pass 2: Sample (Medium, Shallow)**
- Time: 4 hours
- Action: Read 1-2 notes per theme
- Deliverable: Basic familiarity with each theme
- Example: Read one Zettel on each ML theme

**Pass 3: Focus (Narrow, Deep)**
- Time: 2-3 weeks
- Action: Deep-dive each theme sequentially
- Deliverable: Mastery of each theme
- Example: Week 1 = supervised learning, Week 2 = unsupervised, etc.

**Pass 4: Connect (Medium, Medium)**
- Time: 1 week
- Action: Create connections between themes
- Deliverable: Bridge notes, updated MOCs
- Example: Link supervised learning to optimization, evaluation to ethics

**Pass 5: Synthesize (Wide, Deep)**
- Time: 3-5 days
- Action: Build meta-framework
- Deliverable: Synthesis MOC, personal model
- Example: "MOC-MyMLFramework.md" - how all themes relate

### 3-Pass Quick Spiral

**Use when:** Time-constrained but need breadth

**Pass 1: Rapid survey (1 hour)**
- Scan MOCs, identify 3-4 key themes

**Pass 2: Focused study (4 hours)**
- Deep-dive one theme, sample others

**Pass 3: Quick synthesis (1 hour)**
- Create connections, update MOC

### Continuous Spiral

**Use when:** Ongoing learning in established domain

**Pattern:** Return to spiral every 3-6 months
- Pass 1: What's new? (survey recent additions)
- Pass 2: Deepen weak areas (focus)
- Pass 3: Refine frameworks (synthesize)
- Pass 4: Apply to new problems (extend)

## Pattern 3: Question-Driven (Detailed)

### Research Question Flow

**For academic or professional research:**

```
1. FORMULATE
   Research question: "How does X affect Y under condition Z?"

2. DECOMPOSE
   Sub-questions:
   - What is X? (definitional)
   - What is Y? (definitional)
   - What is Z? (contextual)
   - How do X and Y typically relate? (relational)
   - What's unique about Z? (conditional)

3. SEARCH
   find_notes() for each sub-question
   Identify: answers, partial answers, gaps

4. FILL GAPS
   For each gap:
   - Add SRC note with external source
   - Agent synthesizes
   - Review and refine

5. SYNTHESIZE
   Create answer note linking all sub-answers
   Format: "ZTL-[Question-Summary].md"

6. VALIDATE
   Check synthesis against original question
   Identify counter-evidence
   Document limitations

7. APPLY
   Use answer in practice
   Document what worked/failed
   Refine understanding
```

### Curiosity-Driven Flow

**For exploratory learning:**

```
1. NOTICE
   Something interesting in notes
   Example: "Why do these two concepts keep appearing together?"

2. WONDER
   Formulate question
   Example: "What's the relationship between gradient descent and Newton's method?"

3. EXPLORE
   Search notes: find_notes()
   Follow links
   Read related Zettel

4. DISCOVER
   Answer emerges, or...
   New questions appear (iterate)

5. CAPTURE
   Document insight as Zettel
   Link to related notes

6. REFLECT
   What did I learn?
   What new questions arose?
   Where next?
```

### Problem-Driven Flow

**For applied, just-in-time learning:**

```
1. ENCOUNTER PROBLEM
   Practical challenge at work/project
   Example: "Neural network not converging"

2. SEARCH KNOWLEDGE
   find_notes(keywords=["convergence", "neural network"])
   Quick read of results

3. APPLY KNOWLEDGE
   Try solution from notes
   Document outcome

4. IF SUCCESS
   Create application note
   Link to theoretical notes
   Done

5. IF FAILURE
   Identify knowledge gap
   Add SRC note (external resource)
   Agent synthesizes
   Return to step 3
```

## Hybrid Patterns

### Depth-Spiral Hybrid

**Use when:** Need both deep expertise and broad context

**Phase 1: Spiral survey (breadth)**
- 3-pass spiral to identify domain landscape

**Phase 2: Depth ladder (focus)**
- Pick 2-3 critical themes
- Deep ladder for each

**Phase 3: Spiral synthesis (integration)**
- Return to spiral pattern
- Connect deep knowledge across themes

### Question-Ladder Hybrid

**Use when:** Specific question needs systematic depth

**Phase 1: Question formulation**
- Decompose question into sub-questions

**Phase 2: Ladder per sub-question**
- 5-rung ladder for each sub-question

**Phase 3: Synthesis**
- Integrate sub-answers
- Address original question

## Customizing Patterns to Learning Style

### Visual Learners
**Adaptation:** Add visualization step to each pattern
- Create concept maps after survey
- Draw connections between Zettel
- Visualize MOC structure as diagrams

### Kinesthetic Learners
**Adaptation:** Add hands-on step immediately
- Survey → Try → Study pattern
- Prototype before deep reading
- Learn through building

### Auditory Learners
**Adaptation:** Add verbal explanation step
- Record yourself explaining concept
- Discuss with others (or rubber duck)
- Listen to related podcasts/lectures

### Reading/Writing Learners
**Adaptation:** Emphasize note creation
- Write summary after each step
- Create more synthesis notes
- Journaling learning process in _LOG.md

## Pattern Selection Decision Tree

```
What's your learning goal?
  ↓
Build expertise in ONE specific concept?
  YES → Depth Ladder (Standard or Deep)
  NO ↓
  ↓
Learn ENTIRE new domain from scratch?
  YES → Breadth Spiral (5-pass)
  NO ↓
  ↓
Answer a SPECIFIC question?
  YES → Question-Driven (Research or Problem)
  NO ↓
  ↓
Deepen EXISTING knowledge?
  YES → Continuous Spiral or Question-Driven (Curiosity)
  NO ↓
  ↓
Time-constrained but need overview?
  YES → Quick Spiral or Accelerated Ladder
```

## Combining with Zettelkasten Agent

**For each pattern, agent helps with:**

**Depth Ladder:**
- Rung 3-4: Agent synthesizes SRC → ZTL (saves reading time)
- Rung 5: Agent suggests connections for application

**Breadth Spiral:**
- Pass 1-2: Agent maintains INDEX, easy to survey
- Pass 3: Agent creates Zettel as you focus
- Pass 4-5: Agent integrates, updates MOCs

**Question-Driven:**
- Step 3: Agent's find_notes() semantic search
- Step 4: Agent fills gaps via synthesis
- Step 5: Agent suggests related questions

**Key insight:** Agent handles mechanical parts (synthesis, linking, organizing). You handle high-level parts (choosing patterns, asking questions, applying knowledge).

## Measuring Pattern Effectiveness

**Track in _LOG.md:**

```markdown
## Learning Session: [Date]
Pattern used: [Depth Ladder / Breadth Spiral / Question-Driven]
Domain: [e.g., Machine Learning / Gradient Descent]
Time invested: [e.g., 2 hours]
Success metrics:
- Clarity: Can I explain without notes? [Yes/No/Partial]
- Connections: Did I link to existing knowledge? [Count]
- Application: Can I use this? [Yes/No/Not tested]
- Satisfaction: [1-5]

What worked: [brief note]
What didn't: [brief note]
Adjust next time: [brief note]
```

**Review monthly:** Which patterns work best for which domains?

---

**Remember:** Patterns are guides, not rules. Adapt to your needs, learning style, and time constraints. The best pattern is the one you'll actually use consistently.
