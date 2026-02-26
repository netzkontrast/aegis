#!/usr/bin/env python3
"""
NCP Query Tool - MVP Implementation

A command-line tool for querying the Narrative Context Protocol (NCP)
to retrieve scene requirements, character states, and validation criteria.

Usage:
    python ncp_query.py --chapter 4
    python ncp_query.py --scene 1.4 --verbose
    python ncp_query.py --character Lex --chapter 4
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
import argparse


@dataclass
class SceneRequirements:
    """Structured scene requirements from NCP"""
    scene_id: str
    chapter: int
    title: Optional[str]
    location: str
    pov_character: str
    active_alters: List[str]
    goal: str
    conflict: str
    outcome: str
    prose_style: str
    thematic_checkpoints: List[Dict[str, str]]
    world_physics: Optional[Dict[str, Any]] = None


@dataclass
class CharacterState:
    """Character state at a specific chapter"""
    name: str
    chapter: int
    type: str  # ANP, EP, ISH
    function: str
    arc_state: str
    relationships: List[Dict[str, str]]


class NCPManager:
    """Manager for loading and querying NCP data"""

    def __init__(self, ncp_file: Path):
        """Load NCP JSON file"""
        if not ncp_file.exists():
            raise FileNotFoundError(f"NCP file not found: {ncp_file}")

        with open(ncp_file, 'r', encoding='utf-8') as f:
            self.ncp_data = json.load(f)

        self.metadata = self.ncp_data.get('metadata', {})
        self.throughlines = self.ncp_data.get('throughlines', {})
        self.character_systems = self.ncp_data.get('character_systems', {})
        self.structural_framework = self.ncp_data.get('structural_framework', {})
        self.world_building = self.ncp_data.get('world_building', {})
        self.validation_criteria = self.ncp_data.get('validation_criteria', {})

    def get_chapter_info(self, chapter: int) -> Dict:
        """Get basic information about a chapter"""
        acts = self.structural_framework.get('acts', [])

        for act in acts:
            chapter_range = act.get('chapter_range', {})
            if chapter_range.get('start', 0) <= chapter <= chapter_range.get('end', 0):
                return {
                    'chapter': chapter,
                    'act': act.get('act_number'),
                    'act_title': act.get('title'),
                    'thematic_focus': act.get('thematic_focus'),
                    'protagonist_state': act.get('protagonist_state'),
                    'antagonist_state': act.get('antagonist_state')
                }

        return {'chapter': chapter, 'error': 'Chapter not found in NCP'}

    def get_scene_requirements(self, scene_id: str) -> Optional[SceneRequirements]:
        """Get detailed requirements for a specific scene"""
        scenes = self.structural_framework.get('scenes', [])

        for scene in scenes:
            if scene.get('scene_id') == scene_id:
                # Get world physics if location is specified
                world_physics = None
                location = scene.get('location', '')
                if location:
                    world_physics = self._get_world_physics(location)

                return SceneRequirements(
                    scene_id=scene.get('scene_id'),
                    chapter=scene.get('chapter'),
                    title=scene.get('title'),
                    location=location,
                    pov_character=scene.get('pov_character'),
                    active_alters=scene.get('active_alters', []),
                    goal=scene.get('goal'),
                    conflict=scene.get('conflict'),
                    outcome=scene.get('outcome'),
                    prose_style=scene.get('prose_style'),
                    thematic_checkpoints=scene.get('thematic_checkpoints', []),
                    world_physics=world_physics
                )

        return None

    def get_character_state(self, character: str, chapter: int) -> Optional[CharacterState]:
        """Get character state at a specific chapter"""
        protagonist_system = self.character_systems.get('protagonist_system', {})
        parts = protagonist_system.get('parts', [])

        for part in parts:
            if part.get('name') == character:
                # Determine arc state based on chapter
                arc = part.get('arc', {})
                if chapter <= 13:
                    arc_state = arc.get('initial_state', 'Unknown')
                elif chapter <= 26:
                    arc_state = arc.get('midpoint_shift', 'Unknown')
                else:
                    arc_state = arc.get('final_state', 'Unknown')

                return CharacterState(
                    name=part.get('name'),
                    chapter=chapter,
                    type=part.get('type'),
                    function=part.get('function'),
                    arc_state=arc_state,
                    relationships=part.get('relationships', [])
                )

        return None

    def get_thematic_checkpoints(self, chapter: int) -> List[Dict]:
        """Get all thematic checkpoints for a chapter"""
        scenes = self.structural_framework.get('scenes', [])
        checkpoints = []

        for scene in scenes:
            if scene.get('chapter') == chapter:
                scene_checkpoints = scene.get('thematic_checkpoints', [])
                for checkpoint in scene_checkpoints:
                    checkpoints.append({
                        'scene_id': scene.get('scene_id'),
                        'checkpoint': checkpoint.get('checkpoint'),
                        'validation_question': checkpoint.get('validation_question')
                    })

        return checkpoints

    def get_world_physics(self, location: str) -> Optional[Dict]:
        """Get physics rules for a location"""
        return self._get_world_physics(location)

    def _get_world_physics(self, location: str) -> Optional[Dict]:
        """Internal helper to get world physics"""
        ontological_layers = self.world_building.get('ontological_layers', [])

        for layer in ontological_layers:
            if location in layer.get('name', ''):
                return {
                    'realm': layer.get('name'),
                    'description': layer.get('description'),
                    'physical_laws': layer.get('physical_laws'),
                    'entropy_manifestation': layer.get('entropy_manifestation')
                }

        return None

    def get_validation_criteria(self) -> Dict:
        """Get global validation criteria"""
        return self.validation_criteria

    def search_scenes_by_alter(self, alter: str) -> List[Dict]:
        """Find all scenes where an alter is active"""
        scenes = self.structural_framework.get('scenes', [])
        matching_scenes = []

        for scene in scenes:
            active_alters = scene.get('active_alters', [])
            if alter in active_alters:
                matching_scenes.append({
                    'scene_id': scene.get('scene_id'),
                    'chapter': scene.get('chapter'),
                    'title': scene.get('title'),
                    'location': scene.get('location')
                })

        return matching_scenes


def print_chapter_info(ncp: NCPManager, chapter: int, verbose: bool = False):
    """Print chapter information"""
    info = ncp.get_chapter_info(chapter)

    print(f"\n{'='*60}")
    print(f"CHAPTER {chapter} INFORMATION")
    print(f"{'='*60}")
    print(f"Act: {info.get('act')} - {info.get('act_title')}")
    print(f"Thematic Focus: {info.get('thematic_focus')}")
    print(f"\nProtagonist State: {info.get('protagonist_state')}")
    print(f"Antagonist State: {info.get('antagonist_state')}")

    if verbose:
        checkpoints = ncp.get_thematic_checkpoints(chapter)
        if checkpoints:
            print(f"\n{'='*60}")
            print(f"THEMATIC CHECKPOINTS")
            print(f"{'='*60}")
            for cp in checkpoints:
                print(f"\n[{cp['scene_id']}] {cp['checkpoint']}")
                print(f"  → {cp['validation_question']}")


def print_scene_requirements(ncp: NCPManager, scene_id: str, verbose: bool = False):
    """Print scene requirements"""
    scene = ncp.get_scene_requirements(scene_id)

    if not scene:
        print(f"Error: Scene {scene_id} not found in NCP")
        return

    print(f"\n{'='*60}")
    print(f"SCENE REQUIREMENTS: {scene.scene_id}")
    print(f"{'='*60}")
    print(f"Chapter: {scene.chapter}")
    if scene.title:
        print(f"Title: {scene.title}")
    print(f"Location: {scene.location}")
    print(f"POV: {scene.pov_character}")
    print(f"Prose Style: {scene.prose_style}")

    print(f"\nActive Alters: {', '.join(scene.active_alters)}")

    print(f"\n{'─'*60}")
    print(f"SCENE STRUCTURE")
    print(f"{'─'*60}")
    print(f"Goal: {scene.goal}")
    print(f"Conflict: {scene.conflict}")
    print(f"Outcome: {scene.outcome}")

    if scene.thematic_checkpoints:
        print(f"\n{'─'*60}")
        print(f"THEMATIC CHECKPOINTS")
        print(f"{'─'*60}")
        for i, checkpoint in enumerate(scene.thematic_checkpoints, 1):
            print(f"\n{i}. {checkpoint.get('checkpoint')}")
            print(f"   Validation: {checkpoint.get('validation_question')}")

    if verbose and scene.world_physics:
        print(f"\n{'─'*60}")
        print(f"WORLD PHYSICS: {scene.world_physics.get('realm')}")
        print(f"{'─'*60}")
        print(f"{scene.world_physics.get('description')}")
        print(f"\nPhysical Laws: {scene.world_physics.get('physical_laws')}")
        print(f"Entropy Manifestation: {scene.world_physics.get('entropy_manifestation')}")


def print_character_state(ncp: NCPManager, character: str, chapter: int, verbose: bool = False):
    """Print character state"""
    state = ncp.get_character_state(character, chapter)

    if not state:
        print(f"Error: Character {character} not found in NCP")
        return

    print(f"\n{'='*60}")
    print(f"CHARACTER STATE: {state.name} (Chapter {state.chapter})")
    print(f"{'='*60}")
    print(f"Type: {state.type}")
    print(f"Function: {state.function}")
    print(f"Arc State: {state.arc_state}")

    if verbose and state.relationships:
        print(f"\n{'─'*60}")
        print(f"RELATIONSHIPS")
        print(f"{'─'*60}")
        for rel in state.relationships:
            print(f"→ {rel.get('target')}: {rel.get('type')}")
            print(f"  {rel.get('description')}")


def main():
    parser = argparse.ArgumentParser(
        description='Query the Narrative Context Protocol (NCP)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get chapter information
  python ncp_query.py --chapter 4

  # Get scene requirements
  python ncp_query.py --scene 1.4

  # Get character state at chapter
  python ncp_query.py --character Lex --chapter 4

  # Verbose output with all details
  python ncp_query.py --chapter 4 --verbose

  # Find scenes where alter appears
  python ncp_query.py --find-alter Kiko
        """
    )

    parser.add_argument('--ncp', type=Path,
                        default=Path(__file__).parent.parent / 'ncp' / 'kohaerenz_protokoll.ncp.json',
                        help='Path to NCP JSON file')
    parser.add_argument('--chapter', type=int, help='Query chapter information')
    parser.add_argument('--scene', type=str, help='Query scene requirements (e.g., 1.4)')
    parser.add_argument('--character', type=str, help='Query character state')
    parser.add_argument('--find-alter', type=str, help='Find all scenes with this alter')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    # Load NCP
    try:
        ncp = NCPManager(args.ncp)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Execute query
    if args.chapter:
        if args.character:
            print_character_state(ncp, args.character, args.chapter, args.verbose)
        else:
            print_chapter_info(ncp, args.chapter, args.verbose)

    elif args.scene:
        print_scene_requirements(ncp, args.scene, args.verbose)

    elif args.find_alter:
        scenes = ncp.search_scenes_by_alter(args.find_alter)
        print(f"\nScenes featuring {args.find_alter}:")
        for scene in scenes:
            print(f"  [{scene['scene_id']}] Ch{scene['chapter']}: {scene['title']} ({scene['location']})")

    else:
        # No specific query - show project info
        print(f"\n{'='*60}")
        print(f"NCP LOADED: {ncp.metadata.get('title')}")
        print(f"{'='*60}")
        print(f"Author: {ncp.metadata.get('author')}")
        print(f"Genre: {', '.join(ncp.metadata.get('genre', []))}")
        print(f"\nTotal Chapters: {ncp.structural_framework.get('total_chapters')}")
        print(f"\nLogline:")
        print(f"  {ncp.metadata.get('logline')}")
        print(f"\nUse --help for query options")


if __name__ == '__main__':
    main()
