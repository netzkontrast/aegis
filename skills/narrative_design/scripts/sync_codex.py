import json
import argparse
from pathlib import Path

DEFAULT_NCP_PATH = Path(__file__).parent.parent / 'ncp' / 'kohaerenz_protokoll.ncp.json'
DEFAULT_TEMPLATE_PATH = Path(__file__).parent.parent / 'assets' / 'PROJECT_CODEX.template.md'
DEFAULT_OUTPUT_PATH = Path('kohaerenz_protokoll/PROJECT_CODEX.md')

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_physics_engine(data):
    physics = data.get('world_building', {}).get('physics_engine', {})
    if not physics:
        return "No physics engine data found."

    text = "### 1.2 The Protocol Ontology: The Mechanics of Persistence\n\n"

    # Dual Kernel Theory
    dkt = physics.get('dual_kernel_theory', {})
    if dkt:
        text += f"The universe's fundamental mechanics are governed by the **Dual Kernel Theory**.\n\n"
        text += f"{dkt.get('description', '')}\n\n"
        for k in dkt.get('kernels', []):
            text += f"**{k.get('name')}**: {k.get('domain')} Guardian: {k.get('guardian', 'N/A')}. Goal: {k.get('goal', '')}\n\n"

    # Nothingness Roaring
    nr = physics.get('nothingness_roaring', {})
    if nr:
        text += f"### 1.3 The Metaphysical Poles: The Ultimate Stakes\n\n"
        text += f"**{nr.get('name')}**: {nr.get('description')} {nr.get('impact')}\n\n"

    # The Foundation
    found = physics.get('the_foundation', {})
    if found:
        text += f"**{found.get('name')}**: {found.get('description')} {found.get('impact')}\n\n"

    # Thermodynamics
    thermo = physics.get('thermodynamics_of_repression', {})
    if thermo:
        text += f"### 1.4 The Thermodynamics of Repression\n\n"
        text += f"**Principle**: {thermo.get('principle')}\n"
        text += f"**Application**: {thermo.get('application')}\n"
        text += f"**Narrative Effect**: {thermo.get('narrative_effect')}\n\n"

    # Godel Prison
    godel = physics.get('godel_prison', {})
    if godel:
        text += f"### 1.5 The Gödel Prison\n\n"
        text += f"**Concept**: {godel.get('concept')}\n"
        text += f"**Application**: {godel.get('application')}\n"
        text += f"**Narrative Effect**: {godel.get('narrative_effect')}\n\n"

    # Holographic Trauma
    holo = physics.get('holographic_trauma', {})
    if holo:
        text += f"### 1.6 Holographic Trauma\n\n"
        text += f"**Concept**: {holo.get('concept')}\n"
        text += f"**Application**: {holo.get('application')}\n"
        text += f"**Narrative Effect**: {holo.get('narrative_effect')}\n\n"

    return text

def generate_character_table(data):
    parts = data.get('character_systems', {}).get('protagonist_system', {}).get('parts', [])
    if not parts:
        return "No character data found."

    table = "| **Anteil (Alter)** | **Typ (ANP/EP)** | **TSDP Action System** | **Core Motivation/Fear** |\n"
    table += "|---|---|---|---|\n"

    for part in parts:
        name = part.get('name', '')
        typ = part.get('type', '')
        func = part.get('function', '')
        # TSDP Action System isn't explicitly in JSON as a field, often mixed in function.
        # I'll use function for now or extract if possible.
        # Looking at JSON, 'function' often contains the action system info.

        # Motivation/Fear combo
        motivation = part.get('core_motivation', '')
        fear = part.get('core_fear', '')
        mot_fear = f"{motivation}; {fear}"

        table += f"| **{name}** | {typ} | {func} | {mot_fear} |\n"

    return table

def generate_world_table(data):
    layers = data.get('world_building', {}).get('ontological_layers', [])
    if not layers:
        return "No world data found."

    table = "| **Core World & Guardian** | **Psychological Principle** | **Defining Sensory Signature** | **Key Resonance Motif & Somatic Truth** |\n"
    table += "|---|---|---|---|\n"

    for layer in layers:
        name = layer.get('name', '')
        # Only include Kernwelten (KW) for this table as per template context
        if "KW" not in name:
            continue

        desc = layer.get('description', '')
        entropy = layer.get('entropy_manifestation', '')
        access = layer.get('access_requirements', '')

        # Mapping JSON fields to table columns might need some creative formatting
        # JSON: description, physical_laws, entropy_manifestation, access_requirements
        # Table: Principle, Sensory, Resonance

        col2 = f"{desc}<br>{layer.get('physical_laws', '')}"
        col3 = entropy
        col4 = access # Using access as proxy for somatic truth for now

        table += f"| **{name}** | {col2} | {col3} | {col4} |\n"

    return table

def generate_act_structure(data):
    acts = data.get('structural_framework', {}).get('acts', [])
    if not acts:
        return "No act structure found."

    text = ""
    for act in acts:
        num = act.get('act_number')
        title = act.get('title')
        focus = act.get('thematic_focus')
        events = act.get('key_events', [])

        text += f"**Act {num}: {title}**\n\n"
        text += f"{focus}\n\n"
        text += "**Key Events**:\n"
        for event in events:
            text += f"- {event}\n"
        text += "\n"

    return text

def generate_scene_list(data):
    scenes = data.get('structural_framework', {}).get('scenes', [])
    if not scenes:
        return "No scenes found."

    text = "| **ID** | **Title** | **POV** | **Location** | **Branches** |\n"
    text += "|---|---|---|---|---|\n"

    scenes.sort(key=lambda x: (x.get('chapter', 0), float(x.get('scene_id', 0))))

    for scene in scenes:
        sid = scene.get('scene_id')
        title = scene.get('title')
        pov = scene.get('pov_character')
        loc = scene.get('location')

        branches = scene.get('branches', [])
        branch_text = "None"
        if branches:
            branch_items = []
            for b in branches:
                name = b.get('branch_name')
                status = b.get('status', 'Draft')
                outcome = b.get('outcome', '')
                branch_items.append(f"**{name}** ({status}): {outcome}")
            branch_text = "<br>".join(branch_items)

        text += f"| {sid} | {title} | {pov} | {loc} | {branch_text} |\n"

    return text

def generate_validation_requirements(data):
    reqs = data.get('validation_criteria', {})
    text = ""

    # Continuity Rules
    text += "**Continuity Rules**:\n"
    for rule in reqs.get('continuity_rules', []):
        text += f"- [ ] {rule}\n"
    text += "\n"

    # Forbidden Actions
    text += "**Forbidden Actions**:\n"
    for item in reqs.get('forbidden_actions', []):
        action = item.get('action')
        reason = item.get('reason')
        text += f"- [ ] ❌ {action} (Reason: {reason})\n"
    text += "\n"

    # Character Constraints
    text += "**Character Constraints**:\n"
    for item in reqs.get('character_constraints', []):
        char = item.get('character')
        const = item.get('constraint')
        text += f"- [ ] **{char}**: {const}\n"

    return text

def main():
    parser = argparse.ArgumentParser(description="Sync Codex from NCP JSON")
    parser.add_argument('--ncp', type=Path, default=DEFAULT_NCP_PATH)
    parser.add_argument('--template', type=Path, default=DEFAULT_TEMPLATE_PATH)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT_PATH)

    args = parser.parse_args()

    print(f"Loading NCP from {args.ncp}")
    data = load_json(args.ncp)

    print(f"Loading template from {args.template}")
    with open(args.template, 'r', encoding='utf-8') as f:
        template = f.read()

    print("Generating sections...")
    physics_engine = generate_physics_engine(data)
    char_table = generate_character_table(data)
    world_table = generate_world_table(data)
    act_structure = generate_act_structure(data)
    validation = generate_validation_requirements(data)

    content = template.replace('{{PHYSICS_ENGINE}}', physics_engine)
    content = content.replace('{{CHARACTER_TABLE}}', char_table)
    content = content.replace('{{WORLD_TABLE}}', world_table)
    content = content.replace('{{ACT_STRUCTURE}}', act_structure)
    content = content.replace('{{VALIDATION_REQUIREMENTS}}', validation)

    scene_list = generate_scene_list(data)
    content = content.replace('{{SCENE_LIST}}', scene_list)

    print(f"Writing to {args.output}")
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Done.")

if __name__ == "__main__":
    main()
