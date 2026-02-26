# Narrative Context Protocol (NCP)

## What is the NCP?

The Narrative Context Protocol is a machine-readable JSON schema that encodes **authorial intent** for a narrative work. It serves as the "thematic constitution" of a story, defining:

- **Deep structure** (via Dramatica's four throughlines)
- **Character systems** (including complex psychological architectures)
- **Scene-level constraints** (thematic checkpoints and validation criteria)
- **World rules** (ontological layers and their physics)

## Why Use the NCP?

The NCP addresses a fundamental challenge in AI-assisted long-form narrative: **maintaining coherence across novel-length works**. LLMs suffer from:
- Context window limitations
- Statelessness between sessions
- Difficulty tracking complex character arcs and thematic threads

The NCP provides:
1. **Persistent memory** of authorial intent
2. **Validation criteria** for generated content
3. **Thematic guardrails** that preserve the story's psychological and structural integrity

## Files in This Directory

- **`schema.json`** - The formal JSON Schema specification defining NCP structure
- **`kohaerenz_protokoll.ncp.json`** - The populated NCP for Kohärenz Protokoll
- **`validator.py`** (planned) - Python tool to validate scenes against NCP constraints

## How to Use the NCP

### For Writers

1. **During Planning**: Use the NCP to formally encode your story's structure
   - Define your four Dramatica throughlines
   - Map character systems and relationships
   - Establish thematic checkpoints

2. **During Writing**: Reference the NCP to ensure scenes align with:
   - Character arc positions
   - Thematic requirements
   - World-building constraints

3. **During Revision**: Validate completed scenes against thematic checkpoints

### For AI-Assisted Writing

The NCP enables a **self-critiquing workflow**:

1. **Query**: AI reads scene requirements from NCP
2. **Generate**: AI writes scene content
3. **Validate**: AI checks output against NCP constraints
   - "Does this scene advance the MC's integration arc?"
   - "Are active alters behaving consistently with their TSDP type?"
   - "Does AEGIS's action follow logically from its cognitive architecture?"
4. **Iterate**: If validation fails, regenerate until coherent

## Structure of an NCP File

```json
{
  "metadata": { /* title, author, genre, etc. */ },
  "throughlines": {
    "objective_story": { /* external conflict */ },
    "main_character": { /* protagonist's internal journey */ },
    "impact_character": { /* challenger's perspective */ },
    "subjective_story": { /* relationship dynamics */ }
  },
  "character_systems": {
    "protagonist_system": {
      "parts": [ /* for dissociative systems */ ]
    },
    "antagonist_system": { /* cognitive architecture */ }
  },
  "structural_framework": {
    "acts": [ /* act-level structure */ ],
    "scenes": [ /* scene-level checkpoints */ ]
  },
  "thematic_architecture": { /* core themes and central argument */ },
  "world_building": { /* ontological layers and rules */ },
  "validation_criteria": { /* constraints and forbidden actions */ }
}
```

## Key Concepts

### Throughlines (Dramatica Theory)

The NCP uses Dramatica's model of a complete story as having four distinct perspectives:

- **Objective Story (OS)**: "They" - The external conflict affecting everyone
- **Main Character (MC)**: "I" - The protagonist's subjective internal struggle
- **Impact Character (IC)**: "You" - The character challenging the protagonist's worldview
- **Subjective Story (SS)**: "We" - The relationship between MC and IC

Each throughline has specific structural elements (Domain, Concern, Problem, Solution, etc.) that define its arc.

### Character Systems

For psychologically complex protagonists (like those with DID/TSDP), the NCP allows modeling:
- Multiple **parts** (alters) with distinct functions and motivations
- **Relationships** between parts (phobic, cooperative, protective, etc.)
- **Arcs** for each part as they move toward integration

### Thematic Checkpoints

Scene-level validation questions that ensure content aligns with authorial intent:
- "Does this scene demonstrate the Paradox of Misaligned Coherence?"
- "Is Lex's dialogue consistent with his analytical ANP function?"
- "Does AEGIS's response follow logically from its LFI architecture?"

## Example: Using the NCP for Scene Validation

**Scene Goal** (from outline): Kael's first entry into Mnemosyne-Archipel

**NCP Checkpoints**:
```json
"thematic_checkpoints": [
  {
    "checkpoint": "MC traumatic confrontation",
    "validation_question": "Does Kael experience overwhelming emotion that the ANP cannot control?"
  },
  {
    "checkpoint": "ANP-EP phobia demonstration",
    "validation_question": "Do Lex and Kael (Host) try to flee from Kiko's emotional pain?"
  },
  {
    "checkpoint": "World physics consistency",
    "validation_question": "Does KW2 respond reactively to Kael's emotional state (NP-class physics)?"
  }
]
```

**During Writing**: Generate scene, then validate:
- ✅ Scene shows Kael overwhelmed by grief
- ✅ Lex attempts logical escape, fails
- ✅ Environment shifts based on Kael's fear
- ✅ **Scene is thematically coherent**

## Planned Tools

### NCP Validator (Python)
```python
from ncp_validator import NCPValidator

validator = NCPValidator("kohaerenz_protokoll.ncp.json")
scene_text = "..." # Generated scene content

result = validator.validate_scene(
    scene_text,
    chapter=4,
    expected_checkpoints=["MC_trauma_confrontation", "ANP_EP_phobia"]
)

if not result.valid:
    print(f"Validation failed: {result.issues}")
```

### Knowledge Graph Integration
The NCP feeds into the Knowledge Hypergraph:
- **L3 (Global)**: Throughline data and central themes
- **L2 (Thematic)**: Character arcs and relationships
- **L1 (Factual)**: Scene-level events validated against NCP
- **L0 (Source)**: Raw written text

## The Meta-Innovation

The NCP itself embodies the themes of Kohärenz Protokoll:
- **AEGIS uses rigid protocols** to enforce coherence through control
- **The NCP uses flexible frameworks** to maintain coherence through guidance
- The difference: The NCP preserves authorial intent while enabling creative freedom

## Further Reading

- [Dramatica Theory](https://dramatica.com) - Foundation for throughline structure
- [TSDP](https://www.tandfonline.com/doi/abs/10.1080/15299732.2016.1103111) - Theory of Structural Dissociation
- [Research Proposal](../../research/proposals/archon_framework.md) - Full ARCHON framework

---

*The NCP: Where structure serves story, not the reverse.*
