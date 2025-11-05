# Synthesis: Unified Skill Authoring Framework

## Overview

This document synthesizes all four approaches into a unified, practical framework that:
1. Preserves rigor where needed (discipline skills)
2. Enables pragmatism where appropriate (reference skills)
3. Uses persuasion principles ethically and consciously
4. Provides clear decision criteria and stopping conditions
5. Addresses blind spots identified in critical analysis

## Core Principles (Synthesized)

### Principle 1: Proportional Rigor

**From writing-skills + Anthropic + critical analysis**

Testing rigor should match skill criticality:

| Change Type | Risk Level | Testing Requirement | Approach |
|-------------|-----------|---------------------|----------|
| **Typo/formatting** | Minimal | Review only | Quick scan, commit |
| **Small addition** (<50 lines) | Low | Light testing | 1-2 scenarios, verify behavior |
| **Major addition** (50-200 lines) | Medium | Moderate testing | 3-5 scenarios, model testing |
| **New discipline skill** | High | Full TDD | RED-GREEN-REFACTOR, pressure scenarios |
| **Breaking change** | Critical | Full TDD + migration | Full cycle + rollout plan |

**Key insight:** The Iron Law applies to HIGH-RISK changes. Proportionality prevents overhead and abandonment.

### Principle 2: Conscious Persuasion

**From persuasion principles + critical analysis**

Use persuasion principles deliberately:

**Requirements before using heavy Authority/Commitment:**
1. ✅ **Necessity check:** Is compliance critical? (safety, correctness, discipline)
2. ✅ **Ethical test:** Serves user's genuine interests if they understood the psychology?
3. ✅ **Cultural check:** Language appropriate for user culture?
4. ✅ **Transparency option:** Consider disclosing persuasion use in meta-documentation

**Graduated scale:**

| Skill Type | Persuasion Level | Example Language |
|------------|------------------|------------------|
| **Reference** | None | "See reference.md for details" |
| **Technique** | Light | "Consider using X when Y" |
| **Guidance** | Moderate | "Use X for Y. Avoid Z." |
| **Discipline** | Strong | "YOU MUST X. No exceptions: [list]" |

**Key insight:** Persuasion is a tool. Use consciously, proportionally, ethically.

### Principle 3: Progressive Disclosure

**From Anthropic + writing-skills**

Optimize for discovery and loading:

**SKILL.md structure:**
```markdown
---
name: skill-name-with-hyphens
description: Use when [specific triggers] - [what + how]. Keywords: X, Y, Z.
---

# Skill Name

## Overview (50-100 words)
Core principle. When NOT to use.

## Quick Start (<200 words)
Inline example, minimal explanation

## [Domain-specific sections] (<300 words total)
Quick reference tables, bullet patterns

## Advanced Topics
**Topic A:** See [reference/topic-a.md](reference/topic-a.md)
**Topic B:** See [reference/topic-b.md](reference/topic-b.md)

## Common Mistakes
[Red flags, rationalization table if discipline skill]
```

**Token budgets:**
- SKILL.md body: <500 lines (Anthropic)
- Frequently-loaded skills: <200 words total body (writing-skills)
- References: no limit (loaded on-demand)

**Key insight:** Front-load discoverability (name, description), progressive-load details (references).

### Principle 4: Skill-Type Taxonomy

**From all sources + synthesis**

Different skills need different approaches:

| Type | Purpose | Testing | Persuasion | Structure |
|------|---------|---------|------------|-----------|
| **Discipline** | Enforce critical practice | Full TDD | Authority + Commitment + Social Proof | Explicit rules, rationalization table |
| **Technique** | Guide implementation | Moderate (3-5 scenarios) | Moderate Authority + Unity | Examples, workflows, checklists |
| **Pattern** | Mental model | Recognition testing | Unity + light Authority | Before/after, when to apply |
| **Reference** | API/command docs | Retrieval testing | None | Tables, search-optimized |
| **Hybrid** | Combination | Strongest component | Strongest component | Modular structure |

**Key insight:** One size doesn't fit all. Tailor approach to skill type.

### Principle 5: Observable Quality

**New - addresses blind spot in all approaches**

Skills should include observability:

**For discipline skills:**
```markdown
## Validation
Run periodic spot-checks:
- Review 5 random sessions using this skill
- Count compliance rate
- Document new rationalization patterns
- Update skill if <80% compliance
```

**For all skills:**
```markdown
## Effectiveness Metrics
Success indicators:
- Agent completes task correctly
- Time-to-completion within expected range
- No repeated errors on same pattern

Failure indicators:
- Agent skips steps
- Agent rationalizes around rules
- Repeated questions on same topic

If failures > 20%: investigate and update skill.
```

**Key insight:** You can't improve what you don't measure. Build in observability.

## Unified Testing Framework

### Testing Decision Tree

```
"What are you changing?"
  ↓
Typo or formatting?
  YES → Review only, commit
  NO ↓
Small addition (<50 lines)?
  YES → Light testing (1-2 scenarios)
  NO ↓
Is this a discipline skill?
  YES → Full TDD (RED-GREEN-REFACTOR)
  NO ↓
Is this a technique/major addition?
  YES → Moderate testing (3-5 scenarios)
  NO ↓
Is this a reference skill?
  YES → Retrieval testing (can agent find + apply info?)
```

### RED-GREEN-REFACTOR (For High-Risk Changes)

**Preserve from writing-skills, add stopping criteria:**

#### RED Phase - Establish Baseline

**Steps:**
1. Create pressure scenarios (discipline) OR application scenarios (technique)
   - Minimum 3 scenarios
   - Combine stressors for discipline (time + sunk cost + authority)
   - Vary contexts for technique (different inputs, edge cases)

2. Run scenarios WITHOUT skill present
   - Use fresh Claude instance
   - Document behavior verbatim
   - Capture exact rationalizations (for discipline skills)
   - Note success rate and failure modes

3. Analyze baseline
   - Identify patterns in failures
   - Document specific gaps in knowledge/guidance
   - Note which pressure types trigger violations

**Stopping criteria:** You have adequate baseline when:
- ✅ Ran minimum 3 scenarios
- ✅ Documented verbatim behavior for each
- ✅ Identified 2+ specific gaps or rationalization patterns
- ✅ Understand WHY skill is needed (not just that it's needed)

#### GREEN Phase - Write Minimal Skill

**Steps:**
1. Write skill addressing ONLY specific failures from RED
   - Don't add hypothetical content
   - Don't over-explain
   - Focus on identified gaps

2. Apply CSO optimization
   - Description starts with "Use when [specific triggers]"
   - Include keywords from failure scenarios
   - Third person, <1024 chars

3. Run same scenarios WITH skill present
   - Use fresh Claude instance with skill loaded
   - Compare behavior to baseline
   - Measure compliance rate

**Stopping criteria:** You can proceed when:
- ✅ All scenarios show improved behavior
- ✅ Compliance rate >80% (discipline) OR success rate >90% (technique)
- ✅ Skill addresses all major gaps from baseline
- ✅ No new confusions introduced

#### REFACTOR Phase - Close Loopholes

**Steps:**
1. Run additional varied scenarios
   - Different contexts
   - Different pressure combinations (for discipline)
   - Edge cases

2. Identify new rationalizations or failures
   - Document verbatim (again)
   - Look for patterns

3. Add explicit counters
   - Rationalization table entry
   - Red flag list item
   - Tightened language

4. Re-test until adequate

**Stopping criteria:** You can ship when:
- ✅ Ran 5+ total unique scenarios
- ✅ Compliance/success rate >90%
- ✅ No NEW rationalization patterns in last 2 scenarios
- ✅ Rationalization table captures major excuses
- ✅ Red flags list covers known failure modes

**Key addition:** CLEAR STOPPING CRITERIA (addresses critical gap)

### Moderate Testing (For Medium-Risk Changes)

**Simplified from TDD, more rigorous than "evaluations recommended":**

**Steps:**
1. Create 3-5 application scenarios
   - Cover main use case
   - Cover 1-2 edge cases
   - Cover one "could go wrong" case

2. Establish baseline (optional but recommended)
   - Run WITHOUT skill
   - Document behavior
   - Identify gaps

3. Write skill addressing gaps

4. Validate with scenarios
   - Run WITH skill
   - Success rate >85%
   - Agent finds and applies information correctly

5. Test across models (if targeting multiple)
   - Haiku: Does agent have enough guidance?
   - Sonnet: Is it efficient?
   - Opus: Is it too verbose?

**Stopping criteria:**
- ✅ 3+ scenarios pass
- ✅ Success rate >85%
- ✅ Tested on target models

### Light Testing (For Low-Risk Changes)

**Quick validation:**

**Steps:**
1. Create 1-2 scenarios covering the change

2. Validate behavior
   - Agent uses new information correctly
   - No confusion introduced

**Stopping criteria:**
- ✅ Scenarios pass
- ✅ No obvious issues

## Unified Structure Template

**Combining best patterns from all approaches:**

```markdown
---
name: skill-name-with-hyphens
description: Use when [specific triggers and symptoms] - [what it does and how it helps]. Third person. Keywords: X, Y, Z.
---

# Skill Name

## Overview
[Core principle in 1-2 sentences. When NOT to use.]

## When to Use

**Symptoms:**
- Specific symptom 1 (use keywords for search)
- Specific symptom 2
- Specific symptom 3

**Contexts:**
- Context A
- Context B

[Small flowchart ONLY if decision is non-obvious - use graphviz conventions]

## Quick Start

[Inline example with minimal explanation - 50-100 words]

```[language]
[Concrete, runnable example]
```

## Quick Reference

[Table or bullets for scanning common operations]

| Operation | Pattern | Notes |
|-----------|---------|-------|
| X | `code` | When Y |
| Z | `code` | Avoid if W |

## Core Patterns (for techniques)

**Before:**
```[language]
[Anti-pattern]
```

**After:**
```[language]
[Recommended pattern]
```

## Workflows (for complex tasks)

[Copyable checklist:]

```
Task Progress:
- [ ] Step 1: [action] ([tool/command])
- [ ] Step 2: [action]
- [ ] Step 3: [validation] (MUST pass before proceeding)
- [ ] Step 4: [action]
```

[Detailed steps with feedback loops:]

**Step 1: [Action]**
[Instructions]

**Step 2: [Action]**
[Instructions]

**Step 3: [Validation]**
Run: `command`
If fails: [fix and retry]
**Only proceed when passes.**

## Advanced Topics

**[Topic A]**: See [reference/topic-a.md](reference/topic-a.md)
**[Topic B]**: See [reference/topic-b.md](reference/topic-b.md)

[Keep references ONE LEVEL DEEP]

## Common Mistakes

[Table format:]

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| X | Y | Z |

## Red Flags (for discipline skills)

[Explicit warning signals:]

🛑 **STOP and [Action] if you notice:**
- Red flag 1
- Red flag 2
- Red flag 3

**All of these mean:** [Required action]

## Rationalization Table (for discipline skills)

[From baseline testing:]

| Excuse | Reality |
|--------|---------|
| "Too simple to [skip practice]" | [Counter with data/reasoning] |
| "[Rationale for skipping]" | [Counter] |

## Validation (optional - for critical skills)

[Observability guidance:]

**Success indicators:**
- Indicator 1
- Indicator 2

**Failure indicators:**
- Failure mode 1
- Failure mode 2

**Periodic review:** [How often, what to check]

---

**Meta:**
- Token budget: [body <500 lines | frequently-loaded <200 words total]
- Last tested: [date]
- Models tested: [Haiku/Sonnet/Opus]
- Compliance rate: [if tracked]
```

### Template Variations by Skill Type

**Discipline Skill:**
- Include: Red Flags, Rationalization Table, Validation
- Persuasion: Heavy Authority language
- Testing: Full TDD

**Technique Skill:**
- Include: Quick Start, Core Patterns, Workflows, Common Mistakes
- Persuasion: Moderate Authority + Unity
- Testing: Moderate (3-5 scenarios)

**Reference Skill:**
- Include: Quick Reference (prominent), Advanced Topics (linked)
- Persuasion: None (clarity only)
- Testing: Retrieval (can find + apply)

**Pattern Skill:**
- Include: Core Patterns (before/after), When to Use (explicit)
- Persuasion: Light Authority + Unity
- Testing: Recognition (when to apply vs. not)

## CSO Optimization (Enhanced)

**Combining writing-skills + Anthropic:**

### Description Formula

```yaml
description: Use when [symptom1, symptom2, symptom3] - [what it does]. [How it helps]. Keywords: X, Y, Z.
```

**Components:**

1. **"Use when" prefix** (condition-first, discovery-optimized)

2. **Specific symptoms** (3-5 concrete triggers)
   - Error messages: "command not found", "ENOENT"
   - Behaviors: "tests are flaky", "agent skips steps"
   - Contexts: "working with PDFs", "creating forms"

3. **What it does** (concise capability statement)
   - Action-oriented: "extracts text", "validates schemas"
   - Not vague: NOT "helps with documents"

4. **How it helps** (value proposition)
   - "ensuring reliable async tests"
   - "preventing data loss"

5. **Keywords** (explicit list for search)
   - Tool names: "pdfplumber", "pytest"
   - Concepts: "async", "PDF", "validation"
   - Synonyms: "timeout/hang/freeze"

**Length:** Aim for 200-500 chars. Max 1024 chars.

**Voice:** Third person ("Processes PDFs", not "I can process PDFs")

**Technology specificity:**
- Default: Technology-agnostic ("when tests are flaky" not "when pytest tests use sleep")
- Exception: If skill IS technology-specific, make explicit ("Use when working with React Router and handling auth redirects...")

### Examples (Before → After)

**❌ Before:**
```yaml
description: For async testing
```
Problems: No "Use when", vague, missing keywords

**✅ After:**
```yaml
description: Use when tests have race conditions, timing dependencies, or pass/fail inconsistently - replaces arbitrary timeouts with condition polling for reliable async tests. Keywords: flaky, timeout, async, race condition, pytest, jest.
```

**❌ Before:**
```yaml
description: I can help you with PDF processing and form filling
```
Problems: First person, vague "help", no triggers

**✅ After:**
```yaml
description: Use when working with PDF files, form filling, or document extraction - extracts text and tables from PDFs, fills form fields, merges documents using pdfplumber and pypdf. Keywords: PDF, forms, text extraction, pdfplumber, pypdf.
```

### Name Optimization

**Pattern:** `[verb]-[object]` OR `[verb]ing-[object]`

**Good:**
- `creating-skills` (gerund + object)
- `condition-based-waiting` (adjective + gerund + object)
- `working-with-archon` (gerund + object)

**Avoid:**
- `skill-creation` (noun phrase, passive)
- `pdf-stuff` (vague)
- `helper-utils` (generic)

### Keyword Placement

**Throughout SKILL.md, not just description:**

1. **Overview section:** Repeat key terms
2. **When to Use symptoms:** Specific searchable phrases
3. **Quick Reference:** Tool names, command patterns
4. **Common Mistakes:** Error messages verbatim

**Why:** Claude searches entire skill, not just description. More keyword density = better discovery.

## Persuasion Patterns (Ethical Framework)

**From persuasion principles + critical analysis:**

### When to Use Which Principle

**Authority Principle:**

**Use when:**
- Discipline enforcement needed
- Safety-critical practice
- Established best practice with strong consensus

**Language patterns:**
```markdown
YOU MUST [action]
NEVER [anti-pattern]
ALWAYS [pattern]
No exceptions:
- Not for [excuse 1]
- Not for [excuse 2]
```

**Strength levels:**
- Strong: "YOU MUST", "No exceptions"
- Moderate: "Always", "Never" (without YOU MUST)
- Light: "Recommended", "Should"

**Ethical check:**
- ✅ Serves user's genuine interests?
- ✅ Prevents serious failures?
- ✅ Proportional to risk?

**Commitment Principle:**

**Use when:**
- Multi-step process
- Accountability needed
- Preventing "I'll do it later"

**Language patterns:**
```markdown
When you [trigger], you MUST announce: "I'm using [Skill Name]"

Copy this checklist and track progress:
[checkboxes]

Before proceeding to Step 3, you MUST complete Step 2.
```

**Ethical check:**
- ✅ Transparency beneficial?
- ✅ Explicit commitment improves follow-through?
- ✅ Not creating artificial bureaucracy?

**Social Proof Principle:**

**Use when:**
- Establishing norms
- Warning about universal failure modes
- Reinforcing standards

**Language patterns:**
```markdown
X without Y = failure. Every time.

| Excuse | Reality |
|--------|---------|
| "[Common excuse]" | [Why it fails universally] |

This pattern is universal across [domain].
```

**Ethical check:**
- ✅ Claim is accurate? (not exaggerating)
- ✅ Evidence supports "every time"?
- ✅ Not creating false consensus?

**Unity Principle:**

**Use when:**
- Collaborative workflows
- Establishing team culture
- Non-hierarchical practices

**Language patterns:**
```markdown
We're colleagues working together.
I need your honest technical judgment.
Our codebase benefits when...
We both want quality.
```

**Ethical check:**
- ✅ Genuinely collaborative context?
- ✅ Not false familiarity?
- ✅ Respectful of boundaries?

**Scarcity Principle:**

**Use when:**
- Immediate action required
- Preventing procrastination
- Time-sensitive workflow

**Language patterns:**
```markdown
IMMEDIATELY after [event], [action].
Before proceeding, [action].
Do not continue until [condition].
```

**Ethical check:**
- ✅ Genuine time sensitivity?
- ✅ Not creating false urgency?
- ✅ Proportional to actual risk of delay?

**Reciprocity + Liking Principles:**

**DON'T USE** (per persuasion doc, confirmed by critique):
- Reciprocity: Feels manipulative, unnecessary
- Liking: Creates sycophancy, conflicts with honest feedback

### Principle Combination Matrix

| Skill Type | Primary | Secondary | Tertiary | Avoid |
|------------|---------|-----------|----------|-------|
| **Discipline** | Authority | Commitment | Social Proof | Liking, Reciprocity |
| **Technique** | Authority (moderate) | Unity | - | Liking, Reciprocity |
| **Pattern** | Unity | Authority (light) | - | Liking, Reciprocity |
| **Reference** | None | None | None | All persuasion |
| **Collaborative** | Unity | Commitment | - | Authority (heavy), Liking, Reciprocity |

**Rule of thumb:** Maximum 3 principles per skill. More = diminishing returns + compliance fatigue.

### Transparency and Consent (New)

**For team/organizational contexts:**

**Option 1: Disclose in meta-documentation**
```markdown
## About This Skill

This skill uses Authority principle (imperative language) to ensure
critical safety practices are followed. The firm language is intentional
and research-backed (Meincke et al., 2025).
```

**Option 2: User opt-out (for non-critical skills)**
```markdown
## Note

This skill uses directive language. If you prefer a more flexible approach,
see [alternative-skill-name] for guidance-style documentation.
```

**Option 3: Cultural adaptation**
```markdown
## Language Style

This skill uses direct imperatives typical of Western technical communication.
If your cultural context prefers indirect suggestion, adapt the tone while
preserving the core practices.
```

**Recommendation:** Option 1 (transparency) for HIGH-STAKES skills. Option 2 (opt-out) for medium-stakes. Option 3 (cultural note) when international usage expected.

## Graphviz Integration

**From graphviz conventions + critique:**

### When to Use Flowcharts

**Decision tree:**

```
"Do I need to show information?"
  NO → Don't create anything
  YES ↓
"Is it a decision where I might go wrong?"
  NO → Use table, bullets, or numbered list
  YES ↓
"Is it a simple binary decision?"
  NO → Flowchart may help if complex
  YES ↓
"Can I express it clearly in one sentence?"
  YES → Prose: "If X, do Y; otherwise do Z"
  NO → Consider flowchart
```

**Use flowcharts ONLY for:**
- Non-obvious decision points with multiple branches
- Process loops where you might stop too early
- Complex workflows with validation cycles
- "When to use A vs. B vs. C" decisions

**NEVER use flowcharts for:**
- Reference material → Quick reference table
- Code examples → Markdown code blocks
- Linear instructions → Numbered list
- Simple if/then → Prose

**Rule of thumb:** If you can express it clearly in 2-3 sentences, don't flowchart it.

### Graphviz Conventions (Summary)

**Shape semantics (from conventions doc):**
- Diamond = Decision/question
- Box = Action (default)
- Plaintext = Literal command
- Ellipse = State/situation
- Octagon (red) = Warning/stop
- Double circle = Entry/exit

**Naming patterns:**
- Questions end with `?`
- Actions start with verb
- Commands are literal
- States describe situation

**Accessibility consideration (new):**
Always provide text alternative:

```markdown
## When to Use This Skill

[Flowchart here]

**Text version:**
1. If creating new content, use docx-js library
2. If editing existing, unpack → modify XML → validate → repack
3. If tracked changes needed, see REDLINING.md
```

**For details:** See separate graphviz-conventions.dot file.

## Addressing Blind Spots

### Multi-Agent Considerations (New)

**Problem:** Skills assume single agent

**Solution:** Add coordination guidance for discipline skills

```markdown
## Multi-Agent Usage

If multiple agents are using this skill:
- **Priority:** Agent A takes precedence over Agent B when [condition]
- **Conflicts:** If agents disagree, [resolution process]
- **Shared state:** Agents share [what] via [mechanism]
```

### Lifecycle Management (New)

**Problem:** No versioning or deprecation strategy

**Solution:** Add version metadata and deprecation process

```markdown
---
name: skill-name
description: [description]
version: 2.1.0
deprecated: false
supersedes: old-skill-name
---

## Changelog

**v2.1.0 (2025-03-15)**
- Added support for X
- Fixed issue with Y

**v2.0.0 (2025-01-10)** [BREAKING]
- Changed Z (migration: see MIGRATION.md)
```

**Deprecation template:**

```markdown
---
name: old-skill-name
deprecated: true
superseded-by: new-skill-name
---

# [DEPRECATED] Old Skill Name

⚠️ **This skill is deprecated as of 2025-03-01.**

**Use [new-skill-name] instead.**

**Migration guide:** See [MIGRATION.md](MIGRATION.md)

[Keep old content for reference until full deprecation date]
```

### System-Level Integration Testing (New)

**Problem:** Skills tested in isolation, not as system

**Solution:** Integration test suite for skill collections

**Approach:**

1. **Conflict detection:**
   ```
   Test: Load skills A + B simultaneously
   Check: No contradictory guidance
   Check: Priority rules clear
   ```

2. **Emergence detection:**
   ```
   Test: Load all discipline skills
   Check: Not overwhelming (max 3 Authority principles active)
   Check: Combined compliance rate >80%
   ```

3. **Coverage analysis:**
   ```
   Test: Common scenarios
   Check: At least one skill triggered for each scenario
   Check: No scenario triggers conflicting skills
   ```

**Recommendation:** Run integration tests quarterly or when adding new skill to established collection.

### Feedback Mechanisms (New)

**Problem:** No built-in learning from failure

**Solution:** Observability patterns in skills

**For discipline skills (mandatory):**

```markdown
## Validation and Feedback

**Periodic review (monthly):**
1. Sample 10 random sessions using this skill
2. Count violations:
   - Explicit violations (agent acknowledged rule and violated)
   - Implicit violations (agent didn't follow without acknowledging)
3. Calculate compliance rate: (sessions following rule) / (total sessions)
4. Document new rationalization patterns
5. If compliance rate <80%, update skill (REFACTOR phase)

**Incident response:**
If agent causes failure by violating this skill:
1. Document exact failure mode
2. Add to rationalization table or red flags
3. Strengthen language if needed (Principle: Authority)
4. Re-test with scenario that would have caught failure
```

**For technique skills (recommended):**

```markdown
## Effectiveness Tracking

**Success indicators:**
- Task completed correctly
- Time-to-completion reasonable
- No repeated errors

**Failure indicators:**
- Agent skips steps
- Repeated questions on same topic
- Task completion but incorrect result

**Review trigger:** If >20% of uses show failure indicators, investigate and update.
```

### Cost-Benefit Framework (New)

**Problem:** No guidance on when testing overhead is justified

**Solution:** ROI estimation

**Formula:**

```
Testing Value = (Risk × Frequency × Impact) - Testing Cost

Where:
- Risk = Probability of failure without skill (0-1)
- Frequency = Uses per month (estimated)
- Impact = Cost of failure (time, consequences)
- Testing Cost = Hours spent testing × hourly value
```

**Decision matrix:**

| Testing Value | Recommendation |
|---------------|----------------|
| High (>10x testing cost) | Full TDD justified |
| Medium (2-10x testing cost) | Moderate testing justified |
| Low (<2x testing cost) | Light testing, focus on deployment speed |
| Negative | Skip formal testing, learn from production |

**Examples:**

**Discipline skill (data safety):**
- Risk: 0.7 (agent often skips validation)
- Frequency: 50 uses/month
- Impact: $10k average (data loss, recovery time)
- Testing cost: 4 hours × $100/hr = $400
- Testing value: (0.7 × 50 × $10k) - $400 = $349,600
- **Recommendation: FULL TDD absolutely justified**

**Reference skill (command syntax):**
- Risk: 0.2 (agent usually finds info)
- Frequency: 5 uses/month
- Impact: $50 (small time waste)
- Testing cost: 1 hour × $100/hr = $100
- Testing value: (0.2 × 5 × $50) - $100 = -$50
- **Recommendation: Skip formal testing, deploy and observe**

## Implementation Checklist

**Synthesized from all approaches + additions:**

### For HIGH-RISK Skills (Discipline, Breaking Changes)

**RED Phase:**
- [ ] Create 3+ pressure scenarios (discipline) OR application scenarios (technique)
- [ ] Combine stressors: time + sunk cost + authority
- [ ] Run WITHOUT skill, document behavior verbatim
- [ ] Capture rationalizations exactly
- [ ] Identify 2+ specific patterns
- [ ] Understand WHY skill needed

**GREEN Phase:**
- [ ] Name: `verb-object` or `verbing-object`, letters-numbers-hyphens only
- [ ] Description: "Use when [symptoms] - [what + how]", third person, <1024 chars
- [ ] Keywords throughout: errors, symptoms, tools
- [ ] SKILL.md structure follows template
- [ ] Overview: Core principle + when NOT to use
- [ ] Quick Start: Inline example
- [ ] Red Flags section (for discipline)
- [ ] Rationalization Table (from baseline testing)
- [ ] Token budget: Body <500 lines
- [ ] Run same scenarios WITH skill
- [ ] Measure compliance/success rate >80%

**REFACTOR Phase:**
- [ ] Run 2+ additional varied scenarios
- [ ] Document new rationalizations
- [ ] Add explicit counters
- [ ] Re-test until compliance >90%
- [ ] No new rationalization patterns in last 2 scenarios

**Quality Checks:**
- [ ] Persuasion principles: Authority + Commitment + Social Proof (if discipline)
- [ ] Ethical check: Serves user's genuine interests?
- [ ] Cultural check: Language appropriate?
- [ ] Flowchart only if non-obvious decision
- [ ] References one level deep
- [ ] Validation/feedback section included

**Deployment:**
- [ ] Version metadata added
- [ ] Tested on target models (Haiku/Sonnet/Opus)
- [ ] Integration tested with existing skill collection
- [ ] Commit with descriptive message
- [ ] Set up periodic review schedule

### For MEDIUM-RISK Skills (Techniques, Major Additions)

- [ ] Create 3-5 application scenarios
- [ ] Cover main use case + 1-2 edge cases + 1 failure case
- [ ] Optional: Establish baseline
- [ ] Write skill addressing gaps
- [ ] Name and description optimized (per CSO)
- [ ] Structure follows template (technique variation)
- [ ] Persuasion: Moderate Authority + Unity
- [ ] Token budget: <500 lines body
- [ ] Validate: Success rate >85%
- [ ] Test across target models
- [ ] Version metadata added
- [ ] Commit and deploy

### For LOW-RISK Skills (Small Additions, Reference)

- [ ] Create 1-2 validation scenarios
- [ ] Test: Agent uses info correctly
- [ ] Name and description optimized
- [ ] Structure: Quick Reference prominent
- [ ] Persuasion: None (clarity only)
- [ ] Scenarios pass
- [ ] Commit and deploy

### For MINIMAL-RISK Changes (Typos, Formatting)

- [ ] Review change for correctness
- [ ] Commit with clear message

## Recommended Actions for AEGIS Project

**Based on synthesis + your specific context:**

### Priority 1: Create "Working with ARCHON" Skill

**Type:** Technique + Reference hybrid

**Testing:** Moderate (3-5 scenarios)

**Scenarios:**
1. NCP validation workflow
2. Knowledge graph querying (L0-L3 traversal)
3. Thematic coherence checking
4. Narrative Director usage
5. Failure case: Misunderstanding NCP structure

**Structure:**
```
working-with-archon/
├── SKILL.md (overview, quick start, workflows)
├── reference/
│   ├── ncp-schema.md (NCP structure details)
│   ├── knowledge-graph.md (Hypergraph levels L0-L3)
│   └── narrative-director.md (Agent workflows)
```

**Persuasion:** Moderate Authority (established patterns) + Unity (collaborative writing)

**CSO:**
```yaml
name: working-with-archon
description: Use when working with ARCHON narrative coherence framework, NCP validation, knowledge graph queries, or thematic checking - guides usage of Narrative Context Protocol, hierarchical hypergraph (L0-L3), and Narrative Director agent for maintaining story coherence. Keywords: ARCHON, NCP, narrative coherence, knowledge graph, thematic validation, Dramatica.
```

### Priority 2: Create "Zettelkasten Agent Workflow" Skill

**Type:** Technique

**Testing:** Moderate (3-5 scenarios)

**Scenarios:**
1. Creating and linking notes
2. Extracting concepts from source material
3. Traversing knowledge graph
4. Building on existing note network
5. Failure case: Breaking link structure

**Structure:**
```
zettelkasten-agent-workflow/
└── SKILL.md (self-contained)
```

**Persuasion:** Moderate Authority + Unity

**CSO:**
```yaml
name: zettelkasten-agent-workflow
description: Use when creating notes, linking concepts, or building knowledge graphs with Zettelkasten Agent - provides patterns for note creation, concept extraction, bidirectional linking, and knowledge traversal using fast-agents framework. Keywords: Zettelkasten, note-taking, knowledge graph, linking, concept extraction, fast-agents.
```

### Priority 3: Unified Skill Authoring Guide (Meta-Skill)

**Type:** Discipline (meta-level)

**Testing:** Full TDD (this IS discipline enforcement + this document is the basis)

**Approach:**
1. Use THIS synthesis document as foundation
2. Add pressure scenarios for skill authors
3. Test: Do authors skip testing? Rationalize? Use wrong approach for skill type?
4. Create streamlined guide combining:
   - writing-skills rigor (proportional)
   - Anthropic pragmatism (progressive disclosure)
   - Persuasion principles (conscious use)
   - Graphviz (when appropriate)
   - Blind spot fixes (observability, lifecycle, etc.)

**Structure:**
```
skill-authoring/
├── SKILL.md (overview, decision trees, quick reference)
├── reference/
│   ├── testing-framework.md (RED-GREEN-REFACTOR detail)
│   ├── cso-optimization.md (CSO patterns)
│   ├── persuasion-patterns.md (Ethical framework)
│   ├── structure-templates.md (By skill type)
│   └── graphviz-conventions.md (Visual DSL)
```

**Persuasion:** Heavy Authority (TDD for high-stakes) + Commitment (checklists) + Social Proof (research-backed)

**CSO:**
```yaml
name: skill-authoring
description: Use when creating or editing skills - unified framework combining TDD rigor (RED-GREEN-REFACTOR), progressive disclosure, CSO optimization, and ethical persuasion principles with proportional testing by risk level. Keywords: skill authoring, TDD, testing, progressive disclosure, CSO, persuasion principles, skill types.
```

## Next Steps

### Immediate (This Session)

1. **Review this synthesis document**
   - Does it address your needs?
   - Any major disagreements or gaps?
   - Ready to proceed with implementation?

2. **Choose priority**
   - Working with ARCHON skill?
   - Zettelkasten Agent Workflow skill?
   - Unified Skill Authoring Guide?
   - Something else?

3. **Begin RED phase** (if creating skill)
   - Define scenarios
   - Establish baseline
   - Document failures

### Short-term (Next Few Sessions)

4. **Implement chosen priority**
   - Complete TDD cycle or moderate testing
   - Create skill structure
   - Deploy and test

5. **Create second priority skill**

6. **Iterate based on real usage**

### Long-term (Over Time)

7. **Build skill collection for AEGIS project**
   - ARCHON workflows
   - Kohärenz Protokoll writing patterns
   - Zettelkasten operations
   - Research and analysis patterns

8. **Maintain and evolve**
   - Periodic reviews (quarterly)
   - Update based on model changes
   - Deprecate obsolete skills

9. **Contribute back (optional)**
   - Share ARCHON skill patterns with narrative community?
   - Contribute unified framework if broadly useful?

## Summary

This unified framework:
✅ Combines rigor (writing-skills) with pragmatism (Anthropic)
✅ Uses persuasion principles consciously and ethically
✅ Provides clear decision criteria and stopping conditions
✅ Addresses all major blind spots (observability, lifecycle, multi-agent, cost-benefit)
✅ Maintains flexibility via skill-type taxonomy and proportional rigor
✅ Integrates graphviz appropriately
✅ Optimized for Claude search (CSO)
✅ Progressive disclosure for token efficiency
✅ Ready for immediate application to AEGIS project

**Ready to proceed?**
