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
from datetime import datetime, timezone
import uuid
import json
from pathlib import Path
import re


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
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
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
            created_at=data.get("created_at", datetime.now(timezone.utc).isoformat()),
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
                         Defaults to aegis/knowledge_graph/graph.json
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
