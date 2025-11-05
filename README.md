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
├── zettelkasten_agent/         # Knowledge synthesis system
│   ├── agent.py               # Multi-agent orchestrator (4-phase cognitive loop)
│   ├── zettelkasten_tools_mcp.py  # MCP server (7 core tools)
│   ├── vault/                 # Knowledge base (SRC/ZTL/MOC notes)
│   └── schemas/               # Pydantic validation for note types
│
├── skills/                     # Reusable skill library
│   ├── skill-authoring/       # Meta-skill for creating skills (TDD-based)
│   └── progressive-learning-zettelkasten/  # Progressive learning workflows
│
├── docs/                       # Documentation and analysis
│   ├── knowledge-extraction/  # Skill authoring synthesis (4 approaches)
│   ├── sessions/              # Brainstorming session notes
│   └── *.md                   # Design documents
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

### The Zettelkasten Agent

A multi-agent knowledge synthesis system that transforms raw information into an interconnected knowledge graph through a 4-phase cognitive loop:

**Four-Phase Synthesis:**
1. **Prioritization** - Selects unprocessed source notes
2. **Analysis** - Extracts factual, inferential, and generative concepts
3. **Synthesis** - Creates 3-7 atomic Zettel notes (agent's own words, not copy-paste)
4. **Integration** - Weaves notes into knowledge structure, updates MOCs

**Note Taxonomy:**
- **SRC (Source)** - Raw, unprocessed information from external sources
- **ZTL (Zettel)** - Atomic, self-contained ideas
- **MOC (Map of Content)** - Organizing overview documents

**The Tapestry:** Knowledge is woven, not piled. Each Zettel is a thread connecting to others, creating patterns (MOCs) that form a coherent whole (INDEX).

### The Skills Library

Reusable, progressive-disclosure skills for systematic work:

**skill-authoring** (Meta-Skill)
- TDD-based framework for creating skills
- Proportional rigor: testing severity matched to risk level
- Ethical persuasion framework with research backing
- Decision trees, rationalization counters, stopping criteria
- **Use when:** Creating or editing skills

**progressive-learning-zettelkasten** (Technique)
- 4-phase workflow: Survey → Focus → Synthesize → Extend
- 3 learning patterns: Depth Ladder, Breadth Spiral, Question-Driven
- Integration with Zettelkasten Agent
- Knowledge gap detection and systematic filling
- **Use when:** Learning complex domains, building knowledge progressively

Both skills apply the unified framework synthesized from four complementary approaches (TDD methodology, Anthropic best practices, visual DSL, persuasion principles).

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
