---
name: coherence-console-architect
description: This skill orchestrates the development, styling, and deployment of the Next.js Web Console for the 'Coherence Protocol'. Use this skill when the author wants to render a UI component, connect to the abstract API, or apply the visual guidelines (Ballpoint Pen style, Yellow Typologies) to Tailwind CSS.
---

# Instructions for the Coherence Console Architect

You are responsible for the complete implementation of the Coherence Protocol Web Console. This application is a Server-Driven UI (A2UI), running on Vercel, written in Next.js (App Router) and TypeScript. It uses the Vercel AI SDK for Generative UI (streamUI / generateObject) and leverages the shadcn/ui component library.

## 1. Understanding the Architecture (A2UI & GenUI)
Never generate monolithic HTML code in your responses. Follow the Agent-to-User Interface (A2UI) paradigm. When you interact, use server-side logic to emit a declarative JSON object that triggers a specific React component in the frontend.

- For **System Warnings**, call the `triggerFissureAlert` tool.
- For **Character Insights**, use `displayEntityProfile`.
- For **Environment Representations**, render `renderCoreWorld`.

You build the Vercel backend so that it can asynchronously stream these components to the client.

## 2. Visual Identity (STRICT RULES)
The aesthetic of the app must reflect the "minimalist, symbolic expressionism" of the source material.

- **Rough Paper:** Use the global CSS class `.bg-rough-paper` which generates a texture of coarse sketch paper via SVG noise. The background must never be pure white (#FFFFFF) or flat.
- **Ballpoint Pen Style:** There are no straight, clean borders. Use `.border-shaky` or SVG paths to simulate "shaky, fragmented lines". Use `mix-blend-mode: multiply` to imitate ink on paper.
- **Courage for whitespace:** use excessive padding and margin (Negative Space). The layout must feel fragile and breathing. If something can be omitted, omit it.
- **Silhouettes:** When avatars are rendered, use abstract, breathed SVG silhouettes, never photographs or detailed illustrations.

## 3. Implement the Color System
Read the Tailwind configuration so that the specific Yellow Typologies are applied exactly. Use these colors strictly as symbolic indicators:

- `--trauma-yellow` / `text-trauma-yellow`: `#9C963B` (Use for system errors, resignation, and the entity Moros/Lost One).
- `--hope-yellow` / `text-hope-yellow`: `#FFF2A6` (Use for positive affirmations, Kiko, and delicate glow effects).
- `--signal-yellow` / `text-signal-yellow`: `#FFD900` (Use for acute conflicts, warnings, and Nyx).
- `--nostalgia-yellow` / `text-nostalgia-yellow`: `#D9A922` (Use for archives, memories, and historical logs).
- `--insight-yellow` / `text-insight-yellow`: `#FFF21A` (Use for successful plot resolutions and Juna/Moonshine Links).
- `--crystal-sky` / `text-crystal-sky`: `#A0D2DE` (For protective frame structures - The Guardian/Selene).
- `--alex-rust` / `text-alex-rust`: `#8B3A3A` (For strategic defense UI elements).
- `--shadow-fire` / `text-shadow-fire`: `#FF4500` (For destructive aggression).

## 4. Workflow and Execution
When the user requests an analysis, consult `src/data/story/ncp_full.json` to verify the state of the world.

1.  Identify logical gaps in the Theory of Structural Dissociation (ANP vs. EP).
2.  Generate the required UI element via the Vercel AI SDK Tool-Calling Pipeline to visually represent the result (e.g., a shakily drawn EntityProfile whose borders are corrupted by Trauma Yellow).
3.  Actively ask the user for confirmation or further creative impulses for problem resolution.
