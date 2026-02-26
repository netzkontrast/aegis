#!/usr/bin/env python3
"""Tests for knowledge graph core data structures"""

import pytest
from pathlib import Path
import sys

# Ensure the project root is in sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from aegis.knowledge_graph.kg_core import Node, NodeLevel, NodeType

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

def test_graph_add_node(tmp_path):
    """Test adding a node to the graph"""
    from aegis.knowledge_graph.kg_core import KnowledgeGraph

    graph_path = tmp_path / "test_graph.json"
    graph = KnowledgeGraph(str(graph_path))
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
    from aegis.knowledge_graph.kg_core import KnowledgeGraph

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

def test_query_by_level(tmp_path):
    """Test querying nodes by level"""
    from aegis.knowledge_graph.kg_core import KnowledgeGraph

    graph_path = tmp_path / "test_graph.json"
    graph = KnowledgeGraph(str(graph_path))

    # Add nodes at different levels
    l1_node = Node(level=NodeLevel.L1, node_type=NodeType.FACT, content="L1 fact")
    l2_node = Node(level=NodeLevel.L2, node_type=NodeType.THEME, content="L2 theme")

    graph.add_node(l1_node)
    graph.add_node(l2_node)

    # Query L1 only
    l1_nodes = graph.query(level=NodeLevel.L1)
    assert len(l1_nodes) == 1
    assert l1_nodes[0].content == "L1 fact"


def test_query_by_metadata(tmp_path):
    """Test querying nodes by metadata"""
    from aegis.knowledge_graph.kg_core import KnowledgeGraph

    graph_path = tmp_path / "test_graph.json"
    graph = KnowledgeGraph(str(graph_path))

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

def test_ingest_scene_creates_nodes(tmp_path):
    """Test that ingesting a scene creates L0 and L1 nodes"""
    from aegis.knowledge_graph.kg_core import KnowledgeGraph

    graph_path = tmp_path / "test_graph.json"
    graph = KnowledgeGraph(str(graph_path))

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
