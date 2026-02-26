# Quest: Quest-NCP-Writing-Assistant

**Status:** 🔴 Not Started
**Priority:** 🔥 High
**Owner:** [Agent/Human Name]
**Start Date:** 2025-11-05
**Target Date:** TBD

---

## 🎯 Objective
Develop the NCP Writing Assistant to provide real-time, context-aware writing prompts and voice consistency checks based on the Narrative Coherence Protocol.

## CONTEXT
- [CONSOLIDATED_IMPLEMENTATION_PLAN.md](CONSOLIDATED_IMPLEMENTATION_PLAN.md)
- `docs/plans/2025-11-05-ncp-writing-assistant.md`

## 🛠️ Implementation Plan

### Phase 1: Core Functionality (TDD)

- [ ] **Task 1: Test Structure**
  - [ ] Create `tests/test_ncp_assist.py`
  - [ ] Define test cases for each feature

- [ ] **Task 2: Chapter Prompt Generation**
  - [ ] Implement function to generate chapter-level prompts
  - [ ] Use input from `manuscript/chapter_XX_scene_YY.md` frontmatter
  - [ ] Integrate with predefined templates

- [ ] **Task 3: Character Voice Samples**
  - [ ] Load character profiles from `ARCHON/characters/`
  - [ ] Implement function to retrieve voice samples based on active alters
  - [ ] Ensure voice consistency (e.g., Lex vs. Nyx)

- [ ] **Task 4: Scene-Specific Prompts**
  - [ ] Implement function to generate scene-specific prompts
  - [ ] Consider location, time, and active characters
  - [ ] Generate sensory details based on Kernwelt rules

### Phase 2: CLI Tool

- [ ] **Task 5: JSON Output**
  - [ ] Standardize output format for prompts
  - [ ] Support JSON for integration with other tools

- [ ] **Task 6: CLI Integration**
  - [ ] Create `ARCHON/tools/ncp_assist.py`
  - [ ] Support command-line arguments (chapter, scene, character)
  - [ ] Output prompts to stdout or file

### Phase 3: Verification & Polish

- [ ] **Task 7: Manual Verification**
  - [ ] Generate prompts for Chapter 1, Scene 1
  - [ ] Verify relevance and tone
  - [ ] Refine templates based on output

- [ ] **Task 8: Documentation**
  - [ ] Write usage guide for `ncp_assist.py`
  - [ ] Document prompt templates and customization options

## ✅ Validation & Success Criteria
- [ ] `tests/test_ncp_assist.py` passes with 100% coverage
- [ ] CLI tool generates valid prompts for a given scene file
- [ ] Character voice samples match the profiles in `ARCHON/characters/`
- [ ] Output JSON adheres to the defined schema
