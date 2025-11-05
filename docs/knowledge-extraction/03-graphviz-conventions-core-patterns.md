# Graphviz Conventions: Core Knowledge Patterns

## Source
Process DSL style guide for flowchart creation

## Core Philosophy
**Shape communicates meaning** - Visual semantics encode process structure

## Key Patterns

### Node Type Mapping

| What It Is | Shape | Example |
|------------|-------|---------|
| **Question/Decision** | Diamond | `"Is this a question?" [shape=diamond]` |
| **Action** | Box (default) | `"Take an action" [shape=box]` |
| **Command** | Plaintext | `"git commit -m 'msg'" [shape=plaintext]` |
| **State** | Ellipse | `"Current state" [shape=ellipse]` |
| **Warning** | Octagon (red fill) | `"STOP: Critical warning" [shape=octagon, style=filled, fillcolor=red, fontcolor=white]` |
| **Entry/Exit** | Double circle | `"Process starts" [shape=doublecircle]` |

### Edge Label Conventions

**Binary decisions:**
```dot
"Binary decision?" -> "Yes path" [label="yes"];
"Binary decision?" -> "No path" [label="no"];
```

**Multiple choice:**
```dot
"Multiple choice?" -> "Option A" [label="condition A"];
"Multiple choice?" -> "Option B" [label="condition B"];
"Multiple choice?" -> "Option C" [label="otherwise"];
```

**Process triggers:**
```dot
"Process A done" -> "Process B starts" [label="triggers", style=dotted];
```

### Naming Patterns

**Questions end with ?**
- "Should I do X?"
- "Can this be Y?"
- "Is Z true?"
- "Have I done W?"

**Actions start with verb**
- "Write the test"
- "Search for patterns"
- "Commit changes"
- "Ask for help"

**Commands are literal**
- `"grep -r 'pattern' ."`
- `"git status"`
- `"npm run build"`

**States describe situation**
- "Test is failing"
- "Build complete"
- "Stuck on error"

### Decision Tree: Choosing Shape

```dot
"Choosing a shape" [shape=ellipse]
  ↓
"Is it a decision?" [shape=diamond]
  yes → "Use diamond"
  no ↓
"Is it a command?" [shape=diamond]
  yes → "Use plaintext"
  no ↓
"Is it a warning?" [shape=diamond]
  yes → "Use octagon"
  no ↓
"Is it entry/exit?" [shape=diamond]
  yes → "Use doublecircle"
  no ↓
"Is it a state?" [shape=diamond]
  yes → "Use ellipse"
  no ↓
"Default: use box"
```

### Process Structure Template

```dot
"Trigger: Something happens" [shape=ellipse]
  ↓
"Initial check?" [shape=diamond]
  yes → "Main action" [shape=box]
         ↓
        "git status" [shape=plaintext]
         ↓
        "Another check?" [shape=diamond]
          ok → "Process complete" [shape=doublecircle]
          problem → "STOP: Don't do this" [shape=octagon, red]
  no → "Alternative action" [shape=box]
        ↓
       "Process complete" [shape=doublecircle]
```

### Good vs Bad Examples

**✅ GOOD (specific and shaped correctly):**
```dot
"Test failed" [shape=ellipse];
"Read error message" [shape=box];
"Can reproduce?" [shape=diamond];
"git diff HEAD~1" [shape=plaintext];
"NEVER ignore errors" [shape=octagon, red];
```

**❌ BAD (vague and wrong shapes):**
```dot
"Something wrong" [shape=box];  // Should be ellipse (state)
"Fix it" [shape=box];  // Too vague
"Check" [shape=box];  // Should be diamond
"Run command" [shape=box];  // Should be plaintext with actual command
```

### Visual Semantics Rules

**Shape selection is NOT arbitrary:**
- Shape encodes semantic meaning
- Reader should understand node type visually
- Consistency enables pattern recognition
- Breaking conventions creates confusion

**Labels must be semantic:**
- ❌ "step1", "helper2", "pattern4" (no meaning)
- ✅ "Validate input", "Transform data", "Save result" (clear purpose)

### Integration with Skills

**From writing-skills documentation:**

**Use flowcharts ONLY for:**
- Non-obvious decision points
- Process loops where you might stop too early
- "When to use A vs B" decisions

**Never use flowcharts for:**
- Reference material → Tables, lists
- Code examples → Markdown blocks
- Linear instructions → Numbered lists
- Labels without semantic meaning

## Unique Strengths
- Clear visual semantics
- Consistent shape vocabulary
- Process structure templates
- Good/bad examples
- Integration with markdown docs

## Potential Weaknesses
- Limited to graphviz/DOT syntax
- Requires understanding of shape meanings
- Could be over-specified for simple flows
- No guidance on when flowchart is overkill
