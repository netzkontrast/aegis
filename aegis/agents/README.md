# The Narrative Director: Agentic System Specification

## Overview

The **Narrative Director** is the autonomous AI agent at the heart of the ARCHON framework. It is responsible for translating high-level thematic goals from the NCP into actual narrative content while maintaining coherence through self-critique.

## Architecture

The Narrative Director follows a **Reason-Act-Critique** loop:

```
┌─────────────────────────────────────────────────────┐
│                 NARRATIVE DIRECTOR                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌─────────────────────────────────────────────┐  │
│  │         1. REASON (Planning)                │  │
│  │  - Read current thematic goal from NCP      │  │
│  │  - Decompose into concrete scene beats      │  │
│  │  - Identify required context                │  │
│  └────────────────┬────────────────────────────┘  │
│                   ↓                                │
│  ┌─────────────────────────────────────────────┐  │
│  │         2. QUERY (Context Retrieval)        │  │
│  │  - Query Knowledge Graph for:               │  │
│  │    * Thematically resonant past events      │  │
│  │    * Character states at this point         │  │
│  │    * World rules for current location       │  │
│  └────────────────┬────────────────────────────┘  │
│                   ↓                                │
│  ┌─────────────────────────────────────────────┐  │
│  │         3. ACT (Generation)                 │  │
│  │  - Generate scene content using LLM         │  │
│  │  - Apply prose style for integration level  │  │
│  │  - Ensure alter voices are distinct         │  │
│  └────────────────┬────────────────────────────┘  │
│                   ↓                                │
│  ┌─────────────────────────────────────────────┐  │
│  │         4. CRITIQUE (Self-Validation)       │  │
│  │  - Separate LLM call to validate output     │  │
│  │  - Check against NCP checkpoints            │  │
│  │  - Score thematic alignment                 │  │
│  └────────────────┬────────────────────────────┘  │
│                   ↓                                │
│              Valid? ─No─> Iterate (max 5x)        │
│                │                                   │
│               Yes                                  │
│                ↓                                   │
│  ┌─────────────────────────────────────────────┐  │
│  │         5. INGEST (Memory Update)           │  │
│  │  - Extract facts from generated scene       │  │
│  │  - Update Knowledge Graph (L0-L3)           │  │
│  │  - Mark thematic checkpoints as complete    │  │
│  └─────────────────────────────────────────────┘  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## Core Modules

### Module 1: Planner (Reason)

**Inputs**:
- Current chapter/scene from NCP
- Thematic goal (e.g., "Demonstrate ANP-EP phobia")
- Current narrative state from KG

**Process**:
1. Read NCP requirements for scene
2. Decompose abstract goal into concrete beats:
   - "ANP-EP phobia" → "Lex must encounter Kiko's pain and attempt to flee"
3. Identify required context:
   - What has Kael learned so far?
   - What is Lex's current integration level?
   - What are Kiko's known triggers?

**Output**:
- Structured scene plan with beats
- Context query specification

### Module 2: Context Manager (Query)

**Inputs**:
- Context query from Planner
- Current chapter/scene ID

**Process**:
1. Query Knowledge Graph with **thematic resonance**:
   - NOT: "Get all information about Lex"
   - BUT: "Get information tagged with [ANP-EP-phobia] AND [Lex] from chapters 1-3"
2. Apply **active forgetting**:
   - Discard information thematically dissonant with current scene
   - e.g., Details about resolved subplot in KW1 aren't relevant for KW2 trauma processing
3. Compress context to fit LLM window

**Output**:
- Focused, relevant context (typically 2-5K tokens)
- Character voice samples for active alters

### Module 3: Generator (Act)

**Inputs**:
- Scene plan from Planner
- Focused context from Context Manager
- Prose style specification (fragmented/transitional/polyphonic)

**Process**:
1. Construct LLM prompt:
```
You are writing Chapter 4, Scene 1.4 of "Kohärenz Protokoll."

SCENE REQUIREMENTS:
- Location: Mnemosyne-Archipel (KW2)
- POV: Kael (System) - multiple alters co-conscious
- Active Alters: Kael, Rhys, Kiko, Lex
- Prose Style: Fragmented

THEMATIC GOAL:
Demonstrate ANP-EP phobia. Lex must encounter Kiko's traumatic
memory and attempt to flee from the emotional pain.

CONTEXT (from previous scenes):
[Relevant facts from KG]

CHARACTER VOICES:
Lex: [voice sample - analytical, hypotactic]
Kiko: [voice sample - child, sensory, frightened]

WORLD RULES (KW2):
- Physics reactive to emotion
- Time is non-linear
- Memory islands shift based on associations

Generate the scene ensuring:
1. Distinct alter voices
2. Fragmented syntax showing internal conflict
3. Lex's phobic avoidance of Kiko's pain
4. KW2 environment reacting to emotional state
```

2. Call LLM (GPT-4, Claude 3, etc.)
3. Parse and structure output

**Output**:
- Draft scene text (1000-2000 words)

### Module 4: Critic (Critique)

**Inputs**:
- Generated scene text
- NCP checkpoints for this scene
- Character constraints

**Process**:
1. **Separate LLM call** (this is crucial - not same context as generation)
2. Prompt for validation:
```
You are a narrative coherence validator for "Kohärenz Protokoll."

SCENE TO VALIDATE:
[Generated text]

NCP CHECKPOINTS:
1. "Does Lex's voice match his analytical ANP profile?"
   - Expected: Hypotactic syntax, technical vocabulary
   - Forbidden: Direct emotional expression

2. "Is the ANP-EP phobia demonstrated?"
   - Required: Lex must actively avoid Kiko's pain
   - Must be shown, not told

3. "Do KW2 physics operate correctly?"
   - Required: Environment reacts to emotional state
   - Expected: Non-linear time, memory associations

VALIDATION QUESTIONS:
For each checkpoint, answer:
- PASS/FAIL
- Evidence (quote specific lines)
- Suggestions for improvement if failed

Overall coherence score: 0-10
```

3. Parse validation response
4. If score < 7.0, mark as failed and provide feedback

**Output**:
- Validation result (pass/fail)
- Coherence score (0-10)
- Specific issues and suggestions

### Module 5: Knowledge Integrator (Ingest)

**Inputs**:
- Validated scene text
- Scene metadata (chapter, location, active alters)

**Process**:
1. **L0 (Source)**: Store raw scene text in chunks
2. **L1 (Facts)**: Extract using NER + relationship extraction:
   - "Kael entered Mnemosyne-Archipel in Chapter 4"
   - "Lex attempted to flee from Kiko's memory"
   - "Memory loop occurred in Lake of Tears"
3. **L2 (Themes)**: Tag facts with themes:
   - Facts about Lex fleeing → "ANP-EP-phobia" theme
   - Facts about memory loops → "Trauma-processing" theme
4. **L3 (Global)**: Update story-level arcs:
   - Kael's integration level: 2.3/10 → 2.7/10 (progress)
   - ANP-EP cooperation: Still phobic, but first contact made

**Output**:
- Knowledge Graph updated at all levels
- Thematic checkpoints marked as complete

---

## Implementation: Python Class Structure

```python
from dataclasses import dataclass
from typing import List, Dict, Optional
import anthropic  # or openai

@dataclass
class ScenePlan:
    """Output of Planner module"""
    scene_id: str
    thematic_goal: str
    beats: List[str]
    context_query: Dict
    prose_style: str
    active_alters: List[str]

@dataclass
class ValidationResult:
    """Output of Critic module"""
    valid: bool
    score: float  # 0-10
    issues: List[Dict]
    suggestions: List[str]
    evidence: Dict  # Quotes supporting pass/fail

class NarrativeDirector:
    """
    Main agent class implementing the Reason-Act-Critique loop
    """

    def __init__(
        self,
        ncp_path: str,
        kg_path: str,
        llm_client,  # Anthropic/OpenAI client
        max_iterations: int = 5
    ):
        self.ncp = NCPManager(ncp_path)
        self.kg = KnowledgeGraph(kg_path)
        self.llm = llm_client
        self.max_iterations = max_iterations

    def generate_scene(
        self,
        chapter: int,
        scene_id: str,
        temperature: float = 0.7
    ) -> str:
        """
        Main entry point: Generate a valid scene through
        iterative Reason-Act-Critique loops
        """

        # 1. REASON: Plan the scene
        plan = self._plan_scene(chapter, scene_id)

        # 2. QUERY: Get relevant context
        context = self._get_context(plan.context_query)

        # Iterate with self-critique
        for iteration in range(self.max_iterations):
            # 3. ACT: Generate scene
            scene_text = self._generate_draft(plan, context, temperature)

            # 4. CRITIQUE: Validate
            validation = self._validate_scene(scene_text, plan)

            if validation.valid:
                # 5. INGEST: Update knowledge graph
                self._ingest_scene(scene_text, chapter, plan)
                return scene_text

            # If not valid, use feedback to refine
            print(f"Iteration {iteration + 1}: Score {validation.score}")
            print(f"Issues: {validation.issues}")
            # Context for next iteration includes validation feedback
            context['validation_feedback'] = validation.suggestions

        # Max iterations reached without success
        raise Exception(f"Failed to generate valid scene after {self.max_iterations} attempts")

    def _plan_scene(self, chapter: int, scene_id: str) -> ScenePlan:
        """REASON: Create scene plan from NCP"""
        requirements = self.ncp.get_scene_requirements(scene_id)

        # Decompose thematic goals into beats
        beats = self._decompose_goal(requirements.thematic_goal)

        # Build context query
        context_query = {
            'themes': requirements.required_themes,
            'characters': requirements.active_alters,
            'chapter_range': (1, chapter - 1),  # Past context only
            'location': requirements.location
        }

        return ScenePlan(
            scene_id=scene_id,
            thematic_goal=requirements.thematic_goal,
            beats=beats,
            context_query=context_query,
            prose_style=requirements.prose_style,
            active_alters=requirements.active_alters
        )

    def _get_context(self, query: Dict) -> Dict:
        """QUERY: Thematic resonance retrieval from KG"""
        # Query KG with thematic tags
        relevant_nodes = self.kg.thematic_resonance_query(
            themes=query['themes'],
            characters=query['characters'],
            chapter_range=query['chapter_range']
        )

        # Compress to fit context window
        context = self._compress_context(relevant_nodes)

        return context

    def _generate_draft(
        self,
        plan: ScenePlan,
        context: Dict,
        temperature: float
    ) -> str:
        """ACT: Generate scene using LLM"""

        prompt = self._build_generation_prompt(plan, context)

        response = self.llm.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4000,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def _validate_scene(
        self,
        scene_text: str,
        plan: ScenePlan
    ) -> ValidationResult:
        """CRITIQUE: Validate scene against NCP"""

        checkpoints = self.ncp.get_thematic_checkpoints(plan.scene_id)

        # Build validation prompt (separate LLM call)
        prompt = self._build_validation_prompt(scene_text, checkpoints, plan)

        response = self.llm.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            temperature=0.1,  # Low temperature for consistent validation
            messages=[{"role": "user", "content": prompt}]
        )

        # Parse structured validation response
        return self._parse_validation(response.content[0].text)

    def _ingest_scene(
        self,
        scene_text: str,
        chapter: int,
        plan: ScenePlan
    ):
        """INGEST: Update Knowledge Graph"""
        self.kg.ingest_scene(
            scene_text=scene_text,
            chapter=chapter,
            metadata={
                'scene_id': plan.scene_id,
                'active_alters': plan.active_alters,
                'themes': plan.thematic_goal
            }
        )

    # Helper methods for prompt construction, parsing, etc.
    # [Additional implementation details...]
```

---

## Prompt Engineering

### Key Principles for Narrative Director Prompts

1. **Separate Generation and Critique**: Never ask the same LLM call to generate AND validate. Use separate API calls.

2. **Structured Output**: Request JSON or clearly delimited sections for parsing

3. **Few-Shot Examples**: Include voice samples from NCP character profiles

4. **Explicit Constraints**: List forbidden actions clearly

5. **Self-Reference to NCP**: Make the LLM aware it's operating under constraints

### Example Generation Prompt Template

```
You are the Narrative Director for "Kohärenz Protokoll," an AI agent
responsible for generating narrative content that adheres to the
Narrative Context Protocol (NCP).

SCENE SPECIFICATION:
Chapter: {chapter}
Scene ID: {scene_id}
Location: {location}
POV: {pov}
Prose Style: {prose_style}

THEMATIC GOAL:
{thematic_goal}

SCENE BEATS TO HIT:
{beats}

ACTIVE ALTERS (maintain distinct voices):
{alter_profiles}

RELEVANT CONTEXT FROM PRIOR SCENES:
{kg_context}

WORLD RULES:
{world_physics}

CONSTRAINTS:
- Forbidden: {forbidden_actions}
- Required: {required_elements}

Generate 1000-1500 words of narrative that:
1. Hits all scene beats in order
2. Maintains distinct alter voices
3. Respects world physics
4. Uses {prose_style} style

Begin with the scene text:
```

### Example Validation Prompt Template

```
You are a narrative coherence validator. Your task is to check
if the following scene satisfies its NCP requirements.

SCENE TEXT:
\"\"\"
{scene_text}
\"\"\"

VALIDATION CHECKPOINTS:
{checkpoints}

For each checkpoint, provide:
1. STATUS: PASS or FAIL
2. EVIDENCE: Quote specific lines that support your judgment
3. SCORE: 0-10 for this checkpoint
4. SUGGESTION: If failed, how to fix

Then provide:
OVERALL_SCORE: 0-10 (average of checkpoint scores)
VALID: true/false (if overall_score >= 7.0)

Format your response as JSON:
{
  "checkpoints": [
    {
      "name": "...",
      "status": "PASS/FAIL",
      "evidence": "...",
      "score": 8.5,
      "suggestion": "..."
    }
  ],
  "overall_score": 8.2,
  "valid": true
}
```

---

## Performance Considerations

### Context Window Management

**Problem**: Even with large context windows (200K tokens), we need to be selective about what context to include.

**Solution**: Thematic Resonance Query
- Don't load entire Knowledge Graph
- Query only for nodes tagged with current scene's themes
- Use embedding similarity for semantic relevance
- Implement "active forgetting" - discard dissonant information

### Iteration Budget

**Problem**: Self-critique loops could run indefinitely or waste API calls

**Solution**:
- Max 5 iterations per scene
- Early stopping if score >= 9.0
- If failing after 5 iterations, flag for human review
- Track iteration patterns to refine prompts

### Cost Management

**Estimates** (using Claude 3.5 Sonnet):
- Generation: ~$0.10 per scene (4K output)
- Validation: ~$0.05 per scene (2K output)
- Total per scene: ~$0.15
- Total for 39 chapters (avg 3 scenes each): ~$17.55

**Optimization**:
- Use cheaper models for validation (GPT-4o-mini)
- Cache common context (voice samples, world rules)
- Batch process scenes where possible

---

## Testing Strategy

### Unit Tests

```python
def test_planner_decomposes_goal():
    """Test that abstract goals become concrete beats"""
    director = NarrativeDirector(...)
    plan = director._plan_scene(chapter=4, scene_id="1.4")

    assert "ANP-EP phobia" in plan.thematic_goal
    assert any("Lex" in beat and "flee" in beat for beat in plan.beats)

def test_validator_catches_voice_inconsistency():
    """Test that validator catches alter voice errors"""
    scene_with_error = "Lex shouted emotionally, 'I'm so scared!'"
    validation = director._validate_scene(scene_with_error, plan)

    assert not validation.valid
    assert any("Lex" in issue['character'] for issue in validation.issues)

def test_kg_ingest_extracts_facts():
    """Test that scene ingestion updates KG"""
    scene = "Kael entered the Archipelago. Mnemosyne greeted him."
    director._ingest_scene(scene, chapter=4, plan)

    result = director.kg.query(entity="Kael", chapter=4)
    assert "entered Archipelago" in str(result)
```

### Integration Tests

```python
def test_full_generation_loop():
    """Test end-to-end scene generation"""
    director = NarrativeDirector(...)

    scene = director.generate_scene(chapter=4, scene_id="1.4")

    # Should be valid prose
    assert len(scene) > 500
    assert "Kael" in scene

    # Should pass validation
    validation = director._validate_scene(scene, ...)
    assert validation.valid
    assert validation.score >= 7.0
```

---

## Deployment & Usage

### As a CLI Tool

```bash
# Generate a scene
archon generate --chapter 4 --scene 1.4 --output chapter_04_scene_01.md

# Validate existing scene
archon validate manuscript/act_1/chapter_04.md

# Batch generate all scenes in an act
archon generate-act --act 1 --output-dir manuscript/act_1/
```

### As a Python Library

```python
from aegis import NarrativeDirector

director = NarrativeDirector(
    ncp_path="aegis/ncp/kohaerenz_protokoll.ncp.json",
    kg_path="aegis/knowledge_graph/",
    llm_client=anthropic.Anthropic()
)

# Generate single scene
scene = director.generate_scene(chapter=4, scene_id="1.4")
print(scene)

# Or validate human-written scene
with open("my_scene.md") as f:
    result = director.validate_scene(f.read(), chapter=4)

if not result.valid:
    print("Issues:", result.issues)
    print("Suggestions:", result.suggestions)
```

---

## Future Enhancements

1. **Multi-Agent Dialogue**: Separate agents for each alter's voice generation
2. **Reinforcement Learning**: Learn from validation scores to improve prompts
3. **Style Transfer**: Learn prose style from example chapters
4. **Interactive Mode**: Human-in-the-loop for ambiguous decisions
5. **Visualization**: Real-time coherence tracking dashboard

---

*The Narrative Director: Where thematic intent meets agentic execution.*
