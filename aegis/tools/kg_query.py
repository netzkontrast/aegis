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

# Ensure the project root is in sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from aegis.knowledge_graph.kg_core import (
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
