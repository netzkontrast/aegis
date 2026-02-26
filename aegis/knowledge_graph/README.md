# ARCHON Knowledge Graph

Hierarchical narrative memory system for storing and querying story context.

## Overview

The Knowledge Graph implements a four-layer hierarchy:

- **L0 (Source)**: Raw text chunks from scenes
- **L1 (Factual)**: Extracted entities, facts, relationships
- **L2 (Thematic)**: Aggregated themes and patterns
- **L3 (Global)**: Story-wide arcs and conflicts

## Architecture

### Storage Format

JSON-based file storage at `ARCHON/knowledge_graph/graph.json`:

```json
{
  "nodes": {
    "uuid-1": {
      "node_id": "uuid-1",
      "level": "L1",
      "node_type": "entity",
      "content": "Kael",
      "metadata": {"chapter": 4},
      "tags": ["character"],
      "created_at": "2024-11-05T12:00:00"
    }
  },
  "edges": {
    "uuid-2": {
      "edge_id": "uuid-2",
      "source_id": "uuid-1",
      "target_id": "uuid-3",
      "relation_type": "appeared_in"
    }
  }
}
```

### Node Types by Level

**L0 Types:**
- `source_chunk`: Raw text from scenes

**L1 Types:**
- `entity`: Character, location, object
- `fact`: Discrete factual statement
- `relationship`: Connection between entities

**L2 Types:**
- `theme`: Thematic pattern
- `pattern`: Recurring motif

**L3 Types:**
- `arc`: Character or story arc
- `conflict`: Major conflict

## Usage

### Python API

```python
from ARCHON.knowledge_graph.kg_core import (
    KnowledgeGraph, Node, NodeLevel, NodeType
)

# Initialize graph
graph = KnowledgeGraph()

# Add a node
node = Node(
    level=NodeLevel.L1,
    node_type=NodeType.ENTITY,
    content="Kael",
    metadata={"chapter": 4},
    tags=["character", "protagonist"]
)
graph.add_node(node)
graph.save()

# Query nodes
entities = graph.query(level=NodeLevel.L1, node_type=NodeType.ENTITY)
chapter4 = graph.query(metadata_filters={"chapter": 4})
tagged = graph.query(tags=["trauma"])

# Ingest a scene
scene_text = "Kael entered the Archipel..."
graph.ingest_scene(scene_text, {"chapter": 4, "scene_id": "1.4"})
```

### CLI Tools

**Add nodes:**

```bash
# Add an entity
python kg_add.py --level L1 --type entity --content "Kael" \
  --metadata '{"chapter": 4}' --tags character,protagonist

# Add a fact
python kg_add.py --level L1 --type fact \
  --content "Kael entered Mnemosyne-Archipel" \
  --metadata '{"chapter": 4}'

# Add a theme
python kg_add.py --level L2 --type theme \
  --content "Trauma processing" \
  --tags trauma,memory
```

**Query nodes:**

```bash
# Get all L1 nodes
python kg_query.py --level L1

# Get nodes from chapter 4
python kg_query.py --chapter 4

# Search content
python kg_query.py --search "Kael"

# Filter by tags
python kg_query.py --tags trauma --level L2

# Output as JSON
python kg_query.py --level L1 --json
```

## Implementation Status

### ✅ Completed (MVP)
- Core data structures (Node, Edge, Graph)
- JSON-based persistence
- Flexible query system
- CLI tools (kg_add, kg_query)
- Basic scene ingestion (L0, L1)

### 🚧 Planned (Future)
- L2/L3 aggregation logic
- Thematic resonance queries
- Semantic search with embeddings
- Neo4j backend option
- Graph visualization
- Advanced NER for entity extraction

## Testing

```bash
# Run all tests
pytest tests/test_kg_core.py tests/test_kg_tools.py -v

# Test specific functionality
pytest tests/test_kg_core.py::test_graph_persistence -v
```
