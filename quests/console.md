# Quest: AEGIS Console

**Status:** 🟢 Active
**Priority:** 🔥 High
**Owner:** Jules (Agent)
**Start Date:** 2025-05-22
**Target Date:** 2025-06-01

---

## 🎯 Objective
Transform the current `vercel-prototype` into a fully functional **AEGIS Console**.
This web application will serve as the primary interface for interacting with the AEGIS system, replacing the static landing page with a dynamic, conversational "Command Center" inspired by Claude Code.

## 🔗 Related Quests
- [[aegis.md]] - System Architecture
- [[gap-analysis.md]] - Workflow Optimization

## CONTEXT
The current prototype is a static reader. We need a "Mission Control" that allows us to:
1.  Run repository commands (e.g., `/learn`, `/ncp-query`) from a web interface.
2.  Interact with the repository state via an LLM (Gemini).
3.  Visualize complex data (Knowledge Graph, Narrative Arcs).

## 🛠️ Implementation Plan

### Phase 1: Spec Definition & Skills
- [ ] **Frontend Skill**: Create `skills/frontend/` to parse `.claude/commands/*.md` and derive UI specs.
- [ ] **Console Spec**: Define the root UI configuration for the webapp in `skills/console/`.
- [ ] **UI Schema**: Design the JSON schema for dynamic form generation.

### Phase 2: Foundation (Next.js)
- [ ] **Scaffold**: Update `vercel-prototype` to support the new Console layout.
- [ ] **Auth**: Implement Google Login (NextAuth.js or similar).
- [ ] **Terminal UI**: Build the conversational interface component.

### Phase 3: Intelligence (Gemini)
- [ ] **Gemini Integration**: Connect the console to Google's Gemini model.
- [ ] **Context Awareness**: Feed repo state (`REPO_STATE.md`, `quests/README.md`) to the model.

### Phase 4: Dynamic Execution
- [ ] **Command Runner**: Implement a backend (API route) to execute repo scripts safely.
- [ ] **Dynamic Forms**: Render UI inputs based on the Frontend Skill's analysis of commands.

## ✅ Validation & Success Criteria
- [ ] User can log in with Google.
- [ ] User can type "help" and see available commands derived from `.claude/`.
- [ ] User can run `/learn <url>` via a generated form.
- [ ] The interface feels like a "Cyberpunk Terminal" (keeping the AEGIS aesthetic).

## 📝 Notes & Learnings
- 2025-05-22: Quest initialized. Focusing on Phase 1 (Skills & Specs) first.
