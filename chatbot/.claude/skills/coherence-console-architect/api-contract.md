# API Contract: Coherence Console (Abstract A2UI)

The following table details the vocabulary of the abstract API and its mapping to Client components.

| API Tool / A2UI Type | Purpose and Narrative Function | Parameter (JSON Schema Expectation) | Frontend Mapping (shadcn/ui + Custom CSS) |
| :--- | :--- | :--- | :--- |
| **`renderCoreWorld`** | Visualization of the current epistemological landscape (Core World 1-4) or the Digital Overworld. | `world_id` (String), `stability_index` (Integer 0-100), `active_logic` (String). | Complex Card-Layouts with dynamic CSS-Grids. KW1 uses strict symmetry, KW2 uses fluid, overlapping containers. |
| **`displayEntityProfile`** | Representation of clinical and narrative parameters of one of the 13 entities of System Kael. | `entity_id` (String), `tsdp_type` (String), `current_burden` (String), `dominance` (Boolean). | Minimalist Profile-View with Silhouette representation. Accent colors (e.g., Crystal Blue for Selene) injected via CSS variables. |
| **`triggerFissureAlert`** | Warning system for narrative or psychological inconsistencies where $K_0$ (Chaos) breaks into $K_1$ (Order). | `severity_color` (Enum: trauma-yellow, signal-yellow), `intruding_element` (String), `analysis_text` (String). | Asynchronously streamed Alert-Component. Uses SVG filters to generate "cracks" in the UI and infects surrounding colors with the chosen yellow tone. |
| **`invokeMoonshineLink`** | Activation of a non-algorithmic, creative impulse for the author to overcome writer's block. | `sensory_metadata` (String), `intuitive_gnosis` (String). | Highly desaturated component with much "Negative Space" (Courage for whitespace), utilizing Insight-Yellow as a soft glow effect. |
