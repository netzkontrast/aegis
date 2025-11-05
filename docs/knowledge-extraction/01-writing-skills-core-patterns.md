# Writing-Skills: Core Knowledge Patterns

## Source
TDD-focused skill authoring methodology

## Core Philosophy
**Skills ARE code** - Apply TDD rigor to documentation

## Key Patterns

### The Iron Law
```
NO SKILL WITHOUT A FAILING TEST FIRST
```
- Applies to NEW skills AND EDITS
- No exceptions (not for "simple additions", not for "just documentation")
- Delete untested changes immediately

### RED-GREEN-REFACTOR Cycle

**RED Phase - Write Failing Test:**
- Run pressure scenarios WITHOUT the skill
- Document baseline behavior verbatim
- Identify exact rationalizations agents use
- This proves the skill is needed

**GREEN Phase - Write Minimal Skill:**
- Address ONLY the specific failures from RED
- Don't add hypothetical content
- Run same scenarios WITH skill
- Verify agents now comply

**REFACTOR Phase - Close Loopholes:**
- Agent found new rationalization? Add explicit counter
- Build rationalization table from all iterations
- Create red flags list
- Re-test until bulletproof

### Skill Types & Testing Approaches

| Type | Examples | Test With | Success Criteria |
|------|----------|-----------|------------------|
| Discipline-enforcing | TDD, verification-before-completion | Pressure scenarios + combined stressors | Agent follows rule under maximum pressure |
| Technique | condition-based-waiting, root-cause-tracing | Application scenarios + variations | Agent applies technique correctly to new scenario |
| Pattern | reducing-complexity, information-hiding | Recognition + application scenarios | Agent identifies when/how to apply pattern |
| Reference | API docs, command references | Retrieval + application scenarios | Agent finds and correctly applies information |

### Bulletproofing Against Rationalization

**Close Every Loophole Explicitly:**
```markdown
Write code before test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete
```

**Address "Spirit vs Letter" Arguments:**
```markdown
**Violating the letter of the rules is violating the spirit of the rules.**
```

**Build Rationalization Table:**
Capture every excuse from baseline testing:

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |

**Create Red Flags List:**
```markdown
## Red Flags - STOP and Start Over
- Code before test
- "I already manually tested it"
- "Tests after achieve the same purpose"
- "This is different because..."

**All of these mean: Delete code. Start over with TDD.**
```

### Claude Search Optimization (CSO)

**Description Field:**
- Start with "Use when..." (triggering conditions)
- Include symptoms and situations
- Technology-agnostic unless skill is tech-specific
- Third person voice
- Max 1024 chars

**Keyword Coverage:**
- Error messages
- Symptoms (flaky, hanging, zombie, pollution)
- Synonyms
- Tool names

**Naming:**
- Active voice, verb-first
- Gerunds for processes (-ing)
- ✅ `creating-skills` not `skill-creation`

**Token Efficiency:**
- getting-started workflows: <150 words
- Frequently-loaded skills: <200 words
- Other skills: <500 words

### Directory Structure

**Flat namespace:**
```
skills/
  skill-name/
    SKILL.md              # Main reference (required)
    supporting-file.*     # Only if needed
```

**Separate files for:**
1. Heavy reference (100+ lines)
2. Reusable tools

**Keep inline:**
- Principles and concepts
- Code patterns (< 50 lines)
- Everything else

### SKILL.md Structure

```markdown
---
name: Skill-Name-With-Hyphens
description: Use when [specific conditions] - [what it does, third person]
---

# Skill Name

## Overview
What is this? Core principle in 1-2 sentences.

## When to Use
[Small inline flowchart IF decision non-obvious]

Bullet list with SYMPTOMS and use cases
When NOT to use

## Core Pattern (for techniques/patterns)
Before/after code comparison

## Quick Reference
Table or bullets for scanning

## Implementation
Inline code for simple patterns
Link to file for heavy reference/tools

## Common Mistakes
What goes wrong + fixes

## Real-World Impact (optional)
Concrete results
```

### Flowchart Usage

**Use flowcharts ONLY for:**
- Non-obvious decision points
- Process loops where you might stop too early
- "When to use A vs B" decisions

**Never use flowcharts for:**
- Reference material → Tables, lists
- Code examples → Markdown blocks
- Linear instructions → Numbered lists

### Anti-Patterns

❌ Narrative examples ("In session 2025-10-03...")
❌ Multi-language dilution (example-js.js, example-py.py, ...)
❌ Code in flowcharts
❌ Generic labels (helper1, step3)
❌ Creating multiple skills without testing each

### Mandatory Checklist (Per Skill)

**RED Phase:**
- [ ] Create pressure scenarios (3+ combined pressures)
- [ ] Run WITHOUT skill - document baseline verbatim
- [ ] Identify rationalization patterns

**GREEN Phase:**
- [ ] Name uses only letters, numbers, hyphens
- [ ] YAML frontmatter (name + description only)
- [ ] Description starts with "Use when..."
- [ ] Address specific baseline failures
- [ ] Run WITH skill - verify compliance

**REFACTOR Phase:**
- [ ] Identify NEW rationalizations
- [ ] Add explicit counters
- [ ] Build rationalization table
- [ ] Create red flags list
- [ ] Re-test until bulletproof

**Deployment:**
- [ ] Commit and push
- [ ] Consider PR if broadly useful

## Unique Strengths
- Extremely rigorous testing methodology
- Explicit focus on rationalization prevention
- Clear RED-GREEN-REFACTOR cycle
- Pressure scenario framework
- Bulletproofing techniques

## Potential Weaknesses
- Very strict (could be intimidating)
- Heavy process overhead for simple skills
- Assumes high-discipline enforcement needed
- May be overkill for reference-type skills
