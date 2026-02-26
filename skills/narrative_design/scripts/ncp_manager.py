import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict

# Defaults
DEFAULT_NCP_PATH = Path(__file__).parent.parent / 'ncp' / 'kohaerenz_protokoll.ncp.json'

@dataclass
class Scene:
    scene_id: str
    chapter: int
    title: str = ""
    location: str = ""
    pov_character: str = ""
    active_alters: List[str] = None
    goal: str = ""
    conflict: str = ""
    outcome: str = ""
    prose_style: str = ""
    branches: List[Dict] = None

    def to_dict(self):
        d = asdict(self)
        if d['active_alters'] is None:
            d['active_alters'] = []
        if d['branches'] is None:
            d['branches'] = []
        return d

class NCPManager:
    """Manages read/write operations for the NCP JSON."""

    def __init__(self, ncp_file: Path = DEFAULT_NCP_PATH):
        self.ncp_file = ncp_file
        if not self.ncp_file.exists():
            raise FileNotFoundError(f"NCP file not found: {self.ncp_file}")

        self.load()

    def load(self):
        with open(self.ncp_file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

        # Ensure scenes structure exists
        if 'structural_framework' not in self.data:
            self.data['structural_framework'] = {}
        if 'scenes' not in self.data['structural_framework']:
            self.data['structural_framework']['scenes'] = []

    def save(self):
        with open(self.ncp_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
        print(f"Saved changes to {self.ncp_file}")

    def get_scene(self, scene_id: str) -> Optional[Dict]:
        for scene in self.data['structural_framework']['scenes']:
            if scene.get('scene_id') == scene_id:
                return scene
        return None

    def add_scene(self, scene_data: Dict):
        existing = self.get_scene(scene_data['scene_id'])
        if existing:
            print(f"Scene {scene_data['scene_id']} already exists. Updating...")
            existing.update(scene_data)
        else:
            self.data['structural_framework']['scenes'].append(scene_data)
        self.save()

    def add_branch(self, scene_id: str, branch_name: str, description: str, outcome: str, file_path: str = ""):
        scene = self.get_scene(scene_id)
        if not scene:
            print(f"Error: Scene {scene_id} not found.")
            return

        if 'branches' not in scene:
            scene['branches'] = []

        # Check if branch exists
        for b in scene['branches']:
            if b['branch_name'] == branch_name:
                print(f"Updating branch '{branch_name}' for scene {scene_id}")
                b['description'] = description
                b['outcome'] = outcome
                if file_path:
                    b['file_path'] = file_path
                self.save()
                return

        # Create new branch
        new_branch = {
            "branch_name": branch_name,
            "description": description,
            "outcome": outcome,
            "file_path": file_path,
            "status": "Draft"
        }
        scene['branches'].append(new_branch)
        print(f"Added branch '{branch_name}' to scene {scene_id}")
        self.save()

    def list_scenes(self):
        scenes = self.data['structural_framework']['scenes']
        scenes.sort(key=lambda x: (x.get('chapter', 0), x.get('scene_id', '')))
        for s in scenes:
            print(f"[{s.get('scene_id')}] Ch{s.get('chapter')}: {s.get('title')} ({len(s.get('branches', []))} branches)")

def main():
    parser = argparse.ArgumentParser(description="Manage NCP Data (Narrative Codex)")
    subparsers = parser.add_subparsers(dest="command")

    # List Scenes
    parser_list = subparsers.add_parser("list", help="List all scenes")

    # Add Scene
    parser_add = subparsers.add_parser("add-scene", help="Add or update a scene")
    parser_add.add_argument("--scene", required=True, help="Scene ID (e.g. 1.4)")
    parser_add.add_argument("--chapter", type=int, required=True, help="Chapter number")
    parser_add.add_argument("--title", required=True, help="Scene title")
    parser_add.add_argument("--location", default="", help="Location")
    parser_add.add_argument("--pov", default="", help="POV Character")
    parser_add.add_argument("--goal", default="", help="Scene goal")

    # Add Branch
    parser_branch = subparsers.add_parser("branch-scene", help="Create a narrative branch")
    parser_branch.add_argument("--scene", required=True, help="Scene ID")
    parser_branch.add_argument("--branch", required=True, help="Branch name (e.g. aggressive)")
    parser_branch.add_argument("--desc", required=True, help="Description of the branch")
    parser_branch.add_argument("--outcome", required=True, help="Outcome of this branch")
    parser_branch.add_argument("--file", default="", help="File path for branch content")

    args = parser.parse_args()

    manager = NCPManager()

    if args.command == "list":
        manager.list_scenes()
    elif args.command == "add-scene":
        scene_data = {
            "scene_id": args.scene,
            "chapter": args.chapter,
            "title": args.title,
            "location": args.location,
            "pov_character": args.pov,
            "goal": args.goal,
            "active_alters": [],  # Default empty
            "branches": []
        }
        manager.add_scene(scene_data)
    elif args.command == "branch-scene":
        manager.add_branch(args.scene, args.branch, args.desc, args.outcome, args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
