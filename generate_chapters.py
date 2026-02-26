import json
import os

def generate_chapters():
    with open('Story/kohaerenz_protokoll_v2.ncp.json', 'r') as f:
        ncp_data = json.load(f)

    acts = ncp_data['plot']['acts']
    milestones = {m['chapter']: m for m in ncp_data['pkp_milestones']['milestones']}

    # Flatten stasis luecken for easier lookup
    stasis_luecken = {}
    for act in acts:
        if 'stasis_luecken' in act:
            for sl in act['stasis_luecken']:
                stasis_luecken[sl['chapter']] = sl

    # Map chapter number to act data
    chapter_to_act = {}
    chapter_concepts = {}

    for act in acts:
        # Parse chapter range "1-13" -> 1, 13
        start, end = map(int, act['chapters'].replace('–', '-').split('-')) # Handle en-dash or hyphen
        for i in range(start, end + 1):
            chapter_to_act[i] = act

        # Extract concepts
        for concept in act['chapter_concepts']:
            chapter_concepts[concept['ch']] = concept

    # Base path for outlines
    outline_base = 'kohaerenz_protokoll/narrative_design/outlines'

    for i in range(1, 40):
        chapter_num = i
        chapter_str = f"Chapter_{i:02d}"
        filename = f"Story/{chapter_str}.md"

        act_data = chapter_to_act.get(chapter_num)
        concept_data = chapter_concepts.get(chapter_num)

        if not act_data or not concept_data:
            print(f"Warning: No data found for chapter {chapter_num}")
            continue

        # Determine outline file path
        if 1 <= i <= 13:
            outline_path = os.path.join(outline_base, 'act_1', f"chapter_{i:02d}_outline.md")
        elif 14 <= i <= 26:
            outline_path = os.path.join(outline_base, 'act_2', f"chapter_{i:02d}_outline.md")
        else:
            outline_path = os.path.join(outline_base, 'act_3', f"chapter_{i:02d}_outline.md")

        # Read outline content
        outline_content = ""
        if os.path.exists(outline_path):
            with open(outline_path, 'r') as f:
                outline_content = f.read()
        else:
            outline_content = "*No detailed outline available.*"

        # Construct file content
        content = []
        content.append(f"# {chapter_str}: {concept_data['concept']}")
        content.append("")
        content.append(f"**Act**: {act_data['title']}")
        content.append(f"**Archetype**: {act_data['archetype']}")
        content.append(f"**K-State**: {act_data['K_state']}")
        content.append(f"**Style Dominant**: {act_data['style_dominant']}")
        content.append("")
        content.append("## Core Event")
        content.append(concept_data['event'])
        content.append("")

        # Add PKP Milestone if exists
        if chapter_num in milestones:
            ms = milestones[chapter_num]
            content.append("## PKP Milestone")
            content.append(f"**Milestone {ms['pkp']}**: {ms['event']}")
            content.append("")

        # Add Stasis Luecke if exists
        if chapter_num in stasis_luecken:
            sl = stasis_luecken[chapter_num]
            content.append("## Stasis-Lücke (Meta-Twist)")
            content.append(f"**Type**: {sl['type']}")
            content.append(f"**Content**: {sl['content']}")
            content.append("")

        content.append("## Detailed Outline")
        content.append(outline_content)

        with open(filename, 'w') as f:
            f.write('\n'.join(content))

        print(f"Generated {filename}")

if __name__ == "__main__":
    generate_chapters()
