# ARCHON Interface Design

## Overview

The ARCHON framework requires multiple interfaces for different users and workflows. This document specifies the complete interface architecture, from CLI tools for writers to API endpoints for AI agents.

## User Personas

### 1. The Human Writer
**Needs**:
- Query the NCP for scene requirements
- Validate written prose against thematic checkpoints
- Track which alters are active in each scene
- Get writing prompts based on current chapter
- Check continuity and character consistency

**Primary Interface**: Command-line tools + Markdown reports

### 2. The Narrative Director Agent (AI)
**Needs**:
- Programmatic access to NCP data
- Knowledge graph query/update capabilities
- Self-critique validation loops
- Scene generation with constraint satisfaction
- Thematic coherence scoring

**Primary Interface**: Python API + JSON-RPC

### 3. The Researcher
**Needs**:
- Analyze NCP usage patterns
- Track coherence metrics over time
- Compare AI-assisted vs baseline writing
- Export data for publication
- Visualize narrative structure

**Primary Interface**: Data export tools + visualization

## Core Interface Components

### Component 1: NCP Query Interface

**Purpose**: Retrieve structured data from the NCP for a given chapter/scene

**CLI Tool**: `ncp-query`

```bash
# Get all requirements for a chapter
ncp-query --chapter 4

# Get specific throughline data
ncp-query --throughline MC --signpost Memory

# Get active alters for a scene
ncp-query --scene 1.4 --data active_alters

# Get thematic checkpoints
ncp-query --chapter 4 --checkpoints

# Get validation criteria
ncp-query --scene 1.4 --validate
```

**Output Format**: JSON or Markdown tables

**Example Output**:
```json
{
  "chapter": 4,
  "scene_id": "1.4",
  "title": "The Drowning Pool",
  "location": "Mnemosyne-Archipel (KW2)",
  "pov": "Kael (System)",
  "active_alters": ["Kael", "Rhys", "Kiko", "Lex"],
  "prose_style": "Fragmented",
  "thematic_checkpoints": [
    {
      "checkpoint": "First direct trauma confrontation",
      "validation_question": "Does Kael experience overwhelming emotion that ANP cannot control?"
    },
    {
      "checkpoint": "ANP-EP phobia demonstration",
      "validation_question": "Do Lex/Kael try to flee from Kiko's emotional pain?"
    }
  ],
  "world_physics": {
    "realm": "KW2",
    "rules": ["Reactive to emotion", "Non-linear time", "NP-complexity"]
  }
}
```

---

### Component 2: Scene Validator

**Purpose**: Check written prose against NCP constraints

**CLI Tool**: `ncp-validate`

```bash
# Validate a scene file
ncp-validate manuscript/act_1/chapter_04_scene_01.md --chapter 4

# Validate with detailed report
ncp-validate chapter_04.md --verbose --output-format markdown

# Auto-fix mode (suggests corrections)
ncp-validate chapter_04.md --suggest-fixes

# Batch validate entire act
ncp-validate manuscript/act_1/*.md --summary
```

**Validation Checks**:
1. **Character Consistency**: Are active alters behaving according to their type and arc position?
2. **Thematic Alignment**: Are checkpoints satisfied?
3. **World Physics**: Are realm rules respected?
4. **Continuity**: No contradictions with earlier scenes?
5. **Prose Style**: Matches expected fragmentation/integration level?

**Example Output**:
```markdown
# Validation Report: Chapter 4, Scene 1.4

## Status: ⚠️  WARNINGS (3)

### ✅ Passed (5)
- Character voices are distinct and consistent
- Thematic checkpoint: "First trauma confrontation" satisfied
- World physics: KW2 reactivity shown
- Prose style matches "Fragmented" requirement
- No continuity errors detected

### ⚠️  Warnings (3)
- **Lex's voice**: Line 47 uses emotional language ("I'm terrified")
  which contradicts his analytical ANP type
  → Suggestion: "Probability of system failure: 87%" (more Lex-like)

- **Thematic checkpoint partially met**: "ANP-EP phobia" shown but could be stronger
  → Suggestion: Add Lex explicitly avoiding looking at Kiko

- **Missing alter**: Argus is listed as active but has no dialogue/POV presence
  → Suggestion: Add meta-observation from Argus or remove from active list

### ❌ Errors (0)

## Coherence Score: 8.2/10
```

---

### Component 3: Writing Assistant

**Purpose**: Generate writing prompts and suggestions based on NCP

**CLI Tool**: `ncp-assist`

```bash
# Get a writing prompt for next scene
ncp-assist --chapter 5 --prompt

# Get character voice examples
ncp-assist --character Lex --voice-sample

# Get world description prompts
ncp-assist --location KW2 --describe

# Get alter internal dialogue suggestions
ncp-assist --scene 1.4 --alter Kiko --internal-voice
```

**Example Output**:
```markdown
# Writing Prompt: Chapter 5, Scene 2.1

## Scene Requirements
**Location**: Mnemosyne-Archipel (KW2), Lake of Tears
**POV**: Kael (System)
**Active Alters**: Kael, Rhys, Lex, Argus
**Goal**: Map the emotional landscape deliberately
**Conflict**: Mnemosyne attempts to trap in memory loop

## Starter Prompts

### Opening Line Options:
1. "The second time Kael entered the Archipelago, he knew what to expect. He was wrong."
2. "Rhys led them back to the water. 'This time,' he said, 'we observe. We don't dive.'"
3. "The smell of rain hit first—memory before sensation."

## Voice Guidance

**Lex (Analytical ANP)** should sound like:
- "Three islands ahead. Probability of hostile memory: high. Recommend peripheral reconnaissance."
- Hypotactic syntax, technical vocabulary
- Sees patterns, not emotions

**Rhys (Caregiver ANP)** should sound like:
- "I can feel Kiko's fear from here. We need to be gentle. Slow."
- Warm, flowing, emotionally attuned
- Provides reassurance

## Thematic Beats to Hit:
- [ ] Show deliberate cooperation (not just crisis response)
- [ ] Demonstrate Lex using logic to protect against emotional manipulation
- [ ] Rhys must recognize Kiko's pain without being overwhelmed
- [ ] Mnemosyne's seductive offer to "organize" memories

## Environment Details (KW2):
- Mist rolling across water
- Islands that shift with emotional associations
- Time feels non-linear (sunset that doesn't end)
- Sound: Distant echoes of voices, both familiar and forgotten
```

---

### Component 4: Knowledge Graph Interface

**Purpose**: Query and update the hierarchical narrative memory

**CLI Tool**: `kg-query` (Knowledge Graph Query)

```bash
# Add a fact to the knowledge graph
kg-add --level L1 --type fact \
  --entity "Kael" \
  --relation "experienced" \
  --object "memory loop in KW2" \
  --chapter 4

# Query for related information
kg-query --entity "Kael" --chapter 4 --depth 2

# Get thematic aggregations
kg-query --level L2 --theme "trauma processing" --chapters 1-13

# Get global story state
kg-query --level L3 --summary

# Track alter states across chapters
kg-query --entity "Nyx" --attribute "cooperation_level" --timeline
```

**Graph Structure**:
```
L3 (Global)
  └─ "Kael's integration journey"
      └─ L2 (Thematic)
          ├─ "Trauma processing" theme
          │   └─ L1 (Factual)
          │       ├─ "Kael entered KW2 in Ch4"
          │       ├─ "Mnemosyne trapped him in loop"
          │       └─ "Lex found logical exit"
          │           └─ L0 (Source)
          │               └─ Raw text from chapter_04.md
          │
          └─ "ANP-EP cooperation" theme
              └─ L1 (Factual)
                  └─ "First Rhys+Lex cooperation in Ch4"
```

---

### Component 5: Narrative Director Agent API

**Purpose**: Programmatic interface for AI agents to write/validate scenes

**API Specification** (Python)

```python
from aegis import NarrativeDirector

# Initialize with NCP
director = NarrativeDirector(
    ncp_file="aegis/ncp/kohaerenz_protokoll.ncp.json",
    knowledge_graph="aegis/knowledge_graph/"
)

# Query for scene requirements
scene_req = director.get_scene_requirements(chapter=4, scene_id="1.4")

# Generate scene content
scene = director.generate_scene(
    requirements=scene_req,
    max_iterations=5,  # Self-critique loops
    temperature=0.7
)

# The agent's workflow:
# 1. Read requirements from NCP
# 2. Query knowledge graph for relevant context
# 3. Generate scene draft
# 4. Self-critique against checkpoints
# 5. If invalid, iterate; if valid, return

# Validate a human-written scene
validation = director.validate_scene(
    scene_text=open("chapter_04.md").read(),
    chapter=4,
    scene_id="1.4"
)

print(validation.score)  # 0-10
print(validation.issues)  # List of problems
print(validation.suggestions)  # Recommended fixes

# Update knowledge graph with new scene
director.ingest_scene(
    scene_text=scene.content,
    chapter=4,
    metadata=scene_req
)
```

---

### Component 6: Coherence Dashboard

**Purpose**: Visual interface for tracking narrative coherence over time

**Web Interface** (Future: HTML/JavaScript dashboard)

**Features**:
- **Arc Tracker**: Visualize each alter's integration journey across 39 chapters
- **Coherence Score Timeline**: Track validation scores per chapter
- **Thematic Coverage**: Heatmap showing which themes are hit in which chapters
- **Character Activity**: Which alters are active in which scenes
- **World Navigation**: Map of transitions between Kernwelten

**CLI Equivalent**: `ncp-report`

```bash
# Generate comprehensive project report
ncp-report --chapters 1-13 --output report.html

# Track alter integration scores
ncp-report --metric alter_integration --chart

# Thematic coverage analysis
ncp-report --theme-coverage --act 1
```

---

## Workflow Diagrams

### Workflow 1: Human Writer Using ARCHON

```
┌─────────────────────────────────────────────────────────┐
│ 1. PLAN SCENE                                           │
│    $ ncp-query --chapter 4 --verbose                    │
│    → Gets requirements, checkpoints, character states   │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ 2. GET WRITING PROMPTS                                  │
│    $ ncp-assist --chapter 4 --prompt                    │
│    → Gets starter lines, voice examples, beats          │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ 3. WRITE SCENE                                          │
│    → Human creativity + NCP guidance                    │
│    → Save to manuscript/act_1/chapter_04.md             │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ 4. VALIDATE                                             │
│    $ ncp-validate chapter_04.md --verbose               │
│    → Check against constraints                          │
└─────────────────────────────────────────────────────────┘
                          ↓
                    Pass? ──No──> Revise (goto step 3)
                      │
                     Yes
                      ↓
┌─────────────────────────────────────────────────────────┐
│ 5. UPDATE KNOWLEDGE GRAPH                               │
│    $ kg-add --source chapter_04.md --auto-extract       │
│    → Add facts to L1, update L2 themes                  │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ 6. COMMIT                                               │
│    $ git add chapter_04.md                              │
│    $ git commit -m "feat: Complete Chapter 4"           │
└─────────────────────────────────────────────────────────┘
```

### Workflow 2: AI Agent (Narrative Director)

```
┌─────────────────────────────────────────────────────────┐
│ 1. INITIALIZE                                           │
│    director = NarrativeDirector(ncp_file, kg_path)     │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ 2. QUERY NCP + KNOWLEDGE GRAPH                          │
│    requirements = director.get_scene_requirements(ch=4) │
│    context = director.query_kg(thematic_resonance)      │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ 3. GENERATE DRAFT                                       │
│    draft = llm.generate(prompt=requirements + context)  │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ 4. SELF-CRITIQUE                                        │
│    validation = director.validate_scene(draft)          │
│    → Check character consistency                        │
│    → Check thematic alignment                           │
│    → Check world physics                                │
└─────────────────────────────────────────────────────────┘
                          ↓
                  Valid? ──No──> Regenerate (goto step 3)
                    │              (max 5 iterations)
                   Yes
                    ↓
┌─────────────────────────────────────────────────────────┐
│ 5. INGEST TO KNOWLEDGE GRAPH                            │
│    director.ingest_scene(draft, chapter=4)              │
│    → Extract entities, facts, themes                    │
│    → Update L1, L2, L3 layers                           │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ 6. RETURN VALIDATED SCENE                               │
│    return draft                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Implementation Priorities

### Phase 1: Essential CLI Tools (MVP)
**Goal**: Make NCP usable for human writers immediately

**Tools to Build**:
1. ✅ `ncp-query` - Query scene requirements
2. ✅ `ncp-validate` - Basic validation (character names, thematic keywords)
3. ✅ `ncp-assist` - Simple prompts and voice samples

**Tech Stack**: Python 3.10+, Click (CLI framework), JSON parsing

**Timeline**: 1-2 weeks

### Phase 2: Knowledge Graph
**Goal**: Persistent narrative memory

**Components**:
1. Graph database setup (Neo4j or simple JSON-based)
2. L0-L3 layer implementation
3. `kg-query` and `kg-add` tools
4. Auto-extraction from scene text

**Tech Stack**: Neo4j or TinyDB, spaCy (entity extraction)

**Timeline**: 2-3 weeks

### Phase 3: Narrative Director API
**Goal**: Enable AI-assisted scene generation

**Components**:
1. Python API wrapping NCP + KG
2. LLM integration (OpenAI/Anthropic)
3. Self-critique loop implementation
4. Thematic resonance query system

**Tech Stack**: Python API, LangChain/custom LLM wrapper

**Timeline**: 3-4 weeks

### Phase 4: Advanced Features
**Goal**: Research and visualization

**Components**:
1. Coherence dashboard (web interface)
2. Arc visualization
3. Data export for research
4. Comparative analysis tools

**Tech Stack**: React/Next.js for web, D3.js for visualization

**Timeline**: 4-6 weeks

---

## Technical Architecture

### System Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INTERFACES                         │
├─────────────────────────────────────────────────────────────┤
│  CLI Tools          │  Python API        │  Web Dashboard   │
│  - ncp-query        │  - NarrativeDirector│  - React App    │
│  - ncp-validate     │  - NCPValidator    │  - D3 viz        │
│  - ncp-assist       │  - KGInterface     │                  │
│  - kg-query         │                    │                  │
└──────────┬──────────┴──────────┬─────────┴──────────┬───────┘
           │                     │                    │
           └─────────────────────┼────────────────────┘
                                 ↓
┌─────────────────────────────────────────────────────────────┐
│                    CORE ARCHON LAYER                        │
├─────────────────────────────────────────────────────────────┤
│  NCP Manager              Knowledge Graph Engine            │
│  - Schema validation      - Neo4j/JSON backend             │
│  - Checkpoint evaluation  - L0-L3 hierarchy                │
│  - Constraint checking    - Thematic resonance queries     │
└──────────┬──────────────────────────┬───────────────────────┘
           │                          │
           ↓                          ↓
┌──────────────────┐      ┌──────────────────────────┐
│  NCP Data Store  │      │  Knowledge Graph DB      │
│  (JSON files)    │      │  (Neo4j or JSON)         │
└──────────────────┘      └──────────────────────────┘
```

### Data Flow

```
Scene Requirements Request
         ↓
    NCP Manager reads schema
         ↓
    Returns: {chapter, alters, checkpoints, world_rules}
         ↓
    Writer/Agent uses data to write
         ↓
    Validation Request (scene text)
         ↓
    NCP Manager checks:
      - Character voices (via LLM or rules)
      - Thematic keywords
      - Continuity (via KG query)
         ↓
    Returns: {valid: bool, score: float, issues: []}
         ↓
    If valid → Ingest to Knowledge Graph
         ↓
    KG Engine extracts:
      - Entities (L0/L1)
      - Facts (L1)
      - Themes (L2)
      - Updates global arcs (L3)
```

---

## API Specifications

### 1. NCP Query API

```python
class NCPManager:
    def __init__(self, ncp_file: str):
        """Load and parse NCP JSON"""

    def get_chapter_requirements(self, chapter: int) -> ChapterRequirements:
        """Get all requirements for a chapter"""

    def get_scene_requirements(self, scene_id: str) -> SceneRequirements:
        """Get specific scene requirements"""

    def get_character_state(self, character: str, chapter: int) -> CharacterState:
        """Get character arc position at chapter"""

    def get_thematic_checkpoints(self, chapter: int) -> List[Checkpoint]:
        """Get validation checkpoints for chapter"""

    def get_world_rules(self, location: str) -> WorldRules:
        """Get physics/rules for a Kernwelt"""
```

### 2. Validation API

```python
class NCPValidator:
    def __init__(self, ncp_manager: NCPManager, kg: KnowledgeGraph):
        """Initialize with NCP and KG access"""

    def validate_scene(
        self,
        scene_text: str,
        chapter: int,
        strict: bool = False
    ) -> ValidationResult:
        """
        Validate scene against NCP constraints

        Returns:
            ValidationResult with score, issues, suggestions
        """

    def check_character_consistency(
        self,
        scene_text: str,
        active_alters: List[str]
    ) -> List[Issue]:
        """Validate alter voices and behaviors"""

    def check_thematic_alignment(
        self,
        scene_text: str,
        checkpoints: List[Checkpoint]
    ) -> List[Issue]:
        """Check if thematic beats are hit"""

    def check_continuity(
        self,
        scene_text: str,
        chapter: int
    ) -> List[Issue]:
        """Query KG for contradictions"""
```

### 3. Knowledge Graph API

```python
class KnowledgeGraph:
    def __init__(self, db_path: str):
        """Initialize graph database"""

    def add_node(
        self,
        level: str,  # L0, L1, L2, L3
        node_type: str,  # entity, fact, theme, arc
        data: dict
    ) -> NodeID:
        """Add node to graph at specified level"""

    def query(
        self,
        entity: str = None,
        theme: str = None,
        chapter_range: Tuple[int, int] = None,
        depth: int = 1
    ) -> QueryResult:
        """Query graph with flexible filters"""

    def thematic_resonance_query(
        self,
        current_theme: str,
        current_chapter: int
    ) -> List[Node]:
        """
        Get nodes thematically relevant to current scene
        (Core feature for "active forgetting")
        """

    def ingest_scene(
        self,
        scene_text: str,
        chapter: int,
        metadata: dict
    ):
        """
        Auto-extract and add:
        - L0: Raw text chunks
        - L1: Entities and facts
        - L2: Thematic connections
        - L3: Update global arcs
        """
```

---

## File Formats

### Scene File Format (Markdown)

```markdown
---
chapter: 4
scene_id: 1.4
title: "The Drowning Pool"
location: "Mnemosyne-Archipel (KW2)"
pov: "Kael (System)"
active_alters: ["Kael", "Rhys", "Kiko", "Lex"]
prose_style: "Fragmented"
validated: true
coherence_score: 8.7
---

# Chapter 4: The Drowning Pool

The water smells of salt and—

(not water)

—memory.

Kael's feet find no purchase. Falling. Always falling into—

(Kiko's voice, small and terrified: *It's cold*)

[Scene content continues...]

<!-- Validation Notes:
- ✅ Checkpoint: First trauma confrontation
- ✅ Lex avoids Kiko's emotional content
- ⚠️  Could strengthen Rhys's empathic response
-->
```

### Validation Report Format (JSON)

```json
{
  "scene_id": "1.4",
  "chapter": 4,
  "validation_timestamp": "2024-11-05T16:00:00Z",
  "overall_score": 8.7,
  "status": "PASS_WITH_WARNINGS",
  "checks": {
    "character_consistency": {
      "status": "PASS",
      "score": 9.0,
      "details": [
        {
          "alter": "Lex",
          "issue": null,
          "voice_match": 0.92
        },
        {
          "alter": "Kiko",
          "issue": "Voice sample small, but consistent",
          "voice_match": 0.85
        }
      ]
    },
    "thematic_alignment": {
      "status": "PASS",
      "score": 8.5,
      "checkpoints_met": 3,
      "checkpoints_total": 4,
      "missing": ["Strong Rhys empathic demonstration"]
    },
    "world_physics": {
      "status": "PASS",
      "score": 9.0,
      "details": "KW2 reactivity correctly shown"
    },
    "continuity": {
      "status": "PASS",
      "score": 10.0,
      "contradictions": []
    }
  },
  "suggestions": [
    "Add more internal dialogue from Rhys showing empathic attunement",
    "Consider Argus meta-observation about the system dynamics"
  ]
}
```

---

## Next Steps

To make this real, we should:

1. **Start with MVP CLI tools** - Get basic NCP querying working
2. **Define data schemas** - Formalize JSON structures for validation results
3. **Build simple validator** - Rule-based character/theme checking
4. **Prototype KG** - Start with simple JSON-based graph
5. **Iterate** - Use on actual writing, refine based on needs

**Which component should we build first?**
