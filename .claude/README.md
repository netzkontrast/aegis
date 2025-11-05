# Claude Code Skills for AEGIS

This directory contains custom Claude Code skills (slash commands) that enhance your learning and implementation workflow.

## Available Skills

### 🧵 Tapestry - Unified Content Extraction + Action Planning

**Purpose**: Extract content from any URL (YouTube, articles, PDFs) and automatically create an actionable implementation plan.

**When to use**: When you find educational content and want to turn it into concrete action steps.

**Activation keywords**:
- `tapestry <URL>`
- `weave <URL>`
- `help me plan <URL>`
- `extract and plan <URL>`
- `make this actionable <URL>`

### 🚀 Ship-Learn-Next - Action Planning Framework

**Purpose**: Transform learning content into concrete, shippable iterations using the Ship-Learn-Next framework.

**When to use**: When you have content (transcript, article, tutorial) and want to create a progression plan with actionable reps.

**Activation keywords**:
- `ship-learn-next` (after extracting content)
- "turn this into a plan"
- "make this actionable"
- "I want to implement this advice"

## Quick Start Guide

### Basic Workflow

```bash
# Step 1: Extract content and create action plan
tapestry https://www.youtube.com/watch?v=example

# Tapestry will:
# 1. Detect content type (YouTube video)
# 2. Extract transcript
# 3. Create Ship-Learn-Next action plan
# 4. Save both files

# Step 2: Review your plan
cat "Ship-Learn-Next Plan - [Quest Title].md"

# Step 3: Ship Rep 1!
# Follow the action steps in your plan

# Step 4: Reflect and iterate
# Come back after shipping to plan Rep 2
```

## The Complete Tapestry Workflow

### 1. Provide a URL

Give Claude Code any learning content URL:

```
You: tapestry https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### 2. Automatic Content Detection

Tapestry automatically detects:
- **YouTube videos** → Extracts transcript using yt-dlp
- **Web articles** → Extracts content using reader/trafilatura
- **PDFs** → Downloads and extracts text using pdftotext

### 3. Content Extraction

You'll see progress indicators:
```
🧵 Tapestry Workflow Starting...
📍 Detected: youtube
📺 Extracting YouTube transcript...
✓ Saved transcript: Video Title.txt
```

### 4. Automatic Action Planning

Tapestry invokes Ship-Learn-Next to create an implementation plan:
```
🚀 Creating Ship-Learn-Next action plan...
✓ Quest: Master Video Production
✓ Saved plan: Ship-Learn-Next Plan - Master Video Production.md
```

### 5. Review and Ship

You get two files:
1. **Content file**: `Video Title.txt` (raw extracted content)
2. **Action plan**: `Ship-Learn-Next Plan - [Quest].md` (5-rep progression)

## The Ship-Learn-Next Framework

### Core Philosophy

**100 reps beats 100 hours of study**

Learning isn't about consuming content—it's about doing better, not knowing more.

### Three-Phase Cycle

Every learning quest follows this pattern:

1. **SHIP** - Create something real (code, content, product, demonstration)
2. **LEARN** - Honest reflection on what happened
3. **NEXT** - Plan the next iteration based on learnings

### Rep Structure

Each plan contains 5 progressive reps:

#### Rep 1: Smallest Shippable Version (This Week)
- **Ship Goal**: Concrete deliverable
- **Timeline**: 1-7 days
- **Success Criteria**: Specific checkboxes
- **Action Steps**: Concrete steps to complete
- **Reflection Questions**: Honest assessment after shipping

#### Reps 2-5: Progressive Iterations
- Each rep adds ONE new element
- Builds on previous learnings
- Increases difficulty gradually
- Keeps focus on shipping, not studying

## Usage Examples

### Example 1: YouTube Tutorial

```
You: tapestry https://www.youtube.com/watch?v=abc123

Claude:
🧵 Tapestry Workflow Starting...
📍 Detected: youtube
📺 Extracting YouTube transcript...
✓ Saved: Building Your First SaaS.txt (3,847 words)

🚀 Creating action plan...
✓ Quest: Build a SaaS MVP
✓ Saved: Ship-Learn-Next Plan - Build a SaaS MVP.md

✅ Tapestry Complete!

📥 Content: Building Your First SaaS.txt
📋 Plan: Ship-Learn-Next Plan - Build a SaaS MVP.md

🎯 Your Quest: Build and launch a minimal SaaS product in 6 weeks

📍 Rep 1 (This Week): Ship a landing page with email signup

When will you ship Rep 1?
```

### Example 2: Technical Article

```
You: weave https://example.com/how-to-build-distributed-systems

Claude:
🧵 Tapestry Workflow Starting...
📍 Detected: article
📄 Extracting article content...
✓ Using: reader (Mozilla Readability)
✓ Saved: How to Build Distributed Systems.txt (2,156 words)

🚀 Creating action plan...
✓ Quest: Implement Distributed System Patterns
✓ Saved: Ship-Learn-Next Plan - Distributed System Patterns.md

✅ Tapestry Complete!

📍 Rep 1: Build a simple message queue in Python (by Friday)

Ready to ship?
```

### Example 3: Research Paper PDF

```
You: help me plan https://arxiv.org/pdf/example.pdf

Claude:
🧵 Tapestry Workflow Starting...
📍 Detected: pdf
📑 Downloading PDF...
✓ Extracted: Neural Architecture Search.txt (8,923 words)

🚀 Creating action plan...
✓ Quest: Implement NAS Techniques
✓ Saved: Ship-Learn-Next Plan - NAS Implementation.md

📍 Rep 1: Implement random search baseline (this week)
📍 Rep 2: Add evolutionary strategies (next week)
📍 Rep 3: Compare results on small dataset
...

When will you start Rep 1?
```

## Understanding Your Action Plan

Every Ship-Learn-Next plan follows this structure:

```markdown
# Your Ship-Learn-Next Quest: [Title]

## Quest Overview
**Goal**: What you'll achieve in 4-8 weeks
**Source**: The content that inspired this
**Core Lessons**: 3-5 key actionable takeaways

---

## Rep 1: [Specific, Shippable Goal]

**Ship Goal**: Concrete deliverable you'll create
**Timeline**: This week / By [specific date]
**Success Criteria**:
- [ ] Specific, measurable outcome 1
- [ ] Specific, measurable outcome 2
- [ ] Specific, measurable outcome 3

**What You'll Practice** (from the content):
- Skill/concept 1 from source material
- Skill/concept 2 from source material

**Action Steps**:
1. Concrete step 1
2. Concrete step 2
3. Concrete step 3
4. Ship it (publish/deploy/share/demonstrate)

**Minimal Resources** (only for THIS rep):
- Link or reference - if truly needed

**After Shipping - Reflection**:
- What actually happened?
- What worked? What didn't?
- What surprised you?
- Rate this rep: _/10
- What's one thing to try differently next time?

---

## Rep 2-5: Progressive Path
[Similar structure, each building on previous reps]

---

## Remember
- This is about DOING, not studying
- Aim for 100 reps over time (not perfection on rep 1)
- Each rep = Plan → Do → Reflect → Next
- You learn by shipping, not by consuming

**Ready to ship Rep 1?**
```

## Best Practices

### ✅ Do This

- **Ship small, ship fast** - Rep 1 should be completable in 1-7 days
- **Focus on doing** - Don't spend weeks planning, start shipping
- **Reflect honestly** - Use the reflection questions after each rep
- **Iterate progressively** - Each rep adds ONE new element
- **Keep content files** - They're reference material, not study material
- **Commit to deadlines** - "By Friday" not "when I have time"

### ❌ Don't Do This

- **Don't study forever** - Stop reading, start building
- **Don't aim for perfect** - Ship Rep 1, improve in Rep 2
- **Don't skip reflection** - That's where real learning happens
- **Don't jump ahead** - Do Rep 1 before planning Rep 5
- **Don't collect plans** - One active quest at a time
- **Don't ignore action steps** - They're there for a reason

## Technical Details

### Dependencies

Tapestry automatically handles dependencies, but here's what it uses:

**For YouTube**:
- `yt-dlp` (auto-installed via brew/pip)
- Python 3 (for transcript deduplication)

**For Articles**:
- `reader` (npm - Mozilla Readability) OR
- `trafilatura` (pip - web scraping)
- Falls back to basic HTML parsing if neither available

**For PDFs**:
- `curl` (built-in)
- `pdftotext` from poppler (optional but recommended)
  - macOS: `brew install poppler`
  - Linux: `apt install poppler-utils`

### File Naming Conventions

**Content files**:
- `[Title].txt` - cleaned version of title from source

**Plan files**:
- `Ship-Learn-Next Plan - [Quest Title].md`
- Quest title is 3-6 words describing the main goal

### Where Files Are Saved

All files are saved in your current working directory:
```
/home/user/aegis/
├── Video Title.txt
├── Article Title.txt
├── Ship-Learn-Next Plan - Build a SaaS.md
├── Ship-Learn-Next Plan - Learn React.md
└── ...
```

## Advanced Usage

### Using Ship-Learn-Next Standalone

If you already have content extracted:

```
You: I have this transcript in video.txt. Can you help me create a ship-learn-next plan?

Claude: [Reads video.txt and creates action plan]
```

### Customizing Your Quest

After Tapestry creates a plan, you can refine it:

```
You: The plan looks good, but Rep 1 is too ambitious. Can we make it smaller?

Claude: [Adjusts Rep 1 to be more achievable]
```

### Tracking Multiple Quests

Create a quest log:

```bash
# List all your active quests
ls -1 Ship-Learn-Next\ Plan*.md

# Track completed reps
grep -A 5 "Rep 1:" Ship-Learn-Next\ Plan*.md
```

## Philosophy: Why This Works

### Traditional Learning (Doesn't Work)
1. Watch 10 hours of tutorials
2. Read 5 books
3. Take detailed notes
4. **Never build anything**
5. Forget everything in 2 weeks

### Ship-Learn-Next (Actually Works)
1. Extract key lessons (10 minutes)
2. Design smallest shippable version (10 minutes)
3. **Ship Rep 1 this week** (action-based learning)
4. Reflect honestly on results
5. Ship Rep 2 with improvements
6. **Repeat 100 times = mastery**

### The Science

**Deliberate Practice Research**:
- 100 focused reps > 1000 hours of passive study
- Feedback loops accelerate learning exponentially
- Shipping creates real-world constraints that force learning
- Reflection converts experience into knowledge

**Cognitive Load Theory**:
- Don't overwhelm with the full journey
- Focus on one rep at a time
- Build complexity progressively
- Each success creates momentum

## Integration with AEGIS Project

These skills embody the AEGIS philosophy:

- **ARCHON**: Maintains narrative coherence through structured protocols
- **Tapestry**: Maintains learning coherence through structured action plans
- **Both**: Transform scattered information into integrated, functional systems

Just as ARCHON helps maintain thematic coherence in a novel, Tapestry helps maintain **action coherence** in your learning journey.

## Troubleshooting

### Issue: "yt-dlp not found"
**Solution**: Tapestry will attempt to auto-install. If it fails:
```bash
# macOS
brew install yt-dlp

# Linux
pip install yt-dlp

# Or use pipx
pipx install yt-dlp
```

### Issue: "Could not extract article content"
**Solution**: Install reader or trafilatura:
```bash
# Install reader (recommended)
npm install -g @mozilla/readability-cli

# Or install trafilatura
pip install trafilatura
```

### Issue: "PDF downloaded but not extracted"
**Solution**: Install poppler for pdftotext:
```bash
# macOS
brew install poppler

# Linux
apt install poppler-utils
```

### Issue: "Plan is too ambitious"
**Solution**: Ask Claude to adjust Rep 1:
```
You: This Rep 1 is too big. Can we make it smaller?
Claude: [Creates a more achievable Rep 1]
```

### Issue: "I'm stuck on Rep 1"
**Solution**: Ship something, even if imperfect:
```
You: I'm stuck. My Rep 1 isn't perfect.
Claude: Ship it anyway. Learning happens in reflection, not perfection.
```

## Getting Help

If you encounter issues:

1. **Check the skill files**: `.claude/commands/tapestry.md` and `ship-learn-next.md`
2. **Read error messages**: They often explain what's missing
3. **Ask Claude**: "The tapestry skill failed, can you help debug?"

## Next Steps

Ready to start your learning-to-action journey?

```bash
# 1. Find content you want to learn from
# 2. Use Tapestry to extract and plan
tapestry <your-url>

# 3. Review your plan
cat Ship-Learn-Next\ Plan*.md

# 4. Ship Rep 1 this week!

# 5. Come back and reflect
# "I shipped Rep 1! Here's what happened..."

# 6. Plan and ship Rep 2
# Continue the cycle...
```

**Remember**: You don't learn by consuming content. You learn by shipping, reflecting, and iterating.

Now go ship something. 🚀

---

## Philosophy

> *"AEGIS is what AEGIS prevents from not being."*

In the same spirit, **learning is what shipping prevents from not happening**.

Extract → Plan → Ship → Learn → Next.

That's the Tapestry way.
