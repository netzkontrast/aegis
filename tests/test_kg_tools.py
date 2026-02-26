#!/usr/bin/env python3
"""Tests for knowledge graph CLI tools"""

import subprocess
import json
import pytest
from pathlib import Path
import sys

# Ensure the project root is in sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_kg_add_creates_node(tmp_path):
    """Test that kg_add can create a node"""
    graph_path = tmp_path / "test_graph.json"

    result = subprocess.run(
        [
            "python", "aegis/tools/kg_add.py",
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

def test_kg_query_retrieves_nodes(tmp_path):
    """Test that kg_query can retrieve nodes"""
    graph_path = tmp_path / "test_graph.json"

    # First add a node
    subprocess.run(
        [
            "python", "aegis/tools/kg_add.py",
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
            "python", "aegis/tools/kg_query.py",
            "--level", "L1",
            "--graph", str(graph_path)
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Test fact" in result.stdout
    assert "Found 1 node" in result.stdout
