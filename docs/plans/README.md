# AEGIS Implementation Plans

> [← Back to Documentation Hub](../README.md)

This directory contains detailed, step-by-step implementation plans for AEGIS Framework components.

## Purpose

Each plan is designed for engineers with **zero codebase context** and follows:
- **TDD (Test-Driven Development)**: Write test → run to fail → implement → run to pass → commit
- **Bite-sized tasks**: Each step is 2-5 minutes
- **DRY & YAGNI**: Don't Repeat Yourself, You Aren't Gonna Need It
- **Frequent commits**: Commit after each passing test

## Available Plans

### Phase 1: Essential CLI Tools

- **[2025-11-05-ncp-writing-assistant.md](2025-11-05-ncp-writing-assistant.md)**
  - Implements `ncp_assist.py` - Writing Assistant tool
  - Generates writing prompts, character voice samples, and scene guidance
  - Completes AEGIS Phase 1 (MVP CLI tools)
  - **Estimated time:** 2-3 hours
  - **Status:** Ready to implement

### Phase 2: Knowledge Graph Foundation

- **[2025-11-05-knowledge-graph-foundation.md](2025-11-05-knowledge-graph-foundation.md)**
  - Implements hierarchical knowledge graph (L0-L3)
  - Python API (`kg_core.py`) and CLI tools (`kg_add.py`, `kg_query.py`)
  - JSON-based storage, flexible query system, basic scene ingestion
  - Starts AEGIS Phase 2 (Knowledge Graph)
  - **Estimated time:** 4-6 hours
  - **Status:** Ready to implement

## Plan Format

Each plan follows this structure:

```markdown
# Feature Name Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans

**Goal:** One-sentence description
**Architecture:** 2-3 sentences about approach
**Tech Stack:** Key technologies

---

## Task N: Component Name

**Files:**
- Create/Modify: exact/path/to/file.py

**Step 1: Write the failing test**
[Complete test code]

**Step 2: Run test to verify it fails**
Run: `pytest ...`
Expected: FAIL with "..."

**Step 3: Write minimal implementation**
[Complete implementation code]

**Step 4: Run test to verify it passes**
Run: `pytest ...`
Expected: PASS

**Step 5: Commit**
```bash
git add ...
git commit -m "..."
```
```

## How to Execute

### Option 1: Manual Implementation

1. Open a plan file
2. Follow steps sequentially
3. Run tests after each step
4. Commit frequently

### Option 2: Claude-Assisted (Recommended)

Use the `executing-plans` skill in a Claude session:

```
Please implement the plan at docs/plans/2025-11-05-ncp-writing-assistant.md
```

Claude will execute each step, run tests, and commit progress automatically.

### Option 3: Subagent-Driven

From the planning session, use the `subagent-driven-development` skill to dispatch fresh subagents for each task with code review between tasks.

## Plan Quality Standards

Each plan includes:

- ✅ Exact file paths for all operations
- ✅ Complete code snippets (not "add validation here")
- ✅ Exact commands with expected output
- ✅ TDD workflow (test-first, always)
- ✅ Bite-sized steps (2-5 minutes each)
- ✅ Verification checklist at the end
- ✅ Success criteria clearly defined
- ✅ Notes for engineers with design decisions
- ✅ References to relevant documentation

## Integration with AEGIS

These plans build on the existing foundation:

**Completed:**
- ✅ `ncp_query.py` - NCP query tool
- ✅ `ncp_validate.py` - Scene validator
- ✅ NCP schema and data
- ✅ Initial project structure

**Next (from these plans):**
- 🔜 `ncp_assist.py` - Writing assistant
- 🔜 Knowledge Graph foundation
- ⏳ Narrative Director agent (future)
- ⏳ Advanced features (future)

## Development Roadmap

```
Phase 1: Essential CLI Tools (1-2 weeks)
├─ ✅ ncp_query.py
├─ ✅ ncp_validate.py
└─ 🔜 ncp_assist.py ← Plan available

Phase 2: Knowledge Graph (2-3 weeks)
├─ 🔜 kg_core.py (data structures) ← Plan available
├─ 🔜 kg_add.py / kg_query.py (CLI) ← Plan available
├─ ⏳ L2/L3 aggregation logic
└─ ⏳ Thematic resonance queries

Phase 3: Narrative Director API (3-4 weeks)
├─ ⏳ Reason-Act-Critique loop
├─ ⏳ LLM integration
├─ ⏳ Self-critique validation
└─ ⏳ Scene generation

Phase 4: Advanced Features (4-6 weeks)
├─ ⏳ Coherence dashboard
├─ ⏳ Visualization tools
└─ ⏳ Research analytics
```

## Contributing

When adding new plans:

1. Use the date-based filename: `YYYY-MM-DD-feature-name.md`
2. Follow the standard plan format
3. Include verification checklist
4. Provide time estimates
5. Reference relevant design docs
6. Update this README

## Questions?

- See `aegis/INTERFACE_DESIGN.md` for overall architecture
- See `aegis/tools/README.md` for existing tool documentation
- See `aegis/agents/README.md` for Narrative Director spec

---

*Plans that serve the implementation, not the reverse.*
