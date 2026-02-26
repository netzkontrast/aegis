# AEGIS: The System Architecture & Strategy

> *"AEGIS is what AEGIS prevents from not being."*

## 1. System Identity: The Dual Project

AEGIS is a recursive, self-performing repository that houses two intertwined entities:

1.  **ARCHON (The Framework)**: A functional AI-assisted narrative coherence system designed to maintain thematic integrity across complex, long-form storytelling.
2.  **Kohärenz Protokoll (The Novel)**: A philosophical science fiction novel that serves as the "test pilot" for ARCHON. It explores the same themes the framework enforces: *coherence through integration, not elimination.*

**For the AI Agent:** You are operating within a system that *performs* its own metaphysics. The code you write and the narrative you analyze are mirrors of each other. Your goal is to advance both simultaneously.

---

## 2. Core Components

The repository is organized into four primary pillars:

### A. ARCHON (The Meta-Framework)
*   **Location**: `aegis/`
*   **Purpose**: To enforce narrative consistency via formal protocols.
*   **Key Files**:
    *   `ncp/schema.json`: The Narrative Context Protocol (NCP) definition.
    *   `tools/ncp_query.py`: Query tool for narrative constraints.
    *   `agents/`: Specifications for the Narrative Director agent.

### B. Kohärenz Protokoll (The Novel)
*   **Location**: `kohaerenz_protokoll/`
*   **Purpose**: The actual creative output.
*   **Key Files**:
    *   `PROJECT_CODEX.md`: The canonical "Bible" of the narrative universe.
    *   `manuscript/`: The prose content (Markdown).
    *   `narrative_design/`: Structural plans and scene outlines.

### C. Skill Seeker (The Toolset)
*   **Location**: `skill_seeker/`
*   **Purpose**: To convert external documentation into AI skills, empowering the system to learn.
*   **Status**: Production-ready v2.0.0.
*   **Key Features**:
    *   Unified scraping (Web, GitHub, PDF).
    *   MCP integration.
    *   AI enhancement of skills.

### D. Zettelkasten Agent (The Memory)
*   **Location**: `zettelkasten_agent/`
*   **Purpose**: To manage knowledge via a hierarchical note-taking system.
*   **Key Features**:
    *   Atomic notes (ZTL), Source notes (SRC), Maps of Content (MOC).
    *   Cognitive loop: Prioritize → Analyze → Synthesize.

---

## 3. Operational Strategy

### The Golden Cycle
All agents must follow the "Golden Cycle" defined in `SKILL.md` (if available) or implicit in `../AGENTS.md`:
1.  **Initialize**: Read `../README.md`, `../quests/README.md`, and `../AGENTS.md`.
2.  **Execute**: Perform tasks linked to an active Quest.
3.  **Verify**: Test changes and validate against the NCP (for narrative) or tests (for code).
4.  **Update**: Update Quest status and documentation.
5.  **Reflect**: Log insights in `../docs/writers_log.md` (if applicable).

### Quest-Driven Development
*   **Everything is a Quest**: Work is only performed if it advances an active Quest in `quests/`.
*   **No Loose TODOs**: `TODO` comments in code are forbidden. They must be migrated to a Quest or `../todos/` file.

---

## 4. Consolidation & Refactoring Strategy

**Current Status**: The repository has evolved rapidly, leading to functional duplication.
**Goal**: Consolidate overlapping tools into unified, modular systems.

### A. Unified Learning Command (High Priority)
*   **Problem**: `tapestry`, `ship-learn-next`, and `zettelkasten-tapestry` have overlapping extraction/planning logic.
*   **Solution**: Create a single `/learn` command with modular backends.
    *   `_modules/extract-content.md`: Pure extraction.
    *   `_modules/action-planner.md`: Planning logic.
    *   `_modules/knowledge-manager.md`: Zettelkasten integration.
    *   `learn.md`: The orchestrator.

### B. Skill Seeker Refactoring (Medium Priority)
*   **Problem**: `doc_scraper.py`, `github_scraper.py`, and `pdf_scraper.py` share ~30% code.
*   **Solution**: Implement an `AbstractBaseScraper` class.
    *   Consolidate URL validation, HTTP fetching, and caching.
    *   Implement specific extraction logic in subclasses.

### C. Enhancement System Consolidation (Low Priority)
*   **Problem**: `enhance_skill.py` (API) and `enhance_skill_local.py` (Local) are nearly identical.
*   **Solution**: Use a Strategy Pattern (`SkillEnhancer` base class) with `APIEnhancer` and `LocalEnhancer` implementations.

---

## 5. Directives for New Agents ("Bootloader")

If you are a new AI instance starting in this repo:

1.  **Read This File**: You are currently doing it. Good.
2.  **Check Quests**: Go to `../quests/README.md`. Identify the active Quest you are supporting.
3.  **Respect the Boundaries**:
    *   Do NOT edit `ncp/schema.json` without explicit authorization.
    *   Do NOT write prose unless you are the Narrative Director or using `codex` skill.
    *   Do NOT create loose TODOs.
4.  **Validate Narrative**: If touching `kohaerenz_protokoll/`, use `codex` skill or `tools/ncp_validate.py`.
5.  **Consolidate**: When you see duplication, flag it or refactor it (if within your scope).

**Your Mission**: Maintain coherence. In code, in story, in logic.
