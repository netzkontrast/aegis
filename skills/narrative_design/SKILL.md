# Narrative Design Skill

**Version:** 1.0.0
**Author:** Jules (AEGIS)
**Purpose:** Manage the Narrative Coherence Protocol (NCP) as the single source of truth for the novel's structure, characters, and world-building.

## Overview

This skill provides tools to:
1.  **Manage Codex Data:** Use `ncp.json` as the authoritative source for `PROJECT_CODEX.md` and other documentation.
2.  **Validate Scenes:** Ensure manuscript scenes adhere to NCP constraints (characters, themes, physics).
3.  **Handle Scene Splits/Branches:** Manage narrative variants and alternate timelines for scenes.
4.  **Sync & Learn:** Ingest manuscript metadata into the NCP and generate documentation from the NCP.

## Directory Structure

- `ncp/`: Contains the `kohaerenz_protokoll.ncp.json` data file.
- `scripts/`: Python tools for managing the NCP.
- `assets/`: Templates and generated artifacts.

## Tools & Commands

### 1. `ncp_manager.py` (Core Management)

The central tool for manipulating the NCP JSON.

```bash
# Add a new scene
python skills/narrative_design/scripts/ncp_manager.py add-scene --chapter 4 --scene 1.4 --title "The Garden"

# Create a narrative branch for a scene
python skills/narrative_design/scripts/ncp_manager.py branch-scene --scene 1.4 --branch "aggressive-negotiation"

# Update character state
python skills/narrative_design/scripts/ncp_manager.py update-character --name "Lex" --chapter 14 --state "Broken Logic"
```

### 2. `sync_codex.py` (Generate Documentation)

Generates `PROJECT_CODEX.md` from the JSON source.

```bash
python skills/narrative_design/scripts/sync_codex.py --output kohaerenz_protokoll/PROJECT_CODEX.md
```

### 3. `ingest_manuscript.py` (Learn from Files)

Scans the `kohaerenz_protokoll/manuscript/` directory and updates the `scenes` list in the JSON based on file metadata.

```bash
python skills/narrative_design/scripts/ingest_manuscript.py --scan
```

### 4. `ncp_validate.py` (Validate Content)

Validates a scene file against the current NCP constraints.

```bash
python skills/narrative_design/scripts/ncp_validate.py path/to/scene.md
```

## Workflow: Branching Scenes

When exploring alternative narrative paths:

1.  **Identify the scene:** `1.4` (The Garden)
2.  **Create a branch:** `python ncp_manager.py branch-scene --scene 1.4 --branch "aggressive"`
3.  **Result:** The JSON now tracks `1.4-aggressive` as a variant of `1.4`.
4.  **File Management:** The tool may suggest or create a file like `chapter_04_scene_04_aggressive.md`.
5.  **Comparison:** Use `ncp_manager.py diff-branches` to compare metadata/outcomes.

## Workflow: Updating Codex

1.  **Edit JSON:** Modify `ncp/kohaerenz_protokoll.ncp.json` directly or use `ncp_manager.py`.
2.  **Regenerate:** Run `sync_codex.py`.
3.  **Commit:** Commit both the JSON and the updated Markdown file.

---
**Note:** Do not edit `PROJECT_CODEX.md` manually for structural changes. Update the JSON instead.
