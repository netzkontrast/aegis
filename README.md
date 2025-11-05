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
│   │   ├── schema.json        # Formal JSON Schema (Dramatica-based)
│   │   └── kohaerenz_protokoll.ncp.json  # Populated NCP for the novel
│   ├── tools/                 # CLI utilities for narrative management
│   │   ├── ncp_query.py       # Query NCP for scene requirements
│   │   └── ncp_validate.py    # Validate prose against constraints
│   └── agents/                # Narrative Director specifications
│
├── kohaerenz_protokoll/       # The novel
│   ├── manuscript/            # Actual prose (Acts I-III)
│   │   └── act_1/             # Chapter markdown files
│   ├── world/                 # World-building
│   │   ├── kernwelten/        # 4 nested simulation layers (KW0-KW3)
│   │   └── characters/        # Character profiles (Kael's 11 alters, AEGIS)
│   ├── narrative_design/      # Structural documents
│   │   ├── IMPLEMENTATION_SPEC.md  # Technical prose specifications
│   │   └── act_1_scenes.md    # Scene-by-scene breakdown
│   └── PROJECT_CODEX.md       # Canonical narrative architecture
│
├── skill_seeker/              # Documentation to Claude Skills conversion tool
│   ├── mcp/                   # MCP server for Claude Code integration
│   ├── cli/                   # 22 command-line tools
│   │   ├── doc_scraper.py     # Main documentation scraper
│   │   ├── unified_scraper.py # Multi-source (docs + GitHub + PDF)
│   │   ├── github_scraper.py  # Deep code analysis with AST parsing
│   │   ├── pdf_scraper.py     # PDF text/image/table extraction
│   │   ├── enhance_skill*.py  # AI enhancement (API or local)
│   │   └── package_skill.py   # Package skills for upload
│   ├── configs/               # 27 preset configurations
│   │   ├── react.json         # React framework
│   │   ├── django_unified.json # Django + GitHub + PDF
│   │   ├── godot.json         # Godot game engine
│   │   └── ...                # FastAPI, Kubernetes, Tailwind, etc.
│   └── docs/                  # Comprehensive documentation
│       ├── MCP_SETUP.md       # Claude Code integration guide
│       ├── PDF_*.md           # 8 PDF-specific guides
│       └── UNIFIED_SCRAPING.md # Multi-source integration
│
├── zettelkasten_agent/        # Zettelkasten knowledge management agent
│   ├── agent.py               # 4-phase cognitive loop agent
│   ├── zettelkasten_tools_mcp.py # MCP server for file operations
│   ├── schemas/               # Pydantic data validation
│   └── vault/                 # Note storage
│       ├── _INDEX.md          # Master index
│       ├── _LOG.md            # Action log
│       ├── SRC-*.md           # Source notes
│       ├── ZTL-*.md           # Atomic notes
│       └── MOC-*.md           # Maps of Content
│
├── skills/                    # Claude AI skills library
│   ├── skill-authoring/       # Unified framework for creating skills
│   │   ├── SKILL.md           # Main skill document (495 lines)
│   │   └── reference/         # CSO optimization, persuasion patterns
│   └── zettelkasten-tapestry/ # Progressive learning system
│       ├── SKILL.md           # Integration of Tapestry + Zettelkasten
│       └── reference/         # Note taxonomy, workflows
│
└── docs/                      # Research and planning documentation
    ├── knowledge-extraction/  # 10 files analyzing skill authoring
    │   ├── 01-07-*-core-patterns.md  # Pattern extraction
    │   ├── 05-comparative-analysis.md
    │   ├── 06-critical-analysis.md
    │   └── 07-synthesis-unified-framework.md # Primary deliverable
    └── plans/                 # TDD-based implementation plans
        ├── 2025-11-05-ncp-writing-assistant.md
        └── 2025-11-05-knowledge-graph-foundation.md
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

**Implementation**: See [ARCHON/ncp/](ARCHON/ncp/) for schema and populated data.

### The Knowledge Hypergraph
A four-level hierarchical memory system that overcomes LLM context limitations:
- **L0 (Source)**: Raw text chunks and extracted entities
- **L1 (Factual)**: Validated facts and relationships
- **L2 (Thematic)**: Aggregated themes and patterns
- **L3 (Global)**: Story-wide arcs and central conflicts

**Status**: Planned - see [docs/plans/2025-11-05-knowledge-graph-foundation.md](docs/plans/2025-11-05-knowledge-graph-foundation.md)

### The Narrative Director
An agentic system that:
1. Reads thematic goals from the NCP
2. Queries the Knowledge Hypergraph for relevant context
3. Generates narrative content
4. Self-critiques against NCP constraints
5. Iterates until thematic coherence is achieved

**Implementation**: Specification available at [ARCHON/agents/README.md](ARCHON/agents/README.md)

### ARCHON Tools
Command-line utilities for narrative management:

```bash
# Query NCP for scene requirements
python ARCHON/tools/ncp_query.py --chapter 4 --verbose

# Validate prose against NCP constraints
python ARCHON/tools/ncp_validate.py manuscript/chapter_01.md
```

**Available tools**:
- ✅ `ncp_query.py` - Query NCP for scene requirements, character states
- ✅ `ncp_validate.py` - Validate prose against NCP constraints
- 🔜 `ncp_assist.py` - Generate writing prompts, voice samples (planned)

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

**Current Status**: Act I outline complete, 1 sample chapter written. See [kohaerenz_protokoll/PROJECT_CODEX.md](kohaerenz_protokoll/PROJECT_CODEX.md) for canonical narrative architecture.

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

## Integrated Tools & Systems

### Skill Seeker: Documentation to Claude Skills Converter

The **skill_seeker/** directory contains a production-ready tool (v2.0.0) for automatically converting documentation websites, GitHub repositories, and PDF files into Claude AI skills.

**Key Features:**
- 🌐 **Documentation Scraping**: Universal scraper with smart categorization and llms.txt auto-detection
- 📄 **PDF Support**: Extract text, code, images, and tables from PDF files with OCR support
- 🐙 **GitHub Integration**: Deep code analysis with AST parsing (Python, JS, TS, Java, C++, Go)
- 🔄 **Unified Multi-Source**: Combine documentation + GitHub + PDF with automatic conflict detection
- 🤖 **AI Enhancement**: LOCAL (free, uses Claude Code Max) or API-based enhancement
- 🧪 **Production Ready**: 299 tests passing, 27 preset configurations verified
- ⚡ **MCP Server**: Natural language interface through Claude Code
- 📦 **27 Presets**: React, Django, FastAPI, Godot, Kubernetes, Tailwind, and more

**Quick Start:**
```bash
cd skill_seeker

# One-time MCP setup
./setup_mcp.sh

# Then in Claude Code, ask:
"Generate a React skill from https://react.dev/"
"List all available configs"
"Scrape docs using configs/godot.json"
```

**Example Unified Scraping:**
```bash
# Combine docs + GitHub + PDF with conflict detection
python cli/unified_scraper.py configs/react_unified.json
```

**Documentation:**
- [Complete README](skill_seeker/README.md) - 1,042-line comprehensive guide
- [Quick Start](skill_seeker/QUICKSTART.md) - Get started in 5 minutes
- [Bulletproof Quick Start](skill_seeker/BULLETPROOF_QUICKSTART.md) - Step-by-step troubleshooting
- [MCP Setup](skill_seeker/docs/MCP_SETUP.md) - Claude Code integration
- [PDF Guide](skill_seeker/docs/PDF_SCRAPER.md) - PDF documentation scraping
- [Unified Scraping](skill_seeker/docs/UNIFIED_SCRAPING.md) - Multi-source integration
- [Testing](skill_seeker/docs/TESTING.md) - 299 tests, all passing

### Zettelkasten Agent: Knowledge Management System

The **zettelkasten_agent/** provides an AI-powered note-taking system implementing the Zettelkasten method with automatic synthesis and linking.

**Architecture:**
- **4-phase cognitive loop**: Prioritize → Analyze → Synthesize → Integrate
- **Note types**: Source (SRC), Atomic (ZTL), Maps of Content (MOC)
- **Special files**: `_INDEX.md` (master index), `_LOG.md` (action log)
- **Knowledge graph**: Automatically linked bidirectional notes with contextual links

**Quick Start:**
```bash
cd zettelkasten_agent
python agent.py
```

**MCP Tools Available:**
- `create_note` - Create SRC/ZTL/MOC notes with validation
- `read_note_content` - Read full note content
- `get_note_metadata` - Read only frontmatter
- `append_link` - Add contextual links with automatic backlinks
- `find_notes` - Search by keyword or semantically
- `list_files` - List notes (optionally filtered)
- `log_action` - Append to action log

**Documentation:**
- [Complete README](zettelkasten_agent/README.md) - 343-line guide
- [Quick Start](zettelkasten_agent/QUICKSTART.md) - Get up and running

**Status**: MVP implementation complete
- ✅ Core agent workflow
- ✅ MCP server integration
- ✅ Schema validation
- 🔜 Semantic search
- 🔜 MOC_Tender maintenance agent

### Skills Library

The **skills/** directory contains reusable Claude AI skills for domain-specific tasks:

#### 1. Skill Authoring Framework
**Location**: `skills/skill-authoring/`

A unified framework combining TDD methodology, Anthropic best practices, visual DSL patterns, and persuasion principles for creating high-quality Claude skills.

**Key Components:**
- `SKILL.md` (495 lines) - Main discipline + technique skill
- `reference/cso-optimization.md` - Claude Search Optimization patterns
- `reference/persuasion-patterns.md` - Psychology-based compliance principles
- `reference/structure-templates.md` - Templates by skill type (discipline, technique, domain)

**Features:**
- RED/GREEN/REFACTOR TDD cycle for skill development
- CSO optimization for better skill discoverability
- Persuasion principle mappings for user compliance
- Ready-to-use templates and checklists

**Documentation**: See [skills/skill-authoring/SKILL.md](skills/skill-authoring/SKILL.md)

#### 2. Zettelkasten-Tapestry Integration
**Location**: `skills/zettelkasten-tapestry/`

A progressive learning system combining the `/tapestry` slash command (content extraction and action planning) with the Zettelkasten agent (knowledge management).

**Workflow:**
1. Extract content from URL using Tapestry
2. Create action plan with concrete steps
3. Save notes to Zettelkasten vault
4. Synthesize knowledge over time
5. Build knowledge graph

**Documentation**: See [skills/zettelkasten-tapestry/SKILL.md](skills/zettelkasten-tapestry/SKILL.md)

## Research & Analysis

### Knowledge Extraction Studies
**Location**: `docs/knowledge-extraction/`

Comprehensive analysis of skill authoring approaches, extracting patterns from multiple sources:

| Document | Purpose |
|----------|---------|
| `01-04-*-core-patterns.md` | Pattern extraction from 4 sources (TDD, Anthropic, Graphviz, Persuasion) |
| `05-comparative-analysis.md` | Side-by-side comparison of approaches |
| `06-critical-analysis.md` | 9 critical problems identified and addressed |
| `07-synthesis-unified-framework.md` | **Primary deliverable**: Unified skill authoring framework |
| `08-10-phase-analysis.md` | RED/GREEN/REFACTOR phase-specific analysis |

**Statistics:**
- ~71,000 tokens of analysis (~53,000 words)
- 9 critical problems identified with solutions
- 6 blind spots filled
- 10+ ready-to-use artifacts (templates, checklists, formulas)

### Implementation Plans
**Location**: `docs/plans/`

TDD-based implementation roadmaps with bite-sized tasks (2-5 minutes each):

- `2025-11-05-ncp-writing-assistant.md` - Implement `ncp_assist.py` tool
- `2025-11-05-knowledge-graph-foundation.md` - Implement knowledge graph system

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

### 🎯 Choose Your Path

#### For Writers
**Goal**: Understand narrative architecture and prose methodology

1. Read the [Project Codex](kohaerenz_protokoll/PROJECT_CODEX.md) for canonical narrative architecture
2. Study the [NCP Schema](ARCHON/ncp/schema.json) to understand thematic structure
3. Review the [Implementation Spec](kohaerenz_protokoll/narrative_design/IMPLEMENTATION_SPEC.md) for prose guidelines
4. Explore [Scene Outlines](kohaerenz_protokoll/narrative_design/act_1_scenes.md)
5. Try the ARCHON tools:
   ```bash
   python ARCHON/tools/ncp_query.py --chapter 1 --verbose
   ```

#### For Developers
**Goal**: Implement narrative systems and AI-assisted creation

1. Explore the [NCP implementation](ARCHON/ncp/) for the formal protocol
2. Study [Narrative Director specs](ARCHON/agents/README.md) for agentic architecture
3. Review [Knowledge Graph plans](docs/plans/2025-11-05-knowledge-graph-foundation.md)
4. Examine the [ARCHON tools](ARCHON/tools/) source code
5. Try building a skill with Skill Seeker:
   ```bash
   cd skill_seeker
   ./setup_mcp.sh
   # Then in Claude Code: "Generate a FastAPI skill"
   ```

#### For AI Enthusiasts
**Goal**: See practical MCP integration and agentic systems

1. Set up the [Skill Seeker MCP server](skill_seeker/docs/MCP_SETUP.md)
2. Explore the [Zettelkasten Agent](zettelkasten_agent/README.md)
3. Try the [Zettelkasten-Tapestry skill](skills/zettelkasten-tapestry/SKILL.md)
4. Review the [Skill Authoring framework](skills/skill-authoring/SKILL.md)
5. Experiment with unified scraping:
   ```bash
   python skill_seeker/cli/unified_scraper.py configs/react_unified.json
   ```

#### For Researchers
**Goal**: Validate AI's role in creative work

1. Study the [Knowledge Extraction analysis](docs/knowledge-extraction/07-synthesis-unified-framework.md)
2. Review the [Critical Analysis](docs/knowledge-extraction/06-critical-analysis.md)
3. Examine the [Narrative Context Protocol](ARCHON/ncp/schema.json)
4. Explore the [meta-recursive design](#the-meta-recursive-design) concept
5. Read the development philosophy below

#### For Skill Creators
**Goal**: Build Claude skills from documentation

1. Start with [Skill Seeker Quick Start](skill_seeker/QUICKSTART.md)
2. Try the [Bulletproof Quick Start](skill_seeker/BULLETPROOF_QUICKSTART.md) if you encounter issues
3. Explore [preset configs](skill_seeker/configs/) for examples
4. Learn [Unified Scraping](skill_seeker/docs/UNIFIED_SCRAPING.md) for multi-source skills
5. Review the [PDF Guide](skill_seeker/docs/PDF_SCRAPER.md) for PDF documentation
6. Apply the [Skill Authoring framework](skills/skill-authoring/SKILL.md) for quality

## Development Philosophy

This project embraces **recursive self-awareness**:

- We document failures when the NCP feels constraining (mirroring AEGIS's rigidity)
- We document emergence when the framework enables unexpected insights (mirroring Kael's integration)
- We treat the development process itself as research data

The goal is not just to write a novel or build a framework, but to discover whether formal systems can genuinely serve—rather than constrain—the creative process.

## Project Principles

### Integration Over Elimination
True coherence emerges from integration of contradictions, not elimination. This applies to:
- **Narrative**: Kael's 11 alters achieve functional multiplicity, not fusion
- **Tools**: Skill Seeker combines multiple sources with conflict detection, not replacement
- **Knowledge**: Zettelkasten links and synthesizes, not consolidates
- **Development**: We embrace both formal structure and creative emergence

### Formal Systems Serve Creativity
ARCHON provides structure to enable, not constrain:
- The NCP defines thematic guardrails, not rigid rules
- Tools validate and query, not dictate
- The Knowledge Graph augments context, not replaces judgment

### Recursive Self-Performance
The project performs its own themes:
- Repository structure mirrors narrative structure (fragmentation → integration)
- Tools demonstrate principles they enable (coherence through formal systems)
- Development process validates research questions (can AI assist complex creativity?)

## Current Status

### Phases
- 🟡 **Phase 1** (CURRENT): Foundation - Building the living architecture
  - ✅ Project conceptualization and architecture
  - ✅ NCP schema and specification
  - ✅ ARCHON tools (query, validate)
  - ✅ Skill Seeker v2.0.0 (production ready, 299 tests)
  - ✅ Zettelkasten Agent MVP
  - ✅ Skills library (skill-authoring, zettelkasten-tapestry)
  - 🔜 Writing assistant (`ncp_assist.py`)
  - 🔜 Knowledge Graph foundation

- ⚪ **Phase 2**: Implementation - NCP population and validation
  - Knowledge Graph implementation
  - Narrative Director agent
  - Advanced validation and analytics

- ⚪ **Phase 3**: Creation - Writing the manuscript
  - Novel manuscript completion (39 chapters, 3 acts)
  - Currently: Act I outline complete, 1 sample chapter written

- ⚪ **Phase 4**: Synthesis - Research publication
  - Research paper on AI-assisted narrative creation
  - Validation of ARCHON principles
  - Publication and community sharing

### Component Status

| Component | Status | Notes |
|-----------|--------|-------|
| ARCHON NCP | ✅ Complete | Schema + populated data |
| ARCHON Tools | 🟡 Partial | Query + Validate done, Assist planned |
| Narrative Director | 📋 Specified | Architecture documented, not implemented |
| Knowledge Graph | 📋 Planned | Foundation plan ready |
| Kohärenz Protokoll | 🔜 Early | 1 chapter written, Act I outlined |
| Skill Seeker | ✅ Production | v2.0.0, 299 tests passing |
| Zettelkasten Agent | ✅ MVP | Core workflow complete |
| Skills Library | ✅ Complete | 2 skills (authoring, tapestry) |
| Documentation | ✅ Comprehensive | 50+ markdown files, ~100k tokens |

**Legend**: ✅ Complete | 🟡 In Progress | 🔜 Started | 📋 Planned | ⚪ Not Started

## Technology Stack

| Layer | Technology | Location |
|-------|-----------|----------|
| **Narrative Foundation** | Dramatica theory, TSDP psychology | ARCHON/ncp/ |
| **Story Management** | JSON Schema, Python | ARCHON/ |
| **Prose Writing** | Markdown | kohaerenz_protokoll/manuscript/ |
| **Knowledge Graph** | Hierarchical JSON (planned) | ARCHON/knowledge_graph/ |
| **Skill Conversion** | Python 3.10+, BeautifulSoup4, requests | skill_seeker/ |
| **AI Enhancement** | Anthropic API (optional), Claude Code Max | skill_seeker/ |
| **PDF Processing** | PDF extraction, OCR, table extraction | skill_seeker/cli/ |
| **Code Analysis** | AST parsing (Python, JS, TS, Java, C++, Go) | skill_seeker/cli/ |
| **Knowledge Management** | fast-agents, MCP, Pydantic | zettelkasten_agent/ |
| **MCP Integration** | Model Context Protocol servers | skill_seeker/mcp/, zettelkasten_agent/ |

## Contributing

This is a research and creative project exploring the intersection of:
- Narrative theory (Dramatica, TSDP psychology)
- AI-assisted creativity (LLMs, agentic systems, MCP)
- Formal systems (logic, computation, coherence)
- Philosophical fiction (identity, consciousness, reality)

**Ways to contribute:**
- 🐛 Report bugs or issues with tools
- 💡 Suggest improvements to ARCHON or NCP
- 📖 Provide feedback on narrative or prose
- 🔬 Contribute research or analysis
- 🛠️ Implement planned features (see [docs/plans/](docs/plans/))
- 🧪 Add tests or improve documentation

Contributions, critiques, and dialogue are welcome.

## Resources

### Main Documentation
- [ARCHON Framework](ARCHON/README.md)
- [Kohärenz Protokoll Codex](kohaerenz_protokoll/PROJECT_CODEX.md)
- [Skill Seeker Guide](skill_seeker/README.md)
- [Zettelkasten Agent](zettelkasten_agent/README.md)

### Detailed Guides
- [NCP Schema](ARCHON/ncp/schema.json) - Formal narrative specification
- [Implementation Spec](kohaerenz_protokoll/narrative_design/IMPLEMENTATION_SPEC.md) - Prose guidelines
- [Skill Authoring](skills/skill-authoring/SKILL.md) - Skill creation framework
- [Unified Scraping](skill_seeker/docs/UNIFIED_SCRAPING.md) - Multi-source skills

### Research & Analysis
- [Unified Framework Synthesis](docs/knowledge-extraction/07-synthesis-unified-framework.md) - Primary research deliverable
- [Critical Analysis](docs/knowledge-extraction/06-critical-analysis.md) - Problems and solutions
- [Implementation Plans](docs/plans/) - TDD-based roadmaps

## License

The ARCHON framework and supporting tools (Skill Seeker, Zettelkasten Agent) are released under MIT License.

The Kohärenz Protokoll manuscript and associated creative content are © 2024-2025. All rights reserved.

---

*Built at the intersection of system and story, where coherence emerges from contradiction.*

---

## Quick Links

| What | Where |
|------|-------|
| 📖 Read the novel outline | [kohaerenz_protokoll/narrative_design/act_1_scenes.md](kohaerenz_protokoll/narrative_design/act_1_scenes.md) |
| 🔧 Build a skill | [skill_seeker/QUICKSTART.md](skill_seeker/QUICKSTART.md) |
| 📝 Manage knowledge | [zettelkasten_agent/QUICKSTART.md](zettelkasten_agent/QUICKSTART.md) |
| 🎓 Learn skill authoring | [skills/skill-authoring/SKILL.md](skills/skill-authoring/SKILL.md) |
| 🔬 Read the research | [docs/knowledge-extraction/07-synthesis-unified-framework.md](docs/knowledge-extraction/07-synthesis-unified-framework.md) |
| 🛠️ Implement a feature | [docs/plans/](docs/plans/) |
| ⚙️ Query the NCP | `python ARCHON/tools/ncp_query.py --help` |
