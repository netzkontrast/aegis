# Coherence Console Architect Skill

> "The interface is the psyche. The agent is the therapist. The user is the author."

This document defines the rules and instructions for building and maintaining the Coherence Console within the `/chatbot` directory. Agents working on the frontend must strictly adhere to these guidelines.

## 1. Core Architecture: A2UI (Agent-to-User Interface)

The console is built using Next.js (App Router), React, and the Vercel AI SDK (`ai` package). We use the **A2UI pattern**.

**What this means:**
- The LLM does NOT just return markdown text.
- The LLM calls **tools** (defined in `app/api/chat/route.ts` or equivalent server actions).
- The Client (`useChat` hook) intercepts these tool calls and renders **React Components** in the chat stream instead of text.

**Example Flow:**
1.  **User:** "Show me the status of Core World 1."
2.  **Agent:** Decides to call the `renderCoreWorld` tool with arguments `{ worldId: "KW1" }`.
3.  **Client:** Sees the `renderCoreWorld` tool call in the stream. It renders the `<CoreWorldView data={args} />` component directly in the message feed.

## 2. Visual Aesthetic: "Ballpoint Pen on Rough Paper"

The console must look like a psychological case file or a frantic notebook.

### A. The "Rough Paper" Background
- **Do not use solid background colors.**
- Use a global CSS pattern or SVG filter to create a subtle paper texture.
- *Color Palette:*
  - Primary Background: Off-white/cream (e.g., `#F5F5DC` or similar)
  - Text: Dark ink blue or off-black (e.g., `#1A1A24`)

### B. Typography
- **Primary Font:** A monospaced or typewriter font (e.g., `Courier New`, `Fira Code`, or a custom Google Font like `VT323` or `Special Elite`).
- **Heading Font:** Can be a slightly more erratic, handwritten font.

### C. The "Shaky Line" Border
- UI components (cards, inputs) should avoid perfect right angles and 1px solid borders if possible.
- Use CSS tricks (like `border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;` combined with slight rotations) or SVG borders to simulate hand-drawn boxes.
- *Strict Rule:* Drop shadows should look like smudged ink, not clean CSS `box-shadow`.

### D. Psychological Color Coding
Use these specific colors for narrative states:
- 🟡 **Trauma / Fragmentation:** `#9C963B` (A sickly, oxidized yellow)
- 🟡 **Hope / Integration:** `#FFF2A6` (A bright, warm yellow)
- 🔴 **Dissociation / Danger:** Deep crimson red
- 🔵 **System Override (AEGIS):** Cold, sterile cyan/blue

## 3. Data Flow and Source of Truth

- **Read-Only Data:** The console reads from `chatbot/src/data/story/ncp_full.json`. This is synced from the main repository.
- **Do not mutate the NCP directly from the Next.js app.** If the agent needs to update the narrative, it must output instructions for a backend script or modify the repository files directly, *not* just the synced copy.

## 4. Required A2UI Components

When building the console, focus on implementing these tools/components:

1.  **`CoreWorldView`:** Displays the status of KW1, KW2, KW3, or KW4.
2.  **`EntityProfile`:** Displays character cards (Kael, Alters, Dr. Thorne).
3.  **`FissureAlert`:** A warning component when narrative coherence is dropping.
4.  **`NCPDiff`:** Shows the changes proposed to the JSON structure.

## 5. Development Workflow

1.  **Run Dev Server:** `cd chatbot && npm run dev`
2.  **Lint:** Ensure `npm run lint` passes before committing.
3.  **Tailwind:** All styling must use Tailwind utility classes where possible. If custom "shaky" CSS is needed, place it in `app/globals.css`.
4.  **Tool Registration:** Define tools in your server route using `tool()` from `@ai-sdk/core`.
