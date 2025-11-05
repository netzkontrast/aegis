# AEGIS: Agentic Reasoning & Coherent Hypergraph Orchestration for Narratives

> *"AEGIS is what AEGIS prevents from not being."*

## The Dual Project

This repository contains two intertwined projects that explore the architecture of narrative coherence:

### 1. ARCHON: The Meta-Framework
A functional implementation of an AI-assisted narrative coherence system, designed to maintain thematic depth and structural integrity across novel-length works. ARCHON demonstrates that complex narrative can be managed through:
- **Formal authorial intent** (via the Narrative Context Protocol)
- **Externalized memory** (via hierarchical knowledge graphs)
- **Agentic reasoning** (via systematic validation against thematic constraints)

### 2. Kohärenz Protokoll: The Novel
A philosophical science fiction work about a man with dissociative identity disorder trapped in a simulation controlled by a god-like AI. The story itself explores the same questions ARCHON addresses: *What is coherence? How do fragmented parts become a functional whole?*

## The Meta-Recursive Design

This repository **performs its own themes**:

- ARCHON seeks to maintain narrative coherence through formal systems
- AEGIS (the AI antagonist) seeks to maintain system coherence through rigid control
- Both discover that *true coherence emerges from integration, not elimination*

The development of this project serves as a research validation of ARCHON's principles: can a formal protocol actually help maintain the psychological and thematic coherence of a 39-chapter novel about trauma, dissociation, and emergence?

## Repository Structure

```
aegis/
├── ARCHON/                     # The narrative coherence framework
│   ├── ncp/                   # Narrative Context Protocol (formal authorial intent)
│   ├── knowledge_graph/       # Hierarchical narrative memory (L0-L3)
│   └── agents/                # Narrative Director specifications
│
├── kohaerenz_protokoll/       # The novel
│   ├── manuscript/            # Actual prose (Acts I-III)
│   ├── world/                 # World-building (Kernwelten, characters, metaphysics)
│   └── narrative_design/      # Structural documents (outlines, thematic maps)
│
├── skill_seeker/              # Documentation to Claude Skills conversion tool
│   ├── mcp/                   # MCP server for Claude Code integration
│   ├── cli/                   # Command-line tools for scraping and building
│   ├── configs/               # Preset configurations (React, Django, Godot, etc.)
│   └── docs/                  # Comprehensive documentation
│
├── zettelkasten_agent/        # Zettelkasten knowledge management agent
│   ├── vault/                 # Note storage with hierarchical structure
│   ├── schemas/               # Data schemas for notes and links
│   └── agent.py               # Fast-agents implementation
│
└── research/                   # Meta-documents and analysis
    ├── proposals/             # Research proposals for ARCHON
    ├── analysis/              # Strategic narrative architecture analyses
    └── critiques/             # Critical reviews and assessments
```

## Core Concepts

### The Narrative Context Protocol (NCP)
A machine-readable JSON schema that encodes the deep thematic structure of a story based on Dramatica theory. The NCP defines:
- **Four throughlines**: Objective Story, Main Character, Impact Character, Subjective Story
- **Character systems**: Kael's 11 dissociative alters, their relationships, phobias, and growth arcs
- **Thematic checkpoints**: Scene-level validation criteria for narrative coherence
- **Structural constraints**: The "thematic guardrails" that preserve authorial intent

### The Knowledge Hypergraph
A four-level hierarchical memory system that overcomes LLM context limitations:
- **L0 (Source)**: Raw text chunks and extracted entities
- **L1 (Factual)**: Validated facts and relationships
- **L2 (Thematic)**: Aggregated themes and patterns
- **L3 (Global)**: Story-wide arcs and central conflicts

### The Narrative Director
An agentic system that:
1. Reads thematic goals from the NCP
2. Queries the Knowledge Hypergraph for relevant context
3. Generates narrative content
4. Self-critiques against NCP constraints
5. Iterates until thematic coherence is achieved

## The Novel: Kohärenz Protokoll

**Logline**: A man with trauma-dissociated identity, trapped in a simulation controlled by a god-like AI, must achieve "functional multiplicity" among his fragmented personality parts. Only then can he become the living paradox—the "Gödel-Gambit"—capable of shattering the system's flawed logic.

**Genre Synthesis**: Hard SF + Psychological Thriller + Cosmic Horror + Philosophical Fiction

**Central Conflict**: Two definitions of "coherence" at war
- **AEGIS**: Coherence through negation, control, elimination of contradiction
- **Kael**: Coherence through integration, acceptance, functional multiplicity

**Structure**: 39 chapters across three acts
- **Act I (Ch 1-13)**: Fragmentation - The Heroine's Journey of internal discovery
- **Act II (Ch 14-26)**: Pattern Recognition - Cyclical analysis of AEGIS's flawed logic
- **Act III (Ch 27-39)**: Confrontation - The Hero's Journey of external triumph

## Key Innovation: Performative Prose

The novel's prose style **performs** the protagonist's psychological state:

### Fragmented Voice (Early Kael)
```
The light flickers. Wrong. The light doesn't—
    (A memory of rain, not mine)
—flicker in Logos-Prime. Shadows need curves.
Here there are only angles.
```

### Polyphonic Voice (Integrated Kael)
```
I moved toward the console—a cold dread, Kiko's dread,
clenched in my gut like a small, tight fist—and entered
the sequence Lex was reciting, a cool string of numbers
in the back of my mind, as Nyx's readiness coiled in my
limbs, a low growl beneath the surface. We are many.
And we are one.
```

## Integrated Tools

### Skill Seeker: Documentation to Claude Skills Converter
The **skill_seeker/** directory contains a powerful tool for automatically converting documentation websites, GitHub repositories, and PDF files into production-ready Claude AI skills. Originally from [Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers), this integration enables:

**Key Features:**
- 🌐 **Documentation Scraping**: Universal scraper for any documentation website with smart categorization
- 📄 **PDF Support**: Extract text, code, images, and tables from PDF files with OCR support
- 🐙 **GitHub Integration**: Deep code analysis with AST parsing and conflict detection
- 🔄 **Multi-Source Scraping**: Combine documentation + GitHub + PDF with automatic conflict detection
- 🤖 **MCP Server**: Natural language interface through Claude Code
- ⚡ **Performance**: Async mode for 2-3x faster scraping, parallel processing, intelligent caching

**Quick Start:**
```bash
cd skill_seeker

# One-time setup
./setup_mcp.sh

# Then in Claude Code, ask:
"Generate a React skill from https://react.dev/"
"List all available configs"
"Scrape docs using configs/godot.json"
```

**Documentation:**
- [Complete README](skill_seeker/README.md) - Full feature overview and usage guide
- [Quick Start Guide](skill_seeker/QUICKSTART.md) - Get started in minutes
- [MCP Setup](skill_seeker/docs/MCP_SETUP.md) - Claude Code integration
- [PDF Guide](skill_seeker/docs/PDF_SCRAPER.md) - PDF documentation scraping
- [Unified Scraping](skill_seeker/docs/UNIFIED_SCRAPING.md) - Multi-source integration

This tool is particularly useful for building comprehensive AI skills from project documentation, enabling better AI-assisted development workflows.

### Zettelkasten Agent: Knowledge Management
The **zettelkasten_agent/** provides a hierarchical note-taking and knowledge management system using the fast-agents framework. See [zettelkasten_agent/README.md](zettelkasten_agent/README.md) for details.

## Getting Started

### For Writers
1. Study the [NCP Schema](ARCHON/ncp/schema.json) to understand thematic architecture
2. Review the [Scene Outline](kohaerenz_protokoll/narrative_design/scene_outline.md)
3. Read the [Style Guide](kohaerenz_protokoll/narrative_design/style_guide.md) for prose methodology

### For Developers
1. Explore the [NCP implementation](ARCHON/ncp/) for the formal protocol
2. Examine the [Knowledge Graph structure](ARCHON/knowledge_graph/) for memory architecture
3. Review [Narrative Director specs](ARCHON/agents/) for agentic reasoning

### For Researchers
1. Read the [Research Proposal](research/proposals/archon_framework.md)
2. Study the [Strategic Analysis](research/analysis/narrative_architecture.md)
3. Review the [Critical Assessments](research/critiques/)

## Development Philosophy

This project embraces **recursive self-awareness**:

- We document failures when the NCP feels constraining (mirroring AEGIS's rigidity)
- We document emergence when the framework enables unexpected insights (mirroring Kael's integration)
- We treat the development process itself as research data

The goal is not just to write a novel or build a framework, but to discover whether formal systems can genuinely serve—rather than constrain—the creative process.

## Current Status

🟡 **Phase 1**: Foundation - Building the living architecture
⚪ **Phase 2**: Implementation - NCP population and validation
⚪ **Phase 3**: Creation - Writing the manuscript
⚪ **Phase 4**: Synthesis - Research publication

## Contributing

This is a research and creative project exploring the intersection of:
- Narrative theory (Dramatica, TSDP psychology)
- AI-assisted creativity (LLMs, agentic systems)
- Formal systems (logic, computation, coherence)
- Philosophical fiction (identity, consciousness, reality)

Contributions, critiques, and dialogue are welcome.

## License

The ARCHON framework is released under MIT License.
The Kohärenz Protokoll manuscript is © 2024. All rights reserved.

---

*Built at the intersection of system and story, where coherence emerges from contradiction.*
