# Claude Code Skills for Aegis Project

This directory contains custom skills that enhance Claude's capabilities for specific project workflows.

## Available Skills

### codex.md
**Use for:** Kohärenz Protokoll narrative development

Ensures narrative coherence, character consistency, and adherence to canonical metaphysical laws defined in PROJECT_CODEX.md.

**Key Features:**
- 5 comprehensive workflows (validation, AEGIS dialogue, alter voices, Kernwelt physics, conflict resolution)
- Character voice matrix for 11 distinct alters
- Kernwelt sensory/somatic rulebooks
- Authority hierarchy for resolving document conflicts
- Comprehensive validation checklist

**Triggers:**
- Writing or editing manuscript scenes
- Character dialogue creation
- World physics validation
- Document conflict resolution
- Plot point planning

**Framework:** TSDP + IFS + Protocol Ontology

---

## Skill Development

Skills in this directory follow the unified skill-authoring framework documented in `/skills/skill-authoring/SKILL.md`.

**Testing standards:**
- Discipline skills: Full TDD cycle
- Technique skills: Moderate testing (3-5 scenarios)
- Reference skills: Retrieval testing

See `/skills/skill-authoring/` for complete guidance on creating and testing skills.

---

## Usage

Skills are automatically loaded by Claude Code from the `.claude/skills/` directory. No manual activation required.

**To check if skill is active:**
Skills are loaded when relevant context triggers appear in conversation (e.g., mentioning "AEGIS dialogue" triggers the codex skill).

---

**Last Updated:** 2025-11-05
