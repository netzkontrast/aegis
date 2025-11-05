# Zettelkasten-Agent MVP

A recursive knowledge synthesizer built with the fast-agents framework that implements a self-organizing digital knowledge garden based on the Zettelkasten method.

## Overview

The Zettelkasten-Agent is an AI-powered knowledge management system that transforms raw information into a densely interconnected network of atomic ideas. It's not a passive archiver but an active thinking partner that understands, synthesizes, and generates insights through a structured cognitive loop.

### Key Features

- **Automated Knowledge Synthesis**: Processes source materials through a four-phase cognitive loop
- **Atomic Note Creation**: Breaks down complex texts into self-contained, interconnected ideas (Zettel)
- **Dynamic Knowledge Graph**: Automatically organizes notes using Maps of Content (MOCs)
- **Critical Analysis Framework**: Applies three levels of understanding (Factual, Inferential, Generative)
- **Schema-Validated Architecture**: Enforces note taxonomy through Pydantic validation
- **Multi-Agent Workflow**: Specialized agents for prioritization, analysis, synthesis, and integration

## Architecture

The system follows a layered architecture:

1. **Configuration Layer** (`fastagent.config.yaml`): LLM provider and MCP server configuration
2. **Tool Layer** (`zettelkasten_tools_mcp.py`): MCP server providing all file system operations
3. **Schema Layer** (`schemas/note_schemas.py`): Pydantic models enforcing note taxonomy
4. **Agent Layer** (`agent.py`): Multi-agent orchestrator implementing the cognitive loop
5. **Knowledge Layer** (`vault/`): The actual Markdown-based knowledge base

### Note Taxonomy

The system supports three types of notes:

- **Source Notes (SRC)**: Raw, unprocessed information from external sources
  - Filename: `SRC-<YYYYMMDDHHMMSS>.md`
  - Status: `unprocessed`, `processing`, or `processed`

- **Atomic Notes (ZTL)**: Single, self-contained ideas in your own words
  - Filename: `ZTL-<YYYYMMDDHHMMSS>.md`
  - Must have a declarative, self-explanatory title

- **Maps of Content (MOC)**: Structuring overview documents
  - Filename: `MOC-<Topic>.md`
  - Organize related notes around a theme

### Special Files

- **`_INDEX.md`**: The master index, the "MOC of MOCs"
- **`_LOG.md`**: Chronological protocol of all agent actions and decisions

## Installation

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (fast Python package installer)
- Anthropic API key (for Claude access)

### Setup Steps

1. **Clone or navigate to the project directory:**

```bash
cd zettelkasten_agent
```

2. **Install uv (if not already installed):**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. **Install dependencies:**

```bash
uv pip install -r requirements.txt
```

Or create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

4. **Set up your Anthropic API key:**

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Or add it to your `.env` file or shell profile for persistence.

5. **Verify the installation:**

```bash
ls vault/
# Should show: _INDEX.md  _LOG.md
```

## Usage

### Starting the Agent

Run the agent in interactive mode:

```bash
python agent.py
```

This will start an interactive command-line interface where you can:
- Ask questions about your knowledge base
- Request analysis of source materials
- Query the state of your knowledge graph
- Manually trigger the synthesis loop

### Basic Workflow

#### 1. Add a Source Note

Create a new source note manually or programmatically:

```bash
# Example: Create a source note about quantum computing
cat > vault/SRC-20240115120000.md << 'EOF'
---
id: SRC-20240115120000
created: 2024-01-15T12:00:00
note_type: SRC
source_uri: https://example.com/quantum-computing-intro
status: unprocessed
---

# Introduction to Quantum Computing

Quantum computing leverages quantum mechanical phenomena like superposition and entanglement...
[Your source content here]
EOF
```

#### 2. Trigger the Synthesis Loop

In the interactive session, request processing:

```
> Process the unprocessed source notes
```

The agent will:
1. **Prioritize**: Select the most valuable source to process
2. **Analyze**: Apply critical thinking framework to understand the content
3. **Synthesize**: Create 3-7 atomic Zettel notes in its own words
4. **Integrate**: Add the new notes to relevant MOCs and update the index

#### 3. Query Your Knowledge Base

Ask complex questions:

```
> How does quantum entanglement relate to quantum computing?
```

The agent will:
1. Start at `_INDEX.md`
2. Navigate to relevant MOCs
3. Read specific Zettel notes
4. Synthesize an answer
5. Create a new Zettel with the synthesis and link it into the graph

### Available Tools

The agent has access to these tools (via the MCP server):

- `create_note`: Create a new SRC, ZTL, or MOC note
- `read_note_content`: Read the full content of a note
- `get_note_metadata`: Read only the YAML frontmatter (low-cost)
- `append_link`: Add a contextual link with automatic reciprocal backlink
- `find_notes`: Search for notes by keyword or semantically
- `list_files`: List all notes, optionally filtered by type
- `log_action`: Append an entry to the action log

## The Cognitive Core Loop

The agent operates through a recursive four-phase cycle:

### Phase 1: Prioritization
- Scans for unprocessed sources
- Checks `_LOG.md` for user requests
- Applies prioritization matrix to select next task

### Phase 2: Analysis (Deconstruction)
- Applies critical thinking framework:
  - **Factual**: What are the core concepts?
  - **Inferential**: How do they relate? What are the assumptions?
  - **Generative**: What connections, questions, or critiques emerge?

### Phase 3: Synthesis & Generation
- Identifies 3-7 core ideas from the analysis
- Creates atomic Zettel notes in its own words
- Links notes to each other and to existing knowledge

### Phase 4: Integration (Structuring)
- Updates relevant MOCs
- Creates new MOCs when conceptual clusters reach critical mass (5-7+ notes)
- Updates `_INDEX.md`
- Logs completion

## Project Structure

```
zettelkasten_agent/
├── agent.py                    # Main agent with multi-agent workflow
├── zettelkasten_tools_mcp.py   # MCP server for all file operations
├── fastagent.config.yaml       # LLM and MCP configuration
├── requirements.txt            # Python dependencies
├── schemas/
│   └── note_schemas.py        # Pydantic validation schemas
├── vault/                     # The knowledge base
│   ├── _INDEX.md             # Master index
│   ├── _LOG.md               # Action log
│   ├── SRC-*.md              # Source notes
│   ├── ZTL-*.md              # Atomic notes
│   └── MOC-*.md              # Maps of Content
└── README.md                  # This file
```

## Design Philosophy

### The Digital Gardener

The agent embodies the philosophy of a digital gardener:

- **Plant Seeds**: Each source is a seed that grows into multiple Zettel
- **Cultivate Growth**: Link new ideas to existing ones, creating dense networks
- **Prune Redundancy**: Identify and consolidate duplicate concepts
- **Harvest Insights**: Use the structure to answer complex questions and generate syntheses

### Context Management via MOCs

Maps of Content serve as "semantic compression" - they allow the agent to reason about large knowledge bases without loading everything into its context window. The agent uses a "zoom-in" navigation strategy:

1. Start at the root (`_INDEX.md`)
2. Identify relevant MOCs
3. Read MOC summaries
4. Perform targeted deep dives on specific Zettel only when necessary

This mirrors how humans use a library index rather than reading every book.

## Advanced Features (Roadmap)

The MVP architecture provides hooks for future enhancements:

- **Semantic Search**: Upgrade `find_notes` to use vector embeddings
- **MOC_Tender Agent**: Scheduled maintenance agent for pruning broken links and weaving new connections
- **Visual Knowledge Graph**: The vault is compatible with Obsidian, Logseq, and other graph visualization tools
- **Multi-Agent Collaboration**: Share MOCs between agents for efficient knowledge transfer
- **Recursive Self-Improvement**: Agent analyzes its own logs to improve its synthesis process

## Technical Details

### Schema Validation

All notes are validated through Pydantic schemas before file creation. This ensures:
- Correct metadata fields for each note type
- Proper filename conventions
- Non-empty content
- Type safety

### Bidirectional Linking

The `append_link` tool automatically creates reciprocal backlinks:
```
Note A → "Related to concept X" → Note B
Note B → "Referenced by Note A" (automatic backlink)
```

This ensures the knowledge graph is always bidirectionally navigable.

### Timestamp-Based IDs

SRC and ZTL notes use timestamp-based IDs (`YYYYMMDDHHMMSS`) which:
- Guarantee uniqueness
- Encode chronology
- Are software-agnostic
- Avoid fragility of title-based linking

## Troubleshooting

### API Key Issues

```bash
# Verify your API key is set
echo $ANTHROPIC_API_KEY

# If empty, set it:
export ANTHROPIC_API_KEY="your-key"
```

### MCP Server Connection

If the agent can't connect to the MCP server:
1. Verify `uv` is installed: `uv --version`
2. Check that `zettelkasten_tools_mcp.py` exists
3. Ensure the vault directory exists: `ls vault/`

### Import Errors

If you see `ModuleNotFoundError`:
```bash
# Make sure you're in the right directory
pwd  # Should show: .../zettelkasten_agent

# Reinstall dependencies
pip install -r requirements.txt
```

## Contributing

This is a research implementation of the architectural blueprint described in the accompanying specification document. Contributions, improvements, and extensions are welcome.

### Future Work

- Implement the Bootstrapping Directive for initializing from existing Markdown files
- Add semantic search using sentence transformers
- Create the MOC_Tender maintenance agent
- Build a web UI for visualization
- Implement multi-agent collaboration patterns

## License

MIT License - See LICENSE file for details

## References

This implementation is based on:
1. The Zettelkasten method (Niklas Luhmann)
2. Fast-agents framework for MCP-native agents
3. Model Context Protocol (MCP) for tool integration
4. Digital Gardening philosophy
5. Critical thinking frameworks for text analysis

---

*"The agent is not just a tool - it is a collaborative thinking partner that helps you build a second brain."*
