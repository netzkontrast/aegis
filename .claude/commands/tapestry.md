---
name: tapestry
description: Unified content extraction and action planning. Works with URLs (YouTube, articles, PDFs), local files, repository directories, and narrative content. Use when user says "tapestry <URL/path>", "weave <source>", "extract and plan <content>", or wants to analyze repo content. Automatically detects content type and applies Codex validation for narrative work.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
---

# Tapestry: Universal Content Orchestrator

This is the **master skill** that orchestrates content extraction, narrative validation, and action planning:
1. Detect source type (URL, local file, repo directory, or interactive)
2. Extract content using appropriate method
3. Apply Codex validation for narrative content
4. Create Ship-Learn-Next action plan
5. Generate comprehensive output

## When to Use This Skill

Activate when the user:
- Says "tapestry [URL/path]"
- Says "weave [source]"
- Says "extract and plan [content]"
- Says "analyze the manuscript"
- Says "tapestry kohaerenz_protokoll/"
- Wants to extract from local repo files
- Needs narrative content validated against Codex
- Wants the full Tapestry workflow (extract → validate → plan)

**Keywords to watch for**: tapestry, weave, plan, actionable, extract, analyze, manuscript, codex, validate

## Enhanced Capabilities

### 🌐 External Sources (Original)
- YouTube videos (transcript extraction)
- Web articles and blog posts
- PDF documents
- General HTML content

### 📁 Local Repository Sources (NEW)
- Individual files (`tapestry path/to/file.md`)
- Directories (`tapestry kohaerenz_protokoll/world/`)
- Repo patterns (`tapestry the manuscript`, `tapestry world-building`)
- Multiple files (glob patterns)

### 📖 Narrative Integration (NEW)
- Automatic Codex validation for narrative content
- Character consistency checking
- World physics validation
- Integration arc compliance
- Canonical principle enforcement

## Source Detection Logic

### Priority Order:

1. **Local File Path** (highest priority if exists)
   ```
   - Path exists on filesystem
   - Can be absolute or relative
   - File or directory
   ```

2. **Repository Keywords**
   ```
   - "manuscript", "codex", "world", "characters"
   - "narrative_design", "act", "chapter"
   - Maps to specific repo directories
   ```

3. **URL Patterns**
   ```
   - youtube.com, youtu.be
   - .pdf extension
   - http:// or https://
   ```

4. **Interactive Mode** (no argument)
   ```
   - Ask user what to extract
   - Offer repo suggestions
   ```

## Complete Workflow

### Step 1: Detect Source Type

```bash
#!/bin/bash

INPUT="$1"

# No input → Interactive mode
if [ -z "$INPUT" ]; then
    echo "🧵 Tapestry - What would you like to extract?"
    echo ""
    echo "Options:"
    echo "  1. URL (YouTube, article, PDF)"
    echo "  2. Local file or directory"
    echo "  3. Repo content (manuscript, world, characters)"
    echo "  4. Exit"
    echo ""
    read -p "Choose (1-4): " choice
    # Handle choice...
    exit 0
fi

# Check if local path exists
if [ -f "$INPUT" ] || [ -d "$INPUT" ]; then
    SOURCE_TYPE="local"
    SOURCE_PATH="$INPUT"

# Check for repo keywords
elif [[ "$INPUT" =~ manuscript|codex|world|characters|narrative ]]; then
    SOURCE_TYPE="repo_keyword"
    SOURCE_KEYWORD="$INPUT"

# Check for YouTube
elif [[ "$INPUT" =~ youtube\.com/watch|youtu\.be/|youtube\.com/shorts ]]; then
    SOURCE_TYPE="youtube"
    SOURCE_URL="$INPUT"

# Check for PDF
elif [[ "$INPUT" =~ \.pdf$ ]] || curl -sI "$INPUT" 2>/dev/null | grep -iq "Content-Type: application/pdf"; then
    SOURCE_TYPE="pdf"
    SOURCE_URL="$INPUT"

# Default to article
elif [[ "$INPUT" =~ ^https?:// ]]; then
    SOURCE_TYPE="article"
    SOURCE_URL="$INPUT"

else
    echo "❌ Could not detect source type: $INPUT"
    exit 1
fi

echo "📍 Detected: $SOURCE_TYPE"
```

### Step 2: Extract Content (by Type)

#### Local File Extraction (NEW)

```bash
if [ "$SOURCE_TYPE" = "local" ]; then
    echo "📁 Reading local content..."

    if [ -f "$SOURCE_PATH" ]; then
        # Single file
        CONTENT_FILE="$SOURCE_PATH"
        echo "✓ Reading file: $CONTENT_FILE"

    elif [ -d "$SOURCE_PATH" ]; then
        # Directory - combine files
        TIMESTAMP=$(date +%Y%m%d_%H%M%S)
        CONTENT_FILE="extracted_${SOURCE_PATH//\//_}_${TIMESTAMP}.md"

        echo "# Extracted Content from: $SOURCE_PATH" > "$CONTENT_FILE"
        echo "" >> "$CONTENT_FILE"
        echo "Extracted: $(date)" >> "$CONTENT_FILE"
        echo "" >> "$CONTENT_FILE"

        # Find markdown files and combine
        find "$SOURCE_PATH" -name "*.md" -type f | while read -r file; do
            echo "" >> "$CONTENT_FILE"
            echo "---" >> "$CONTENT_FILE"
            echo "## File: $file" >> "$CONTENT_FILE"
            echo "---" >> "$CONTENT_FILE"
            echo "" >> "$CONTENT_FILE"
            cat "$file" >> "$CONTENT_FILE"
        done

        FILE_COUNT=$(find "$SOURCE_PATH" -name "*.md" -type f | wc -l)
        echo "✓ Combined $FILE_COUNT files into: $CONTENT_FILE"
    fi

    # Detect if narrative content
    if grep -iq "AEGIS\|Kael\|Kernwelt\|alter\|Kohärenz" "$CONTENT_FILE" 2>/dev/null; then
        IS_NARRATIVE="true"
        echo "📖 Narrative content detected - Codex validation will be applied"
    else
        IS_NARRATIVE="false"
    fi
fi
```

#### Repository Keyword Mapping (NEW)

```bash
if [ "$SOURCE_TYPE" = "repo_keyword" ]; then
    echo "🔍 Mapping keyword to repository..."

    case "$SOURCE_KEYWORD" in
        manuscript|manuscript*)
            SOURCE_PATH="kohaerenz_protokoll/manuscript"
            ;;
        world|worldbuilding|world-building)
            SOURCE_PATH="kohaerenz_protokoll/world"
            ;;
        characters|alters)
            SOURCE_PATH="kohaerenz_protokoll/world/characters"
            ;;
        codex|project\ codex)
            SOURCE_PATH="kohaerenz_protokoll/PROJECT_CODEX.md"
            ;;
        narrative|narrative\ design)
            SOURCE_PATH="kohaerenz_protokoll/narrative_design"
            ;;
        *)
            echo "❌ Unknown keyword: $SOURCE_KEYWORD"
            echo "Known keywords: manuscript, world, characters, codex, narrative"
            exit 1
            ;;
    esac

    echo "→ Mapped to: $SOURCE_PATH"
    IS_NARRATIVE="true"

    # Now process as local path
    # [Use local file extraction logic from above]
fi
```

#### YouTube/Article/PDF Extraction (Existing)

[Keep existing extraction logic for URLs - see original tapestry.md]

### Step 3: Apply Codex Validation (NEW)

**Only for narrative content detected from repo or Kohärenz Protokoll keywords**

```markdown
## Codex Validation

When `IS_NARRATIVE="true"`, perform comprehensive validation:

### 3.1: Load Codex Reference

Read the PROJECT_CODEX.md to understand canonical principles:
- Section 1.0: Philosophical Foundation
- Section 2.0: Principal Entities (AEGIS, Kael, Juna)
- Section 3.0: World Architecture (Risse, Kernwelten)
- Section 4.0: Canonical Plot
- Section 5.0: Supporting Factions

### 3.2: Analyze Extracted Content

Check content against Codex principles:

**Character Validation:**
- [ ] Does AEGIS behavior match Section 2.1? (tragic, not evil)
- [ ] Are alter voices distinct per Section 2.2.1?
- [ ] Do alters follow TSDP action systems correctly?
- [ ] Is integration level appropriate for act position?

**World Physics Validation:**
- [ ] Do Kernwelt descriptions match sensory signatures (3.2)?
- [ ] Do Risse follow 4-step causal chain (3.1)?
- [ ] Does world react to internal psychological state?
- [ ] Are somatic truths correctly applied?

**Philosophical Validation:**
- [ ] Is K₁/K₀ dynamics correctly represented (1.2)?
- [ ] Does AEGIS embody Coherence Theory (1.1)?
- [ ] Does Kael embody Correspondence Theory (1.1)?
- [ ] Is dialetheic logic (holding paradox) present?

**Plot Structure Validation:**
- [ ] Does content fit three-act trauma-integration arc (4.1)?
- [ ] Is prose style appropriate for integration level?
- [ ] Are ANP-EP phobia dynamics present (2.2)?
- [ ] Moving toward functional multiplicity, not "cure"?

### 3.3: Generate Validation Report

Create a markdown report:

```markdown
# Codex Validation Report
**Content**: [source]
**Validated**: [timestamp]

## Summary
[Overall assessment - compliant/has issues/major violations]

## Character Consistency
[Findings for characters]

## World Physics
[Findings for Kernwelten and Risse]

## Philosophical Principles
[Findings for core concepts]

## Plot Structure
[Findings for narrative arc]

## Recommendations
[Specific suggestions for alignment]

## References
[Relevant Codex sections cited]
```

Save as: `codex_validation_[timestamp].md`

### 3.4: Integrate Findings into Plan

When creating Ship-Learn-Next plan, include:
- Codex compliance as success criteria
- Validation checkpoints for each rep
- References to specific Codex sections
- Character/world constraints for implementation
```

### Step 4: Create Ship-Learn-Next Plan

**Always create an action plan, adapted based on content type:**

#### For Narrative Content (with Codex)

```markdown
## Ship-Learn-Next Plan: [Title]
**Quest**: [4-8 week narrative goal]
**Codex Compliance Required**: Yes

### 📖 Codex Constraints
[Key canonical principles from validation report]

### 🎯 Rep 1: [First Shippable Scene/Chapter]
**Ship Goal**: Write [specific content] that adheres to Codex
**Success Criteria**:
- [ ] Content passes Codex validation
- [ ] Character voices match Section 2.2.1
- [ ] World physics comply with Section 3.2
- [ ] [Additional specific criteria]

**Codex Checkpoints**:
- Before writing: Review relevant Codex sections
- During writing: Apply voice matrix and world rules
- After writing: Run validation against canonical principles

**Action Steps**:
1. Read Codex Section [X] for this content
2. [Specific narrative action]
3. Validate using Codex Workflow [N]
4. [Continue...]

### 📦 Rep 2-5: [Progressive iterations]
[Each with Codex compliance built in]

### 🔄 The Narrative Loop
Ship compliant content → Learn from validation → Refine understanding → Next iteration

### 📚 Codex References
- [List relevant sections for this quest]
```

#### For Technical/Learning Content (without Codex)

[Use standard Ship-Learn-Next format - see ship-learn-next.md]

### Step 5: Generate Comprehensive Output

Present complete results:

```
✅ Tapestry Workflow Complete!

📥 Content Extracted:
   ✓ Source: [type] - [name]
   ✓ Location: [path/url]
   ✓ File: [output filename]
   ✓ Size: [word count] words

[IF NARRATIVE]
📖 Codex Validation:
   ✓ Report: codex_validation_[timestamp].md
   ✓ Status: [Compliant/Has Issues/Violations]
   ✓ Key Findings: [summary]

📋 Action Plan Created:
   ✓ Quest: [quest title]
   ✓ Plan File: Ship-Learn-Next Plan - [title].md
   [IF NARRATIVE] ✓ Codex Integration: Enabled

🎯 Your Quest: [one-line summary]

📍 Rep 1 Focus: [specific goal]
[IF NARRATIVE] 📖 Codex Sections to Review: [list]

🚀 Ready to ship? When will you complete Rep 1?
```

## Usage Examples

### Example 1: YouTube Video (Original Functionality)

```
User: tapestry https://www.youtube.com/watch?v=dQw4w9WgXcQ

Claude:
🧵 Tapestry Workflow Starting...
📍 Detected: youtube
📺 Extracting YouTube transcript...
✓ Saved: Never Gonna Give You Up.txt (1,234 words)

🚀 Creating action plan...
✓ Quest: Master Video Production
✓ Plan: Ship-Learn-Next Plan - Master Video Production.md

✅ Complete! When will you ship Rep 1?
```

### Example 2: Local File (NEW)

```
User: tapestry notes/tutorial.md

Claude:
🧵 Tapestry Workflow Starting...
📍 Detected: local
📁 Reading local content...
✓ File: notes/tutorial.md (2,456 words)

🚀 Creating action plan...
✓ Quest: Implement Tutorial Concepts
✓ Plan: Ship-Learn-Next Plan - Tutorial Implementation.md

✅ Complete! When will you ship Rep 1?
```

### Example 3: Repo Directory (NEW)

```
User: tapestry kohaerenz_protokoll/world/characters/

Claude:
🧵 Tapestry Workflow Starting...
📍 Detected: local
📁 Reading local content...
✓ Combined 12 files into: extracted_characters_20251105.md (15,234 words)
📖 Narrative content detected - Codex validation will be applied

🔍 Validating against Codex...
✓ Loaded: PROJECT_CODEX.md
✓ Validated: Character profiles
✓ Status: 2 minor inconsistencies found
✓ Report: codex_validation_20251105.md

🚀 Creating action plan with Codex integration...
✓ Quest: Harmonize Character Profiles with Codex
✓ Plan: Ship-Learn-Next Plan - Character Codex Compliance.md

✅ Complete!
📖 Review validation report for specific issues
🎯 Rep 1: Fix AEGIS behavior description (Section 2.1)
When will you ship Rep 1?
```

### Example 4: Repo Keyword (NEW)

```
User: tapestry the manuscript

Claude:
🧵 Tapestry Workflow Starting...
📍 Detected: repo_keyword
🔍 Mapping keyword to repository...
→ Mapped to: kohaerenz_protokoll/manuscript
📁 Reading local content...
✓ Combined 5 chapters into: extracted_manuscript_20251105.md (28,543 words)
📖 Narrative content detected - Codex validation will be applied

🔍 Validating against Codex...
✓ Loaded: PROJECT_CODEX.md
✓ Validated: Manuscript chapters
✓ Status: Mostly compliant, 3 suggestions
✓ Report: codex_validation_20251105.md

🚀 Creating action plan with Codex integration...
✓ Quest: Complete Act II with Codex Compliance
✓ Plan: Ship-Learn-Next Plan - Act II Manuscript.md

✅ Complete!
📖 Validation found:
   ✓ AEGIS voice is tragic and correct (Section 2.1)
   ✓ Alter voices are distinct (Section 2.2.1)
   ⚠️  Consider: More Kernwelt sensory detail in Ch 15 (Section 3.2)
   ⚠️  Consider: Kiko's voice could be more childlike (Section 2.2.1)
   ⚠️  Consider: Risse manifestation needs 4-step chain (Section 3.1)

🎯 Rep 1: Address Ch 15 Kernwelt descriptions
📖 Review: Codex Section 3.2 (Kernwelten sensory signatures)
When will you ship Rep 1?
```

### Example 5: Interactive Mode (NEW)

```
User: tapestry

Claude:
🧵 Tapestry - What would you like to extract?

Options:
  1. URL (YouTube, article, PDF)
  2. Local file or directory
  3. Repo content (manuscript, world, characters)
  4. Exit

Choose (1-4): 3

Repo content options:
  a. Manuscript (kohaerenz_protokoll/manuscript)
  b. World-building (kohaerenz_protokoll/world)
  c. Characters (kohaerenz_protokoll/world/characters)
  d. Narrative Design (kohaerenz_protokoll/narrative_design)
  e. Project Codex (kohaerenz_protokoll/PROJECT_CODEX.md)

Choose (a-e): b

[Continues with repo directory extraction...]
```

## Narrative Detection Rules

Tapestry automatically detects narrative content and applies Codex validation when:

**File Content Indicators:**
- Contains keywords: AEGIS, Kael, Kernwelt, alter, Kohärenz, Risse, dissociative
- File path includes: kohaerenz_protokoll/, manuscript/, world/, characters/
- File mentions: Protocol, System Kael, trauma-dissociation, functional multiplicity

**When Detected:**
- Load PROJECT_CODEX.md
- Perform validation workflows
- Generate validation report
- Integrate Codex constraints into plan
- Include canonical references

**When NOT Detected:**
- Skip Codex validation
- Create standard Ship-Learn-Next plan
- Focus on technical/learning implementation

## Error Handling

### Common Issues:

**1. Path not found**
```
❌ Path not found: /path/to/file
Suggestions:
  - Check if path exists: ls /path/to/
  - Use relative path from repo root
  - Try repo keyword instead: tapestry manuscript
```

**2. No markdown files in directory**
```
⚠️  No .md files found in directory
Found: [list other file types]
Extract anyway? (y/n)
```

**3. Codex not found**
```
⚠️  PROJECT_CODEX.md not found
Narrative validation disabled
Continue without Codex? (y/n)
```

**4. URL extraction failed**
[Keep existing error handling from original]

**5. Empty content extracted**
```
❌ No content extracted
- File may be empty
- Directory may have no .md files
- URL may require authentication
Try different source? (y/n)
```

## Best Practices

### For All Content:
- ✅ Always show detected source type
- ✅ Display progress at each step
- ✅ Save extracted content before planning
- ✅ Show preview of content (first 10 lines)
- ✅ Present clear summary at end

### For Narrative Content:
- ✅ Always run Codex validation
- ✅ Generate detailed validation report
- ✅ Include Codex references in plan
- ✅ Cite specific sections (e.g., "Section 2.1")
- ✅ Provide actionable recommendations
- ✅ Don't just flag issues - explain why

### For Planning:
- ✅ Create plan automatically (don't ask)
- ✅ Make Rep 1 shippable this week
- ✅ Include validation checkpoints
- ✅ Ask commitment question at end

## Dependencies

**Core (Required):**
- Bash (for orchestration)
- Read tool (for file access)
- Write tool (for saving outputs)

**Local Sources (NEW):**
- Glob tool (for directory scanning)
- Grep tool (for narrative detection)
- find command (for file discovery)

**External URLs (Original):**
- yt-dlp (YouTube - auto-installed)
- curl (URLs - built-in)
- pdftotext (PDFs - optional)
- reader/trafilatura (Articles - fallback available)

**Narrative Validation (NEW):**
- Access to kohaerenz_protokoll/PROJECT_CODEX.md
- Read tool for Codex sections
- Validation workflows from codex skill

## Integration with Other Skills

**Tapestry orchestrates:**
- **YouTube/Article/PDF extractors** - For external content
- **File readers** - For local content
- **Codex skill** - For narrative validation
- **Ship-Learn-Next** - For action planning

**Tapestry provides:**
- Unified interface for all content sources
- Automatic source type detection
- Narrative vs. technical content routing
- Integrated validation + planning

**Use Tapestry as entry point, it delegates to specialists.**

## Philosophy

**Tapestry weaves all sources into action.**

Whether from the web or your repository, whether technical tutorial or narrative manuscript, Tapestry extracts it, validates it (when needed), and creates an actionable plan.

**For narrative work:** Codex ensures canonical compliance.
**For learning work:** Ship-Learn-Next ensures practical application.
**For all work:** Extract → Validate → Plan → Ship → Learn → Next.

That's the enhanced Tapestry way.

---

**Version**: 2.0.0
**Added**: Local file support, repo keyword mapping, Codex integration
**Maintains**: Full backward compatibility with URL extraction
