# Quest: Quest-System-Refactoring

**Status:** 🟡 In Progress
**Priority:** 🔥 High
**Owner:** [AI Agent]
**Start Date:** 2025-11-06
**Target Date:** TBD

---

## 🎯 Objective
Consolidate overlapping tools, reduce code duplication, and create a unified, modular architecture for the AEGIS repository. This quest focuses on implementing the refactoring strategies outlined in `aegis.md`.

## 🔗 Related Quests / Merged Context
- [Quest-System-Maintenance](quests/Quest-System-Maintenance.md)

## CONTEXT
- [aegis.md](../aegis.md) - The canonical system architecture guide.
- [REFACTORING_PROPOSAL.md](../docs/REFACTORING_PROPOSAL.md) - Detailed analysis of duplication.

## 🛠️ Implementation Plan

### Phase 1: Unified Learning Command (High Priority)

- [ ] **Task 1: Create Modular Directory Structure**
  - [ ] Create `.claude/commands/_modules/` directory.
  - [ ] Implement `_modules/extract-content.md` (pure extraction logic).
  - [ ] Implement `_modules/action-planner.md` (Ship-Learn-Next logic).
  - [ ] Implement `_modules/knowledge-manager.md` (Zettelkasten logic).

- [ ] **Task 2: Implement Orchestrator Command**
  - [ ] Create `.claude/commands/learn.md` (Unified `/learn` command).
  - [ ] Implement intent detection and flag parsing.
  - [ ] Orchestrate calls to modules.

- [ ] **Task 3: Deprecate Legacy Commands**
  - [ ] Update `tapestry.md`, `ship-learn-next.md`, and `zettelkasten-tapestry.md` with redirection notices.
  - [ ] Verify redirects work.

### Phase 2: Skill Seeker Refactoring (Medium Priority)

- [ ] **Task 4: Create Abstract Base Scraper**
  - [ ] Create `skill_seeker/cli/base_scraper.py`.
  - [ ] Implement abstract methods (`validate_url`, `extract_content`) and concrete shared logic (`fetch_url`, `cache_data`).

- [ ] **Task 5: Refactor Concrete Scrapers**
  - [ ] Refactor `doc_scraper.py` to inherit from `BaseScraper`.
  - [ ] Refactor `github_scraper.py` to inherit from `BaseScraper`.
  - [ ] Refactor `pdf_scraper.py` to inherit from `BaseScraper`.
  - [ ] Verify `unified_scraper.py` works with new architecture.

### Phase 3: Enhancement Consolidation (Low Priority)

- [ ] **Task 6: Implement Strategy Pattern for Enhancer**
  - [ ] Create `skill_seeker/cli/skill_enhancer.py` with `SkillEnhancer` base class.
  - [ ] Implement `APIEnhancer` using Anthropic API.
  - [ ] Implement `LocalEnhancer` using Claude Code CLI.
  - [ ] Update CLI tools to use the factory pattern.

## ✅ Validation & Success Criteria
- [ ] `/learn` command successfully handles URLs, local files, and knowledge saving.
- [ ] `skill_seeker` tools maintain existing functionality with reduced code duplication (~30% reduction).
- [ ] All tests pass: `python skill_seeker/cli/run_tests.py`.
- [ ] No regressions in core workflows.

## 📝 Notes & Learnings
- 2025-11-06: Initial Quest creation based on `aegis.md` strategy.
