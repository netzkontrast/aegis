# Write Scene: ARCHON-Assisted Scene Writing for Kohärenz Protokoll

**Purpose**: Lightweight writing assistant that provides NCP guidance without interrupting creative flow.

**When to use**: Before starting a new scene in the Kohärenz Protokoll manuscript.

**Philosophy**: Get guidance, then write freely. The novel is the boss. ARCHON is the assistant.

---

## Command Usage

```
/write-scene <chapter> <scene_id>
/write-scene 4 1.4
/write-scene 2
```

**Arguments**:
- `<chapter>` - Chapter number (required)
- `<scene_id>` - Scene ID like "1.4" (optional - provides detailed scene prompt)

**Examples**:
```bash
/write-scene 4 1.4          # Get full scene prompt for Scene 1.4
/write-scene 4              # Get chapter overview and style guide
```

---

## What This Command Does

### 1. Quick NCP Check (5-10 minutes)

**If scene ID provided:**
```bash
python ARCHON/tools/ncp_assist.py --scene {scene_id} --prompt --verbose
```

**Provides:**
- ✅ Scene structure (goal, conflict, outcome)
- ✅ Active alters with their current arc states
- ✅ Act-specific prose style guidance
- ✅ Sensory keywords for the location (KW1-4)
- ✅ 5-6 opening hook suggestions
- ✅ Thematic checkpoints to hit

**If only chapter provided:**
```bash
python ARCHON/tools/ncp_assist.py --chapter {chapter} --prompt
python ARCHON/tools/ncp_assist.py --chapter {chapter} --style-guide
```

**Provides:**
- ✅ Chapter thematic focus
- ✅ All scenes in the chapter
- ✅ Prose style guidance for this Act
- ✅ Protagonist/antagonist states

### 2. Character Voice Samples (Optional)

For each active alter in the scene:
```bash
python ARCHON/tools/ncp_assist.py --character {alter} --chapter {chapter} --voice-sample
```

**Provides:**
- ✅ Speech patterns and vocabulary
- ✅ 3 dialogue samples
- ✅ 3 internal voice samples
- ✅ Emotional register across arc
- ✅ Character relationships

### 3. Writing Guidance Summary

Present a concise summary:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 SCENE WRITING GUIDE: Chapter {N}, Scene {X.Y}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎬 SCENE STRUCTURE
Goal:     [Scene goal]
Conflict: [Scene conflict]
Outcome:  [Scene outcome]

📍 LOCATION: {Location}
Sensory Focus: [3-4 key sensory keywords]
Physics:       [One-line physics rule]

🎭 ACTIVE ALTERS
• {Alter 1} - {Function} - "{Sample dialogue}"
• {Alter 2} - {Function} - "{Sample dialogue}"
• {Alter 3} - {Function} - "{Sample dialogue}"

✍️  PROSE STYLE: {Act-specific style}
Technique: {Key technique to focus on}

💡 OPENING HOOKS (Choose one)
1. {Hook 1}
2. {Hook 2}
3. {Hook 3}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏱️  Read this once, then close it and write freely.
   Trust your instincts. Let the alters perform themselves.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 4. Prompt User to Begin

```
Ready to write?

I've prepared the guidance above. When you're ready:
1. Open: kohaerenz_protokoll/manuscript/act_1/chapter_{N}_scene_{Y}.md
2. Read the guidance once
3. Close this window
4. Write freely for 30-60 minutes without interruption

Remember:
- First draft = messy and alive
- Fragments are your friend
- Let alters interrupt each other
- Follow discoveries

When you're done, I can help validate if you want.

Let me know when you're ready to start!
```

---

## Implementation

```python
#!/usr/bin/env python3
"""
Execute the /write-scene command
"""

import sys
import subprocess
from pathlib import Path

def main():
    # Parse arguments
    if len(sys.argv) < 2:
        print("Usage: /write-scene <chapter> [scene_id]")
        sys.exit(1)

    chapter = sys.argv[1]
    scene_id = sys.argv[2] if len(sys.argv) > 2 else None

    tools_dir = Path("/home/user/aegis/ARCHON/tools")

    print("━" * 60)
    print(f"📝 SCENE WRITING GUIDE: Chapter {chapter}")
    if scene_id:
        print(f"   Scene {scene_id}")
    print("━" * 60)
    print()

    # Get scene/chapter prompt
    if scene_id:
        cmd = [
            "python", str(tools_dir / "ncp_assist.py"),
            "--scene", scene_id, "--prompt", "--verbose"
        ]
        print("🎬 SCENE STRUCTURE & GUIDANCE")
        print()
        subprocess.run(cmd, cwd=tools_dir)
    else:
        # Chapter overview
        cmd = [
            "python", str(tools_dir / "ncp_assist.py"),
            "--chapter", chapter, "--prompt"
        ]
        subprocess.run(cmd, cwd=tools_dir)

        # Style guide
        print()
        cmd = [
            "python", str(tools_dir / "ncp_assist.py"),
            "--chapter", chapter, "--style-guide"
        ]
        subprocess.run(cmd, cwd=tools_dir)

    print()
    print("━" * 60)
    print("⏱️  Read this once, then close it and write freely.")
    print("   Trust your instincts. Let the alters perform themselves.")
    print("━" * 60)
    print()
    print("Ready to write?")
    print()
    print("When you're ready:")
    print(f"1. Open: kohaerenz_protokoll/manuscript/act_1/chapter_{chapter}_scene_*.md")
    print("2. Read the guidance once")
    print("3. Close this window")
    print("4. Write freely for 30-60 minutes without interruption")
    print()
    print("Remember:")
    print("- First draft = messy and alive")
    print("- Fragments are your friend")
    print("- Let alters interrupt each other")
    print("- Follow discoveries")
    print()
    print("When you're done, I can help validate if you want.")
    print()

if __name__ == "__main__":
    main()
```

---

## Integration with Writing Protocol

This command fits into the existing WRITING_PROTOCOL.md:

### Before: Manual Process
```
1. Read scene outline (5-10 min)
2. Query NCP manually (optional)
3. Review character profiles
4. Set prose style target
5. Write
```

### After: With /write-scene
```
1. Run: /write-scene 4 1.4 (2-3 min to review output)
2. Write immediately
```

**Time saved**: 7-12 minutes of context gathering
**Flow preserved**: Still lightweight, not prescriptive

---

## Advanced Usage

### Get Character Voice Before Writing
```
/write-scene 4 1.4

# Then if you need specific character voice:
python ARCHON/tools/ncp_assist.py --character Lex --chapter 4 --voice-sample
python ARCHON/tools/ncp_assist.py --character Kiko --chapter 4 --voice-sample
```

### Chapter Planning Session
```
# At start of week, plan the chapter:
/write-scene 4

# Shows all scenes, thematic focus, style guidance
# Then write each scene individually
```

### Quick Style Check Mid-Writing
```
# If you lose the voice mid-scene:
python ARCHON/tools/ncp_assist.py --chapter 4 --style-guide
```

---

## Post-Scene Validation (Optional)

After writing, validate if desired:
```bash
python ARCHON/tools/ncp_validate.py manuscript/act_1/chapter_04_scene_01.md --verbose
```

**Only fix**:
- ❌ Critical plot contradictions
- ❌ World physics violations
- ❌ Missing key characters

**Ignore**:
- ✅ Minor style suggestions
- ✅ Word count warnings
- ✅ Anything that weakens the voice

---

## Philosophy

**The Golden Rule**: *The novel is the boss. ARCHON is the assistant.*

This command provides:
- ✅ Just enough structure to start confidently
- ✅ Character voice reminders when needed
- ✅ Sensory/thematic anchors for authenticity
- ✅ Freedom to discover and deviate

It does NOT:
- ❌ Dictate how to write the scene
- ❌ Block creative flow with validation
- ❌ Make you follow every guideline
- ❌ Replace your instincts as a writer

**Use it to start writing faster, not to write "correctly."**

---

## Troubleshooting

### "The guidance feels restrictive"
→ Read it once, then ignore it. Write what feels right.

### "I don't need all this info"
→ Just use `/write-scene <chapter>` for minimal guidance

### "The opening hooks are generic"
→ They're starting points, not commands. Make them your own.

### "I want to skip the guidance entirely"
→ Perfect! Just open the manuscript and write. This is optional.

---

## See Also

- [WRITING_PROTOCOL.md](kohaerenz_protokoll/WRITING_PROTOCOL.md) - Full writing workflow
- [ncp_assist.py](ARCHON/tools/ncp_assist.py) - Writing assistant tool
- [ncp_validate.py](ARCHON/tools/ncp_validate.py) - Scene validator
- [Codex Skill](.claude/skills/codex.md) - Narrative coherence validation

---

**Remember**: This is a 5-minute prep tool, not a 30-minute planning session. Get the guidance, then write freely. The prose knows what it needs.
