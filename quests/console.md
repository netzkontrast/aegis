# Quest: Coherence Console (AEGIS Interface)

**Status:** 🟢 Active
**Priority:** 🔥 High
**Owner:** Jules (Agent)
**Start Date:** 2025-05-22
**Target Date:** 2025-06-01

---

## 🎯 Objective
Establish the **Coherence Console** as the primary, agent-driven interface for the Coherence Protocol novel. This web application (located in `/chatbot`) synthesizes narrative theory, clinical psychology, and generative UI into a "Mission Control" for the author. It replaces the static prototype with a dynamic, conversational interface powered by the Vercel AI SDK and Next.js.

## 🔗 Related Quests
- [[aegis.md]] - System Architecture
- [[gap-analysis.md]] - Workflow Optimization
- [[chatbot-integration.md]] - Merged Scope

## CONTEXT
The console is not just a display but an isomorphic representation of the protagonist's psyche (TSDP - Structural Dissociation).
It must:
1.  **Visualize Narrative State:** Render `CoreWorld` states and `EntityProfile` cards dynamically based on the story context.
2.  **Enable Agent Control (A2UI):** Allow the AI to "call tools" that stream React Server Components (GenUI) directly to the chat stream.
3.  **Enforce Aesthetic:** Use a strict "Ballpoint Pen on Rough Paper" style with specific CMYK-derived colors to represent psychological states.

## 🛠️ Implementation Plan

### Phase 1: Architecture & Data (Current Focus)
- [x] **Consolidate Scope**: Merge `/chatbot` development with Console requirements.
- [ ] **Data Pipeline**: Create `chatbot/src/data/story/` and a sync script (`sync_ncp_to_app.py`) to mirror `kohaerenz_protokoll.ncp.json` and chapter snippets.
- [ ] **Skill Definition**: Author `skills/coherence-console-architect/SKILL.md` to instruct agents on the A2UI pattern and visual rules.

### Phase 2: Visual System (The "Ballpoint Pen")
- [ ] **Tailwind Config**: Define custom colors (Trauma Yellow `#9C963B`, Hope Yellow `#FFF2A6`, etc.).
- [ ] **Global CSS**: Implement "Rough Paper" SVG noise texture and "Shaky Line" grammar.
- [ ] **Typography**: Ensure fonts align with the "handwritten/typewriter" aesthetic.

### Phase 3: Generative UI Components (A2UI)
- [ ] **Core Components**: Build `CoreWorldView`, `EntityProfile`, `FissureAlert`, `DialogueSurface`.
- [ ] **AI Integration**: Register these components as "Tools" in the Vercel AI SDK (`useChat` / `streamUI`).
- [ ] **Dynamic Forms**: Allow the agent to request user input via structured forms.

### Phase 4: Intelligence & Context
- [ ] **Context Awareness**: Feed `REPO_STATE.md` and the synced NCP data to the model system prompt.
- [ ] **Command Execution**: Enable the console to trigger safe repository scripts (e.g., `/learn`, `/validate`).

## ✅ Validation & Success Criteria
- [ ] **Data Sync**: `chatbot/src/data/story/ncp_full.json` exists and is valid.
- [ ] **Visuals**: The app background looks like rough paper; borders are shaky/hand-drawn.
- [ ] **GenUI**: Typing "Analyze Act 1" triggers a streamed `CoreWorldView` component, not just text.
- [ ] **Aesthetic**: The specific yellow hues (Trauma vs. Hope) are used correctly in the UI.

## 📝 Notes & Learnings
- **Architecture**: We are using the "Agent-to-User Interface" (A2UI) pattern. The Agent emits JSON intent; the Client renders the Component.
- **Source of Truth**: The `kohaerenz_protokoll.ncp.json` is the single source of truth for narrative logic.
