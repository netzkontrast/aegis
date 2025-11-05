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

## Planned Tools

### 3. ncp_assist.py - Writing Assistant
Generate writing prompts and character voice samples

**Status**: Design phase

**Planned Usage**:
```bash
python ncp_assist.py --chapter 4 --prompt
python ncp_assist.py --character Lex --voice-sample
```

### 4. kg_query.py - Knowledge Graph Query
Query and update the hierarchical narrative memory

**Status**: Design phase

**Planned Usage**:
```bash
kg_query.py --entity Kael --chapter 4
kg_add.py --fact "Kael entered KW2" --chapter 4
```

### 5. archon_generate.py - Narrative Director CLI
Full AI-assisted scene generation with self-critique

**Status**: Design phase

**Planned Usage**:
```bash
python archon_generate.py --chapter 4 --scene 1.4
```

## Development Roadmap

### Phase 1: Essential Read-Only Tools ✅
- [x] `ncp_query.py` - Basic NCP querying

### Phase 2: Validation Tools (In Progress)
- [x] `ncp_validate.py` - Rule-based validation
- [x] Character presence checking
- [x] Thematic keyword matching
- [ ] Advanced character voice consistency (LLM-based)
- [ ] Prose style deep analysis

### Phase 3: Knowledge Graph
- [ ] Graph database setup
- [ ] `kg_query.py` and `kg_add.py`
- [ ] Auto-extraction from scenes

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
# 1. Plan scene
python ncp_query.py --scene 1.4 --verbose > scene_plan.txt

# 2. Write scene (human)
vim manuscript/act_1/chapter_04.md

# 3. Validate (future)
python ncp_validate.py chapter_04.md

# 4. Update knowledge graph (future)
python kg_add.py --source chapter_04.md --auto-extract

# 5. Generate next scene (future)
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
# Get chapter context
python ncp_query.py --chapter 4 --verbose

# Get specific scene requirements
python ncp_query.py --scene 1.4

# Get voice samples for active alters
python ncp_query.py --character Lex --chapter 4
python ncp_query.py --character Kiko --chapter 4

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
