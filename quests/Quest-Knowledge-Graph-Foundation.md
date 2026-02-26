# Quest: Quest-Knowledge-Graph-Foundation

**Status:** 🔴 Not Started
**Priority:** 🚨 Critical
**Owner:** [Agent/Human Name]
**Start Date:** 2025-11-05
**Target Date:** TBD

---

## 🎯 Objective
Establish the core data structures, persistence layer, and CLI tools for the AEGIS Narrative Knowledge Graph. This is the foundational system that enables context-aware writing, scene ingestion, and advanced querying.

## CONTEXT
- [CONSOLIDATED_IMPLEMENTATION_PLAN.md](CONSOLIDATED_IMPLEMENTATION_PLAN.md)
- `docs/plans/2025-11-05-knowledge-graph-foundation.md`

## 🛠️ Implementation Plan

### Phase 1: Core Implementation (TDD)

- [ ] **Task 1: Core Data Structures**
  - [ ] Design `Node` class (id, type, attributes)
  - [ ] Design `Edge` class (source, target, type, weight)
  - [ ] Design `Graph` class (nodes, edges, adjacency list)
  - [ ] Implement in `ARCHON/knowledge_graph/kg_core.py`

- [ ] **Task 2: JSON Persistence**
  - [ ] Implement `save_to_json(filepath)` method
  - [ ] Implement `load_from_json(filepath)` method
  - [ ] Ensure atomic writes to prevent corruption

- [ ] **Task 3: Query Operations**
  - [ ] Implement `get_node(id)`
  - [ ] Implement `get_neighbors(id)`
  - [ ] Implement `find_path(start, end)`
  - [ ] Implement basic filtering (by type, attribute)

### Phase 2: CLI Tools

- [ ] **Task 4: kg_add Tool**
  - [ ] Create `ARCHON/tools/kg_add.py`
  - [ ] Support adding nodes/edges via CLI arguments
  - [ ] Validate input against schema

- [ ] **Task 5: kg_query Tool**
  - [ ] Create `ARCHON/tools/kg_query.py`
  - [ ] Support basic queries via CLI
  - [ ] Output results in readable format (JSON/Table)

### Phase 3: Ingestion & Integration

- [ ] **Task 6: Basic Scene Ingestion**
  - [ ] Parse manuscript markdown files
  - [ ] Extract basic entities (Characters, Locations)
  - [ ] Create nodes/edges automatically

- [ ] **Task 7: Documentation**
  - [ ] Write API documentation for `kg_core.py`
  - [ ] Write usage guide for CLI tools
  - [ ] Update `ARCHON/README.md`

- [ ] **Task 8: Integration Testing**
  - [ ] Create end-to-end test: Add -> Save -> Load -> Query
  - [ ] Verify data integrity

## ✅ Validation & Success Criteria
- [ ] `tests/test_kg_core.py` passes with 100% coverage
- [ ] Can add a node via `kg_add`, save it, and retrieve it via `kg_query`
- [ ] Scene ingestion script successfully parses a sample chapter and populates the graph
- [ ] Persistence layer handles large graphs (1000+ nodes) without errors
