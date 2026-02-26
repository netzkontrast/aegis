# Quest: Documentation Consolidation & Navigation

**Status:** 🟡 In Progress
**Priority:** 🎯 High
**Owner:** [Agent/Human Name]
**Start Date:** 2025-11-06
**Target Date:** TBD

---

## 🎯 Objective
Create a centralized, cohesive documentation hub in `docs/` that seamlessly integrates the **AEGIS Framework** (System Architecture, Agent Guidelines) with the **Kohärenz Protokoll** (Narrative Design, Manuscript). Eliminate fragmentation and ensure clear entry points for both developers and writers.

## 🔗 Context & References
- **System Architecture**: `aegis/README.md` (The "Grand Strategy")
- **Agent OS**: `aegis/SKILL.md` (Mandatory Instructions)
- **Narrative Navigation**: `docs/kohaerenz_protokoll_navigation.md` (The Novel's Map)
- **Quest System**: `quests/README.md` (Active Work)
- **Writing Excellence**: `quests/writing.md`

## 🛠️ Implementation Plan

### Phase 1: The Central Hub (Structure & Navigation)

- [ ] **Task 1: Create `docs/README.md`**
  - [ ] Establish a clear Table of Contents linking to all major project areas:
    - **System**: AEGIS Framework, Agent Rules, Tools (`skill_seeker`, `zettelkasten`).
    - **Narrative**: Kohärenz Protokoll, NCP, Worldbuilding.
    - **Project Management**: Quests, Plans, Status.
  - [ ] Define "How to Use This Documentation" for different personas (Agent vs. Human).

- [ ] **Task 2: Integrate Narrative Documentation**
  - [ ] Review `docs/kohaerenz_protokoll_navigation.md` and ensure it serves as the primary entry point for narrative work.
  - [ ] Verify links to "Cluster" documents (`docs/cluster_*.md`) and consolidate if necessary.
  - [ ] Ensure clear separation but easy navigation between "System" and "Story" docs.

- [ ] **Task 3: Link System Documentation**
  - [ ] Explicitly link `aegis/README.md` and `aegis/SKILL.md` from the new hub.
  - [ ] Ensure `REPO_STATE.md` is referenced as the architectural map.

### Phase 2: Content Refinement & Standardization

- [ ] **Task 4: Update Key Guides**
  - [ ] Review `docs/writing/` for outdated style guides.
  - [ ] Ensure `docs/plans/` reflects current roadmap status.
  - [ ] Check `docs/knowledge-extraction/` for relevance.

- [ ] **Task 5: Standardize Formatting**
  - [ ] Apply consistent headers and navigation links across all `docs/` files.
  - [ ] Add "Back to Hub" links in sub-documents.

### Phase 3: Validation

- [ ] **Task 6: Link Verification**
  - [ ] Verify all internal links in `docs/README.md` and sub-pages.
  - [ ] Ensure external links (if any) are valid.

## ✅ Validation & Success Criteria
- [ ] `docs/README.md` exists and serves as a comprehensive index.
- [ ] A new agent can find "How to Contribute" within 1 click.
- [ ] A writer can find "Narrative Architecture" within 1 click.
- [ ] No orphaned files in `docs/`.
- [ ] Broken links to `CONSOLIDATED_IMPLEMENTATION_PLAN.md` are removed.
