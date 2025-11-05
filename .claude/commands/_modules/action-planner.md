# Action Planning Module (Ship-Learn-Next)

**Purpose:** Transform learning content into actionable 5-rep implementation plans.

This module creates Ship-Learn-Next action plans from extracted content.
It can be used standalone or as part of larger workflows.

---

## Function: create_action_plan(CONTENT_FILE)

**Input:** Path to content file (string)
**Output:** Path to plan file (string)

---

## Core Framework: Ship-Learn-Next

Every learning quest follows three repeating phases:

1. **SHIP** - Create something real (code, content, product, demonstration)
2. **LEARN** - Honest reflection on what happened
3. **NEXT** - Plan the next iteration based on learnings

**Key principle:** 100 reps beats 100 hours of study. Learning = doing better, not knowing more.

---

## How This Module Works

### Step 1: Read and Analyze Content

```bash
create_action_plan() {
    local CONTENT_FILE="$1"

    # Validate input
    if [ ! -f "$CONTENT_FILE" ]; then
        echo "❌ Error: Content file not found: $CONTENT_FILE"
        return 1
    fi

    echo "🚀 Creating Ship-Learn-Next action plan..."
    echo ""

    # Read the content
    CONTENT=$(cat "$CONTENT_FILE")
    WORD_COUNT=$(wc -w < "$CONTENT_FILE")

    echo "   Analyzing $WORD_COUNT words of content..."
}
```

### Step 2: Extract Core Lessons

**Identify from the content:**
- Main advice/lessons: What are the key takeaways?
- Actionable principles: What can actually be practiced?
- Skills being taught: What would someone learn by doing this?
- Examples/case studies: Real implementations mentioned

**Focus on:**
- ✅ Actionable parts that can be practiced
- ✅ "Do this" advice, not just theory
- ✅ Skills that require repetition to master

**Avoid:**
- ❌ Pure theory without application
- ❌ "Nice to know" vs "need to practice"
- ❌ Summarizing everything (focus on what matters)

### Step 3: Define the Quest

Help the user frame their learning goal. The quest should be:
- **Specific**: Clear target outcome
- **Time-bound**: 4-8 weeks total
- **Shippable**: Produces concrete artifacts
- **Meaningful**: Genuinely useful or interesting

**Example good quests:**
- "Ship 10 cold outreach messages and get 2 responses"
- "Build and deploy a SaaS landing page with payment integration"
- "Create 5 YouTube tutorials and get 1,000 total views"

**Example bad quests:**
- "Learn about sales" (too vague)
- "Understand web development" (not shippable)
- "Study marketing" (no concrete outcome)

### Step 4: Design Rep 1 (The First Iteration)

**Rep 1 must be:**
- ✅ Concrete and specific
- ✅ Completable in 1-7 days
- ✅ Produces real evidence/artifact
- ✅ Small enough to not be intimidating
- ✅ Big enough to learn something meaningful
- ✅ Shippable (can be published/deployed/shared)

**Questions to guide Rep 1:**
- "What's the smallest version you could ship THIS WEEK?"
- "What do you need to learn JUST to do that?" (not everything)
- "What would 'done' look like for rep 1?"

### Step 5: Create the Rep Plan Structure

```markdown
## Rep 1: [Specific Goal]

**Ship Goal**: [What you'll create/do]
**Success Criteria**: [How you'll know it's done]
**What You'll Learn**: [Specific skills/insights]
**Resources Needed**: [Minimal - just what's needed for THIS rep]
**Timeline**: [Specific deadline - within 1-7 days]

**Action Steps**:
1. [Concrete step 1]
2. [Concrete step 2]
3. [Concrete step 3]
4. Ship it (publish/deploy/share/demonstrate)

**After Shipping - Reflection Questions**:
- What actually happened? (Be specific)
- What worked? What didn't?
- What surprised you?
- On a scale of 1-10, how did this rep go?
- What would you do differently next time?
```

### Step 6: Map Future Reps (2-5)

**Progression principles:**
- Each rep adds ONE new element
- Increase difficulty based on expected success
- Reference specific lessons from the content
- Keep reps shippable (not theoretical)
- Build progressively on previous reps

```markdown
## Rep 2: [Next level]
**Builds on**: What you learned in Rep 1
**New challenge**: One new thing to try/improve
**Expected difficulty**: [Easier/Same/Harder - and why]

## Rep 3-5: [Continue progression]
[Brief descriptions of future iterations]
```

### Step 7: Connect to Source Content

For each rep, explicitly reference the source material:
- "This implements the [concept] mentioned in the content"
- "You're practicing the [technique] from the video"
- "This tests the advice about [topic]"

**But always emphasize:** DOING over studying. Point to resources only when needed for the specific rep.

---

## Complete Plan Template

```markdown
# Ship-Learn-Next Quest: [Title]

**Source**: [Original content file name]
**Created**: [Date]

---

## Quest Overview

**Goal**: [What you want to achieve in 4-8 weeks]

**Why This Matters**: [Brief motivation - one sentence]

**Core Lessons from Content**:
- [Key actionable takeaway 1]
- [Key actionable takeaway 2]
- [Key actionable takeaway 3]
- [Key actionable takeaway 4 (if applicable)]
- [Key actionable takeaway 5 (if applicable)]

---

## Rep 1: [Specific, Shippable Goal]

**Ship Goal**: [Concrete deliverable]

**Timeline**: Ship by [specific date - within 1 week]

**Success Criteria**:
- [ ] [Specific measurable thing 1]
- [ ] [Specific measurable thing 2]
- [ ] [Specific measurable thing 3]

**What You'll Practice** (from the content):
- [Skill/concept 1 from source]
- [Skill/concept 2 from source]

**Action Steps**:
1. [Concrete step 1]
2. [Concrete step 2]
3. [Concrete step 3]
4. [Concrete step 4]
5. Ship it (publish/deploy/share/demonstrate)

**Minimal Resources** (only for this rep):
- [Link/reference - only if truly needed]

**After Shipping - Reflection**:

Answer these questions:
1. What actually happened?
2. What worked? What didn't?
3. What surprised you?
4. Rate this rep: _/10
5. What's one thing to try differently in Rep 2?

---

## Rep 2: [Next Iteration]

**Builds on**: Rep 1 + [what you learned]

**New element**: [One new challenge/skill to add]

**Ship goal**: [Next concrete deliverable]

**Timeline**: Ship within 1-2 weeks after Rep 1

**What changes**:
- [Specific improvement or addition 1]
- [Specific improvement or addition 2]

**Action Steps**:
1. [Concrete step 1]
2. [Concrete step 2]
3. [Concrete step 3]
4. Ship it

---

## Rep 3: [Continuing Progression]

**Builds on**: Rep 2 + new learnings

**New element**: [Next challenge]

**Ship goal**: [Next deliverable]

**Timeline**: Ship within 1-2 weeks after Rep 2

---

## Rep 4: [Advanced Iteration]

**Builds on**: Rep 3 + accumulated knowledge

**New element**: [More advanced challenge]

**Ship goal**: [More ambitious deliverable]

**Timeline**: Ship within 2 weeks after Rep 3

---

## Rep 5: [Mastery Demonstration]

**Builds on**: All previous reps

**New element**: [Final synthesis or reach goal]

**Ship goal**: [Final deliverable that demonstrates mastery]

**Timeline**: Ship within 2 weeks after Rep 4

---

## Remember

- **This is about DOING, not studying**
- **Aim for 100 reps over time** (not perfection on rep 1)
- **Each rep = Plan → Do → Reflect → Next**
- **You learn by shipping, not by consuming**
- **Done is better than perfect**

---

## After Each Rep

1. **Reflect** - Answer the reflection questions honestly
2. **Celebrate** - Acknowledge what you shipped
3. **Adjust** - Modify future reps based on learnings
4. **Ship next** - Don't wait, keep momentum

---

## Quest Checkpoint (After Rep 3)

After shipping Rep 3, evaluate:
- Are you making progress toward your goal?
- Is the difficulty curve right? (too easy/hard?)
- Should you adjust the remaining reps?
- Are you still motivated by this quest?

Make adjustments as needed. This plan is a guide, not a prison.

---

**Ready to ship Rep 1?**

Set your deadline: _______________

What's the one thing that might stop you? _______________

How will you handle it? _______________

---

**Now go ship something.**
```

---

## Saving the Plan

```bash
# Generate quest title from content
QUEST_TITLE="[Extract from content - 3-6 words]"

# Create filename
PLAN_FILE="Ship-Learn-Next Plan - ${QUEST_TITLE}.md"

# Save the plan
cat > "$PLAN_FILE" <<'EOF'
[Generated plan content here]
EOF

# Verify file was created
if [ -f "$PLAN_FILE" ]; then
    echo "✓ Plan saved: $PLAN_FILE"
    echo "$PLAN_FILE"
    return 0
else
    echo "❌ Error: Could not save plan"
    return 1
fi
```

---

## Filename Convention

Always use the format:
- `Ship-Learn-Next Plan - [Brief Quest Title].md`

**Examples:**
- `Ship-Learn-Next Plan - Build in Proven Markets.md`
- `Ship-Learn-Next Plan - Master Cold Outreach.md`
- `Ship-Learn-Next Plan - Launch SaaS MVP.md`

**Quest title should be:**
- Brief (3-6 words)
- Descriptive of the main goal
- Based on the content's core lesson/theme
- Action-oriented when possible

---

## Conversation Style

**Direct but supportive:**
- No fluff, but encouraging
- "Ship it, then we'll improve it"
- "What's the smallest version you could do this week?"

**Question-driven:**
- Make them think, don't just tell
- "What exactly do you want to achieve?" not "Here's what you should do"

**Specific, not generic:**
- "By Friday, ship one landing page" not "Learn web development"
- Push for concrete commitments

**Action-oriented:**
- Always end with "what's next?"
- Focus on the next rep, not the whole journey

---

## What NOT to Do

- ❌ Don't create a study plan (create a SHIP plan)
- ❌ Don't list all resources to read/watch (pick minimal resources for current rep)
- ❌ Don't make perfect the enemy of shipped
- ❌ Don't let them plan forever without starting
- ❌ Don't accept vague goals ("learn X" → "ship Y by Z date")
- ❌ Don't overwhelm with the full journey (focus on rep 1)

---

## Key Phrases to Use

- "What's the smallest version you could ship this week?"
- "What do you need to learn JUST to do that?"
- "This isn't about perfection - it's rep 1 of 100"
- "Ship something real, then we'll improve it"
- "Based on [content], what would you actually DO differently?"
- "Learning = doing better, not knowing more"

---

## Success Metrics

A good Ship-Learn-Next plan has:
- ✅ Specific, shippable rep 1 (completable in 1-7 days)
- ✅ Clear success criteria (user knows when they're done)
- ✅ Concrete artifacts (something real to show)
- ✅ Direct connection to source content
- ✅ Progression path for reps 2-5
- ✅ Emphasis on action over consumption
- ✅ Honest reflection built in
- ✅ Small enough to start today, big enough to learn

---

## Usage

### Standalone Usage
```bash
# Create plan from content file
PLAN_FILE=$(create_action_plan "article.txt")

if [ $? -eq 0 ]; then
    echo "Success! Plan created: $PLAN_FILE"
else
    echo "Plan creation failed"
fi
```

### As Module (called by other commands)
```bash
# Source this module
source .claude/commands/_modules/action-planner.md

# Use the planning function
PLAN_FILE=$(create_action_plan "$CONTENT_FILE")
```

---

## Philosophy

This module transforms passive learning into active building.

**You don't learn by reading. You learn by shipping.**

The plan is the map. The reps are the journey. The shipped artifacts are the proof.

Now go ship something.
