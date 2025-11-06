# Ship-Learn-Next: Mastering Claude Code Skills

**Created:** 2025-11-06
**Source:** How-to-Use-Skills-Guide.md
**Quest Duration:** 3 weeks
**Framework:** Extract → Plan → Ship → Learn → Next

---

## Core Learning Objectives

**What you'll master:**
1. Understanding how auto-loaded skills work in `.claude/skills/`
2. Triggering skills naturally through context
3. Creating custom skills using the skill-authoring framework
4. Testing skills with proportional rigor
5. Integrating skills into your daily workflow

**Why this matters:**
Skills are the most powerful way to enhance Claude's capabilities for your specific project needs - but only if you know how to use them effectively.

---

## Quest: Become a Skill Power User

**Mission:** Go from "what's a skill?" to confidently using and creating skills in your AEGIS workflow.

**Success criteria:**
- ✅ Successfully trigger 3+ different skills in natural workflow
- ✅ Create 1 custom skill following the authoring framework
- ✅ Test your skill with appropriate rigor
- ✅ Integrate skill usage into daily work
- ✅ Understand when to create a new skill vs. use existing ones

---

## Rep 1: Trigger Existing Skills (This Week)

**Goal:** Experience how skills activate automatically through natural usage.

**Shippable outcome:** Successfully trigger and use 3 different existing skills.

### Tasks:

#### Task 1.1: Trigger archon-writer skill
```
Action: Ask Claude to help you write a scene
Example: "Help me write scene 1.4"

What to observe:
- Does archon-writer activate?
- What guidance do you receive?
- How does it enhance your workflow?

Success: You receive scene guidance and understand the flow
```

#### Task 1.2: Trigger codex skill
```
Action: Work on narrative content that involves characters
Example: "Is this dialogue correct for Lex?" or "Validate this scene"

What to observe:
- Does codex skill activate?
- Character voice validation works?
- Coherence checking helpful?

Success: You get character-specific feedback
```

#### Task 1.3: Trigger coherence-enforcer skill
```
Action: Request a project audit
Example: "Can you audit the project for duplication?"

What to observe:
- Does coherence-enforcer activate?
- What audit findings do you get?
- How thorough is the analysis?

Success: You receive coherence audit report
```

**Weekly checkpoint:**
- [ ] Triggered 3+ skills successfully
- [ ] Understand activation patterns
- [ ] Can recognize when skills are active

**Time investment:** 3-4 hours

---

## Rep 2: Read Skill Implementation (Week 2)

**Goal:** Understand how skills are structured by reading existing skill code.

**Shippable outcome:** Deep understanding of skill anatomy.

### Tasks:

#### Task 2.1: Anatomy study
```
Files to read:
1. /home/user/aegis/.claude/skills/archon-writer.md
2. /home/user/aegis/.claude/skills/coherence-enforcer.md
3. /home/user/aegis/skills/skill-authoring/SKILL.md

Questions to answer:
- How are skills structured (frontmatter, sections)?
- What makes a good skill description?
- How are keywords used for discoverability?
- What testing was applied?
```

#### Task 2.2: Compare skill types
```
Create a comparison table:

| Skill | Type | Testing Rigor | Persuasion Level | Key Sections |
|-------|------|---------------|------------------|--------------|
| archon-writer | ? | ? | ? | ? |
| coherence-enforcer | ? | ? | ? | ? |

Answer: What patterns emerge?
```

#### Task 2.3: CSO optimization analysis
```
Pick one skill. Analyze its CSO:
- Description formula: Does it follow "Use when [triggers]"?
- Keywords: Are they strategic?
- Discoverability: Could you improve it?

Document findings.
```

**Weekly checkpoint:**
- [ ] Read 3+ skill implementations
- [ ] Understand skill structure
- [ ] Can identify skill type and testing rigor
- [ ] Know what makes good CSO

**Time investment:** 4-5 hours

---

## Rep 3: Create Your First Custom Skill (Week 3)

**Goal:** Ship a working custom skill following the authoring framework.

**Shippable outcome:** 1 tested skill saved to `.claude/skills/`

### Tasks:

#### Task 3.1: Identify a need
```
Questions:
- What repetitive guidance do you give Claude?
- What domain knowledge is missing?
- What workflow could be enhanced?

Examples:
- "Git commit message style guide"
- "AEGIS documentation structure validator"
- "Zettelkasten note-taking assistant"

Choose ONE small, focused skill idea.
```

#### Task 3.2: Determine skill type
```
Use the taxonomy from skill-authoring:
- Discipline? (enforce critical practice)
- Technique? (guide implementation)
- Pattern? (mental model)
- Reference? (API/docs)

Your skill: _____________
Type: _____________
Testing rigor: _____________
```

#### Task 3.3: RED phase - Establish baseline (if technique/discipline)
```
1. Create 2-3 pressure scenarios
2. Test WITHOUT your skill (fresh Claude session)
3. Document failure modes
4. Understand WHY skill is needed

Note: Skip this for reference skills (use retrieval testing instead)
```

#### Task 3.4: GREEN phase - Write minimal skill
```
Structure:
---
name: your-skill-name
description: Use when [triggers] - [what it does]. Keywords: X, Y, Z.
---

# Your Skill Name

## Overview
[Core principle]

## When to Use
[Specific triggers and symptoms]

## Quick Start
[Minimal example]

[Add other sections as needed]

Save to: /home/user/aegis/.claude/skills/your-skill-name.md
```

#### Task 3.5: Test and refine
```
1. Run same scenarios WITH skill loaded
2. Measure success rate
3. Identify new issues
4. Refine until adequate

Success criteria:
- Technique: >85% success rate
- Reference: Can find + apply correctly
```

**Weekly checkpoint:**
- [ ] Identified skill need
- [ ] Determined skill type
- [ ] Established baseline (if needed)
- [ ] Written and tested skill
- [ ] Saved to `.claude/skills/`

**Time investment:** 6-8 hours

---

## Rep 4: Integrate into Daily Workflow (Week 4)

**Goal:** Make skill usage second nature.

**Shippable outcome:** 1 week of daily work using skills naturally.

### Tasks:

#### Task 4.1: Morning skill check
```
Daily ritual:
1. What am I working on today?
2. Which skills might help?
3. What contexts will trigger them?

Document: Which skills activated each day
```

#### Task 4.2: Track skill effectiveness
```
For each skill usage:
- Did it activate when expected?
- Was the guidance helpful?
- What could be improved?

Keep a simple log.
```

#### Task 4.3: Iterate your custom skill
```
Based on usage:
- Does it trigger correctly?
- Is guidance accurate?
- Are there new failure modes?
- Does CSO need improvement?

Update and re-test if needed.
```

**Weekly checkpoint:**
- [ ] Used skills daily for 1 week
- [ ] Tracked effectiveness
- [ ] Iterated on your custom skill
- [ ] Skills feel natural, not forced

**Time investment:** 30 min/day for 7 days (~3-4 hours)

---

## Rep 5: Advanced Skill Creation (Week 5)

**Goal:** Master advanced skill patterns and testing.

**Shippable outcome:** 1 advanced skill with full TDD cycle OR comprehensive skill documentation audit.

### Tasks (Choose path A or B):

#### Path A: Advanced Skill with Full TDD

```
Create a discipline skill (enforces critical practice):

1. Full RED phase
   - 3+ pressure scenarios with stressors
   - Document baseline failures verbatim
   - Identify 2+ specific patterns

2. Full GREEN phase
   - Write skill addressing ONLY baseline failures
   - Test with skill loaded
   - Achieve >80% compliance

3. Full REFACTOR phase
   - Run 2+ additional scenarios
   - Document new rationalizations
   - Add explicit counters
   - Re-test until >90% compliance

4. Apply persuasion ethically
   - Necessity check
   - Ethical test
   - Cultural check
   - Document decisions
```

#### Path B: Comprehensive Skill Audit

```
Audit all existing skills in `.claude/skills/`:

1. For each skill:
   - [ ] CSO optimized?
   - [ ] Keywords strategic?
   - [ ] Testing adequate for type?
   - [ ] Persuasion appropriate?
   - [ ] Structure follows templates?
   - [ ] Token budget reasonable?

2. Create improvement plan:
   - Priority 1: Critical issues
   - Priority 2: Optimization opportunities
   - Priority 3: Nice-to-haves

3. Implement 2-3 high-priority improvements
```

**Weekly checkpoint:**
- [ ] Completed either Path A or B
- [ ] Documented process and learnings
- [ ] Can teach skill creation to others

**Time investment:** 8-10 hours

---

## Quest Completion Checklist

**By end of Week 5, you should:**

- [x] ✅ Understand how auto-loaded skills work
- [x] ✅ Successfully trigger skills naturally in workflow
- [x] ✅ Create at least 1 custom skill
- [x] ✅ Test with appropriate rigor
- [x] ✅ Integrate skills into daily work
- [x] ✅ Know when to create new skills vs. use existing
- [x] ✅ Understand advanced patterns (TDD, CSO, persuasion)

---

## Reflection Questions

**After completing the quest:**

1. **What surprised you about skills?**
   - Were they easier or harder to use than expected?
   - What activation patterns did you notice?

2. **What skill had the biggest impact?**
   - Why was it so helpful?
   - How did it change your workflow?

3. **What skill would you create next?**
   - What gap does it fill?
   - What testing rigor would you apply?

4. **How has your understanding evolved?**
   - What misconceptions did you have initially?
   - What would you teach someone else?

---

## Resources

**Essential reading:**
- `/home/user/aegis/How-to-Use-Skills-Guide.md` (this guide)
- `/home/user/aegis/skills/skill-authoring/SKILL.md` (creation framework)
- `/home/user/aegis/.claude/skills/README.md` (available skills)

**Reference materials:**
- `/skills/skill-authoring/reference/cso-optimization.md`
- `/skills/skill-authoring/reference/persuasion-patterns.md`
- `/skills/skill-authoring/reference/structure-templates.md`
- `/skills/skill-authoring/reference/testing-framework.md`

**Example skills:**
- `/home/user/aegis/.claude/skills/archon-writer.md`
- `/home/user/aegis/.claude/skills/coherence-enforcer.md`
- `/home/user/aegis/.claude/skills/codex.md`

---

## Ship-Learn-Next Framework Applied

**Ship:** Create a working skill (Rep 3)
**Learn:** Understand through usage and iteration (Reps 1-4)
**Next:** Master advanced patterns (Rep 5)

**Extract:** Key insights from How-to-Use-Skills-Guide.md
**Plan:** This 5-rep progressive learning quest
**Action:** Complete each rep, building mastery incrementally

---

## Success Metrics

Track your progress:

| Rep | Goal | Success Criteria | Status |
|-----|------|------------------|--------|
| 1 | Trigger existing skills | 3+ skills activated | ⬜ |
| 2 | Understand structure | Read + analyze 3+ skills | ⬜ |
| 3 | Create custom skill | 1 tested skill shipped | ⬜ |
| 4 | Daily integration | 1 week consistent usage | ⬜ |
| 5 | Advanced mastery | Full TDD OR comprehensive audit | ⬜ |

**Overall progress:** 0/5 reps complete

---

## Commitment

**When will you complete Rep 1?**

Rep 1 is achievable this week. It takes 3-4 hours and gives you immediate value.

**What's your commitment?**

I will complete Rep 1 by: _______________

**Accountability:**
- [ ] Schedule time on calendar
- [ ] Block distractions
- [ ] Set success criteria
- [ ] Review progress weekly

---

**Ready to start?**

Begin with Rep 1, Task 1.1: Trigger the archon-writer skill.

Simply say: "Help me write scene 1.4" (or any scene number)

Observe what happens. That's the first step to mastery.

---

**Document Status:** Ready for Action
**Next Step:** Begin Rep 1
