---
name: learn
description: Unified learning workflow - extract content from URLs, create action plans, and optionally build knowledge graphs. Use when user wants to learn from any content source (YouTube, articles, PDFs, or existing files).
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
ui:
  component: "CommandForm"
  title: "Learn New Skill"
  description: "Extract knowledge from a URL or file."
  inputs:
    - name: "url"
      type: "text"
      label: "Source URL"
      placeholder: "https://example.com/article"
      required: true
    - name: "save"
      type: "boolean"
      label: "Save to Zettelkasten"
      default: false
---

# Learn Command - Unified Learning Workflow

**Your all-in-one learning command.**

Extract content → Create action plans → Build knowledge graphs

---

## Usage

```bash
/learn <URL>                      # Extract + Plan
/learn <URL> --save              # Extract + Plan + Save to Zettelkasten
/learn <file>                    # Plan from existing content
/learn <file> --save             # Plan + Save to Zettelkasten
```

**Flags:**
- `--save` or `-s`: Save to Zettelkasten knowledge vault
- `--extract-only`: Extract content without planning
- `--plan-only`: Assume content already extracted, just plan

---

## What This Command Does

### Mode 1: Extract + Plan (Default for URLs)
1. **Detect content type** (YouTube, article, PDF)
2. **Extract content** to text file
3. **Create Ship-Learn-Next action plan** with 5 reps
4. **Present results** and ask for commitment

**Use case:** "I found this great video/article and want to implement the advice"

---

### Mode 2: Extract + Plan + Zettelkasten (with --save)
1. **Extract content** from URL
2. **Create action plan** with 5 reps
3. **Create Source Note** (SRC) with metadata
4. **Extract atomic concepts** into Zettel notes (ZTL)
5. **Create Quest MOC** integrating the plan
6. **Connect to existing knowledge** in your vault
7. **Update vault index and log**

**Use case:** "I want to deeply learn this AND preserve the knowledge for future reference"

---

### Mode 3: Plan Only (Default for files)
1. **Read existing content file**
2. **Create Ship-Learn-Next action plan**
3. **Present results**

**Use case:** "I already have the content, just help me create an action plan"

---

### Mode 4: Plan + Zettelkasten (file with --save)
1. **Read existing content file**
2. **Create action plan**
3. **Save to Zettelkasten** (Source Note + Zettel + MOC)

**Use case:** "I have content and want to both plan and preserve knowledge"

---

## Implementation

### Step 1: Parse Input and Detect Mode

```bash
INPUT="$1"
FLAGS="$2"

# Validate input
if [ -z "$INPUT" ]; then
    echo "❌ Error: No input provided"
    echo ""
    echo "Usage:"
    echo "  /learn <URL>              # Extract content and create plan"
    echo "  /learn <URL> --save       # Extract + plan + save to Zettelkasten"
    echo "  /learn <file>             # Create plan from existing content"
    echo "  /learn <file> --save      # Plan + save to Zettelkasten"
    echo ""
    exit 1
fi

# Detect mode
if [[ "$INPUT" =~ ^https?:// ]]; then
    MODE="extract"
    URL="$INPUT"
elif [ -f "$INPUT" ]; then
    MODE="plan-only"
    CONTENT_FILE="$INPUT"
else
    echo "❌ Error: Input must be a URL or existing file"
    echo "   Got: $INPUT"
    exit 1
fi

# Check for save flag
SAVE_TO_VAULT=false
if [[ "$FLAGS" == "--save" ]] || [[ "$FLAGS" == "-s" ]] || [[ "$INPUT" =~ zettelkasten ]]; then
    SAVE_TO_VAULT=true
fi

# Check for extract-only flag
if [[ "$FLAGS" == "--extract-only" ]]; then
    EXTRACT_ONLY=true
else
    EXTRACT_ONLY=false
fi

# Check for plan-only flag (overrides auto-detection)
if [[ "$FLAGS" == "--plan-only" ]]; then
    MODE="plan-only"
fi

echo "🧵 Learn Command Starting..."
echo "   Mode: $MODE"
if [ "$SAVE_TO_VAULT" = true ]; then
    echo "   Save to Zettelkasten: Yes"
fi
echo ""
```

---

### Step 2: Execute Workflow Based on Mode

#### Mode: Extract Content (for URLs)

```bash
if [ "$MODE" = "extract" ]; then
    # Source the extract-content module
    # Note: In practice, we'll implement the extraction inline
    # but conceptually we're using the module

    echo "📥 Extracting content..."
    echo ""

    # Detect content type
    if [[ "$URL" =~ youtube\.com/watch || "$URL" =~ youtu\.be/ || "$URL" =~ youtube\.com/shorts || "$URL" =~ m\.youtube\.com/watch ]]; then
        CONTENT_TYPE="youtube"
    elif [[ "$URL" =~ \.pdf$ ]] || curl -sI "$URL" 2>/dev/null | grep -iq "Content-Type: application/pdf"; then
        CONTENT_TYPE="pdf"
    else
        CONTENT_TYPE="article"
    fi

    echo "📍 Detected: $CONTENT_TYPE"
    echo ""

    # Extract based on type
    case $CONTENT_TYPE in
        youtube)
            # YouTube extraction
            echo "📺 Extracting YouTube transcript..."

            # Check for yt-dlp
            if ! command -v yt-dlp &> /dev/null; then
                echo "⚙️  Installing yt-dlp..."
                if command -v brew &> /dev/null; then
                    brew install yt-dlp
                elif command -v pip3 &> /dev/null; then
                    pip3 install yt-dlp
                else
                    echo "❌ Error: Cannot install yt-dlp. Please install manually."
                    exit 1
                fi
            fi

            # Get video title
            VIDEO_TITLE=$(yt-dlp --print "%(title)s" "$URL" 2>/dev/null | tr '/' '_' | tr ':' '-' | tr '?' '' | tr '"' '' | tr '<' '' | tr '>' '' | tr '|' '' | tr '*' '')

            if [ -z "$VIDEO_TITLE" ]; then
                echo "❌ Error: Could not fetch video title"
                exit 1
            fi

            # Download transcript
            yt-dlp --write-auto-sub --skip-download --sub-langs en --output "temp_transcript" "$URL" 2>/dev/null

            if [ ! -f "temp_transcript.en.vtt" ]; then
                echo "❌ Error: Could not download transcript"
                exit 1
            fi

            # Convert to clean text
            python3 -c "
import sys, re
seen = set()
vtt_file = 'temp_transcript.en.vtt'
with open(vtt_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('WEBVTT') and not line.startswith('Kind:') and not line.startswith('Language:') and '-->' not in line:
            clean = re.sub('<[^>]*>', '', line)
            clean = clean.replace('&amp;', '&').replace('&gt;', '>').replace('&lt;', '<')
            if clean and clean not in seen:
                print(clean)
                seen.add(clean)
" > "${VIDEO_TITLE}.txt"

            rm -f temp_transcript.en.vtt temp_transcript.*.vtt
            CONTENT_FILE="${VIDEO_TITLE}.txt"
            ;;

        article)
            # Article extraction
            echo "📄 Extracting article content..."

            if command -v reader &> /dev/null; then
                TOOL="reader"
            elif command -v trafilatura &> /dev/null; then
                TOOL="trafilatura"
            else
                TOOL="fallback"
            fi

            echo "   Using: $TOOL"

            case $TOOL in
                reader)
                    reader "$URL" > temp_article.txt 2>/dev/null
                    ARTICLE_TITLE=$(head -n 1 temp_article.txt | sed 's/^# //' | tr '/' '-' | tr ':' '-' | tr '?' '' | tr '"' '')
                    ;;
                trafilatura)
                    METADATA=$(trafilatura --URL "$URL" --json 2>/dev/null)
                    ARTICLE_TITLE=$(echo "$METADATA" | python3 -c "import json, sys; data=json.load(sys.stdin); print(data.get('title', 'Article'))" 2>/dev/null)
                    trafilatura --URL "$URL" --output-format txt --no-comments > temp_article.txt 2>/dev/null
                    ;;
                fallback)
                    echo "⚠️  Using basic fallback extraction"
                    ARTICLE_TITLE=$(curl -sL "$URL" | grep -oP '<title>\K[^<]+' | head -n 1 | sed 's/ - .*//' | tr '/' '-' | tr ':' '-')
                    curl -sL "$URL" | python3 -c "
from html.parser import HTMLParser
import sys

class ArticleExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.content = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside', 'form'}
        self.in_content = False

    def handle_starttag(self, tag, attrs):
        if tag not in self.skip_tags and tag in {'p', 'article', 'main', 'div'}:
            self.in_content = True

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.in_content = False

    def handle_data(self, data):
        if self.in_content and data.strip() and len(data.strip()) > 20:
            self.content.append(data.strip())

    def get_content(self):
        return '\n\n'.join(self.content)

parser = ArticleExtractor()
parser.feed(sys.stdin.read())
print(parser.get_content())
" > temp_article.txt
                    ;;
            esac

            if [ ! -s temp_article.txt ]; then
                echo "❌ Error: Could not extract content"
                exit 1
            fi

            FILENAME=$(echo "$ARTICLE_TITLE" | cut -c 1-80 | sed 's/ *$//')
            CONTENT_FILE="${FILENAME}.txt"
            mv temp_article.txt "$CONTENT_FILE"
            ;;

        pdf)
            # PDF extraction
            echo "📑 Extracting PDF content..."

            PDF_FILENAME=$(basename "$URL" | sed 's/%20/ /g')
            if [[ ! "$PDF_FILENAME" =~ \.pdf$ ]]; then
                PDF_FILENAME="document.pdf"
            fi

            curl -L -o "$PDF_FILENAME" "$URL" 2>/dev/null

            if [ ! -f "$PDF_FILENAME" ]; then
                echo "❌ Error: Could not download PDF"
                exit 1
            fi

            if command -v pdftotext &> /dev/null; then
                CONTENT_FILE="${PDF_FILENAME%.pdf}.txt"
                pdftotext "$PDF_FILENAME" "$CONTENT_FILE" 2>/dev/null

                if [ -s "$CONTENT_FILE" ]; then
                    echo "✓ Extracted text from PDF"
                    rm "$PDF_FILENAME"
                else
                    echo "⚠️  PDF appears empty (may be scanned)"
                    CONTENT_FILE="$PDF_FILENAME"
                fi
            else
                echo "⚠️  pdftotext not found. Install: brew install poppler"
                CONTENT_FILE="$PDF_FILENAME"
            fi
            ;;
    esac

    # Show extraction results
    if [ -f "$CONTENT_FILE" ]; then
        WORD_COUNT=$(wc -w < "$CONTENT_FILE" 2>/dev/null || echo "0")
        echo ""
        echo "✅ Content Extracted!"
        echo "   File: $CONTENT_FILE"
        echo "   Size: $WORD_COUNT words"
        echo ""
    else
        echo "❌ Extraction failed"
        exit 1
    fi

    # If extract-only, stop here
    if [ "$EXTRACT_ONLY" = true ]; then
        echo "✅ Extract-only mode: Done!"
        exit 0
    fi
fi
```

---

### Step 3: Create Action Plan

```bash
# At this point, we have CONTENT_FILE (either extracted or provided)

echo "🚀 Creating Ship-Learn-Next action plan..."
echo ""

# Read content
if [ ! -f "$CONTENT_FILE" ]; then
    echo "❌ Error: Content file not found: $CONTENT_FILE"
    exit 1
fi

CONTENT=$(cat "$CONTENT_FILE")
WORD_COUNT=$(wc -w < "$CONTENT_FILE")

echo "   Analyzing $WORD_COUNT words..."
echo ""

# Analyze content and create plan
# This is where we would apply the action-planner module logic
# For now, we guide Claude to create the plan based on the content

# The plan creation happens through Claude's analysis
# Following the Ship-Learn-Next framework:
# 1. Extract core actionable lessons
# 2. Define a specific quest (4-8 weeks)
# 3. Design Rep 1 (shippable this week)
# 4. Map Reps 2-5 (progressive)
# 5. Connect to source content
# 6. Save as markdown file

echo "I'll now analyze this content and create a Ship-Learn-Next action plan."
echo ""
echo "First, let me understand what you want to achieve..."
echo ""
```

**At this point, Claude would:**
1. Read and analyze the content file
2. Ask the user about their goals
3. Create a structured 5-rep plan
4. Save the plan to a markdown file

---

### Step 4: Save to Zettelkasten (if --save flag)

```bash
if [ "$SAVE_TO_VAULT" = true ]; then
    echo ""
    echo "🧠 Saving to Zettelkasten..."
    echo ""

    # Set vault directory
    VAULT_DIR="/home/user/aegis/zettelkasten_agent/vault"

    # Ensure vault exists
    if [ ! -d "$VAULT_DIR" ]; then
        echo "📁 Creating Zettelkasten vault..."
        mkdir -p "$VAULT_DIR"
    fi

    # Create Source Note
    TIMESTAMP=$(date +"%Y%m%d-%H%M")
    TITLE=$(basename "$CONTENT_FILE" .txt | tr '_' ' ' | cut -c 1-60 | tr ' ' '-')

    SRC_FILE="SRC-${TIMESTAMP}-${TITLE}.md"
    SRC_PATH="${VAULT_DIR}/${SRC_FILE}"

    echo "📝 Creating Source Note..."

    cat > "$SRC_PATH" <<EOF
# Source: ${TITLE//-/ }

**Type:** Source Note (SRC)
**Created:** $(date +"%Y-%m-%d %H:%M")
**Status:** unprocessed
**URL:** ${URL:-"Local file"}

---

## Metadata

- **Content File:** [[${CONTENT_FILE}]]
- **Action Plan:** [[${PLAN_FILE}]]
- **Date Captured:** $(date +"%Y-%m-%d")

---

## Processing Notes

This source has been captured and is ready for cognitive processing.

### Next Steps:
- [ ] Read and analyze content deeply
- [ ] Extract atomic concepts (3-7 Zettel notes)
- [ ] Create Quest MOC
- [ ] Connect to existing knowledge
- [ ] Update status to 'processed'

---

## Related Notes

(To be added during processing)

EOF

    echo "✓ Source note created: $SRC_FILE"
    echo ""
    echo "📍 Saved to: $VAULT_DIR"
    echo ""
    echo "Next: Extract atomic concepts and create Zettel notes"
    echo "      (This requires deep cognitive processing)"
fi
```

---

### Step 5: Present Results

```bash
echo ""
echo "✅ Learn Workflow Complete!"
echo "================================"
echo ""
echo "📥 Content:"
echo "   ✓ File: $CONTENT_FILE"
echo "   ✓ Size: $(wc -w < "$CONTENT_FILE") words"
echo ""
echo "📋 Action Plan:"
echo "   ✓ File: $PLAN_FILE"
echo "   ✓ Quest: [Quest title]"
echo ""

if [ "$SAVE_TO_VAULT" = true ]; then
    echo "🧠 Knowledge Vault:"
    echo "   ✓ Source Note: $SRC_FILE"
    echo "   ✓ Location: $VAULT_DIR"
    echo ""
fi

echo "🎯 Your Quest: [One-line summary]"
echo ""
echo "📍 Rep 1 (This Week): [Rep 1 goal]"
echo ""
echo "❓ When will you ship Rep 1?"
echo ""
```

---

## Examples

### Example 1: Extract + Plan from YouTube

```
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
   Analyzing 1,234 words...

[Analysis and plan creation follows]
```

---

### Example 2: Extract + Plan + Zettelkasten

```
User: /learn https://example.com/article --save

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
   [Plan creation]

🧠 Saving to Zettelkasten...
📝 Creating Source Note...
✓ Source note created: SRC-20251105-1430-How-to-Build-a-SaaS.md

✅ Learn Workflow Complete!
```

---

### Example 3: Plan from Existing File

```
User: /learn article.txt

Claude:
🧵 Learn Command Starting...
   Mode: plan-only

🚀 Creating Ship-Learn-Next action plan...
   Analyzing 1,500 words...

[Plan creation follows]
```

---

## Philosophy

**One command. Any content. Actionable learning.**

Whether it's a YouTube video, an article, a PDF, or notes you already have - the `/learn` command helps you:

1. **Extract** content efficiently
2. **Plan** concrete action steps
3. **Preserve** knowledge for future reference

Extract → Plan → Ship → Learn → Next

That's the way.

---

## Modular Architecture

This command is built on three independent modules:

- **`_modules/extract-content.md`** - Pure content extraction
- **`_modules/action-planner.md`** - Ship-Learn-Next planning
- **`_modules/knowledge-manager.md`** - Zettelkasten management

Each module can be used standalone or composed together.

---

**Ready to learn? Just type `/learn` and a URL or file.**
