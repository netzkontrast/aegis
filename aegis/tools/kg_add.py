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

# Ensure the project root is in sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from aegis.knowledge_graph.kg_core import (
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
