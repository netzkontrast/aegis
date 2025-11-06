# How to Use Skills in Claude Code

**Created:** 2025-11-06
**Topic:** Understanding and using Claude Code skills in the AEGIS project

---

## What Are Skills?

Skills are **custom capabilities** that enhance Claude's functionality for specific workflows. They're like specialized knowledge modules that Claude automatically loads when relevant context appears.

**Key insight:** Skills are NOT commands you invoke manually - they're **automatic enhancements** that activate when you're working on relevant tasks.

---

## Two Types of Skills in This System

### 1. Auto-Loaded Skills (`.claude/skills/`)

These skills are automatically available when you work with Claude Code. No manual activation required.

**Location:** `/home/user/aegis/.claude/skills/`

**Available skills:**
- `codex.md` - Narrative development for Kohärenz Protokoll
- `archon-writer.md` - Scene writing assistance
- `coherence-enforcer.md` - Project architecture maintenance
- `codex-zettelkasten.md` - Knowledge management integration
- `all-systems.md` - Comprehensive system reference

**How they work:**
- Claude automatically loads them from `.claude/skills/`
- They activate when relevant keywords/contexts appear
- Example: Mention "write scene" → `archon-writer` activates
- Example: Say "AEGIS dialogue" → `codex` skill activates

**No action needed:** Just work naturally, and skills activate when helpful.

---

### 2. Skill Tool Skills (Invoked Manually)

These are skills you explicitly invoke using the Skill tool.

**Current status:** No skills currently available via Skill tool in this project.

**How they would work (if available):**
```
Claude uses the Skill tool: Skill("pdf")
```

**Note:** The Skill tool's `<available_skills>` list is currently empty in this environment.

---

## How to Use Auto-Loaded Skills

### For Writing Scenes (archon-writer)

**Trigger phrases:**
- "Help me write scene X.Y"
- "I need writing guidance"
- "What should I know before writing this scene?"
- "ncp assist"

**What happens:**
1. Claude recognizes you're writing a scene
2. `archon-writer` skill activates automatically
3. You get scene guidance (structure, characters, prose style)
4. You write freely

**Example workflow:**
```
You: Help me write scene 1.4
Claude: *activates archon-writer skill*
        *provides scene guidance*

        📝 SCENE 1.4: The Drowning Pool
        🎬 STRUCTURE
        Goal: Kael discovers KW2...

        Ready to write? Open the file and start.
```

---

### For Narrative Coherence (codex)

**Trigger phrases:**
- Working on manuscript scenes
- Character dialogue creation
- "AEGIS dialogue"
- "validate this scene"
- Mentions of Kernwelt physics

**What happens:**
1. Claude recognizes narrative work
2. `codex` skill activates
3. You get coherence checking, character voice guidance
4. Validation against PROJECT_CODEX.md

**Use cases:**
- Writing/editing manuscript scenes
- Creating character dialogue
- Checking world physics consistency
- Resolving document conflicts

---

### For Project Maintenance (coherence-enforcer)

**Trigger phrases:**
- "audit the project"
- "check for duplication"
- "consolidate documentation"
- "orphaned files"
- "dead code"

**What happens:**
1. Claude recognizes maintenance request
2. `coherence-enforcer` skill activates
3. You get 4-phase audit (Audit → Analyze → Propose → Execute → Validate)

**Use cases:**
- Monthly maintenance audits
- Pre-release coherence checks
- Before adding new features
- When code feels fragmented

---

## How to Create New Skills

If you want to create your own skills, follow the **skill-authoring framework**:

**Documentation:** `/home/user/aegis/skills/skill-authoring/SKILL.md`

**Quick process:**

1. **Choose skill type:**
   - **Discipline** - Enforce critical practice (full TDD)
   - **Technique** - Guide implementation (moderate testing)
   - **Pattern** - Mental model (recognition testing)
   - **Reference** - API/command docs (retrieval testing)

2. **Apply testing rigor proportional to risk:**
   - High risk (discipline) → Full TDD
   - Medium risk (technique) → 3-5 scenarios
   - Low risk (reference) → Basic retrieval test

3. **Optimize for discoverability (CSO):**
   ```yaml
   ---
   name: skill-name
   description: Use when [triggers] - [what it does]. Keywords: X, Y, Z.
   ---
   ```

4. **Save to `.claude/skills/`:**
   - File: `/home/user/aegis/.claude/skills/your-skill.md`
   - Claude auto-loads on next session

**Key principles:**
- Skills are living documentation
- Apply testing rigor proportional to risk
- Use persuasion ethically (Authority only when critical)
- Keep SKILL.md body <500 lines

---

## Common Questions

### Q: How do I "activate" a skill?

**A:** You don't! Skills activate automatically when relevant context appears. Just work naturally.

### Q: How do I know if a skill is active?

**A:** Skills work silently in the background. You'll notice Claude providing specialized guidance without being asked.

### Q: Can I disable a skill?

**A:** Remove or rename the file in `.claude/skills/` (e.g., rename `codex.md` to `codex.md.disabled`).

### Q: What's the difference between skills and slash commands?

**A:**
- **Skills** = Passive knowledge/capabilities (auto-activate)
- **Slash commands** = Explicit workflows you invoke (e.g., `/learn`, `/tapestry`)

### Q: Where do I put a new skill?

**A:** `.claude/skills/` directory for auto-loading, OR create as a standalone skill package in `/skills/` directory.

---

## Examples of Skill Usage

### Example 1: Writing a Scene

```
You: I need to write scene 2.3 where Kael confronts Lex

Claude: *archon-writer activates silently*

I'll help you prepare for scene 2.3. Let me get the scene guidance...

*Runs ncp_assist.py*

📝 SCENE 2.3: The Confrontation
🎬 STRUCTURE
- Goal: Kael challenges Lex's control
- Conflict: Logic vs emotion, authority crisis
...

Ready to write?
```

**What happened:** Claude recognized "write scene" context and activated `archon-writer` skill automatically.

---

### Example 2: Checking Project Coherence

```
You: Can you audit the project for duplication?

Claude: *coherence-enforcer activates*

I'll run a comprehensive coherence audit...

**Phase 1: AUDIT**
Scanning for:
- Duplicate functionality
- Disconnected systems
- Orphaned documentation
...
```

**What happened:** "audit" + "duplication" triggered `coherence-enforcer` skill.

---

### Example 3: Validating Narrative Coherence

```
You: Is this dialogue correct for Lex?

"I understand you're upset, Kael, but maybe we should just accept it?"

Claude: *codex skill activates*

That dialogue doesn't match Lex's character voice. Let me check the voice matrix...

❌ Issues:
1. Lex uses logic, not empathy ("I understand you're upset")
2. Lex doesn't suggest acceptance, he enforces control
3. Missing characteristic speech patterns

✅ Corrected version:
"Control your emotional response. The data suggests..."
```

**What happened:** Character name + dialogue triggered `codex` skill for voice validation.

---

## Summary

**Key takeaways:**

1. ✅ Skills auto-load from `.claude/skills/` directory
2. ✅ No manual activation needed - they trigger on context
3. ✅ Current skills: codex, archon-writer, coherence-enforcer, etc.
4. ✅ Create new skills using `/skills/skill-authoring/SKILL.md` framework
5. ✅ Skills ≠ Commands (skills are passive, commands are explicit)

**Philosophy:** Skills make Claude smarter about your project without requiring you to remember special commands.

---

## Next Steps

Want to learn more about specific skills?

- **Writing scenes:** Read `/home/user/aegis/.claude/skills/archon-writer.md`
- **Creating skills:** Read `/home/user/aegis/skills/skill-authoring/SKILL.md`
- **Project coherence:** Read `/home/user/aegis/.claude/skills/coherence-enforcer.md`
- **Narrative work:** Read `/home/user/aegis/.claude/skills/codex.md`

**Ready to use skills:** Just start working! Skills activate automatically when you need them.

---

**Document Status:** Complete
**Next Action:** Start using skills naturally in your workflow
