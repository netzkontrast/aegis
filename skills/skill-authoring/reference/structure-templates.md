# Structure Templates by Skill Type

## Overview

Different skill types need different structures. Use these templates as starting points, adapt to your specific needs.

**Token budgets:**
- SKILL.md body: <500 lines
- Frequently-loaded skills: <200 words total
- References: No limit (loaded on-demand)

## Universal SKILL.md Header

**All skills start with this:**

```markdown
---
name: skill-name-with-hyphens
description: Use when [specific triggers] - [what + how]. Keywords: X, Y, Z.
---

# Skill Name

## Overview
[Core principle in 1-2 sentences. When NOT to use.]

## When to Use

**Symptoms:**
- Specific symptom 1
- Specific symptom 2
- Specific symptom 3

**Contexts:**
- Context A
- Context B

[Small flowchart ONLY if decision is non-obvious]
```

After header, structure diverges by type.

## Discipline Skill Template

**Purpose:** Enforce critical practice (TDD, security, data safety)

**Testing:** Full TDD (RED-GREEN-REFACTOR)

**Persuasion:** Authority + Commitment + Social Proof

### Full Template

```markdown
---
name: discipline-skill-name
description: Use when [critical situation] - [what rule enforces]. [Why critical]. Keywords: safety, discipline, enforcement, [domain terms].
---

# Discipline Skill Name

## Overview

**Core principle:** [State the rule clearly and directly]

**When NOT to use:** [Explicit exceptions, if any]

## When to Use

**Symptoms:**
- [Critical failure mode 1]
- [Critical failure mode 2]
- [Warning sign 1]
- [Warning sign 2]

**This skill prevents:** [Specific bad outcome]

## The Rule

**YOU MUST [required action].**

**Before [event], you MUST:**
1. [Required step 1]
2. [Required step 2]
3. [Required step 3]

**No exceptions:**
- Not for [common excuse 1]
- Not for [common excuse 2]
- Not for [common excuse 3]

## Quick Start

[Minimal example showing correct application of rule]

```[language]
[Code or process example]
```

## Workflows (if multi-step)

**Copy this checklist and track progress:**

```
Task Progress:
- [ ] Step 1: [action] (MUST complete before Step 2)
- [ ] Step 2: [action] (MUST complete before Step 3)
- [ ] Step 3: [validation] (MUST pass before proceeding)
- [ ] Step 4: [action]
```

[Detailed steps with feedback loops]

## Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|--------------|-----|
| [Common violation 1] | [Consequence] | [Correct approach] |
| [Common violation 2] | [Consequence] | [Correct approach] |

## Red Flags - STOP and [Action]

🛑 **If you notice any of these, STOP immediately:**

- [Red flag 1]
- [Red flag 2]
- [Red flag 3]
- "[Quote common rationalization]"

**All of these mean:** [Required corrective action]

## Rationalization Table

**These excuses ALL fail:**

| Excuse | Reality |
|--------|---------|
| "[Common excuse 1]" | [Why it's wrong, with evidence if possible] |
| "[Common excuse 2]" | [Why it's wrong] |
| "[Common excuse 3]" | [Why it's wrong] |

## Validation (for critical skills)

**Periodic review ([frequency]):**

1. [How to check compliance]
2. [What metrics to measure]
3. If compliance <[threshold]%, [corrective action]

---

**Meta:**
- Version: X.Y.Z
- Token budget: Body <500 lines
- Last tested: [date]
```

### Example: TDD Enforcement Skill

```markdown
---
name: test-driven-development
description: Use when implementing features or fixing bugs, before writing implementation code - enforces RED-GREEN-REFACTOR cycle, preventing untested code from shipping. Keywords: TDD, testing, RED-GREEN-REFACTOR, test-first, discipline.
---

# Test-Driven Development

## Overview

**Core principle:** Test before code. Every time.

**When NOT to use:** Exploratory spikes (mark as `spike/` and delete after learning)

## When to Use

**Symptoms:**
- About to write implementation code
- About to fix a bug
- About to add a feature

## The Rule

**YOU MUST write the test first. No exceptions.**

**Before writing implementation:**
1. Write a test that fails (RED)
2. Write minimal code to pass (GREEN)
3. Refactor while keeping tests green (REFACTOR)

**No exceptions:**
- Not for "simple" features
- Not for "quick fixes"
- Not for "obvious" code
- Not because "I'll test after"

## Red Flags - STOP and Delete Code

🛑 **If you notice any of these, STOP and delete the code:**

- Implementation exists before test
- "I already manually tested it"
- "The code is too simple to test"
- "I'll write tests after"

**All of these mean:** Delete implementation. Start with failing test.

## Rationalization Table

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Writing test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing about design. |
| "I already manually tested" | Manual testing doesn't create regression suite. |
```

## Technique Skill Template

**Purpose:** Guide implementation approach (async patterns, API usage, workflows)

**Testing:** Moderate (3-5 scenarios)

**Persuasion:** Moderate Authority + Unity

### Full Template

```markdown
---
name: technique-skill-name
description: Use when [situation] - [what technique provides]. [How it helps]. Keywords: technique, pattern, [domain terms].
---

# Technique Name

## Overview

[Core principle in 1-2 sentences. When NOT to use.]

## When to Use

**Symptoms:**
- [Symptom 1]
- [Symptom 2]
- [Symptom 3]

**Use this technique when:**
- [Context A]
- [Context B]

**Don't use when:**
- [Exception 1]
- [Exception 2]

## Quick Start

[Inline example with minimal explanation]

```[language]
[Concrete, runnable example]
```

## Core Pattern

**Before (anti-pattern):**

```[language]
[Code showing wrong approach]
```

**After (recommended):**

```[language]
[Code showing right approach]
```

**Why this works:** [Brief explanation]

## Quick Reference

| Task | Pattern | Notes |
|------|---------|-------|
| [Task A] | `[code pattern]` | [When to use] |
| [Task B] | `[code pattern]` | [When to use] |
| [Task C] | `[code pattern]` | [When to use] |

## Workflows (if complex)

[Copyable checklist if multi-step]

**Step 1: [Action]**
[Detailed instructions]

**Step 2: [Action]**
[Detailed instructions]

[Include feedback loops: validate → fix → retry]

## Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|--------------|-----|
| [Mistake 1] | [Reason] | [Solution] |
| [Mistake 2] | [Reason] | [Solution] |

## Advanced Topics

**[Topic A]:** See [reference/topic-a.md](reference/topic-a.md)
**[Topic B]:** See [reference/topic-b.md](reference/topic-b.md)

---

**Meta:**
- Token budget: Body <500 lines
```

## Pattern Skill Template

**Purpose:** Mental model for recognizing when to apply approach

**Testing:** Recognition testing

**Persuasion:** Unity + light Authority

### Full Template

```markdown
---
name: pattern-name
description: Use when [recognition criteria] - [what pattern is]. [Mental model]. Keywords: pattern, [domain].
---

# Pattern Name

## Overview

[Core insight in 1-2 sentences.]

## When to Use

**Recognize this pattern when:**
- [Recognition signal 1]
- [Recognition signal 2]
- [Recognition signal 3]

**Don't use when:**
- [Anti-indication 1]
- [Anti-indication 2]

## Core Pattern

**Before (complex):**

[Example of complexity/problem]

**After (simplified):**

[Example of pattern applied]

**Key insight:** [Why this works]

## Recognition Guide

| If you see... | Consider... | Because... |
|---------------|-------------|------------|
| [Signal A] | [This pattern] | [Reason] |
| [Signal B] | [This pattern] | [Reason] |

## Examples

**Example 1: [Context]**

[Before/after comparison]

**Example 2: [Context]**

[Before/after comparison]

## Common Applications

- [Application domain 1]
- [Application domain 2]
- [Application domain 3]

---

**Meta:**
- Token budget: Body <500 lines
```

## Reference Skill Template

**Purpose:** API documentation, command reference, lookup tables

**Testing:** Retrieval testing

**Persuasion:** None (clarity only)

### Full Template

```markdown
---
name: reference-name
description: Use when [looking for X] - [what this documents]. [Coverage]. Keywords: reference, docs, API, [tool names].
---

# Reference Name

## Overview

[What this documents. Coverage scope.]

## Quick Start

[Minimal example of most common operation]

```[language]
[Code]
```

## Quick Reference

[Prominent table or organized list]

| Operation | Command/Code | Parameters | Notes |
|-----------|--------------|------------|-------|
| [Op 1] | `[syntax]` | [params] | [when to use] |
| [Op 2] | `[syntax]` | [params] | [when to use] |
| [Op 3] | `[syntax]` | [params] | [when to use] |

## Common Operations

**[Operation A]**

```[language]
[Code example]
```

[Brief explanation]

**[Operation B]**

```[language]
[Code example]
```

[Brief explanation]

## Advanced Topics

**[Topic A]:** See [reference/topic-a-details.md](reference/topic-a-details.md)
**[Topic B]:** See [reference/topic-b-details.md](reference/topic-b-details.md)

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| [Error 1] | [Why it happens] | [How to fix] |
| [Error 2] | [Why it happens] | [How to fix] |

---

**Meta:**
- Token budget: Body <500 lines
- API version: [if applicable]
```

### Example: kubectl Reference

```markdown
---
name: kubectl-reference
description: Use when managing Kubernetes resources, checking pod status, viewing logs, or troubleshooting deployments - provides kubectl command reference for common operations. Keywords: kubectl, Kubernetes, pods, deployments, services, logs, k8s.
---

# kubectl Command Reference

## Overview

Quick reference for common kubectl operations: pods, deployments, services, logs.

## Quick Start

```bash
# Get all pods
kubectl get pods

# View pod logs
kubectl logs pod-name

# Describe resource
kubectl describe pod pod-name
```

## Quick Reference

| Operation | Command | Notes |
|-----------|---------|-------|
| List pods | `kubectl get pods` | Add `-n namespace` for specific namespace |
| Pod details | `kubectl describe pod <name>` | Shows events and config |
| Pod logs | `kubectl logs <pod>` | Add `-f` to follow |
| Delete pod | `kubectl delete pod <name>` | Add `--force` if stuck |
| List deployments | `kubectl get deployments` | Shows replicas status |
| Scale deployment | `kubectl scale deployment <name> --replicas=N` | Updates desired count |

## Common Operations

[... examples ...]
```

## Progressive Disclosure Pattern

**When SKILL.md approaches 500 lines, split content:**

### Main SKILL.md (Keep Essential)

- Overview
- When to Use
- Quick Start
- Quick Reference
- Common operations (3-5 most used)
- Links to advanced topics

### reference/advanced-topic-a.md

- Deep dive into specific topic
- Extended examples
- Edge cases
- No line limit (loaded on-demand)

### reference/api-details.md

- Complete API reference
- All parameters
- All methods
- Comprehensive examples

**Linking pattern:**

```markdown
## Advanced Topics

**Topic A:** See [reference/topic-a.md](reference/topic-a.md)
**Topic B:** See [reference/topic-b.md](reference/topic-b.md)

For complete API: See [reference/api-details.md](reference/api-details.md)
```

**Keep references ONE level deep.** Don't nest references within references.

## Hybrid Skills

**Some skills combine types:**

Example: "Working with ARCHON" = Technique + Reference
- Technique part: Workflows for NCP validation
- Reference part: Schema structure, command reference

**Approach:**
- Main SKILL.md: Technique structure (workflows, patterns)
- reference/: Reference material (schemas, API details)
- Testing: Moderate (technique testing)
- Persuasion: Moderate Authority + Unity

## Adaptation Guidelines

**These are templates, not straitjackets:**

- ✅ Adapt section order if it improves flow
- ✅ Add sections for your domain needs
- ✅ Remove sections that don't apply
- ❌ Don't remove critical sections (e.g., Red Flags from discipline skills)
- ❌ Don't skip testing "because template is good"
- ❌ Don't violate token budgets

**The template exists to:**
- Prevent forgetting critical sections
- Provide structure for clarity
- Match expectations (users learn structure)

**Not to:**
- Replace thinking about your skill's specific needs
- Create cookie-cutter documentation
- Eliminate judgment calls

---

**When in doubt:** Start with template, adapt during GREEN phase, validate with testing.
