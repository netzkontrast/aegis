---
name: skill-authoring
description: Use when creating or editing skills, before writing implementation - applies proportional rigor by risk level, preventing common failures like skipping testing, wrong persuasion, poor discoverability. Combines TDD discipline with pragmatic efficiency. Keywords: skill authoring, TDD, testing, CSO, persuasion, skill types, discipline, technique, reference.
---

# Skill Authoring: Unified Framework

## Overview

**Core principle:** Skills are living documentation. Apply testing rigor proportional to risk level.

**When NOT to use:** For trivial changes (typos, formatting). For those: review and commit.

**Applies to:**
- Creating NEW skills
- Major edits to existing skills (>50 lines)
- Changing discipline/enforcement in existing skills

**For skill updates:** Use the same decision tree. "What are you changing?" applies to updates too.

## When to Use

**Symptoms:**
- Creating a new skill
- Making substantial edits to existing skill (>50 lines)
- Unsure what testing rigor to apply
- Wondering if skill needs testing

**Use this skill to:**
- Choose right testing approach for skill type
- Apply persuasion principles ethically
- Optimize discoverability (CSO)
- Avoid common failure modes

## Quick Start: Testing Decision Tree

```
What are you changing?
  ↓
Typo or formatting only?
  YES → Review and commit
  NO ↓
  ↓
Small addition (<50 lines)?
  YES → Light testing (1-2 scenarios)
  NO ↓
  ↓
New discipline skill OR breaking change?
  YES → Full TDD (RED-GREEN-REFACTOR)
  NO ↓
  ↓
Major addition OR technique skill?
  YES → Moderate testing (3-5 scenarios)
  NO ↓
  ↓
Reference skill?
  YES → Retrieval testing (can find + apply?)
```

## Skill Type Taxonomy

**Use this table to determine approach:**

| Type | Purpose | Testing Rigor | Persuasion Level | Key Sections |
|------|---------|---------------|------------------|--------------|
| **Discipline** | Enforce critical practice | Full TDD | Authority + Commitment + Social Proof | Red Flags, Rationalization Table |
| **Technique** | Guide implementation | Moderate (3-5 scenarios) | Moderate Authority + Unity | Workflows, Examples, Checklists |
| **Pattern** | Mental model | Recognition testing | Unity + light Authority | Before/After, When to Apply |
| **Reference** | API/command docs | Retrieval testing | None (clarity only) | Quick Reference Table |

## Full TDD Cycle (For High-Risk Skills)

**Use when:** Creating discipline skill, breaking change, safety-critical

### RED Phase - Establish Baseline

**You MUST complete these steps:**

1. **Create pressure scenarios**
   - Minimum 3 scenarios
   - For discipline: Combine stressors (time + sunk cost + authority)
   - For technique: Vary contexts (different inputs, edge cases)

   **Scenario quality criteria:**
   - ✅ Represent real usage (not contrived)
   - ✅ Include edge cases and failure modes
   - ✅ Vary contexts meaningfully
   - ❌ Avoid: All scenarios essentially identical
   - ❌ Avoid: Only testing obvious functionality
   - ❌ Avoid: Designed to pass rather than find issues

   **Test:** Would an adversary design different scenarios? If yes, yours may be too soft.

2. **Run without skill**
   - Fresh Claude instance
   - Document behavior verbatim
   - Capture exact rationalizations

3. **Analyze patterns**
   - Identify 2+ specific failure modes
   - Understand WHY skill needed

**Stopping criteria:**
- ✅ 3+ scenarios documented
- ✅ Verbatim behaviors captured
- ✅ 2+ patterns identified
- ✅ Understand root cause

### GREEN Phase - Write Minimal Skill

**You MUST address ONLY the failures from RED. Do not add hypothetical content.**

1. **Create skill structure** (see Templates section)

2. **Apply CSO optimization:**
   - Description: "Use when [specific triggers] - [what + how]"
   - Keywords throughout
   - Third person voice

3. **Run same scenarios WITH skill**
   - Fresh instance with skill loaded
   - Measure compliance/success rate

**Stopping criteria:**
- ✅ All scenarios show improved behavior
- ✅ Compliance >80% (discipline) OR success >90% (technique)
- ✅ Addresses all major gaps from baseline
- ✅ No new confusions introduced

### REFACTOR Phase - Close Loopholes

1. **Run 2+ additional varied scenarios**

2. **Identify new rationalizations**
   - Document verbatim

3. **Add explicit counters**
   - Update rationalization table
   - Add to red flags list

4. **Re-test until adequate**

**Stopping criteria:**
- ✅ 5+ total unique scenarios
- ✅ Compliance >90%
- ✅ No NEW rationalizations in last 2 scenarios
- ✅ Rationalization table complete

## Moderate Testing (For Medium-Risk Skills)

**Use when:** Creating technique skill, major addition (50-200 lines)

**Steps:**

1. Create 3-5 application scenarios
   - Main use case
   - 1-2 edge cases
   - 1 "could go wrong" case

2. Optional: Establish baseline
   - Run WITHOUT skill
   - Document gaps

3. Write skill addressing gaps

4. Validate with scenarios
   - Success rate >85%
   - Agent finds and applies correctly

5. Test across models (if targeting multiple)
   - Haiku: Enough guidance?
   - Sonnet: Efficient?
   - Opus: Too verbose?

**Stopping criteria:**
- ✅ 3+ scenarios pass
- ✅ Success rate >85%
- ✅ Tested on target models

## Light Testing (For Low-Risk Skills)

**Use when:** Small addition (<50 lines), minor updates

**Steps:**

1. Create 1-2 scenarios covering the change

2. Validate behavior
   - Agent uses info correctly
   - No confusion introduced

**Stopping criteria:**
- ✅ Scenarios pass
- ✅ No obvious issues

## CSO (Claude Search Optimization)

**Description formula:**

```yaml
description: Use when [symptom1, symptom2, symptom3] - [what it does]. [How it helps]. Keywords: X, Y, Z.
```

**Requirements:**
- Start with "Use when" (condition-first)
- Include 3-5 specific symptoms/triggers
- Error messages, behaviors, contexts
- Technology-agnostic by default (unless skill is tech-specific)
- Third person voice
- Max 1024 chars
- Explicit keywords list

**Name formula:**
- `verb-object` OR `verbing-object`
- Letters, numbers, hyphens only
- Examples: `creating-skills`, `condition-based-waiting`, `working-with-archon`

**Keyword placement:**
- Throughout SKILL.md, not just description
- Overview section: Repeat key terms
- When to Use: Specific searchable phrases
- Quick Reference: Tool names, commands
- Common Mistakes: Error messages verbatim

**For details:** See [reference/cso-optimization.md](reference/cso-optimization.md)

## Persuasion Principles (Use Consciously)

**Before using heavy Authority/Commitment, check:**

1. ✅ **Necessity:** Is compliance critical? (safety, correctness, discipline)
2. ✅ **Ethical test:** Serves user's genuine interests if they understood?
3. ✅ **Cultural check:** Language appropriate for user culture?
4. ✅ **Transparency:** Consider disclosing persuasion use

**Graduated scale:**

| Skill Type | Level | Example Language |
|------------|-------|------------------|
| **Reference** | None | "See reference.md for details" |
| **Technique** | Light | "Consider using X when Y" |
| **Guidance** | Moderate | "Use X for Y. Avoid Z." |
| **Discipline** | Strong | "YOU MUST X. No exceptions: [list]" |

**Principle combinations by type:**

| Type | Use | Avoid |
|------|-----|-------|
| **Discipline** | Authority + Commitment + Social Proof | Liking, Reciprocity |
| **Technique** | Moderate Authority + Unity | Heavy Authority |
| **Pattern** | Unity + light Authority | Authority (heavy) |
| **Reference** | None | All persuasion |

**For details:** See [reference/persuasion-patterns.md](reference/persuasion-patterns.md)

## Structure Templates

**Token budgets:**
- SKILL.md body: <500 lines
- Frequently-loaded skills: <200 words total
- References: No limit (loaded on-demand)

**Progressive disclosure:**
- Keep references ONE level deep
- Split when approaching 500 lines
- Quick start inline, advanced topics linked

**For complete templates by type:** See [reference/structure-templates.md](reference/structure-templates.md)

## Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|--------------|-----|
| Skipping testing entirely | Untested skills have issues. Always. | Apply proportional testing by risk level |
| Same rigor for all skills | Over-testing wastes time, under-testing creates failures | Use skill-type taxonomy |
| Heavy Authority everywhere | Compliance fatigue, sycophancy | Match persuasion to skill type |
| No ethical check for persuasion | Manipulation risk, user trust erosion | Run necessity + ethical + cultural checks |
| Monolithic SKILL.md (2000+ lines) | Blows token budget, hard to navigate | Progressive disclosure, <500 lines body |
| Over-explaining fundamentals | Assumes Claude is ignorant | "Claude is already smart" - add only new context |
| Poor discoverability | Skill exists but Claude can't find it | CSO optimization: keywords, triggers, symptoms |
| Never shipping (perfectionism) | Perfect is enemy of good | Ship when "good enough for skill type" |

## Resolving Disagreements

**If team members disagree on rigor level:**

1. **Use risk assessment:** What's worst-case if skill fails?
   - Data loss? Security issue? Major time waste?
   - Higher risk → Higher rigor

2. **When in doubt, go higher:**
   - Disagreement signals uncertainty
   - Uncertainty signals risk
   - Risk means more testing

3. **Try both approaches:**
   - Quick test with lower rigor
   - If issues found → Escalate to higher rigor
   - Data wins arguments

**Rule of thumb:** If you can't agree on rigor level, the skill is probably higher risk than you think.

## Red Flags - STOP and Assess

🛑 **If you notice any of these, PAUSE and consult decision tree:**

- Writing skill without testing plan
- "I don't have time to test"
- "It's just documentation, not code"
- "AI generated it, so it should work"
- Using same process for all skill types
- Heavy Authority without ethical check
- SKILL.md approaching 500+ lines
- "I need to add just one more section..."
- Explaining what async/promises/etc. mean (Claude knows)
- Multiple examples in 5+ languages

**All of these mean:** STOP. Assess skill type. Apply proportional rigor. Check stopping criteria.

## Rationalization Table

**From baseline testing, these excuses ALL fail:**

| Excuse | Reality |
|--------|---------|
| "Testing is for code, not documentation" | Documentation can be wrong, unclear, incomplete. Testing reveals issues. |
| "I reviewed it myself, that's good enough" | Authors have blind spots. Testing with fresh context reveals gaps. |
| "AI generated this skill, so it's good" | AI generates plausible content that may have gaps, wrong info, or miss context. Testing reveals AI limitations. |
| "It's just a reference list" | Reference skills can have poor discoverability, missing info, wrong commands. |
| "More authority = more compliance" | Over-use creates fatigue. Calibrated persuasion is more effective. (Research: Meincke et al., 2025) |
| "It's for their own good, ethics don't apply" | Ethics require user's informed consent and genuine interests, not just author judgment. |
| "I don't have time to test" | Untested skills fail in production, causing MORE time waste later. Test now or debug later. |
| "I'll test later / fix issues as they come" | "Later" rarely happens. Issues compound. Testing up-front prevents this. |
| "One-size-fits-all is simpler" | Wrong rigor wastes time (over-testing simple) or creates failures (under-testing critical). |
| "More comprehensive = better" | Verbose skills blow token budgets. Concise + progressive disclosure is more effective. |
| "I need to cover all edge cases before shipping" | Perfect is enemy of good. Ship when "good enough for skill type". Iterate based on usage. |

## Validation

**Periodic review (quarterly for critical skills):**

1. Sample 10 random sessions using your skills
2. Measure:
   - Skills found when needed? (discovery rate)
   - Skills followed correctly? (compliance rate for discipline, success rate for technique)
   - New failure modes observed?
3. If discovery rate <80% OR compliance rate <80%:
   - Update CSO (better keywords, triggers)
   - Update persuasion (close new loopholes)
   - Re-test

**For newly created skills:**
- Test within first week of deployment
- Review 3-5 actual usage sessions
- Update based on real behavior

## Advanced Topics

**Detailed guidance:**
- **Testing framework:** See [reference/testing-framework.md](reference/testing-framework.md)
- **CSO optimization:** See [reference/cso-optimization.md](reference/cso-optimization.md)
- **Persuasion patterns:** See [reference/persuasion-patterns.md](reference/persuasion-patterns.md)
- **Structure templates:** See [reference/structure-templates.md](reference/structure-templates.md)
- **Lifecycle management:** See [reference/lifecycle-management.md](reference/lifecycle-management.md)

---

**Meta:**
- Version: 1.0.0
- Based on: Synthesis of writing-skills + Anthropic + persuasion + graphviz
- Token budget: Body 495 lines (within limit)
- Last tested: 2025-11-05
- Models tested: Sonnet 4.5
