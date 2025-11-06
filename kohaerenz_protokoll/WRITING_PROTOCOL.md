# Writing Protocol for Kohärenz Protokoll
## Minimal Viable Workflow

**Purpose**: This protocol keeps you **writing**, not planning. Use ARCHON tools lightly—they're assistants, not gatekeepers.

**Core Principle**: If a tool interrupts creative flow, skip it. The prose is the priority.

---

## Pre-Scene Checklist (2-5 minutes)

### Option A: Automated (Recommended - NEW!)

Use the `/write-scene` command or just ask for instant guidance:

```bash
# In Claude Code, just ask:
"Help me write scene 1.4"
"What do I need for scene 1.4?"

# Or use the command:
/write-scene 4 1.4    # Specific scene
/write-scene 4        # Chapter overview
```

**This gives you:**
- ✅ Scene structure (goal/conflict/outcome)
- ✅ Active alter voices with dialogue samples
- ✅ Location sensory keywords (KW1-4)
- ✅ Prose style guidance for your Act
- ✅ Opening hook suggestions

**Time**: 2-3 minutes to review → Start writing immediately

---

### Option B: Manual (If You Prefer)

### 1. Query NCP Directly
```bash
# Scene-specific guidance:
python ARCHON/tools/ncp_assist.py --scene 1.4 --prompt --verbose

# Chapter overview:
python ARCHON/tools/ncp_assist.py --chapter 4 --prompt

# Character voice samples:
python ARCHON/tools/ncp_assist.py --character Lex --chapter 4 --voice-sample
```

### 2. Read Scene Outline
- **File**: `kohaerenz_protokoll/narrative_design/act_1_scenes.md`
- **Goal**: Know the scene's purpose, location, active alters
- **Don't**: Get lost in details—skim for essence

### 3. Set Prose Style Target
Based on where you are in the arc:
- **Chapters 1-3**: Maximum fragmentation
- **Chapters 4-7**: Emerging voices
- **Chapters 8-13**: Nascent polyphony

---

## During Scene: The Creative Zone

### 5. Write Without Interruption
- **Trust your instincts**: The alters' voices should flow naturally
- **Don't validate mid-draft**: Finish the scene before checking anything
- **Follow discoveries**: If a character does something unexpected, let them

### 6. Keep Reference Docs Open (But Don't Over-Consult)
- `PROJECT_CODEX.md` - for world physics questions only
- `system_kael.md` - for alter voice consistency
- `kernwelten/overview.md` - for Kernwelt sensory details

### 7. Trust the Internal Voices
- Let Lex provide precise measurements and logic
- Let Rhys bleed emotion into the prose
- Let Kiko intrude with fear at the right moments
- Let the alters **perform** themselves through the prose

---

## Post-Scene: Light Validation (10-15 minutes)

### 8. Read Aloud (Optional but Recommended)
- Does the prose rhythm match the psychological state?
- Are the fragments and intrusions landing as intended?
- Is the voice distinct from generic prose?

### 9. Validate Against NCP (Optional)
```bash
# In Claude Code, just ask:
"Can you validate scene 1.4?"

# Or run manually:
python ARCHON/tools/ncp_validate.py manuscript/act_1/chapter_N_scene_M.md --verbose
```
- **Fix**: Critical coherence breaks (plot contradictions, world physics violations)
- **Ignore**: Minor stylistic suggestions that would weaken the voice
- **Remember**: Validation is optional. Only use if you want feedback.

### 10. Reflect Briefly
- What worked well in this scene?
- What felt forced or artificial?
- Did ARCHON help or hinder?
- Note this in the writer's log (see below)

---

## Post-Chapter: Integration (20-30 minutes)

### 11. Update Character/World Docs If Needed
- Did you discover something new about an alter?
- Did the world physics evolve during writing?
- Add it to the relevant docs so future chapters stay consistent

### 12. Commit to Git
```bash
git add kohaerenz_protokoll/manuscript/act_1/chapter_N.md
git commit -m "feat(manuscript): Complete Chapter N - [Brief description]

- Scene descriptions
- Key character moments
- Thematic achievements

Reflection: [One sentence about what you learned]"
git push -u origin claude/aegis-project-reflection-011CUrJZyHbQbkkokmatDXVv
```

### 13. Writer's Log Entry
- **File**: `docs/writers_log.md`
- **Time**: 5-10 minutes of honest reflection
- **Questions**:
  - What helped? (Tools, docs, process)
  - What hindered? (Interruptions, over-planning)
  - What surprised you?
  - Is the prose style sustainable?

---

## Emergency Protocols

### If You Get Stuck:
1. **Don't consult tools**—walk away for 10 minutes
2. **Ask**: What does this scene *feel* like? Not what it's *about*.
3. **Try**: Write from a different alter's perspective
4. **Remember**: First drafts are supposed to be messy

### If ARCHON Feels Like a Burden:
1. **Ignore it completely for this scene**
2. **Write intuitively**
3. **Note the difference in your writer's log**
4. **This is valuable data**

### If You Lose the Voice:
1. **Re-read Chapter 1, Scene 1.1** to reconnect with the rhythm
2. **Remember**: Fragments are your friend
3. **Trust**: Parenthetical intrusions
4. **Perform**: Let the alters speak, don't describe them speaking

---

## Success Metrics

**You're succeeding if**:
- ✅ You're writing regularly (1 scene every 2-3 days)
- ✅ The prose *feels* like Kael's consciousness
- ✅ You're excited to discover what happens next
- ✅ ARCHON is helping, not blocking

**You're struggling if**:
- ⚠️ You spend more time planning than writing
- ⚠️ The prose feels generic or flat
- ⚠️ You're afraid to deviate from the plan
- ⚠️ Tools feel like gatekeepers instead of assistants

**When in doubt**: Write first, validate later.

---

## Weekly Rhythm

**Target**: 1 chapter per week (3-4 scenes, ~5,000-6,000 words)

**Monday**: Review week's chapter
- Run: `/write-scene <chapter>` for overview (2 min)
- Prep first scene: `/write-scene <chapter> <scene>` (2 min)

**Tuesday-Thursday**: Write 1 scene per day
- Morning: Get scene guidance (2 min)
- Write: 30-60 min uninterrupted
- Optional: Validate if desired (5 min)

**Friday**: Light revision, commit
**Weekend**: Rest, reflect, read what you've written

**End of Week**: Writer's log entry reflecting on the whole chapter

---

## The Golden Rule

> **The novel is the boss. ARCHON is the assistant.**

If a tool, document, or process doesn't serve the writing, **don't use it**.

If you discover something better than the plan, **follow the better path**.

If the prose demands you break a rule, **break the rule**.

The architecture exists to serve the story, not the other way around.

---

## Tools Quick Reference

### ARCHON Writing Assistant (NEW!)
When working in Claude Code, just ask naturally:
- **"Help me write scene 1.4"** → Full scene guidance
- **"What do I need for chapter 4?"** → Chapter overview
- **"How should Lex sound?"** → Character voice sample
- **"What's the style for Act I?"** → Prose style guide
- **"Validate scene 1.4"** → Post-writing validation

### Direct Tool Usage (Advanced)
```bash
# Scene prompts
python ARCHON/tools/ncp_assist.py --scene 1.4 --prompt --verbose

# Character voices
python ARCHON/tools/ncp_assist.py --character Lex --chapter 4 --voice-sample

# Style guidance
python ARCHON/tools/ncp_assist.py --chapter 4 --style-guide

# Validation
python ARCHON/tools/ncp_validate.py scene_file.md --verbose
```

### Slash Commands
```bash
/write-scene 4 1.4    # Get scene guidance
/write-scene 4        # Get chapter overview
```

---

*Protocol established: November 6, 2025*
*Updated: November 6, 2025 - Added ARCHON writing assistant integration*
*Principle: Write first, validate later, iterate always*
