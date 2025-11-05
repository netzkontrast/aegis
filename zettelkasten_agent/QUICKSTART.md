# Zettelkasten-Agent MVP - Quick Start Guide

Get up and running with the Zettelkasten-Agent in 5 minutes.

## Prerequisites

- Python 3.10+
- An Anthropic API key ([Get one here](https://console.anthropic.com/))

## Installation

```bash
# 1. Navigate to the project directory
cd zettelkasten_agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API key
export ANTHROPIC_API_KEY="your-api-key-here"
```

## First Run

```bash
# Start the agent
python agent.py
```

You'll see:
```
============================================================
Zettelkasten-Agent MVP
============================================================
Starting interactive mode...
Type '/help' for available commands
Type '/exit' to quit
============================================================
```

## Quick Test

### 1. Check Your Knowledge Base

In the interactive prompt, type:
```
What's in my knowledge base?
```

The agent will read `_INDEX.md` and report that the knowledge base is empty and ready for content.

### 2. Add Your First Source Note

Create a simple source note to test the system:

```bash
# In a new terminal window (keep the agent running)
cat > vault/SRC-20240115120000.md << 'EOF'
---
id: SRC-20240115120000
created: 2024-01-15T12:00:00
note_type: SRC
source_uri: https://en.wikipedia.org/wiki/Zettelkasten
status: unprocessed
---

# The Zettelkasten Method

The Zettelkasten method is a knowledge management system developed by
sociologist Niklas Luhmann. The word "Zettelkasten" is German for "slip box."

Key principles:
1. Atomicity: Each note contains one idea
2. Connectivity: Notes are densely linked
3. Autonomy: Each note is self-contained

Luhmann used this system to write over 70 books and 400 articles.
EOF
```

### 3. Process the Source

Back in the agent prompt:
```
Process the unprocessed source notes
```

The agent will:
1. Find your source note
2. Analyze it using the critical thinking framework
3. Create 3-5 atomic Zettel notes
4. Create a MOC for "Zettelkasten"
5. Update the `_INDEX.md`
6. Log everything to `_LOG.md`

### 4. Verify the Results

Check what was created:
```bash
ls vault/
```

You should now see:
- `SRC-20240115120000.md` (your source, now marked as "processed")
- `ZTL-*.md` (multiple atomic notes created by the agent)
- `MOC-Zettelkasten.md` (a map organizing the new notes)
- `_INDEX.md` (updated with link to the new MOC)
- `_LOG.md` (records of all actions)

### 5. Query Your Knowledge

Ask the agent a question:
```
What are the key principles of the Zettelkasten method?
```

The agent will:
1. Read `_INDEX.md`
2. Navigate to `MOC-Zettelkasten.md`
3. Read relevant Zettel notes
4. Synthesize an answer
5. Create a new Zettel with the synthesis

## Next Steps

### Add More Sources

Create more source notes by:
1. Copy-pasting articles into new `SRC-*.md` files
2. Using the timestamp format: `SRC-YYYYMMDDHHMMSS.md`
3. Setting `status: unprocessed`
4. Running "Process the unprocessed source notes"

### Explore Your Graph

```bash
# View the master index
cat vault/_INDEX.md

# View a specific MOC
cat vault/MOC-Zettelkasten.md

# View the action log
cat vault/_LOG.md
```

### Use with Obsidian

The vault is fully compatible with Obsidian:
1. Open Obsidian
2. "Open folder as vault"
3. Select the `vault/` directory
4. Enable graph view to visualize connections

## Common Commands

In the interactive agent prompt:

- `"What topics do I have in my knowledge base?"`
- `"Process unprocessed sources"`
- `"How does [concept A] relate to [concept B]?"`
- `"Show me what you did today"` (reads `_LOG.md`)
- `/exit` to quit

## Troubleshooting

### "API key not found"
```bash
# Make sure it's exported
echo $ANTHROPIC_API_KEY
```

### "Module not found"
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### "MCP server connection failed"
```bash
# Install uv for the MCP server
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## What's Happening Behind the Scenes?

When you ask the agent to process a source:

1. **Prioritizer Agent**: Selects which source to process
2. **Analyzer Agent**: Applies critical thinking framework (Factual → Inferential → Generative)
3. **Synthesizer-Generator Agent**: Creates atomic Zettel notes in its own words
4. **Integrator Agent**: Organizes notes into MOCs and updates the index

All file operations go through the MCP server, which enforces:
- Correct filename conventions
- Valid YAML metadata
- Bidirectional linking
- Schema validation

## Need Help?

- Read the full [README.md](README.md) for detailed documentation
- Check the [architectural blueprint](../README.md) for system design
- Open an issue on the repository

---

**Happy knowledge gardening! 🌱**
