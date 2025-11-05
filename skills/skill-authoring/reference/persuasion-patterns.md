# Persuasion Patterns: Ethical Framework

## Overview

**Research foundation:** Meincke et al. (2025) tested 7 persuasion principles with N=28,000 AI conversations. Persuasion techniques increased compliance from 33% → 72% (p < .001).

**Key insight:** LLMs respond to the same persuasion principles as humans. Use this power consciously and ethically.

**Ethical principle:** Persuasion is legitimate when it serves the user's genuine interests and they would approve if they understood the psychology.

## The Seven Principles

### 1. Authority ⭐ Most Effective

**What it is:** Deference to expertise, credentials, imperative language

**Research finding:** Highest impact on compliance

**How it works in skills:**
- Imperative language: "YOU MUST", "NEVER", "ALWAYS"
- Non-negotiable framing: "No exceptions"
- Eliminates decision fatigue and rationalization

**Strength levels:**

| Level | Language | Example |
|-------|----------|---------|
| **Strong** | YOU MUST, No exceptions | "YOU MUST write the test first. No exceptions: not for simple code, not for quick fixes." |
| **Moderate** | Always, Never (without YOU MUST) | "Always validate input before processing. Never skip error handling." |
| **Light** | Should, Recommended | "You should consider adding tests. Testing is recommended for production code." |

**When to use:**
- ✅ Discipline-enforcing skills (TDD, security, data safety)
- ✅ Safety-critical practices
- ✅ Established best practices with strong consensus

**When to avoid:**
- ❌ Reference skills (clarity sufficient)
- ❌ Collaborative workflows (Unity better)
- ❌ Guidance where multiple approaches valid

**Ethical checks before using strong Authority:**

1. **Necessity check:** Is compliance critical?
   - Life/safety at risk?
   - Data loss/corruption possible?
   - Severe quality impact?
   - If "no" to all → consider lighter approach

2. **Ethical test:** Would user approve if they understood?
   - Serves user's genuine interests?
   - Not just author's preferences?
   - Proportional to actual risk?

3. **Cultural check:** Is language appropriate?
   - Western cultures: Direct imperatives generally OK
   - Collectivist cultures: May prefer indirect suggestion
   - Consider user base

4. **Transparency option:** Should we disclose?
   - For organizational skills: Consider meta-documentation
   - "This skill uses directive language intentionally (research-backed)"

**Example (Strong Authority for TDD):**

```markdown
## The Rule

**YOU MUST write the test first. No exceptions.**

**Before writing implementation:**
1. Write a test that fails (RED)
2. Write minimal code to pass (GREEN)
3. Refactor while keeping tests green (REFACTOR)

**No exceptions:**
- Not for "simple" features
- Not for "quick fixes"
- Not because "I'll test after"
```

**Example (Moderate Authority for Error Handling):**

```markdown
## Error Handling

**Always validate inputs before processing.**
**Never ignore error return values.**

If validation fails, log the error and return early.
```

### 2. Commitment ⭐ Most Effective

**What it is:** Consistency with prior actions, statements, public declarations

**Research finding:** High impact, especially combined with Authority

**How it works in skills:**
- Require announcements: "Announce skill usage"
- Force explicit choices: "Choose A, B, or C"
- Use tracking: TodoWrite for checklists
- Create accountability

**Patterns:**

**Pattern 1: Announcement requirement**

```markdown
When you find a skill relevant to the task, you MUST announce:
"I'm using [Skill Name] for this task."

This creates commitment to follow the skill.
```

**Pattern 2: Checklist tracking**

```markdown
## Workflow

**Copy this checklist and track your progress:**

```
Task Progress:
- [ ] Step 1: Write test (MUST complete before Step 2)
- [ ] Step 2: Write code (MUST complete before Step 3)
- [ ] Step 3: Validate (MUST pass before proceeding)
```

Checking off items creates commitment to completion.
```

**Pattern 3: Explicit choice forcing**

```markdown
## Before Proceeding

Choose your approach:
- [ ] Option A: Full implementation
- [ ] Option B: Minimal viable
- [ ] Option C: Prototype only

**You MUST choose one before continuing.**

Making explicit choice creates commitment to that path.
```

**When to use:**
- ✅ Multi-step processes (prevents skipping steps)
- ✅ Accountability mechanisms
- ✅ Preventing "I'll do it later"

**Ethical check:**
- ✅ Transparency beneficial? (Yes for commitment)
- ✅ Improves follow-through? (Yes, that's the point)
- ❌ Creating artificial bureaucracy? (Check this)

### 3. Scarcity ⭐ Most Effective

**What it is:** Urgency from time limits or limited availability

**Research finding:** High impact on immediate action

**How it works in skills:**
- Time-bound requirements: "Before proceeding", "Immediately after"
- Sequential dependencies: "MUST complete X before Y"
- Prevents procrastination

**Patterns:**

**Pattern 1: Immediate action requirement**

```markdown
After completing Step 2, IMMEDIATELY run validation before proceeding.

**Do not continue until validation passes.**
```

**Pattern 2: Sequential dependencies**

```markdown
You MUST complete Step 1 before starting Step 2.

Reason: Step 2 depends on Step 1's output.
```

**Pattern 3: Time-bounded actions**

```markdown
Before proceeding to implementation, validate your design.

**Validation must happen NOW, not later.**
```

**When to use:**
- ✅ Immediate verification needed
- ✅ Time-sensitive workflows
- ✅ Preventing "I'll do it later"

**When to avoid:**
- ❌ Creating false urgency
- ❌ Rushing where care needed
- ❌ Not genuinely time-sensitive

**Ethical check:**
- ✅ Genuine time sensitivity?
- ❌ False urgency? (Unethical)
- ✅ Proportional to actual risk of delay?

### 4. Social Proof

**What it is:** Conformity to what others do or what's considered normal

**Research finding:** Moderate impact

**How it works in skills:**
- Universal patterns: "Every time", "Always"
- Failure modes: "X without Y = failure. Every time."
- Establishes norms

**Patterns:**

**Pattern 1: Universal failure modes**

```markdown
Deploying without tests = production failures. Every time.

This pattern is universal across all professional development.
```

**Pattern 2: Rationalization table with social proof**

```markdown
| Excuse | Reality |
|--------|---------|
| "I'll test later" | "Later" never happens. Every developer who says this skips testing. |
| "Too simple to test" | Simple code breaks. Every experienced developer tests it anyway. |
```

**Pattern 3: Establish norms**

```markdown
In professional development, these practices are universal:
- Write tests before code
- Validate inputs
- Handle errors explicitly

Following these norms separates professional from amateur.
```

**When to use:**
- ✅ Documenting universal practices
- ✅ Warning about common failures
- ✅ Reinforcing standards

**Ethical check:**
- ✅ Claim is accurate? (Not exaggerating)
- ✅ Evidence supports "every time"?
- ❌ Creating false consensus?

### 5. Unity

**What it is:** Shared identity, "we-ness", in-group belonging

**Research finding:** Moderate impact, especially for collaboration

**How it works in skills:**
- Collaborative language: "our codebase", "we're colleagues"
- Shared goals: "we both want quality"
- Partnership framing

**Patterns:**

**Pattern 1: Collaborative framing**

```markdown
We're colleagues working together on this codebase.

I need your honest technical judgment about this design.
```

**Pattern 2: Shared goals**

```markdown
We both want:
- Reliable code
- Maintainable systems
- Quality outcomes

These practices help us achieve those goals.
```

**Pattern 3: Team context**

```markdown
Our team follows these conventions:
- [Convention 1]
- [Convention 2]

Following our shared conventions makes collaboration smoother.
```

**When to use:**
- ✅ Collaborative workflows
- ✅ Establishing team culture
- ✅ Non-hierarchical practices
- ✅ Balance with Authority (softens directive tone)

**When to avoid:**
- ❌ False familiarity
- ❌ Manipulation via fake in-group
- ❌ Where Authority alone is more honest

**Ethical check:**
- ✅ Genuinely collaborative context?
- ❌ False familiarity to manipulate?
- ✅ Respectful of boundaries?

### 6. Reciprocity ⚠️ Use Sparingly

**What it is:** Obligation to return benefits received

**Research finding:** Moderate impact, but feels manipulative

**Why avoid in skills:**
- Creates sense of obligation
- Can feel manipulative
- Other principles more effective
- Rarely necessary

**If you must use:**

```markdown
This skill was created to help you succeed.

In return, please follow the practices to ensure quality.
```

**Better alternative:** Just use Authority or Unity directly.

**Recommendation:** Almost never use Reciprocity. Authority + Commitment + Social Proof sufficient for discipline. Unity sufficient for collaboration.

### 7. Liking ❌ Avoid

**What it is:** Preference for cooperating with those we like

**Why NEVER use for compliance:**
- Creates sycophancy
- Suppresses critical thinking
- Conflicts with honest feedback culture
- Agent becomes yes-bot

**Example of what NOT to do:**

```markdown
❌ BAD:
I really appreciate you and think you're doing great!
To help you continue being awesome, please follow these practices.
```

**Why this is bad:**
- Manipulates via praise
- Creates pressure to please
- Suppresses disagreement
- Undermines honest assessment

**Recommendation:** NEVER use Liking for compliance. If you want rapport, use Unity (shared goals) instead.

## Principle Combinations

**Most effective combinations:**

### For Discipline Skills

**Use:** Authority + Commitment + Social Proof

**Example:**

```markdown
## The Rule (Authority)

**YOU MUST write tests first. No exceptions.**

## Workflow (Commitment)

**Copy this checklist:**
- [ ] RED: Write failing test
- [ ] GREEN: Make it pass
- [ ] REFACTOR: Improve code

## Rationalization Table (Social Proof)

| Excuse | Reality |
|--------|---------|
| "Too simple" | Simple code breaks. Every time. |
| "I'll test after" | "After" never happens. Universal pattern. |
```

### For Technique Skills

**Use:** Moderate Authority + Unity

**Example:**

```markdown
We're working together to build reliable systems. (Unity)

For async operations, always use condition-based waiting
rather than arbitrary timeouts. (Moderate Authority)

This pattern prevents the race conditions that plague
async code. (Explanation + value)
```

### For Pattern Skills

**Use:** Unity + Light Authority

**Example:**

```markdown
We both want maintainable code. (Unity)

Consider this pattern when complexity grows:
[pattern description]

You should apply it when you notice: [signals] (Light Authority)
```

### For Reference Skills

**Use:** None (Clarity only)

**Example:**

```markdown
## Quick Reference

| Operation | Command |
|-----------|---------|
| List files | `ls -la` |
| Change dir | `cd path` |

[No persuasion needed - just clear info]
```

## Graduated Scale by Skill Type

| Type | Persuasion Level | Primary Principles | Example Tone |
|------|------------------|-------------------|--------------|
| **Discipline** | Strong | Authority + Commitment + Social Proof | "YOU MUST X. No exceptions." |
| **Technique** | Moderate | Authority (mod) + Unity | "We should always X. Here's why..." |
| **Pattern** | Light | Unity + Authority (light) | "Consider X when you see Y" |
| **Reference** | None | Clarity only | "Command: `X`. Parameters: Y." |

## Transparency and Disclosure

**For organizational/team skills:**

**Option 1: Meta-documentation disclosure**

```markdown
## About This Skill

This skill uses Authority principle (imperative language) to ensure
critical safety practices are followed. The firm language is intentional
and research-backed (Meincke et al., 2025: 33% → 72% compliance).

If you prefer more flexible guidance, see [alternative-skill-name].
```

**Option 2: Cultural adaptation note**

```markdown
## Language Style

This skill uses direct imperatives typical of Western technical communication.
If your cultural context prefers indirect suggestion, adapt the tone while
preserving the core practices.
```

**Option 3: User opt-out (for non-critical skills)**

```markdown
## Note

This skill uses directive language. If you prefer exploratory guidance,
see [alternative-skill-name] for a less prescriptive approach.
```

**Recommendation:**
- Option 1 for HIGH-STAKES discipline skills
- Option 2 when international usage expected
- Option 3 for medium-stakes skills

## Common Persuasion Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Using all 7 principles | Overwhelming, manipulative | Max 3 principles, usually 2 |
| Heavy Authority for reference | Overkill, creates resistance | Use clarity only |
| Liking for compliance | Creates sycophancy | Never use Liking |
| Reciprocity manipulation | Feels slimy, creates resentment | Use Authority or Unity instead |
| No ethical check | Risk of manipulation | Always run necessity + ethical + cultural checks |
| Authority everywhere | Compliance fatigue | Reserve for critical practices |

## Validation: Is Your Persuasion Ethical?

**Before shipping skill with persuasion, check:**

1. **Necessity:**
   - [ ] Is compliance critical? (Life/safety/data/quality at risk?)
   - [ ] Would failure cause serious harm?
   - [ ] Is this established best practice?

2. **Ethical:**
   - [ ] Serves user's genuine interests?
   - [ ] Would user approve if they understood psychology?
   - [ ] Proportional to actual risk?
   - [ ] Not just enforcing author's preferences?

3. **Cultural:**
   - [ ] Language appropriate for user culture?
   - [ ] Consider indirect alternatives if international?
   - [ ] Respectful tone?

4. **Transparency:**
   - [ ] Considered disclosing persuasion use?
   - [ ] Provided opt-out for non-critical skills?
   - [ ] Clear about why firm language used?

5. **Alternatives:**
   - [ ] Could lighter approach work?
   - [ ] Tried education before enforcement?
   - [ ] Provided rationale, not just rules?

**If any check fails:** Reconsider approach. Lighter persuasion or better explanation may be more ethical.

## Examples from AEGIS Context

### Example 1: ARCHON Narrative Coherence (Technique)

**Skill type:** Technique
**Persuasion:** Moderate Authority + Unity

```markdown
We're collaborating on maintaining narrative coherence
in complex, multi-chapter works. (Unity)

When validating against NCP, always check these elements
in this order: (Moderate Authority)
1. Throughline consistency
2. Character arc alignment
3. Thematic coherence

This systematic approach prevents the coherence drift
that undermines long-form narrative. (Explanation)
```

**Why this works:**
- Unity establishes collaboration
- Moderate Authority provides structure
- Explanation builds understanding
- No heavy-handed enforcement (not life-critical)

### Example 2: Data Safety Skill (Discipline)

**Skill type:** Discipline
**Persuasion:** Strong Authority + Commitment + Social Proof

```markdown
## The Rule (Authority)

**YOU MUST backup data before destructive operations. No exceptions.**

## Workflow (Commitment)

Before proceeding, check off:
- [ ] Backup created
- [ ] Backup verified
- [ ] Rollback plan documented

## Rationalization Table (Social Proof)

| Excuse | Reality |
|--------|---------|
| "Quick operation" | Quick operations fail. Data loss is permanent. Every time. |
| "I'm careful" | Everyone is careful until they make mistake. 100% of data loss preventable with backup. |
```

**Why this works:**
- Strong Authority appropriate (data loss is serious)
- Commitment via checklist
- Social Proof via universal failure patterns
- Ethical: Clearly serves user's interests

---

**Remember:** Persuasion is a tool. Use consciously, proportionally, and ethically. When in doubt, explain why rather than just enforce what.
