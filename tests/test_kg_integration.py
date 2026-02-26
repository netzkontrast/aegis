#!/usr/bin/env python3
"""Integration tests for complete KG workflow"""

import pytest
from pathlib import Path
import sys

# Ensure the project root is in sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from aegis.knowledge_graph.kg_core import (
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
