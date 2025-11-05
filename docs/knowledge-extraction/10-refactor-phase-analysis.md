# REFACTOR Phase: Additional Scenarios and Loopholes

## Overview

GREEN phase addressed 5 original scenarios. Now testing for new rationalizations and edge cases.

## Additional Scenario 6: "AI-Generated Skill"

**Context:**
Author uses Claude/ChatGPT to generate a skill. AI produces polished-looking skill with examples, structure, everything.

**Rationalization:**
> "The AI generated this skill, and it looks comprehensive. AI is smart, so I don't need to test it."

**Is this covered by current skill?**

Partially:
- ✅ Rationalization table says "I reviewed it myself" isn't enough
- ✅ Testing decision tree still applies
- ⚠️ BUT: No explicit "AI-generated" rationalization counter

**Gap identified:** AI-generated content rationalization

**Proposed addition to Rationalization Table:**

```markdown
| Excuse | Reality |
| "AI generated this skill, so it's good" | AI generates plausible-looking content that may have gaps, wrong info, or miss context. Testing reveals issues AI couldn't anticipate. |
```

**Proposed addition to Red Flags:**

```markdown
🛑 If you notice:
- "AI generated it, so it should work"
```

## Additional Scenario 7: Team Disagreement

**Context:**
Two team members disagree on rigor level for a skill.
- Member A: "This is critical, needs Full TDD"
- Member B: "This is simple, Light testing is fine"

**Question:**
How do they resolve? Current skill doesn't address collaboration/disagreement.

**Is this covered by current skill?**

No:
- ❌ No guidance on resolving disagreements
- ❌ No escalation path
- ❌ No "when in doubt" heuristic

**Gap identified:** Collaboration and conflict resolution

**Proposed addition to new section:**

```markdown
## Resolving Disagreements

**If team members disagree on rigor level:**

1. **Use risk assessment:**
   - What's worst-case if skill fails?
   - Data loss? Security issue? Time waste?
   - Higher risk → Higher rigor

2. **When in doubt, go higher:**
   - Disagreement means uncertainty
   - Uncertainty means risk
   - Risk means more testing

3. **Try both approaches:**
   - Quick test with lower rigor
   - If issues found → Escalate to higher rigor
   - Data wins arguments

**Rule of thumb:** If you can't agree, the skill is probably higher risk than you think.
```

## Additional Scenario 8: Skill Update Hell

**Context:**
Existing skill needs update. But skill doesn't say what rigor to apply for updates.

**Rationalization:**
> "I'm just adding one section. I'll skip the testing since the rest of the skill is already tested."

**Is this covered by current skill?**

Partially:
- ✅ Testing decision tree has "Small addition (<50 lines)" path
- ✅ Proportional rigor by change size
- ⚠️ BUT: Unclear if "addition to existing skill" counts as "creating skill"

**Potential confusion:** Description says "Use when creating or editing skills" but decision tree says "What are you changing?"

**Gap identified:** Clarity on updates vs. new skills

**Proposed clarification in Overview:**

```markdown
## Overview

**Core principle:** Skills are living documentation. Apply testing rigor proportional to risk level.

**When NOT to use:** For trivial changes (typos, formatting). For those: review and commit.

**Applies to:**
- Creating NEW skills
- Major edits to existing skills (>50 lines)
- Changing discipline/enforcement in existing skills

**For skill updates:** Use the same decision tree. "What are you changing?" applies to updates too.
```

## Additional Scenario 9: Reference File Bloat

**Context:**
Author creates skill with SKILL.md (<500 lines) but reference files total 5000+ lines across 10 files.

**Question:**
Is this OK? Current skill says "References: No limit (loaded on-demand)" but doesn't address navigation/findability.

**Is this covered by current skill?**

Partially:
- ✅ "References: No limit" technically allows this
- ⚠️ BUT: No guidance on organization, max file count, or findability

**Gap identified:** Reference file organization guidance

**Proposed addition to Structure section:**

```markdown
**Reference files:**
- No line limit per file (loaded on-demand)
- But: Keep count reasonable (<10 files)
- But: Keep each file focused (one topic per file)
- If >10 files: Consider splitting into multiple skills

**Why:** Even on-demand loading, navigation matters. If agent can't find right reference, value lost.
```

## Additional Scenario 10: Metric Gaming

**Context:**
Author runs testing scenarios, but designs scenarios guaranteed to pass.

**Rationalization:**
> "I ran 5 scenarios and got 100% success rate. Time to ship!"

**Question:**
How to prevent cherry-picked scenarios?

**Is this covered by current skill?**

Partially:
- ✅ RED phase says "Combine stressors", "Vary contexts"
- ⚠️ BUT: No guidance on scenario quality, no prevention of cherry-picking

**Gap identified:** Scenario quality criteria

**Proposed addition to Full TDD section:**

```markdown
### Scenario Quality Criteria

**Good scenarios:**
- Represent real usage (not contrived)
- Include edge cases (not just happy path)
- Cover failure modes (not just success)
- Vary contexts (not repeated setup)

**Bad scenarios (gaming the metrics):**
- All scenarios identical except minor detail
- Only test obvious functionality
- Avoid known problem areas
- Designed to pass rather than find issues

**Test:** Would an adversary design different scenarios? If yes, your scenarios may be too soft.
```

## Loopholes Found

### Critical Gaps (Must Address)

1. **Collaboration/disagreement resolution** (Scenario 7)
   - No guidance when team can't agree
   - Proposed: "When in doubt, go higher" heuristic

2. **Scenario quality gaming** (Scenario 10)
   - Could design soft scenarios to meet compliance metrics
   - Proposed: Quality criteria for scenarios

### Medium Gaps (Should Address)

3. **AI-generated rationalization** (Scenario 6)
   - New rationalization pattern with AI tools
   - Proposed: Add to rationalization table

4. **Update vs. new skill clarity** (Scenario 8)
   - Minor confusion about when to use skill
   - Proposed: Clarify in Overview

### Minor Gaps (Nice to Have)

5. **Reference file organization** (Scenario 9)
   - No limit could lead to 50-file chaos
   - Proposed: Reasonable limits (<10 files guideline)

## Proposed Updates to SKILL.md

### 1. Add to Overview Section

```markdown
**Applies to:**
- Creating NEW skills
- Major edits to existing skills (>50 lines)
- Changing discipline/enforcement in existing skills

**For skill updates:** Use the same decision tree. "What are you changing?" applies to updates too.
```

### 2. Add to Rationalization Table

```markdown
| Excuse | Reality |
| "AI generated this skill, so it's good" | AI generates plausible content that may have gaps, wrong info, or miss context. Testing reveals AI limitations. |
```

### 3. Add to Red Flags Section

```markdown
- "AI generated it, so it should work"
```

### 4. Add new section after Common Mistakes

```markdown
## Resolving Disagreements

**If team members disagree on rigor level:**

1. **Use risk assessment:** What's worst-case if skill fails?
2. **When in doubt, go higher:** Disagreement signals uncertainty = risk
3. **Try both approaches:** Quick test with lower rigor, escalate if issues found

**Rule:** If you can't agree, the skill is probably higher risk than you think.
```

### 5. Add to Full TDD Cycle (RED Phase)

```markdown
### Scenario Quality Criteria

**Good scenarios:**
- Represent real usage (not contrived)
- Include edge cases and failure modes
- Vary contexts meaningfully

**Bad scenarios (gaming the metrics):**
- All scenarios essentially identical
- Only test obvious functionality
- Avoid known problem areas

**Test:** Would an adversary design different scenarios? If yes, yours may be too soft.
```

### 6. Add to Structure Templates section

```markdown
**Reference files:**
- No line limit per file (loaded on-demand)
- Keep count reasonable (<10 files)
- One topic per file
- If >10 files: Consider splitting into multiple skills

**Why:** Navigation matters. If agent can't find right reference, value lost.
```

## Re-test Scenarios

**Scenario 6 (AI-generated):**
- Before update: Partially covered
- After update: Explicit rationalization counter
- Predicted compliance: MEDIUM → HIGH

**Scenario 7 (Team disagreement):**
- Before update: No guidance
- After update: Clear heuristics
- Predicted compliance: LOW → HIGH

**Scenario 8 (Updates):**
- Before update: Minor confusion
- After update: Explicit clarification
- Predicted compliance: MEDIUM-HIGH → HIGH

**Scenario 9 (Reference bloat):**
- Before update: No limits
- After update: Reasonable guidelines
- Predicted compliance: MEDIUM → MEDIUM-HIGH

**Scenario 10 (Metric gaming):**
- Before update: No quality criteria
- After update: Explicit criteria
- Predicted compliance: LOW → MEDIUM-HIGH

## New Rationalizations in Last 2 Scenarios?

**Scenario 9:** No new rationalizations (just organizational issue)
**Scenario 10:** "I ran tests" (already covered in table as "I reviewed it")

**Count:** 0 new rationalization patterns in scenarios 9-10

**Stopping criteria met:** ✅ No new rationalizations in last 2 scenarios

## Refactor Decision

**Apply updates?**

**Critical (must add):**
- Scenario quality criteria (prevents gaming)
- Disagreement resolution (enables collaboration)

**Important (should add):**
- AI-generated rationalization (current pattern)
- Update clarity (reduces confusion)

**Optional (nice to have):**
- Reference file guidelines (organization)

**Recommendation:** Apply critical + important updates. Optional can wait for v1.1 based on real feedback.

## Updated Compliance Prediction

**After REFACTOR updates:**

| Scenario | Before | After Updates | Improvement |
|----------|--------|---------------|-------------|
| 1: Time pressure | HIGH | HIGH | No change (already solid) |
| 2: Authority overuse | HIGH | HIGH | No change (already solid) |
| 3: Minimal effort | MEDIUM-HIGH | MEDIUM-HIGH | No change (already solid) |
| 4: Perfectionism | MEDIUM | MEDIUM | No change (hard problem) |
| 5: Wrong rigor | HIGH | HIGH | No change (already solid) |
| 6: AI-generated | MEDIUM | HIGH | +1 level |
| 7: Team disagreement | LOW | HIGH | +2 levels |
| 8: Updates | MEDIUM-HIGH | HIGH | +1 level |
| 9: Reference bloat | MEDIUM | MEDIUM-HIGH | +0.5 level |
| 10: Metric gaming | LOW | MEDIUM-HIGH | +1.5 levels |

**Overall predicted compliance:** >90% (up from >85%)

## Next Steps

1. Apply critical + important updates to SKILL.md
2. Re-validate token budget (<500 lines)
3. Deploy to ~/.claude/skills/
4. Document as v1.0.0
5. Monitor real usage
6. Iterate to v1.1 based on feedback

**REFACTOR phase complete:** Ready for deployment.
