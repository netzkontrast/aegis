# Content Extraction Module

**Purpose:** Extract content from URLs (YouTube, articles, PDFs) into text files.

This module provides pure content extraction without planning or knowledge management.
It can be used standalone or as part of larger workflows.

---

## Function: extract_content(URL)

**Input:** URL (string)
**Output:** Path to extracted content file (string)

### Step 1: Detect Content Type

```bash
URL="$1"

# Validate URL
if [ -z "$URL" ]; then
    echo "Error: No URL provided"
    return 1
fi

# Check for YouTube
if [[ "$URL" =~ youtube\.com/watch || "$URL" =~ youtu\.be/ || "$URL" =~ youtube\.com/shorts || "$URL" =~ m\.youtube\.com/watch ]]; then
    CONTENT_TYPE="youtube"

# Check for PDF
elif [[ "$URL" =~ \.pdf$ ]]; then
    CONTENT_TYPE="pdf"

# Check if URL returns PDF Content-Type
elif curl -sI "$URL" 2>/dev/null | grep -iq "Content-Type: application/pdf"; then
    CONTENT_TYPE="pdf"

# Default to article
else
    CONTENT_TYPE="article"
fi

echo "📍 Detected: $CONTENT_TYPE"
```

---

## Step 2: Extract Based on Type

### YouTube Video Extraction

```bash
extract_youtube() {
    local URL="$1"

    echo "📺 Extracting YouTube transcript..."

    # 1. Check for yt-dlp
    if ! command -v yt-dlp &> /dev/null; then
        echo "⚙️  Installing yt-dlp..."
        if command -v brew &> /dev/null; then
            brew install yt-dlp
        elif command -v pip3 &> /dev/null; then
            pip3 install yt-dlp
        else
            echo "❌ Error: Cannot install yt-dlp. Please install manually:"
            echo "   brew install yt-dlp  (macOS)"
            echo "   pip3 install yt-dlp  (Linux)"
            return 1
        fi
    fi

    # 2. Get video title (clean filename)
    VIDEO_TITLE=$(yt-dlp --print "%(title)s" "$URL" 2>/dev/null | tr '/' '_' | tr ':' '-' | tr '?' '' | tr '"' '' | tr '<' '' | tr '>' '' | tr '|' '' | tr '*' '')

    if [ -z "$VIDEO_TITLE" ]; then
        echo "❌ Error: Could not fetch video title. Check URL or network connection."
        return 1
    fi

    # 3. Download transcript
    yt-dlp --write-auto-sub --skip-download --sub-langs en --output "temp_transcript" "$URL" 2>/dev/null

    if [ ! -f "temp_transcript.en.vtt" ]; then
        echo "❌ Error: Could not download transcript. Video may not have captions."
        return 1
    fi

    # 4. Convert VTT to clean text (deduplicate lines)
    python3 -c "
import sys, re
seen = set()
vtt_file = 'temp_transcript.en.vtt'
try:
    with open(vtt_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('WEBVTT') and not line.startswith('Kind:') and not line.startswith('Language:') and '-->' not in line:
                clean = re.sub('<[^>]*>', '', line)
                clean = clean.replace('&amp;', '&').replace('&gt;', '>').replace('&lt;', '<')
                if clean and clean not in seen:
                    print(clean)
                    seen.add(clean)
except FileNotFoundError:
    print('Error: Could not find transcript file', file=sys.stderr)
    sys.exit(1)
" > "${VIDEO_TITLE}.txt"

    # 5. Cleanup temp files
    rm -f temp_transcript.en.vtt temp_transcript.*.vtt

    # 6. Return filename
    echo "${VIDEO_TITLE}.txt"
}
```

---

### Article/Blog Post Extraction

```bash
extract_article() {
    local URL="$1"

    echo "📄 Extracting article content..."

    # 1. Determine available extraction tool
    if command -v reader &> /dev/null; then
        TOOL="reader"
    elif command -v trafilatura &> /dev/null; then
        TOOL="trafilatura"
    else
        TOOL="fallback"
    fi

    echo "   Using: $TOOL"

    # 2. Extract based on tool
    case $TOOL in
        reader)
            # Mozilla Readability (best quality)
            reader "$URL" > temp_article.txt 2>/dev/null

            if [ ! -s temp_article.txt ]; then
                echo "❌ Error: Could not extract content with reader"
                return 1
            fi

            ARTICLE_TITLE=$(head -n 1 temp_article.txt | sed 's/^# //' | tr '/' '-' | tr ':' '-' | tr '?' '' | tr '"' '')
            ;;

        trafilatura)
            # Trafilatura (good quality, Python)
            METADATA=$(trafilatura --URL "$URL" --json 2>/dev/null)
            ARTICLE_TITLE=$(echo "$METADATA" | python3 -c "import json, sys; data=json.load(sys.stdin); print(data.get('title', 'Article'))" 2>/dev/null)

            trafilatura --URL "$URL" --output-format txt --no-comments > temp_article.txt 2>/dev/null

            if [ ! -s temp_article.txt ]; then
                echo "❌ Error: Could not extract content with trafilatura"
                return 1
            fi
            ;;

        fallback)
            # Fallback: Basic HTML parsing with curl + Python
            echo "⚠️  No extraction tools found. Using basic fallback."
            echo "   For better results, install:"
            echo "   - reader: npm install -g @mozilla/readability-cli"
            echo "   - trafilatura: pip3 install trafilatura"

            # Get title from HTML
            ARTICLE_TITLE=$(curl -sL "$URL" | grep -oP '<title>\K[^<]+' | head -n 1 | sed 's/ - .*//' | tr '/' '-' | tr ':' '-' | tr '?' '' | tr '"' '')

            if [ -z "$ARTICLE_TITLE" ]; then
                ARTICLE_TITLE="Article"
            fi

            # Extract content
            curl -sL "$URL" | python3 -c "
from html.parser import HTMLParser
import sys

class ArticleExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.content = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside', 'form'}
        self.in_content = False
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
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

            if [ ! -s temp_article.txt ]; then
                echo "❌ Error: Could not extract content from URL"
                return 1
            fi
            ;;
    esac

    # 3. Clean filename and save
    FILENAME=$(echo "$ARTICLE_TITLE" | cut -c 1-80 | sed 's/ *$//')
    CONTENT_FILE="${FILENAME}.txt"
    mv temp_article.txt "$CONTENT_FILE"

    # 4. Return filename
    echo "$CONTENT_FILE"
}
```

---

### PDF Document Extraction

```bash
extract_pdf() {
    local URL="$1"

    echo "📑 Extracting PDF content..."

    # 1. Download PDF
    PDF_FILENAME=$(basename "$URL" | sed 's/%20/ /g')

    if [ -z "$PDF_FILENAME" ] || [[ ! "$PDF_FILENAME" =~ \.pdf$ ]]; then
        PDF_FILENAME="document.pdf"
    fi

    echo "   Downloading: $PDF_FILENAME"
    curl -L -o "$PDF_FILENAME" "$URL" 2>/dev/null

    if [ ! -f "$PDF_FILENAME" ]; then
        echo "❌ Error: Could not download PDF"
        return 1
    fi

    # 2. Extract text using pdftotext
    if command -v pdftotext &> /dev/null; then
        CONTENT_FILE="${PDF_FILENAME%.pdf}.txt"
        pdftotext "$PDF_FILENAME" "$CONTENT_FILE" 2>/dev/null

        if [ -s "$CONTENT_FILE" ]; then
            echo "✓ Extracted text from PDF: $CONTENT_FILE"

            # Ask if user wants to keep PDF
            echo ""
            echo "Keep original PDF? (y/n)"
            read -r KEEP_PDF
            if [[ ! "$KEEP_PDF" =~ ^[Yy]$ ]]; then
                rm "$PDF_FILENAME"
                echo "   Removed PDF, kept text file"
            fi

            echo "$CONTENT_FILE"
        else
            echo "⚠️  PDF extracted but appears empty. PDF may be scanned/image-based."
            echo "   Keeping PDF: $PDF_FILENAME"
            echo "$PDF_FILENAME"
        fi
    else
        # No pdftotext available
        echo "⚠️  pdftotext not found. PDF downloaded but not extracted."
        echo "   Install with:"
        echo "   - macOS: brew install poppler"
        echo "   - Linux: apt install poppler-utils"
        echo ""
        echo "   Keeping PDF: $PDF_FILENAME"
        echo "$PDF_FILENAME"
    fi
}
```

---

## Main Extraction Function

```bash
extract_content() {
    local URL="$1"
    local CONTENT_TYPE
    local CONTENT_FILE

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
            CONTENT_FILE=$(extract_youtube "$URL")
            ;;
        article)
            CONTENT_FILE=$(extract_article "$URL")
            ;;
        pdf)
            CONTENT_FILE=$(extract_pdf "$URL")
            ;;
    esac

    # Verify extraction
    if [ -z "$CONTENT_FILE" ] || [ ! -f "$CONTENT_FILE" ]; then
        echo ""
        echo "❌ Extraction failed. Could not create content file."
        return 1
    fi

    # Show success
    WORD_COUNT=$(wc -w < "$CONTENT_FILE")
    echo ""
    echo "✓ Content extracted successfully!"
    echo "  File: $CONTENT_FILE"
    echo "  Size: $WORD_COUNT words"
    echo ""

    # Return the filename (for use by other modules)
    echo "$CONTENT_FILE"
    return 0
}
```

---

## Usage

### Standalone Usage
```bash
# Extract YouTube video
CONTENT_FILE=$(extract_content "https://youtube.com/watch?v=xxx")

# Extract article
CONTENT_FILE=$(extract_content "https://example.com/article")

# Extract PDF
CONTENT_FILE=$(extract_content "https://example.com/paper.pdf")

# Check if extraction succeeded
if [ $? -eq 0 ]; then
    echo "Success! Content saved to: $CONTENT_FILE"
else
    echo "Extraction failed"
fi
```

### As Module (called by other commands)
```bash
# Source this module
source .claude/commands/_modules/extract-content.md

# Use the extraction function
CONTENT_FILE=$(extract_content "$URL")
```

---

## Error Handling

**Common errors:**
- **No URL provided:** Returns error code 1
- **Unsupported URL type:** Falls back to article extraction
- **Network issues:** Returns error with clear message
- **Missing dependencies:** Attempts auto-install, or provides install instructions
- **Empty extraction:** Returns error, asks user to verify URL

---

## Dependencies

### YouTube
- `yt-dlp` (auto-installed if missing)
- `python3` (for VTT parsing)

### Articles
- `reader` (npm, optional - best quality)
- `trafilatura` (pip3, optional - good quality)
- `curl` + `python3` (fallback - basic quality)

### PDFs
- `curl` (built-in on most systems)
- `pdftotext` from `poppler` package (optional but recommended)
  - macOS: `brew install poppler`
  - Linux: `apt install poppler-utils`

---

## Philosophy

This module does ONE thing well: **extract content from URLs into text files.**

It doesn't:
- Create action plans (see action-planner module)
- Manage knowledge (see knowledge-manager module)
- Make assumptions about what you'll do with the content

It's a building block for larger workflows.
