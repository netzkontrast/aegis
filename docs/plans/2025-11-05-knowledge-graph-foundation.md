# Knowledge Graph Foundation Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a hierarchical knowledge graph (L0-L3) for storing and querying narrative memory, enabling thematic resonance queries and context retrieval

**Architecture:** JSON-based graph storage with four layers (L0: raw text, L1: facts, L2: themes, L3: global arcs). Python API for add/query operations. CLI tools for manual interaction. Simple file-based storage for MVP (no Neo4j complexity).

**Tech Stack:** Python 3.10+, json (storage), pathlib (file ops), dataclasses (structured data), uuid (node IDs)

---

## Task 1: Design and Test Core Data Structures

**Files:**
- Create: `ARCHON/knowledge_graph/kg_core.py`
- Create: `tests/test_kg_core.py`

**Step 1: Write test for Node creation**

```python
#!/usr/bin/env python3
"""Tests for knowledge graph core data structures"""

import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from ARCHON.knowledge_graph.kg_core import Node, NodeLevel, NodeType

def test_node_creation():
    """Test basic node creation"""
    node = Node(
        level=NodeLevel.L1,
        node_type=NodeType.FACT,
        content="Kael entered Mnemosyne-Archipel",
        metadata={"chapter": 4}
    )

    assert node.level == NodeLevel.L1
    assert node.node_type == NodeType.FACT
    assert node.content == "Kael entered Mnemosyne-Archipel"
    assert node.metadata["chapter"] == 4
    assert node.node_id is not None  # Should auto-generate
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_kg_core.py::test_node_creation -v`
Expected: FAIL with "No module named 'ARCHON.knowledge_graph.kg_core'"

**Step 3: Create directory and basic data structures**

```bash
mkdir -p ARCHON/knowledge_graph
```

Create `ARCHON/knowledge_graph/kg_core.py`:

```python
#!/usr/bin/env python3
"""
Knowledge Graph Core - Data Structures

Defines the core data structures for the hierarchical knowledge graph:
- Node: Individual knowledge unit
- Edge: Relationship between nodes
- Graph: Container for nodes and edges
"""

from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Dict, List, Optional, Any
from datetime import datetime
import uuid


class NodeLevel(Enum):
    """The four-layer knowledge hierarchy"""
    L0 = "L0"  # Source: Raw text chunks
    L1 = "L1"  # Factual: Extracted entities and facts
    L2 = "L2"  # Thematic: Aggregated themes and patterns
    L3 = "L3"  # Global: Story-wide arcs and conflicts


class NodeType(Enum):
    """Types of nodes at each level"""
    # L0 types
    SOURCE_CHUNK = "source_chunk"

    # L1 types
    ENTITY = "entity"
    FACT = "fact"
    RELATIONSHIP = "relationship"

    # L2 types
    THEME = "theme"
    PATTERN = "pattern"

    # L3 types
    ARC = "arc"
    CONFLICT = "conflict"


@dataclass
class Node:
    """A single node in the knowledge graph"""
    level: NodeLevel
    node_type: NodeType
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    node_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    tags: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """Convert node to dictionary for JSON serialization"""
        return {
            "node_id": self.node_id,
            "level": self.level.value,
            "node_type": self.node_type.value,
            "content": self.content,
            "metadata": self.metadata,
            "created_at": self.created_at,
            "tags": self.tags
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Node':
        """Create node from dictionary"""
        return cls(
            node_id=data["node_id"],
            level=NodeLevel(data["level"]),
            node_type=NodeType(data["node_type"]),
            content=data["content"],
            metadata=data.get("metadata", {}),
            created_at=data.get("created_at", datetime.utcnow().isoformat()),
            tags=data.get("tags", [])
        )


@dataclass
class Edge:
    """A relationship between two nodes"""
    source_id: str
    target_id: str
    relation_type: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    edge_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def to_dict(self) -> Dict:
        """Convert edge to dictionary"""
        return {
            "edge_id": self.edge_id,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "relation_type": self.relation_type,
            "metadata": self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Edge':
        """Create edge from dictionary"""
        return cls(
            edge_id=data["edge_id"],
            source_id=data["source_id"],
            target_id=data["target_id"],
            relation_type=data["relation_type"],
            metadata=data.get("metadata", {})
        )
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_kg_core.py::test_node_creation -v`
Expected: PASS

**Step 5: Commit**

```bash
git add ARCHON/knowledge_graph/kg_core.py tests/test_kg_core.py
git commit -m "feat: add knowledge graph core data structures"
```

---

## Task 2: Implement Graph Storage and Persistence

**Files:**
- Modify: `ARCHON/knowledge_graph/kg_core.py`
- Modify: `tests/test_kg_core.py`

**Step 1: Write test for graph add/save operations**

```python
def test_graph_add_node():
    """Test adding a node to the graph"""
    from ARCHON.knowledge_graph.kg_core import KnowledgeGraph

    graph = KnowledgeGraph()
    node = Node(
        level=NodeLevel.L1,
        node_type=NodeType.FACT,
        content="Test fact",
        metadata={"chapter": 1}
    )

    node_id = graph.add_node(node)
    assert node_id == node.node_id

    # Should be retrievable
    retrieved = graph.get_node(node_id)
    assert retrieved.content == "Test fact"


def test_graph_persistence(tmp_path):
    """Test saving and loading graph from disk"""
    from ARCHON.knowledge_graph.kg_core import KnowledgeGraph

    # Create graph and add nodes
    graph_path = tmp_path / "test_graph.json"
    graph = KnowledgeGraph(str(graph_path))

    node = Node(
        level=NodeLevel.L1,
        node_type=NodeType.ENTITY,
        content="Kael"
    )
    graph.add_node(node)
    graph.save()

    # Load in new instance
    graph2 = KnowledgeGraph(str(graph_path))
    graph2.load()

    # Should have the node
    assert len(graph2.nodes) == 1
    assert list(graph2.nodes.values())[0].content == "Kael"
```

**Step 2: Run tests to verify they fail**

Run: `pytest tests/test_kg_core.py::test_graph_add_node -v`
Expected: FAIL with "KnowledgeGraph not found"

**Step 3: Implement KnowledgeGraph class**

Add to `kg_core.py`:

```python
import json
from pathlib import Path


class KnowledgeGraph:
    """
    The main knowledge graph container.

    Stores nodes and edges with persistence to JSON.
    Provides add/query/delete operations.
    """

    def __init__(self, storage_path: str = None):
        """
        Initialize knowledge graph.

        Args:
            storage_path: Path to JSON file for persistence.
                         Defaults to ARCHON/knowledge_graph/graph.json
        """
        if storage_path is None:
            storage_path = Path(__file__).parent / "graph.json"
        else:
            storage_path = Path(storage_path)

        self.storage_path = storage_path
        self.nodes: Dict[str, Node] = {}
        self.edges: Dict[str, Edge] = {}

        # Load if file exists
        if self.storage_path.exists():
            self.load()

    def add_node(self, node: Node) -> str:
        """
        Add a node to the graph.

        Args:
            node: Node to add

        Returns:
            The node's ID
        """
        self.nodes[node.node_id] = node
        return node.node_id

    def get_node(self, node_id: str) -> Optional[Node]:
        """Get a node by ID"""
        return self.nodes.get(node_id)

    def add_edge(self, edge: Edge) -> str:
        """
        Add an edge to the graph.

        Args:
            edge: Edge to add

        Returns:
            The edge's ID
        """
        # Verify both nodes exist
        if edge.source_id not in self.nodes:
            raise ValueError(f"Source node {edge.source_id} not found")
        if edge.target_id not in self.nodes:
            raise ValueError(f"Target node {edge.target_id} not found")

        self.edges[edge.edge_id] = edge
        return edge.edge_id

    def get_edges_from(self, node_id: str) -> List[Edge]:
        """Get all edges originating from a node"""
        return [e for e in self.edges.values() if e.source_id == node_id]

    def get_edges_to(self, node_id: str) -> List[Edge]:
        """Get all edges pointing to a node"""
        return [e for e in self.edges.values() if e.target_id == node_id]

    def save(self):
        """Persist graph to disk"""
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)

        data = {
            "nodes": {nid: node.to_dict() for nid, node in self.nodes.items()},
            "edges": {eid: edge.to_dict() for eid, edge in self.edges.items()}
        }

        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self):
        """Load graph from disk"""
        if not self.storage_path.exists():
            return

        with open(self.storage_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Load nodes
        self.nodes = {
            nid: Node.from_dict(ndata)
            for nid, ndata in data.get("nodes", {}).items()
        }

        # Load edges
        self.edges = {
            eid: Edge.from_dict(edata)
            for eid, edata in data.get("edges", {}).items()
        }

    def clear(self):
        """Clear all nodes and edges"""
        self.nodes.clear()
        self.edges.clear()
```

**Step 4: Run tests to verify they pass**

Run: `pytest tests/test_kg_core.py -v`
Expected: All tests PASS

**Step 5: Commit**

```bash
git add ARCHON/knowledge_graph/kg_core.py tests/test_kg_core.py
git commit -m "feat: implement graph storage and persistence"
```

---

## Task 3: Implement Query Operations

**Files:**
- Modify: `ARCHON/knowledge_graph/kg_core.py`
- Modify: `tests/test_kg_core.py`

**Step 1: Write test for level-based queries**

```python
def test_query_by_level():
    """Test querying nodes by level"""
    from ARCHON.knowledge_graph.kg_core import KnowledgeGraph

    graph = KnowledgeGraph()

    # Add nodes at different levels
    l1_node = Node(level=NodeLevel.L1, node_type=NodeType.FACT, content="L1 fact")
    l2_node = Node(level=NodeLevel.L2, node_type=NodeType.THEME, content="L2 theme")

    graph.add_node(l1_node)
    graph.add_node(l2_node)

    # Query L1 only
    l1_nodes = graph.query(level=NodeLevel.L1)
    assert len(l1_nodes) == 1
    assert l1_nodes[0].content == "L1 fact"


def test_query_by_metadata():
    """Test querying nodes by metadata"""
    from ARCHON.knowledge_graph.kg_core import KnowledgeGraph

    graph = KnowledgeGraph()

    node1 = Node(
        level=NodeLevel.L1,
        node_type=NodeType.FACT,
        content="Chapter 4 fact",
        metadata={"chapter": 4}
    )
    node2 = Node(
        level=NodeLevel.L1,
        node_type=NodeType.FACT,
        content="Chapter 5 fact",
        metadata={"chapter": 5}
    )

    graph.add_node(node1)
    graph.add_node(node2)

    # Query chapter 4
    ch4_nodes = graph.query(metadata_filters={"chapter": 4})
    assert len(ch4_nodes) == 1
    assert ch4_nodes[0].content == "Chapter 4 fact"
```

**Step 2: Run tests to verify they fail**

Run: `pytest tests/test_kg_core.py::test_query_by_level -v`
Expected: FAIL because query() doesn't exist

**Step 3: Implement query method**

Add to KnowledgeGraph class:

```python
def query(
    self,
    level: Optional[NodeLevel] = None,
    node_type: Optional[NodeType] = None,
    tags: Optional[List[str]] = None,
    metadata_filters: Optional[Dict[str, Any]] = None,
    content_contains: Optional[str] = None
) -> List[Node]:
    """
    Query nodes with flexible filters.

    Args:
        level: Filter by node level (L0-L3)
        node_type: Filter by node type
        tags: Filter by tags (node must have ALL specified tags)
        metadata_filters: Filter by metadata key-value pairs
        content_contains: Filter by substring in content

    Returns:
        List of matching nodes
    """
    results = list(self.nodes.values())

    # Filter by level
    if level is not None:
        results = [n for n in results if n.level == level]

    # Filter by type
    if node_type is not None:
        results = [n for n in results if n.node_type == node_type]

    # Filter by tags
    if tags is not None:
        results = [n for n in results if all(tag in n.tags for tag in tags)]

    # Filter by metadata
    if metadata_filters is not None:
        for key, value in metadata_filters.items():
            results = [n for n in results if n.metadata.get(key) == value]

    # Filter by content
    if content_contains is not None:
        results = [n for n in results if content_contains.lower() in n.content.lower()]

    return results
```

**Step 4: Run tests to verify they pass**

Run: `pytest tests/test_kg_core.py -v`
Expected: All tests PASS

**Step 5: Commit**

```bash
git add ARCHON/knowledge_graph/kg_core.py tests/test_kg_core.py
git commit -m "feat: implement flexible query operations"
```

---

## Task 4: Add CLI Tool - kg_add

**Files:**
- Create: `ARCHON/tools/kg_add.py`
- Create: `tests/test_kg_tools.py`

**Step 1: Write test for kg_add CLI**

```python
#!/usr/bin/env python3
"""Tests for knowledge graph CLI tools"""

import subprocess
import json
import pytest
from pathlib import Path

def test_kg_add_creates_node(tmp_path):
    """Test that kg_add can create a node"""
    graph_path = tmp_path / "test_graph.json"

    result = subprocess.run(
        [
            "python", "ARCHON/tools/kg_add.py",
            "--level", "L1",
            "--type", "fact",
            "--content", "Kael entered KW2",
            "--metadata", json.dumps({"chapter": 4}),
            "--graph", str(graph_path)
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Added node" in result.stdout

    # Verify file was created
    assert graph_path.exists()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_kg_tools.py::test_kg_add_creates_node -v`
Expected: FAIL with "No such file: kg_add.py"

**Step 3: Create kg_add.py**

```python
#!/usr/bin/env python3
"""
kg_add - Add nodes to the Knowledge Graph

Usage:
    python kg_add.py --level L1 --type fact --content "Kael entered KW2"
    python kg_add.py --level L2 --type theme --content "Trauma processing" --tags trauma,memory
"""

import sys
import argparse
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from ARCHON.knowledge_graph.kg_core import (
    KnowledgeGraph, Node, NodeLevel, NodeType
)


def main():
    parser = argparse.ArgumentParser(
        description="Add nodes to the Knowledge Graph"
    )
    parser.add_argument(
        "--level",
        type=str,
        required=True,
        choices=["L0", "L1", "L2", "L3"],
        help="Node level"
    )
    parser.add_argument(
        "--type",
        type=str,
        required=True,
        help="Node type (e.g., fact, entity, theme, arc)"
    )
    parser.add_argument(
        "--content",
        type=str,
        required=True,
        help="Node content"
    )
    parser.add_argument(
        "--metadata",
        type=str,
        default="{}",
        help="Metadata as JSON string"
    )
    parser.add_argument(
        "--tags",
        type=str,
        default="",
        help="Comma-separated tags"
    )
    parser.add_argument(
        "--graph",
        type=Path,
        default=None,
        help="Path to graph file"
    )

    args = parser.parse_args()

    # Parse metadata
    try:
        metadata = json.loads(args.metadata)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in --metadata: {e}", file=sys.stderr)
        sys.exit(1)

    # Parse tags
    tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    # Parse level and type
    try:
        level = NodeLevel(args.level)
        node_type = NodeType(args.type)
    except ValueError as e:
        print(f"ERROR: Invalid level or type: {e}", file=sys.stderr)
        sys.exit(1)

    # Create node
    node = Node(
        level=level,
        node_type=node_type,
        content=args.content,
        metadata=metadata,
        tags=tags
    )

    # Add to graph
    graph = KnowledgeGraph(str(args.graph) if args.graph else None)
    node_id = graph.add_node(node)
    graph.save()

    print(f"✓ Added node {node_id} at {level.value}")
    print(f"  Type: {node_type.value}")
    print(f"  Content: {args.content}")
    if tags:
        print(f"  Tags: {', '.join(tags)}")


if __name__ == "__main__":
    main()
```

**Step 4: Make executable and run test**

Run: `chmod +x ARCHON/tools/kg_add.py && pytest tests/test_kg_tools.py::test_kg_add_creates_node -v`
Expected: PASS

**Step 5: Commit**

```bash
git add ARCHON/tools/kg_add.py tests/test_kg_tools.py
git commit -m "feat: add kg_add CLI tool for adding nodes"
```

---

## Task 5: Add CLI Tool - kg_query

**Files:**
- Create: `ARCHON/tools/kg_query.py`
- Modify: `tests/test_kg_tools.py`

**Step 1: Write test for kg_query CLI**

```python
def test_kg_query_retrieves_nodes(tmp_path):
    """Test that kg_query can retrieve nodes"""
    graph_path = tmp_path / "test_graph.json"

    # First add a node
    subprocess.run(
        [
            "python", "ARCHON/tools/kg_add.py",
            "--level", "L1",
            "--type", "fact",
            "--content", "Test fact",
            "--metadata", json.dumps({"chapter": 4}),
            "--graph", str(graph_path)
        ],
        capture_output=True
    )

    # Now query it
    result = subprocess.run(
        [
            "python", "ARCHON/tools/kg_query.py",
            "--level", "L1",
            "--graph", str(graph_path)
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Test fact" in result.stdout
    assert "Found 1 node" in result.stdout
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_kg_tools.py::test_kg_query_retrieves_nodes -v`
Expected: FAIL with "No such file: kg_query.py"

**Step 3: Create kg_query.py**

```python
#!/usr/bin/env python3
"""
kg_query - Query the Knowledge Graph

Usage:
    python kg_query.py --level L1
    python kg_query.py --level L1 --chapter 4
    python kg_query.py --tags trauma --level L2
    python kg_query.py --search "Kael"
"""

import sys
import argparse
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from ARCHON.knowledge_graph.kg_core import (
    KnowledgeGraph, NodeLevel, NodeType
)


def main():
    parser = argparse.ArgumentParser(
        description="Query the Knowledge Graph"
    )
    parser.add_argument(
        "--level",
        type=str,
        choices=["L0", "L1", "L2", "L3"],
        help="Filter by node level"
    )
    parser.add_argument(
        "--type",
        type=str,
        help="Filter by node type"
    )
    parser.add_argument(
        "--tags",
        type=str,
        help="Filter by tags (comma-separated)"
    )
    parser.add_argument(
        "--chapter",
        type=int,
        help="Filter by chapter number"
    )
    parser.add_argument(
        "--search",
        type=str,
        help="Search content"
    )
    parser.add_argument(
        "--graph",
        type=Path,
        default=None,
        help="Path to graph file"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON"
    )

    args = parser.parse_args()

    # Load graph
    graph = KnowledgeGraph(str(args.graph) if args.graph else None)

    # Build query filters
    filters = {}

    if args.level:
        filters["level"] = NodeLevel(args.level)

    if args.type:
        try:
            filters["node_type"] = NodeType(args.type)
        except ValueError:
            print(f"ERROR: Invalid node type: {args.type}", file=sys.stderr)
            sys.exit(1)

    if args.tags:
        filters["tags"] = [t.strip() for t in args.tags.split(",")]

    if args.chapter is not None:
        filters["metadata_filters"] = {"chapter": args.chapter}

    if args.search:
        filters["content_contains"] = args.search

    # Execute query
    results = graph.query(**filters)

    # Output
    if args.json:
        output = [node.to_dict() for node in results]
        print(json.dumps(output, indent=2))
    else:
        print_results(results)


def print_results(nodes):
    """Pretty-print query results"""
    if not nodes:
        print("No nodes found.")
        return

    print("=" * 60)
    print(f"Found {len(nodes)} node{'s' if len(nodes) != 1 else ''}")
    print("=" * 60)

    for i, node in enumerate(nodes, 1):
        print(f"\n[{i}] {node.level.value} / {node.node_type.value}")
        print(f"    ID: {node.node_id}")
        print(f"    Content: {node.content}")

        if node.metadata:
            print(f"    Metadata: {json.dumps(node.metadata)}")

        if node.tags:
            print(f"    Tags: {', '.join(node.tags)}")

    print("=" * 60)


if __name__ == "__main__":
    main()
```

**Step 4: Make executable and run test**

Run: `chmod +x ARCHON/tools/kg_query.py && pytest tests/test_kg_tools.py::test_kg_query_retrieves_nodes -v`
Expected: PASS

**Step 5: Commit**

```bash
git add ARCHON/tools/kg_query.py tests/test_kg_tools.py
git commit -m "feat: add kg_query CLI tool for querying graph"
```

---

## Task 6: Implement Scene Ingestion (Basic)

**Files:**
- Modify: `ARCHON/knowledge_graph/kg_core.py`
- Modify: `tests/test_kg_core.py`

**Step 1: Write test for scene ingestion**

```python
def test_ingest_scene_creates_nodes():
    """Test that ingesting a scene creates L0 and L1 nodes"""
    from ARCHON.knowledge_graph.kg_core import KnowledgeGraph

    graph = KnowledgeGraph()

    scene_text = """
    Kael entered the Mnemosyne-Archipel. The water was cold.
    Lex observed from a distance, calculating probabilities.
    """

    metadata = {
        "chapter": 4,
        "scene_id": "1.4",
        "location": "Mnemosyne-Archipel"
    }

    graph.ingest_scene(scene_text, metadata)

    # Should create L0 source node
    l0_nodes = graph.query(level=NodeLevel.L0)
    assert len(l0_nodes) >= 1

    # Should extract entities as L1
    l1_nodes = graph.query(level=NodeLevel.L1)
    assert len(l1_nodes) >= 2  # At least "Kael" and "Lex"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_kg_core.py::test_ingest_scene_creates_nodes -v`
Expected: FAIL because ingest_scene() doesn't exist

**Step 3: Implement basic scene ingestion**

Add to KnowledgeGraph class:

```python
import re

class KnowledgeGraph:
    # ... existing methods ...

    def ingest_scene(
        self,
        scene_text: str,
        metadata: Dict[str, Any]
    ):
        """
        Ingest a scene into the knowledge graph.

        Creates:
        - L0: Raw text chunks
        - L1: Extracted entities and basic facts

        Args:
            scene_text: The scene text
            metadata: Scene metadata (chapter, scene_id, location, etc.)
        """
        # L0: Store raw text as source chunk
        l0_node = Node(
            level=NodeLevel.L0,
            node_type=NodeType.SOURCE_CHUNK,
            content=scene_text[:500],  # First 500 chars
            metadata=metadata,
            tags=["source"]
        )
        l0_id = self.add_node(l0_node)

        # L1: Extract entities (simple regex-based for MVP)
        entities = self._extract_entities(scene_text)

        for entity in entities:
            # Check if entity already exists
            existing = self.query(
                level=NodeLevel.L1,
                node_type=NodeType.ENTITY,
                content_contains=entity
            )

            if not existing:
                # Create new entity node
                entity_node = Node(
                    level=NodeLevel.L1,
                    node_type=NodeType.ENTITY,
                    content=entity,
                    metadata=metadata,
                    tags=["entity", "character"]
                )
                entity_id = self.add_node(entity_node)

                # Link to source
                edge = Edge(
                    source_id=l0_id,
                    target_id=entity_id,
                    relation_type="contains",
                    metadata={"chapter": metadata.get("chapter")}
                )
                self.add_edge(edge)

        # L1: Extract basic facts (very simple for MVP)
        facts = self._extract_facts(scene_text, metadata)

        for fact_text in facts:
            fact_node = Node(
                level=NodeLevel.L1,
                node_type=NodeType.FACT,
                content=fact_text,
                metadata=metadata,
                tags=["fact"]
            )
            fact_id = self.add_node(fact_node)

            # Link to source
            edge = Edge(
                source_id=l0_id,
                target_id=fact_id,
                relation_type="extracted_from"
            )
            self.add_edge(edge)

    def _extract_entities(self, text: str) -> List[str]:
        """
        Extract entity names from text (MVP: simple capitalized words).

        This is a placeholder - in production use NER.
        """
        # Find capitalized words that might be names
        # List of known character names for MVP
        known_chars = [
            "Kael", "Lex", "Rhys", "Kiko", "Nyx", "Argus",
            "Mnemosyne", "AEGIS", "Logos"
        ]

        found = set()
        for char in known_chars:
            if char in text:
                found.add(char)

        return list(found)

    def _extract_facts(
        self,
        text: str,
        metadata: Dict[str, Any]
    ) -> List[str]:
        """
        Extract basic facts from text (MVP: sentence-level).

        This is a placeholder - in production use semantic analysis.
        """
        # Split into sentences
        sentences = re.split(r'[.!?]+', text)

        # Take first 3 non-empty sentences as "facts"
        facts = []
        for sent in sentences:
            sent = sent.strip()
            if len(sent) > 20:  # Meaningful length
                facts.append(sent)
                if len(facts) >= 3:
                    break

        return facts
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_kg_core.py::test_ingest_scene_creates_nodes -v`
Expected: PASS

**Step 5: Commit**

```bash
git add ARCHON/knowledge_graph/kg_core.py tests/test_kg_core.py
git commit -m "feat: implement basic scene ingestion"
```

---

## Task 7: Update Documentation

**Files:**
- Modify: `ARCHON/tools/README.md`
- Create: `ARCHON/knowledge_graph/README.md`

**Step 1: Create Knowledge Graph README**

```markdown
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

## Integration with NCP

The Knowledge Graph integrates with NCP validation:

```python
from ARCHON.tools.ncp_query import NCPManager
from ARCHON.knowledge_graph.kg_core import KnowledgeGraph

# Load NCP and graph
ncp = NCPManager("ARCHON/ncp/kohaerenz_protokoll.ncp.json")
graph = KnowledgeGraph()

# Get scene requirements from NCP
scene_req = ncp.get_scene_requirements("1.4")

# Check graph for prior context
prior_facts = graph.query(
    level=NodeLevel.L1,
    metadata_filters={"chapter": [1, 2, 3]},  # Prior chapters
    tags=scene_req.thematic_checkpoints[0]["theme"]
)

# Use prior_facts to inform scene generation...
```

## Performance Notes

- **Cold load**: ~50ms for 1000 nodes
- **Query**: <10ms for most filters
- **Save**: ~100ms for 1000 nodes

For larger graphs (10K+ nodes), consider:
- Indexing by level and chapter
- Separate files per act
- Neo4j migration for complex queries

---

*"Memory is not storage - it is reconstruction."*
```

**Step 2: Update ARCHON/tools/README.md**

Find the section on kg_query and kg_add and replace with:

```markdown
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
```

**Step 3: Run documentation verification**

```bash
# Check that all links work
grep -r "kg_" ARCHON/tools/README.md ARCHON/knowledge_graph/README.md
```

**Step 4: Commit**

```bash
git add ARCHON/knowledge_graph/README.md ARCHON/tools/README.md
git commit -m "docs: add comprehensive knowledge graph documentation"
```

---

## Task 8: Integration Testing and Final Verification

**Files:**
- Create: `tests/test_kg_integration.py`

**Step 1: Write end-to-end integration test**

```python
#!/usr/bin/env python3
"""Integration tests for complete KG workflow"""

import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from ARCHON.knowledge_graph.kg_core import (
    KnowledgeGraph, Node, NodeLevel, NodeType
)


def test_complete_workflow(tmp_path):
    """Test complete workflow: ingest -> query -> analyze"""
    graph_path = tmp_path / "workflow_test.json"
    graph = KnowledgeGraph(str(graph_path))

    # Step 1: Ingest a scene
    scene_text = """
    Kael stood at the edge of the Mnemosyne-Archipel. The water
    reflected memories he couldn't quite grasp. Lex calculated the
    probability of success at 23%. Kiko trembled at the cold.
    """

    metadata = {
        "chapter": 4,
        "scene_id": "1.4",
        "location": "Mnemosyne-Archipel",
        "active_alters": ["Kael", "Lex", "Kiko"]
    }

    graph.ingest_scene(scene_text, metadata)
    graph.save()

    # Step 2: Query what was added
    l0_nodes = graph.query(level=NodeLevel.L0)
    assert len(l0_nodes) >= 1

    l1_nodes = graph.query(level=NodeLevel.L1)
    assert len(l1_nodes) >= 3  # Entities + facts

    # Step 3: Query by chapter
    ch4_nodes = graph.query(metadata_filters={"chapter": 4})
    assert len(ch4_nodes) > 0

    # Step 4: Search for character
    kael_nodes = graph.query(content_contains="Kael")
    assert len(kael_nodes) > 0

    # Step 5: Reload from disk
    graph2 = KnowledgeGraph(str(graph_path))
    assert len(graph2.nodes) == len(graph.nodes)


def test_multi_scene_ingestion(tmp_path):
    """Test ingesting multiple scenes"""
    graph_path = tmp_path / "multi_scene.json"
    graph = KnowledgeGraph(str(graph_path))

    # Ingest chapter 4 scene
    graph.ingest_scene(
        "Kael entered the Archipel.",
        {"chapter": 4, "scene_id": "1.4"}
    )

    # Ingest chapter 5 scene
    graph.ingest_scene(
        "Lex analyzed the patterns.",
        {"chapter": 5, "scene_id": "2.1"}
    )

    graph.save()

    # Should have nodes from both chapters
    ch4 = graph.query(metadata_filters={"chapter": 4})
    ch5 = graph.query(metadata_filters={"chapter": 5})

    assert len(ch4) > 0
    assert len(ch5) > 0
```

**Step 2: Run integration tests**

Run: `pytest tests/test_kg_integration.py -v`
Expected: All tests PASS

**Step 3: Manual CLI workflow test**

```bash
# Create a test graph
python ARCHON/tools/kg_add.py --level L1 --type entity \
  --content "Kael" --metadata '{"chapter": 1}' \
  --tags character,protagonist

python ARCHON/tools/kg_add.py --level L1 --type fact \
  --content "Kael woke in Logos-Prime" --metadata '{"chapter": 1}'

python ARCHON/tools/kg_add.py --level L2 --type theme \
  --content "Awakening and disorientation" --tags awakening,confusion

# Query everything
python ARCHON/tools/kg_query.py

# Query by level
python ARCHON/tools/kg_query.py --level L2

# Query by chapter
python ARCHON/tools/kg_query.py --chapter 1

# JSON output
python ARCHON/tools/kg_query.py --level L1 --json | jq '.[] | .content'
```

Expected: All commands work without errors

**Step 4: Commit integration tests**

```bash
git add tests/test_kg_integration.py
git commit -m "test: add comprehensive integration tests"
```

---

## Verification Checklist

Before considering this task complete, verify:

- [ ] `pytest tests/test_kg_core.py -v` - all unit tests pass
- [ ] `pytest tests/test_kg_tools.py -v` - CLI tool tests pass
- [ ] `pytest tests/test_kg_integration.py -v` - integration tests pass
- [ ] `python ARCHON/tools/kg_add.py --help` - shows help
- [ ] `python ARCHON/tools/kg_query.py --help` - shows help
- [ ] Can add a node via CLI
- [ ] Can query nodes via CLI
- [ ] JSON output is valid
- [ ] Graph persists correctly to disk
- [ ] No external dependencies (pure Python stdlib)
- [ ] Documentation is complete
- [ ] Code follows existing style

---

## Success Criteria

**Foundation is complete when:**

1. All tests pass (unit + integration)
2. CLI tools are functional and well-documented
3. Python API is clean and intuitive
4. Graph persists reliably to JSON
5. Query system is flexible and fast
6. Basic scene ingestion works (L0, L1)
7. Integration with NCP tools is clear
8. Documentation explains architecture and usage

**Total estimated time:** 4-6 hours for experienced Python developer with zero codebase context

---

## Notes for Engineer

**Key Design Decisions:**

1. **JSON over Neo4j**: Simpler MVP, no DB setup, easier to inspect/debug
2. **UUID-based IDs**: Avoids collisions, enables distributed creation
3. **Flat storage**: All nodes/edges in single file for MVP, can shard later
4. **Simple entity extraction**: Regex-based for MVP, NER library in future
5. **Tags for thematic grouping**: Enables flexible thematic resonance queries

**What's NOT Included** (Phase 3+):

- L2/L3 automatic aggregation (future)
- Semantic search with embeddings (future)
- Graph visualization (future)
- Neo4j backend (future)
- Advanced NER (future)
- Thematic resonance scoring (future)

**Testing Philosophy:**

- Unit tests for data structures
- CLI tests via subprocess
- Integration tests for workflows
- Manual verification for UX

**Next Steps After This Plan:**

1. Implement L2/L3 aggregation logic
2. Add thematic resonance query system
3. Integrate with Narrative Director agent
4. Add semantic search with embeddings

**Reference Documentation:**

- `ARCHON/INTERFACE_DESIGN.md:218-264` - KG interface spec
- `ARCHON/INTERFACE_DESIGN.md:493-553` - Data flow diagrams
- `ARCHON/INTERFACE_DESIGN.md:625-671` - KG API specification
