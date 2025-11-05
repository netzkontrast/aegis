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

## 🧭 Quick Navigation

### 📚 Documentation & Guides
- **[This README](#aegis-agentic-reasoning--coherent-hypergraph-orchestration-for-narratives)** - Project overview and philosophy
- **[Claude Code How-To](#-using-claude-code-with-aegis)** - Step-by-step guide for skills and slash commands
- **[Skill Seeker README](skill_seeker/README.md)** - Documentation-to-skills converter
- **[Zettelkasten Agent README](zettelkasten_agent/README.md)** - Knowledge management system

### 🎯 For Different Use Cases

**Writers & Creators:**
- [Kohärenz Protokoll Novel](kohaerenz_protokoll/) - The philosophical SF novel
- [Codex Skill](.claude/skills/codex.md) - Narrative coherence assistant for the novel
- [Manuscript](kohaerenz_protokoll/manuscript/) - Actual prose (Acts I-III)
- [World-building](kohaerenz_protokoll/world/) - Kernwelten, characters, metaphysics
- [Style Guide](kohaerenz_protokoll/narrative_design/style_guide.md) - Prose methodology

**Developers & Engineers:**
- [ARCHON Framework](ARCHON/) - Narrative coherence system
- [NCP Implementation](ARCHON/ncp/) - Formal protocol schemas
- [Knowledge Graph](ARCHON/knowledge_graph/) - Hierarchical memory (L0-L3)
- [Narrative Director](ARCHON/agents/) - Agentic reasoning specs
- [Skill Seeker Tool](skill_seeker/) - Build AI skills from any docs

**Learners & Knowledge Builders:**
- [Tapestry Command](.claude/commands/tapestry.md) - Extract content + create action plans
- [Zettelkasten-Tapestry Command](.claude/commands/zettelkasten-tapestry.md) - Build knowledge graphs
- [Ship-Learn-Next Command](.claude/commands/ship-learn-next.md) - Transform learning into 5-rep plans
- [Zettelkasten Agent](zettelkasten_agent/) - Hierarchical note-taking system

**Researchers:**
- [Research Proposals](research/proposals/) - Framework proposals
- [Strategic Analysis](research/analysis/) - Narrative architecture analysis
- [Critical Assessments](research/critiques/) - Reviews and critiques

### 🔧 Claude Code Integration
- [Skills Directory](.claude/skills/) - Available Claude Code skills (Codex, etc.)
- [Commands Directory](.claude/commands/) - Slash commands (Tapestry, Zettelkasten-Tapestry, Ship-Learn-Next)
- **[Complete How-To Guide](#-using-claude-code-with-aegis)** - Usage instructions below

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

## 🤖 Using Claude Code with AEGIS

This repository includes powerful Claude Code skills and slash commands that enhance your workflow. Here's everything you need to know.

### Available Skills

Skills are persistent AI assistants that provide specialized capabilities. They're automatically available when working in this repository.

#### 1. **Codex** - Kohärenz Protokoll Narrative Coherence

**What it does:**
Ensures narrative consistency for the Kohärenz Protokoll novel by validating content against canonical sources, character voice matrices, and thematic frameworks.

**When to use:**
- Writing or editing manuscript chapters
- Creating dialogue for Kael's alters (AEGIS, Lex, Nyx, Kiko, etc.)
- Validating world physics (Kernwelten, simulation rules)
- Resolving conflicts between narrative documents
- Checking thematic coherence (TSDP, IFS principles)

**How to use:**
```
# Simply mention it in your request:
"Using the Codex skill, validate this dialogue for AEGIS's character voice"
"Check if this scene aligns with the Codex"
"Codex: Does this physics explanation match Kernwelt rules?"
```

**Key workflows:**
1. **Scene Validation** - Check any scene against all canonical sources
2. **AEGIS Dialogue** - Generate AEGIS voice using 3 temperature passes
3. **Alter Voices** - Access character matrix for 11 distinct personalities
4. **Kernwelt Physics** - Validate simulation rules and metaphysical consistency
5. **Document Conflicts** - Resolve contradictions using authority hierarchy

**Reference location:** `.claude/skills/codex.md`

---

### Available Slash Commands

Slash commands are powerful workflows you can trigger with simple syntax. They combine multiple operations into unified pipelines.

#### 1. **/tapestry** - Content Extraction + Action Planning

**What it does:**
Master orchestrator that extracts content from any source and automatically creates a Ship-Learn-Next action plan.

**When to use:**
- You have a YouTube video you want to implement
- You found an article/blog post with useful techniques
- You need to extract and plan from a PDF
- You want actionable steps from any web content

**How to use:**
```bash
# In Claude Code, simply type:
/tapestry https://www.youtube.com/watch?v=example
/tapestry https://blog.example.com/great-article
/tapestry https://example.com/docs.pdf

# Or use natural language triggers:
"tapestry this video: [URL]"
"weave [URL]"
"extract and plan [URL]"
"make this actionable [URL]"
```

**What it creates:**
- `extracted_content_[timestamp].md` - Clean content extraction
- `action_plan_[timestamp].md` - 5-rep Ship-Learn-Next progression

**Supported sources:**
- YouTube videos (transcript extraction)
- Web articles and blog posts
- PDF documents
- General HTML content (fallback)

**Example workflow:**
```
You: /tapestry https://www.youtube.com/watch?v=dQw4w9WgXcQ

Claude extracts the video transcript →
Creates action plan with 5 concrete reps →
You ship Rep 1, learn from it, iterate to Rep 2
```

---

#### 2. **/zettelkasten-tapestry** - Progressive Learning + Knowledge Graph

**What it does:**
Extends Tapestry by building a persistent Zettelkasten knowledge graph with atomic concepts, learning quests, and connections to existing knowledge.

**When to use:**
- You want to build a permanent knowledge base
- You're learning a complex topic progressively
- You need atomic concept extraction (3-7 key ideas)
- You want to connect new learning to existing notes

**How to use:**
```bash
/zettelkasten-tapestry https://example.com/advanced-tutorial

# Or natural language:
"zettelkasten tapestry [URL]"
"progressive learning from [URL]"
"learn and save to knowledge base [URL]"
```

**Six-phase workflow:**
1. **Extract & Plan** - Runs Tapestry + Ship-Learn-Next
2. **Source Note (SRC)** - Creates reference note with metadata
3. **Atomic Concepts** - Extracts 3-7 Zettel notes (one idea each)
4. **Learning Quest MOC** - Creates Map of Content for this learning journey
5. **Connect Knowledge** - Links to existing Zettel notes
6. **Summary** - Shows knowledge graph structure

**Output structure:**
```
zettelkasten_agent/vault/
├── zettels/
│   ├── [timestamp]_concept_1.md
│   ├── [timestamp]_concept_2.md
│   └── [timestamp]_concept_3.md
├── source_notes/
│   └── SRC_[timestamp].md
└── mocs/
    └── MOC_[topic]_[timestamp].md
```

**Example:**
```
You: /zettelkasten-tapestry https://react.dev/learn/thinking-in-react

Output:
✅ Source Note: SRC_thinking_in_react_20250105.md
✅ 5 Atomic Concepts extracted:
   - Component Hierarchy
   - Single Source of Truth
   - Data Flow Direction
   - State Lifting
   - Minimal State Principle
✅ Learning Quest: MOC_React_Design_20250105.md
✅ Connected to 3 existing notes
✅ Action Plan: 5 concrete reps to practice
```

---

#### 3. **/ship-learn-next** - Action Planning Framework

**What it does:**
Transforms learning content into actionable 5-rep implementation plans. Core philosophy: **100 reps beats 100 hours of study.**

**When to use:**
- You have extracted content (transcript, article, tutorial)
- You want to turn advice into concrete actions
- You need a progressive learning plan with shibbable iterations

**How to use:**
```bash
# Typically used automatically by Tapestry, but can be standalone:
/ship-learn-next

# Then provide the content you want to plan
```

**Output format:**
```markdown
## Ship-Learn-Next Action Plan

### 🎯 Core Learning Objective
[What you're trying to master]

### 📦 Rep 1: [Minimal First Ship]
- [ ] Concrete action 1
- [ ] Concrete action 2
- [ ] Concrete action 3

### 📦 Rep 2: [Build on Rep 1]
- [ ] Next level actions...

[... through Rep 5]

### 🔄 The Loop
Ship Rep 1 → Learn from it → Plan Rep 2 → Ship → Learn → Next...
```

**Philosophy:**
- Each rep is shippable and complete
- Focus on doing, not consuming
- Learn by shipping, not by reading more
- 5 reps creates muscle memory

---

### Complete Usage Examples

#### Example 1: Learning from a YouTube Tutorial

```bash
# Start with Tapestry for quick extraction + planning
You: /tapestry https://www.youtube.com/watch?v=tutorial-on-react-hooks

# Claude extracts transcript and creates 5-rep plan
# You get:
# - extracted_content_20250105_1430.md
# - action_plan_20250105_1430.md

# Work through Rep 1, then iterate:
You: "I finished Rep 1 of the hooks tutorial. Help me refine Rep 2 based on what I learned."
```

#### Example 2: Building a Knowledge Base

```bash
# Use Zettelkasten-Tapestry for permanent knowledge
You: /zettelkasten-tapestry https://martinfowler.com/articles/microservices.html

# Claude creates:
# 1. Source note with full context
# 2. 5-7 atomic concept notes (one idea each)
# 3. Learning Quest MOC
# 4. Links to existing architecture notes
# 5. 5-rep action plan

# Later, when you learn about event sourcing:
You: /zettelkasten-tapestry https://example.com/event-sourcing

# New concepts automatically link to microservices notes
# Your knowledge graph grows organically
```

#### Example 3: Writing Kohärenz Protokoll

```bash
# Use Codex for narrative consistency
You: "Using Codex, validate this dialogue for Chapter 15:

[AEGIS]: 'The Protocol demands coherence. You are fragmentation.'
[Kael]: 'I'm not broken. I'm a choir.'"

# Codex checks:
# ✅ AEGIS voice matches character matrix (authoritative, absolutist)
# ✅ Kael's metaphor aligns with Act II integration themes
# ✅ "The Protocol" is canonical terminology
# ⚠️  Consider: Is "choir" resonant with Kael's established metaphors?

# Then continue writing with confidence
```

#### Example 4: Multi-Step Workflow

```bash
# Complex learning pipeline:

Step 1: Extract and plan
You: /tapestry https://www.youtube.com/watch?v=advanced-ai-agents

Step 2: Ship Rep 1
You: [Implement first version based on plan]

Step 3: Build knowledge base
You: /zettelkasten-tapestry [same URL]
# Now it's permanently indexed with atomic concepts

Step 4: Connect to existing work
You: "Link these AI agent concepts to ARCHON/agents/narrative_director.md"

Step 5: Iterate
You: "Based on Rep 1 learnings, update Rep 2 of the action plan"
```

---

### Tips & Best Practices

**For Tapestry:**
- ✅ Use for quick extraction + immediate action planning
- ✅ Great for one-off tutorials or articles
- ✅ Generates files in current directory
- ⚠️  Content is not indexed in knowledge graph (use Zettelkasten-Tapestry for that)

**For Zettelkasten-Tapestry:**
- ✅ Use when building permanent knowledge
- ✅ Extracts atomic concepts (one idea per note)
- ✅ Automatically links to existing knowledge
- ✅ Creates learning quests (MOCs) for progressive mastery
- ⚠️  Takes longer than plain Tapestry (6-phase process)

**For Ship-Learn-Next:**
- ✅ Usually automatic (triggered by Tapestry)
- ✅ Can be used standalone for planning from existing content
- ✅ Focus on shippable reps, not perfect plans
- ✅ Iterate after each rep based on real learning

**For Codex:**
- ✅ Specific to Kohärenz Protokoll narrative work
- ✅ Validates against canonical sources automatically
- ✅ Use for any manuscript writing or world-building
- ✅ Includes character voice matrix for all 11 alters

---

### Philosophy: The Tapestry Ecosystem

These tools work together as an integrated learning pipeline:

```
Content Source (URL/PDF/Video)
        ↓
    TAPESTRY (extract)
        ↓
    SHIP-LEARN-NEXT (plan 5 reps)
        ↓
    YOU (ship Rep 1)
        ↓
    LEARN (from real implementation)
        ↓
    NEXT (iterate to Rep 2)
        ↓
    [Optional: ZETTELKASTEN-TAPESTRY to build knowledge graph]
```

**Core principle:** *100 reps beats 100 hours of study*

Don't just consume content. Extract it, plan it, ship it, learn from it, repeat.

---

### Troubleshooting

**"Slash command not found"**
- Ensure you're in the `/home/user/aegis` directory
- Check `.claude/commands/` directory exists
- Commands must be in `.md` format

**"Skill not activating"**
- Skills auto-activate when mentioned
- Try explicitly: "Using the Codex skill, [your request]"
- Check `.claude/skills/` directory

**"Zettelkasten notes not linking"**
- Ensure `zettelkasten_agent/vault/` directory exists
- Check that previous notes exist to link to
- First use will have no links (knowledge graph starts empty)

**"YouTube extraction failed"**
- Some videos disable transcripts
- Try the video URL in different formats
- Fallback: Use Tapestry on the video description page

---

### Next Steps

1. **Try Tapestry**: Find a tutorial and run `/tapestry [URL]`
2. **Build Knowledge**: Use `/zettelkasten-tapestry` on something you want to master
3. **Write with Codex**: If working on the novel, invoke Codex for validation
4. **Ship Reps**: Don't just plan—actually implement Rep 1, then iterate

**Remember:** These tools are designed for *doing*, not just *organizing*. Ship early, ship often.

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
