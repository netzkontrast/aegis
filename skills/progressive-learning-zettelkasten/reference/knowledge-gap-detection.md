# Knowledge Gap Detection: Systematic Gap Analysis

## Overview

Knowledge gaps are the difference between what you know and what you need to know. Systematic detection helps focus learning efforts and ensures comprehensive understanding.

**Key insight:** Gaps aren't failures - they're learning opportunities. Progressive learning means systematically identifying and filling gaps.

## Types of Knowledge Gaps

### 1. Awareness Gaps
**Definition:** Don't know that you don't know

**Symptoms:**
- Surprised by unexpected requirements
- Misunderstand domain scope
- Overlook entire sub-fields

**Detection:**
- Survey _INDEX.md: What MOCs exist that you've never explored?
- Compare to external domain maps (Wikipedia categories, textbook ToCs)
- Ask experts: "What am I missing?"

**Priority:** HIGH - These are dangerous (unknown unknowns)

### 2. Understanding Gaps
**Definition:** Know concept exists, but don't understand it

**Symptoms:**
- Can't explain concept clearly
- Can't generate examples
- Can't apply in practice

**Detection:**
- Try explaining concept to imaginary beginner
- Try creating original example
- Check if you can answer: "When does this NOT apply?"

**Priority:** MEDIUM-HIGH - Core learning work

### 3. Connection Gaps
**Definition:** Understand concepts individually, but not relationships

**Symptoms:**
- Knowledge feels fragmented
- Can't see how concepts relate
- Miss cross-domain insights

**Detection:**
- Check Zettel link density (orphaned notes?)
- Try explaining how X relates to Y
- Look for bridge notes between MOCs

**Priority:** MEDIUM - Important for synthesis

### 4. Application Gaps
**Definition:** Understand theory, can't apply in practice

**Symptoms:**
- Can explain but can't use
- Theory without practice
- "I understand it but can't do it"

**Detection:**
- Count application examples vs. theory notes
- Try solving novel problem
- Check: Do you have implementation notes?

**Priority:** HIGH - Knowledge without application is incomplete

### 5. Depth Gaps
**Definition:** Surface understanding, lack depth

**Symptoms:**
- Can give textbook answer
- Can't handle edge cases
- Don't know limitations

**Detection:**
- Try explaining to expert
- Ask: "What are the edge cases?"
- Ask: "When does this break?"

**Priority:** MEDIUM - Depends on domain need

## Manual Detection Methods

### Method 1: Explain-to-Yourself Test

**Process:**
1. Pick random Zettel
2. Close note
3. Explain concept out loud (or write)
4. Open note, compare

**Gap signals:**
- Can't recall key points → Understanding gap
- Can't explain clearly → Depth gap
- Can't give examples → Application gap
- Can't explain connections → Connection gap

**Frequency:** Weekly, 5-10 random notes

### Method 2: Teach-to-Imaginary-Student Test

**Process:**
1. Pick a MOC (topic)
2. Imagine teaching it to beginner
3. Create teaching outline
4. Identify what you'd struggle to explain

**Gap signals:**
- Can't create clear progression → Structure gap
- Can't think of examples → Application gap
- Can't explain "why" → Depth gap
- Can't connect to prior knowledge → Connection gap

**Frequency:** After completing each learning phase (monthly)

### Method 3: Question Generation Test

**Process:**
1. Review MOC
2. Generate 10 questions someone might ask
3. Try answering each
4. Note which you can't answer

**Types of questions:**
- **Factual:** "What is X?"
- **Relational:** "How does X relate to Y?"
- **Causal:** "Why does X cause Y?"
- **Application:** "When would I use X?"
- **Limitation:** "When does X fail?"
- **Comparison:** "How is X different from Z?"

**Gap signals:**
- Can't generate questions → Awareness gap
- Can't answer factual → Understanding gap
- Can't answer relational → Connection gap
- Can't answer application → Application gap

**Frequency:** End of learning sprint (bi-weekly)

### Method 4: External Comparison Test

**Process:**
1. Find external resource (textbook ToC, Wikipedia, course syllabus)
2. Compare to your _INDEX.md and MOCs
3. Identify topics in external but not in yours

**Gap signals:**
- Missing entire sections → Awareness gap
- Have section but few notes → Depth gap
- Notes but no applications → Application gap

**Frequency:** Quarterly or when starting new domain

### Method 5: Application Challenge Test

**Process:**
1. Set practical challenge
2. Try solving using only your notes
3. Document where you get stuck

**Example challenges:**
- Implement algorithm from your notes
- Solve novel problem in domain
- Critique published work
- Design system using principles

**Gap signals:**
- Can't solve → Application gap
- Missing concepts → Understanding gap
- Don't know which concepts apply → Connection gap

**Frequency:** End of learning cycle (monthly)

## Automated Detection (Using Zettelkasten Structure)

### Structural Gap Signals

**1. Orphaned Zettel**
```
Search: Notes with zero or one link
Query: find_notes(), filter by link count
Interpretation: Isolated knowledge, connection gap
```

**2. Thin MOCs**
```
Search: MOCs with < 5 notes
Interpretation: Underexplored topic, possible depth gap
```

**3. Imbalanced MOCs**
```
Check: Theory notes vs. application notes ratio
Example: 20 theory, 0 application → Application gap
```

**4. Stale Notes**
```
Check: Last-modified dates
Interpretation: Notes not revisited/refined → Possible depth gap
```

**5. Question Backlog**
```
Check: _LOG.md for unanswered questions
Interpretation: Explicit awareness gaps
```

### Query-Based Detection

**Run these searches periodically:**

**Find orphans:**
```
For each Zettel:
  If link_count == 0 or 1:
    Flag as orphan, investigate connection gap
```

**Find imbalanced MOCs:**
```
For each MOC:
  Count: theory notes, application notes, example notes
  If application < theory/3:
    Flag application gap
```

**Find question-poor MOCs:**
```
For each MOC:
  Count notes tagged "question" or containing "?"
  If count == 0:
    Flag possible understanding gap (no curiosity)
```

## Gap Prioritization Matrix

| Gap Type | Impact | Urgency | Priority |
|----------|--------|---------|----------|
| **Awareness (unknown unknowns)** | HIGH | HIGH | 1 |
| **Application (can't use)** | HIGH | MEDIUM | 2 |
| **Understanding (don't get it)** | HIGH | MEDIUM | 3 |
| **Connection (fragmented)** | MEDIUM | MEDIUM | 4 |
| **Depth (surface-level)** | MEDIUM | LOW | 5 |

**Priority formula:**
```
Priority = (Impact × 2) + Urgency
```

**Action plan:**
1. Fix Priority 1-2 gaps immediately
2. Schedule Priority 3-4 gaps in learning plan
3. Address Priority 5 gaps opportunistically

## Gap Filling Strategies

### For Awareness Gaps
**Strategy:** Expand survey, external comparison

1. Review external domain maps
2. Identify missing topics
3. Add SRC notes for each missing area
4. Let agent synthesize
5. Create new MOCs as patterns emerge

**Time investment:** Survey phase (few hours to days)

### For Understanding Gaps
**Strategy:** Deep focus, multiple sources

1. Identify specific concept not understood
2. Add 2-3 SRC notes from different sources
3. Agent synthesizes multiple perspectives
4. Test understanding with explain-to-yourself
5. Iterate until clear

**Time investment:** Focus phase (1-3 hours per concept)

### For Connection Gaps
**Strategy:** Active linking, bridge notes

1. Identify isolated notes (orphans)
2. Ask: "How does this relate to X?"
3. Search for related concepts: `find_notes()`
4. Create bridge notes explaining connections
5. Update MOCs to show relationships

**Time investment:** Synthesis phase (30-60 min per connection)

### For Application Gaps
**Strategy:** Practice, examples, projects

1. Identify theory-heavy MOC
2. Set practical challenge
3. Attempt application
4. Document approach (SRC note)
5. Create application Zettel
6. Link to theory notes

**Time investment:** Extension phase (hours to days)

### For Depth Gaps
**Strategy:** Expert sources, edge cases

1. Find advanced sources (papers, not tutorials)
2. Add as SRC notes with "advanced" tag
3. Agent synthesizes advanced concepts
4. Create notes on limitations and edge cases
5. Link to foundational notes

**Time investment:** Focused study (1-2 weeks)

## Gap Detection Workflow

**Monthly routine:**

```markdown
## Monthly Knowledge Gap Check

### Step 1: Structural Check (30 min)
- [ ] Run orphan detection
- [ ] Check thin MOCs (<5 notes)
- [ ] Check MOC balance (theory vs. application)
- [ ] Review _LOG.md question backlog

### Step 2: Understanding Check (1 hour)
- [ ] Explain-to-yourself test (5-10 random Zettel)
- [ ] Note failures, grade each (1-5)
- [ ] Identify patterns in failures

### Step 3: Connection Check (30 min)
- [ ] Pick one MOC, generate questions
- [ ] Focus on relational questions
- [ ] Identify missing connections

### Step 4: Application Check (1 hour)
- [ ] Set practical challenge
- [ ] Attempt solution
- [ ] Document gaps encountered

### Step 5: Prioritize (30 min)
- [ ] List all gaps found
- [ ] Apply priority matrix
- [ ] Create learning plan for top 3

### Step 6: Document (15 min)
- [ ] Add findings to _LOG.md
- [ ] Set reminders for gap-filling
- [ ] Track gap-filling progress
```

**Total time:** ~3.5 hours/month

## Documenting Gaps

**In _LOG.md, create gaps section:**

```markdown
## Known Knowledge Gaps (2024-11-05)

### Priority 1: Awareness
- [ ] Missing: Bayesian optimization (entire sub-field)
- [ ] Missing: Reinforcement learning ethics
- [ ] Action: Survey papers, add SRC notes

### Priority 2: Application
- [ ] Can't implement: Gradient descent variants
- [ ] Can't apply: Regularization techniques
- [ ] Action: Practical projects, code examples

### Priority 3: Understanding
- [ ] Unclear: Backpropagation through time
- [ ] Unclear: Attention mechanisms
- [ ] Action: Multiple sources, agent synthesis

### Priority 4: Connection
- [ ] Isolated: Optimization orphans (5 notes)
- [ ] Fragmented: ML theory not linked to stats
- [ ] Action: Create bridge notes

### Priority 5: Depth
- [ ] Surface: Neural networks (only basics)
- [ ] Surface: Evaluation metrics
- [ ] Action: Advanced papers when time permits
```

## Gap Tracking Metrics

**Track over time:**

```markdown
## Gap Metrics (Quarterly)

Total Zettel: 150
Orphaned: 8 (5.3%)  ← Goal: <5%
MOCs: 15
Thin MOCs: 2 (13%) ← Goal: <10%

Application ratio: 0.6 (60 app / 90 theory) ← Goal: >0.5

Unanswered questions in _LOG.md: 3 ← Goal: <5

Average explanation score (1-5): 4.1 ← Goal: >4.0

Trends:
- Orphans decreasing (was 12 last quarter) ✓
- Application ratio improving (was 0.4) ✓
- Need more connection work in ML→Stats
```

## Red Flags: Critical Gaps

🚩 **Immediate attention needed:**

- **>10% orphaned notes** → Serious connection gap
- **Application ratio <0.3** → Theory without practice
- **Can't complete basic challenge** → Fundamental understanding gap
- **Multiple MOCs with <3 notes** → Awareness gap (scattered knowledge)
- **>20 unanswered questions in _LOG** → Overwhelmed, need focus

**If you see these:** Stop adding new knowledge. Focus on integration and application.

## Tools for Gap Detection

**Simple bash queries:**

```bash
# Count orphans (notes with 0-1 links)
cd vault/
grep -l "ZTL-" *.md | while read file; do
  links=$(grep -o "\[\[ZTL-" "$file" | wc -l)
  if [ $links -le 1 ]; then
    echo "$file: $links links (orphan)"
  fi
done

# Check MOC sizes
grep "MOC-" *.md | wc -l

# Find notes without examples
grep -L "Example:" ZTL-*.md
```

**Future tools (not implemented yet):**
- Semantic similarity search (find related but unlinked notes)
- Knowledge graph visualization (see gaps visually)
- Auto-question generation (suggest questions to explore)

---

**Remember:** Gaps are normal and ongoing. Progressive learning is the process of systematically identifying and filling gaps while building new knowledge. Regular gap detection keeps learning focused and comprehensive.
