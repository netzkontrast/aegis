# Claude Commands Documentation

**AEGIS Learning System**
**Version:** 2.0 (Unified Architecture)
**Last Updated:** 2025-11-05

---

## Overview

This directory contains slash commands for the AEGIS learning system.

**Current Commands:**
- `/learn` - **[NEW]** Unified learning workflow (recommended)
- `/tapestry` - ⚠️ Deprecated (use `/learn` instead)
- `/ship-learn-next` - ⚠️ Deprecated (use `/learn` instead)
- `/zettelkasten-tapestry` - ⚠️ Deprecated (use `/learn --save` instead)

---

## Quick Start

### Extract Content + Create Plan
```bash
/learn https://youtube.com/watch?v=xxx     # YouTube video
/learn https://example.com/article         # Article
/learn https://example.com/paper.pdf       # PDF
```

### Create Plan from Existing File
```bash
/learn article.txt
/learn transcript.txt
```

### Full Workflow with Zettelkasten
```bash
/learn <URL> --save                        # Extract + Plan + Knowledge vault
/learn <file> --save                       # Plan + Knowledge vault
```

### Extract Only (No Planning)
```bash
/learn <URL> --extract-only
```

---

## The `/learn` Command

**Purpose:** Unified learning workflow for any content type

**Supported content:**
- YouTube videos (with transcripts)
- Web articles and blog posts
- PDF documents
- Existing text files

**Workflows:**
1. **Extract + Plan** - From URLs
2. **Plan Only** - From existing files
3. **Extract + Plan + Zettelkasten** - Full knowledge management
4. **Extract Only** - Just get the content

---

## Command Reference

### `/learn <URL>`

**Description:** Extract content from URL and create action plan

**Input:** URL (YouTube, article, or PDF)

**Output:**
- Content text file
- Ship-Learn-Next action plan (5 reps)

**Example:**
```bash
/learn https://www.youtube.com/watch?v=xxx

# Results:
# ✓ Video Title.txt (content)
# ✓ Ship-Learn-Next Plan - Quest Title.md (plan)
```

---

### `/learn <file>`

**Description:** Create action plan from existing content file

**Input:** Path to text file

**Output:**
- Ship-Learn-Next action plan (5 reps)

**Example:**
```bash
/learn article.txt

# Results:
# ✓ Ship-Learn-Next Plan - Quest Title.md (plan)
```

---

### `/learn <URL> --save`

**Description:** Full workflow with Zettelkasten knowledge management

**Input:** URL (YouTube, article, or PDF)

**Output:**
- Content text file
- Ship-Learn-Next action plan
- Source Note (SRC)
- Zettel Notes (ZTL) - atomic concepts
- Quest MOC (Map of Content)
- Updated vault index

**Example:**
```bash
/learn https://example.com/article --save

# Results:
# ✓ Article Title.txt (content)
# ✓ Ship-Learn-Next Plan - Quest.md (plan)
# ✓ SRC-20251105-1430-Article-Title.md (source note)
# ✓ ZTL-... (zettel notes)
# ✓ MOC-Quest-Title.md (map of content)
```

---

### `/learn <file> --save`

**Description:** Create plan from file and save to Zettelkasten

**Input:** Path to text file

**Output:**
- Ship-Learn-Next action plan
- Source Note (SRC)
- Zettel Notes (ZTL)
- Quest MOC

**Example:**
```bash
/learn transcript.txt --save

# Results:
# ✓ Ship-Learn-Next Plan - Quest.md (plan)
# ✓ SRC-... (source note)
# ✓ Knowledge vault updated
```

---

### `/learn <URL> --extract-only`

**Description:** Extract content without creating a plan

**Input:** URL

**Output:**
- Content text file only (no plan)

**Example:**
```bash
/learn https://example.com/article --extract-only

# Results:
# ✓ Article Title.txt (content only)
```

---

## Modular Architecture

The `/learn` command is built on three independent modules:

```
_modules/
├── extract-content.md      # Content extraction (YouTube, articles, PDFs)
├── action-planner.md       # Ship-Learn-Next planning framework
└── knowledge-manager.md    # Zettelkasten knowledge management
```

**Benefits:**
- Each module does ONE thing well
- Modules can be used independently
- Easy to test and maintain
- Easy to extend

**Module usage:**
```bash
# Modules are automatically sourced by /learn command
# Can also be used independently in other commands
```

---

## Ship-Learn-Next Framework

All action plans follow the Ship-Learn-Next framework:

**3 Phases (Repeated):**
1. **SHIP** - Create something real
2. **LEARN** - Reflect on what happened
3. **NEXT** - Plan the next iteration

**5-Rep Progression:**
- **Rep 1:** Shippable this week (smallest version)
- **Rep 2:** Next iteration (adds one new element)
- **Rep 3:** Continuing progression
- **Rep 4:** Advanced iteration
- **Rep 5:** Mastery demonstration

**Philosophy:** 100 reps beats 100 hours of study. Learning = doing better, not knowing more.

---

## Zettelkasten Integration

When using `--save` flag, knowledge is preserved in your Zettelkasten vault:

**Vault Structure:**
```
zettelkasten_agent/vault/
├── _INDEX.md               # Master navigation
├── _LOG.md                 # Activity log
├── SRC-*.md                # Source notes
├── ZTL-*.md                # Zettel notes (atomic concepts)
└── MOC-*.md                # Maps of content
```

**Note Types:**

1. **Source Note (SRC)**
   - Captures original material
   - Links to content and plan
   - Tracks processing status

2. **Zettel Note (ZTL)**
   - One atomic concept per note
   - Declarative title (states a claim)
   - Self-contained explanation
   - Practical application
   - Links to related concepts

3. **Map of Content (MOC)**
   - Organizes related notes
   - Provides quest structure
   - Tracks rep progress
   - Shows knowledge connections

---

## Content Types Supported

### YouTube Videos
- **Requirements:** yt-dlp (auto-installed)
- **Extracts:** Video transcripts (auto-generated or manual)
- **Formats:** VTT → Clean text (deduplicated)

### Web Articles
- **Tools:** reader (npm), trafilatura (pip), or fallback
- **Extracts:** Main article content (no ads, nav, etc.)
- **Formats:** HTML → Clean text

### PDF Documents
- **Requirements:** pdftotext (optional but recommended)
- **Extracts:** Text content from PDFs
- **Formats:** PDF → Plain text
- **Note:** Scanned PDFs may not extract well (requires OCR)

### Text Files
- **Formats:** .txt, .md, or any plain text
- **Use:** Create plans from existing content

---

## Dependencies

### Required (Built-in)
- `bash`
- `curl`
- `python3`

### Optional (Auto-installed when possible)
- `yt-dlp` - YouTube transcript extraction
- `reader` - High-quality article extraction (npm)
- `trafilatura` - Good article extraction (pip)
- `pdftotext` - PDF text extraction (poppler package)

### Installation Commands

```bash
# YouTube support
brew install yt-dlp              # macOS
pip3 install yt-dlp              # Linux/Windows

# Article extraction (choose one or both)
npm install -g @mozilla/readability-cli   # reader (best)
pip3 install trafilatura                  # trafilatura (good)

# PDF extraction
brew install poppler             # macOS
apt install poppler-utils        # Linux
```

---

## Examples

### Example 1: Learn from YouTube Video

```bash
User: /learn https://www.youtube.com/watch?v=dQw4w9WgXcQ

Claude:
🧵 Learn Command Starting...
   Mode: extract

📥 Extracting content...
📍 Detected: youtube
📺 Extracting YouTube transcript...
✅ Content Extracted!
   File: Never Gonna Give You Up.txt
   Size: 1,234 words

🚀 Creating Ship-Learn-Next action plan...

[Analyzes content and creates 5-rep plan]

✅ Learn Workflow Complete!

📥 Content: Never Gonna Give You Up.txt
📋 Plan: Ship-Learn-Next Plan - Master Video Production.md

🎯 Your Quest: Master Video Production Techniques
📍 Rep 1 (This Week): Create and publish one music video

❓ When will you ship Rep 1?
```

---

### Example 2: Learn from Article with Zettelkasten

```bash
User: /learn https://example.com/how-to-build-saas --save

Claude:
🧵 Learn Command Starting...
   Mode: extract
   Save to Zettelkasten: Yes

📥 Extracting content...
📍 Detected: article
📄 Extracting article content...
   Using: reader
✅ Content Extracted!
   File: How to Build a SaaS.txt
   Size: 2,500 words

🚀 Creating Ship-Learn-Next action plan...

[Creates 5-rep plan]

🧠 Saving to Zettelkasten...
📝 Creating Source Note...
✓ Source note: SRC-20251105-1430-How-to-Build-a-SaaS.md

🧠 Extracting atomic concepts...
✓ Created 5 Zettel notes
✓ Created Quest MOC
✓ Found 3 connections to existing knowledge

✅ Learn Workflow Complete!

📥 Content: How to Build a SaaS.txt (2,500 words)
📋 Plan: Ship-Learn-Next Plan - Launch SaaS MVP.md
🧠 Vault: 5 concepts saved, 3 connections made

🎯 Your Quest: Launch SaaS MVP in 8 weeks
📍 Rep 1 (This Week): Build landing page with signup form

❓ When will you ship Rep 1?
```

---

### Example 3: Plan from Existing File

```bash
User: /learn transcript.txt

Claude:
🧵 Learn Command Starting...
   Mode: plan-only

🚀 Creating Ship-Learn-Next action plan...
   Analyzing 1,500 words...

[Analyzes content and creates plan]

✅ Plan Created!

📋 Plan: Ship-Learn-Next Plan - Master Cold Outreach.md

🎯 Your Quest: Send 20 cold emails, get 5 responses
📍 Rep 1 (This Week): Send 5 cold emails

❓ When will you ship Rep 1?
```

---

## Deprecated Commands

### ⚠️ These commands still work but will be removed

- `/tapestry <URL>` → Use `/learn <URL>`
- `/ship-learn-next <file>` → Use `/learn <file>`
- `/zettelkasten-tapestry <URL>` → Use `/learn <URL> --save`

**Timeline:** These will be removed after 1 month (December 2025)

**Action:** Start using `/learn` now

**See:** [MIGRATION_GUIDE.md](./MIGRATION_GUIDE.md) for details

---

## Best Practices

### 1. Choose the Right Mode

- **Want to implement advice?** → `/learn <URL>`
- **Want to preserve knowledge?** → `/learn <URL> --save`
- **Already have content?** → `/learn <file>`
- **Just need the content?** → `/learn <URL> --extract-only`

### 2. Ship Rep 1 Quickly

- Don't overthink Rep 1
- Ship something real within 1 week
- Learn by doing, not by planning
- Iterate based on learnings

### 3. Use Zettelkasten for Important Content

- Use `--save` for content you want to reference later
- Build your knowledge graph over time
- Connect new concepts to existing knowledge
- Review your vault regularly

### 4. Focus on Action, Not Consumption

- The plan is a guide, not a prison
- Ship first, perfect later
- 100 reps beats 100 hours of study
- Learning = doing better, not knowing more

---

## Troubleshooting

### Issue: YouTube transcript not available

**Solution:**
- Try different video (not all have captions)
- Check if video is available in your region
- Ensure yt-dlp is up to date: `pip3 install -U yt-dlp`

### Issue: Article extraction failed

**Solution:**
- Install better extraction tools (reader or trafilatura)
- Try different URL (may be paywalled or require login)
- Check internet connection

### Issue: PDF extraction is empty

**Solution:**
- Install pdftotext: `brew install poppler`
- PDF may be scanned/image-based (requires OCR)
- Try manual copy-paste to text file

### Issue: Plan seems generic

**Solution:**
- Provide more context about your goals
- Answer Claude's questions honestly
- Review and modify the plan yourself
- Remember: Rep 1 should be shippable this week

---

## Future Enhancements

Coming soon:
- `/learn <URL> --export pdf` - Export plans as PDF
- `/learn <URL> --share` - Generate shareable links
- `/learn <URL> --review` - Review and update existing plans
- `/learn <URL> --collaborative` - Multi-user learning quests
- Twitter thread extraction
- Podcast transcript integration

---

## Support

### Need Help?

1. Check this README
2. See [MIGRATION_GUIDE.md](./MIGRATION_GUIDE.md)
3. Try the command with different options
4. Create an issue if stuck

### Feedback Welcome

Tell us:
- What works well
- What's confusing
- What features you want
- What bugs you found

---

## Philosophy

**Extract → Plan → Ship → Learn → Next**

That's the AEGIS way.

We don't just consume content. We transform it into action, learn by shipping, and build knowledge that compounds over time.

**One command. Any content. Actionable learning.**

Welcome to the unified learning system. 🚀
