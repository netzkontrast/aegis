# ARCHON Tools

Command-line utilities for interacting with the ARCHON framework.

## Available Tools

### 1. ncp_query.py - NCP Query Tool

Query the Narrative Context Protocol for scene requirements, character states, and validation criteria.

**Installation**: No dependencies beyond Python 3.10+ standard library

**Usage**:

```bash
# Show project overview
python ncp_query.py

# Get chapter information
python ncp_query.py --chapter 4

# Get detailed scene requirements
python ncp_query.py --scene 1.4

# Get character state at specific chapter
python ncp_query.py --character Lex --chapter 4

# Verbose output with all details
python ncp_query.py --chapter 4 --verbose

# Find all scenes featuring an alter
python ncp_query.py --find-alter Kiko
```

**Examples**:

```bash
$ python ncp_query.py --chapter 4
============================================================
CHAPTER 4 INFORMATION
============================================================
Act: 1 - Fragmentation and First Echoes
Thematic Focus: Establishing the oppressive order...
Protagonist State: Fragmented, amnesic, trauma-avoidant...
```

```bash
$ python ncp_query.py --character Lex --chapter 4
============================================================
CHARACTER STATE: Lex (Chapter 4)
============================================================
Type: ANP
Function: Analyst and intellectual controller
Arc State: Believes pure logic is the solution
```

```bash
$ python ncp_query.py --find-alter Kiko
Scenes featuring Kiko:
  [1.4] Ch4: The Drowning Pool (Mnemosyne-Archipel)
  [2.3] Ch16: The Child in the Maze (Mnemosyne-Archipel)
  ...
```

### 2. ncp_validate.py - Scene Validator ✅

Validate written prose against NCP constraints using rule-based checks.

**Installation**: No dependencies beyond Python 3.10+ standard library

**Usage**:

```bash
# Validate a scene file
python ncp_validate.py manuscript/act_1/chapter_01_scene_01.md

# Specify chapter explicitly
python ncp_validate.py scene.md --chapter 1

# Verbose output with all issues
python ncp_validate.py scene.md --verbose

# Specify scene ID for detailed checks
python ncp_validate.py scene.md --scene 1.1
```

**Validation Checks**:
- **Length**: 500-3000 word range (warnings outside)
- **Character Presence**: Expected alters mentioned in scene
- **Prose Style**: Act-specific style matching (fragmented/transitional/polyphonic)
- **World Physics**: Location-specific keywords (KW1-KW4)
- **Thematic Checkpoints**: Required themes present

**Scoring**: 0-10 scale with ERROR/WARNING/INFO severity levels

**Example Output**:
```bash
$ python ncp_validate.py chapter_01_scene_01.md --verbose
============================================================
VALIDATION REPORT
============================================================

Status: ✅ PASS
Score: 10.0/10.0
Checks Passed: 5/5
Word Count: 1711

✨ No issues found! Scene is excellent.
============================================================
```

### 3. ncp_assist.py - Writing Assistant ✅

Generate writing prompts, character voice samples, and stylistic guidance.

**Installation**: No dependencies beyond Python 3.10+ standard library

**Usage**:

```bash
# Generate scene writing prompt
python ncp_assist.py --scene 1.4 --prompt

# Generate chapter overview prompt
python ncp_assist.py --chapter 4 --prompt

# Get character voice sample
python ncp_assist.py --character Lex --voice-sample

# Get character voice at specific chapter
python ncp_assist.py --character Lex --chapter 4 --voice-sample

# Get style guidance for a chapter
python ncp_assist.py --chapter 15 --style-guide

# Verbose output with all details
python ncp_assist.py --scene 1.4 --prompt --verbose
```

**Features**:
- **Scene Prompts**: Complete writing guide including structure, active alters, sensory keywords, and opening hooks
- **Chapter Prompts**: Overview of all scenes in a chapter with thematic focus
- **Character Voice Samples**: Speech patterns, vocabulary, dialogue, and internal voice examples
- **Style Guidance**: Act-specific prose techniques and emotional registers
- **Sensory Keywords**: Location-specific visual, tactile, auditory, and emotional vocabulary
- **Opening Hooks**: Suggested opening lines for scenes

**Example Output**:

```bash
$ python ncp_assist.py --character Lex --voice-sample
============================================================
CHARACTER VOICE: Lex (Chapter 1)
============================================================
Type: ANP
Function: Analyst and intellectual controller

VOICE PROFILE
────────────────────────────────────────────────────────────
Speech Patterns: Logical, analytical, precise. Full sentences with technical detail.
Vocabulary: Scientific, technical, controlling. Uses statistics and facts.

DIALOGUE SAMPLES
────────────────────────────────────────────────────────────
  "Your emotional response is counterproductive. Focus on the data."
  "I've calculated seventeen potential outcomes. None are optimal."
```

### 4. kg_add.py - Add Nodes to Knowledge Graph ✅

Add nodes manually to the knowledge graph.

**Status**: Implemented

**Usage**:

```bash
# Add an entity
python kg_add.py --level L1 --type entity --content "Kael" \
  --metadata '{"chapter": 4}' --tags character,protagonist

# Add a fact
python kg_add.py --level L1 --type fact \
  --content "Kael entered Mnemosyne-Archipel" \
  --metadata '{"chapter": 4}'
```

### 5. kg_query.py - Query Knowledge Graph ✅

Query the knowledge graph with flexible filters.

**Status**: Implemented

**Usage**:

```bash
# Query by level
python kg_query.py --level L1

# Query by chapter
python kg_query.py --chapter 4

# Search content
python kg_query.py --search "Kael"

# JSON output
python kg_query.py --level L1 --json
```

## Planned Tools

### archon_generate.py - Narrative Director CLI
Full AI-assisted scene generation with self-critique

**Status**: Design phase

**Planned Usage**:
```bash
python archon_generate.py --chapter 4 --scene 1.4
```

## Development Roadmap

### Phase 1: Essential Read-Only Tools ✅
- [x] `ncp_query.py` - Basic NCP querying

### Phase 2: Writing Support Tools ✅
- [x] `ncp_validate.py` - Rule-based validation
- [x] `ncp_assist.py` - Writing prompts and voice samples
- [x] Character presence checking
- [x] Thematic keyword matching
- [x] Style guidance per Act
- [ ] Advanced character voice consistency (LLM-based)
- [ ] Prose style deep analysis

### Phase 3: Knowledge Graph ✅
- [x] JSON storage setup
- [x] `kg_query.py` and `kg_add.py` (CLI tools)
- [x] Auto-extraction from scenes (Basic)
- [ ] Advanced Graph database (Neo4j - Future)

### Phase 4: AI Integration
- [ ] `archon_generate.py` - Full Narrative Director
- [ ] Self-critique loops
- [ ] Thematic resonance queries

## Tool Design Principles

1. **Unix Philosophy**: Each tool does one thing well
2. **Composable**: Tools can be piped and chained
3. **Human-Readable**: Default output is formatted for humans
4. **Machine-Readable**: `--json` flag for programmatic use
5. **Self-Documenting**: Comprehensive `--help` text

## Contributing

When adding new tools:

1. Follow the naming convention: `ncp_*.py`, `kg_*.py`, `archon_*.py`
2. Use `argparse` for CLI interface
3. Provide `--help`, `--verbose`, and `--json` options
4. Include examples in docstring
5. Update this README

## Integration with Workflow

```bash
# 1. Get writing prompt and guidance
python ncp_assist.py --scene 1.4 --prompt --verbose

# 2. Get character voice samples for active alters
python ncp_assist.py --character Lex --voice-sample
python ncp_assist.py --character Rhys --voice-sample

# 3. Check detailed scene requirements
python ncp_query.py --scene 1.4 --verbose > scene_plan.txt

# 4. Write scene (human)
vim manuscript/act_1/chapter_04.md

# 5. Validate
python ncp_validate.py chapter_04.md --verbose

# 6. Update knowledge graph (future)
python kg_add.py --source chapter_04.md --auto-extract

# 7. Generate next scene (future)
python archon_generate.py --chapter 5 --scene 2.1
```

## Technical Notes

### NCP File Location
Tools auto-detect NCP file at `ARCHON/ncp/kohaerenz_protokoll.ncp.json`

Override with `--ncp /path/to/file.json`

### JSON Schema Validation
All tools validate NCP against `ARCHON/ncp/schema.json` on load

### Error Handling
- Missing files → Clear error message
- Invalid JSON → Show parse error location
- Missing data → Graceful degradation, warn user

### Performance
- Cold start: ~100ms (JSON parsing)
- Queries: <10ms (in-memory)
- Batch operations: Use `--json` for programmatic processing

## Examples: Complete Workflow

### Workflow 1: Planning a Scene

```bash
# Get chapter context and style guidance
python ncp_assist.py --chapter 4 --prompt

# Get comprehensive scene writing prompt
python ncp_assist.py --scene 1.4 --prompt --verbose

# Get voice samples for active alters
python ncp_assist.py --character Lex --chapter 4 --voice-sample
python ncp_assist.py --character Kiko --chapter 4 --voice-sample

# Get detailed technical requirements
python ncp_query.py --scene 1.4 --verbose

# Now write scene with this guidance...
```

### Workflow 2: Tracking Alter Activity

```bash
# Find all scenes with Nyx
python ncp_query.py --find-alter Nyx

# Track Nyx's arc across acts
python ncp_query.py --character Nyx --chapter 1   # Act I
python ncp_query.py --character Nyx --chapter 20  # Act II
python ncp_query.py --character Nyx --chapter 35  # Act III
```

### Workflow 3: Validation (Future)

```bash
# Write scene
vim chapter_04.md

# Validate
python ncp_validate.py chapter_04.md --verbose

# If validation fails:
python ncp_validate.py chapter_04.md --suggest-fixes

# Revise and re-validate
vim chapter_04.md
python ncp_validate.py chapter_04.md

# When passed, update knowledge graph
python kg_add.py --source chapter_04.md
```

---

*Tools that serve the story, not the reverse.*
