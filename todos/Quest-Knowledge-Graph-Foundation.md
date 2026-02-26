# Todos: Quest-Knowledge-Graph-Foundation

| Priority | Status | Task | Owner | Due Date | Notes |
| :---: | :---: | :--- | :---: | :---: | :--- |
| 🔴 High | ⚪ | Task 1 | Agent | [Next Review] | Core Data Structures |
| 🔴 High | ⚪ | Design `Node` class (id, type, attributes) | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Design `Edge` class (source, target, type, weight) | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Design `Graph` class (nodes, edges, adjacency list) | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Implement in `ARCHON/knowledge_graph/kg_core.py` | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Task 2 | Agent | [Next Review] | JSON Persistence |
| 🔴 High | ⚪ | Implement `save_to_json(filepath)` method | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Implement `load_from_json(filepath)` method | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Ensure atomic writes to prevent corruption | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Task 3 | Agent | [Next Review] | Query Operations |
| 🔴 High | ⚪ | Implement `get_node(id)` | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Implement `get_neighbors(id)` | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Implement `find_path(start, end)` | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Implement basic filtering (by type, attribute) | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Task 4 | Agent | [Next Review] | kg_add Tool |
| 🔴 High | ⚪ | Create `ARCHON/tools/kg_add.py` | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Support adding nodes/edges via CLI arguments | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Validate input against schema | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Task 5 | Agent | [Next Review] | kg_query Tool |
| 🔴 High | ⚪ | Create `ARCHON/tools/kg_query.py` | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Support basic queries via CLI | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Output results in readable format (JSON/Table) | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Task 6 | Agent | [Next Review] | Basic Scene Ingestion |
| 🔴 High | ⚪ | Parse manuscript markdown files | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Extract basic entities (Characters, Locations) | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Create nodes/edges automatically | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Task 7 | Agent | [Next Review] | Documentation |
| 🔴 High | ⚪ | Write API documentation for `kg_core.py` | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Write usage guide for CLI tools | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Update `ARCHON/README.md` | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Task 8 | Agent | [Next Review] | Integration Testing |
| 🔴 High | ⚪ | Create end-to-end test | Agent | [Next Review] | Add -> Save -> Load -> Query |
| 🔴 High | ⚪ | Verify data integrity | Agent | [Next Review] | - |
| 🔴 High | ⚪ | `tests/test_kg_core.py` passes with 100% coverage | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Can add a node via `kg_add`, save it, and retrieve it via `kg_query` | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Scene ingestion script successfully parses a sample chapter and populates the graph | Agent | [Next Review] | - |
| 🔴 High | ⚪ | Persistence layer handles large graphs (1000+ nodes) without errors | Agent | [Next Review] | - |
