#!/usr/bin/env python3
"""
NCP Writing Assistant - MVP Implementation

A command-line tool for generating writing prompts, character voice samples,
and stylistic guidance based on the Narrative Context Protocol (NCP).

Usage:
    python ncp_assist.py --chapter 4 --prompt
    python ncp_assist.py --scene 1.4 --prompt
    python ncp_assist.py --character Lex --voice-sample
    python ncp_assist.py --chapter 4 --style-guide
"""

import sys
import random
from pathlib import Path
from typing import Dict, List, Optional
import argparse

# Import NCP Manager from ncp_query
sys.path.insert(0, str(Path(__file__).parent))
from ncp_query import NCPManager


class WritingAssistant:
    """Generate writing prompts and guidance from NCP"""

    def __init__(self, ncp: NCPManager):
        self.ncp = ncp

    def generate_scene_prompt(self, scene_id: str, verbose: bool = False) -> Dict:
        """Generate a comprehensive writing prompt for a scene"""
        scene = self.ncp.get_scene_requirements(scene_id)

        if not scene:
            return {'error': f'Scene {scene_id} not found'}

        chapter_info = self.ncp.get_chapter_info(scene.chapter)

        # Get character states for active alters
        character_states = []
        for alter in scene.active_alters:
            # Extract base name (remove annotations like "(background)")
            alter_name = alter.split('(')[0].strip()
            state = self.ncp.get_character_state(alter_name, scene.chapter)
            if state:
                character_states.append(state)

        # Build prompt
        prompt = {
            'scene_id': scene.scene_id,
            'chapter': scene.chapter,
            'title': scene.title,
            'act': chapter_info.get('act'),
            'location': scene.location,
            'pov': scene.pov_character,
            'prose_style': scene.prose_style,
            'structure': {
                'goal': scene.goal,
                'conflict': scene.conflict,
                'outcome': scene.outcome
            },
            'active_alters': [
                {
                    'name': cs.name,
                    'type': cs.type,
                    'function': cs.function,
                    'arc_state': cs.arc_state
                }
                for cs in character_states
            ],
            'thematic_checkpoints': scene.thematic_checkpoints,
            'style_guidance': self._get_style_guidance(scene.chapter, scene.prose_style),
            'sensory_keywords': self._get_sensory_keywords(scene.location),
            'opening_hooks': self._generate_opening_hooks(scene),
        }

        if verbose and scene.world_physics:
            prompt['world_physics'] = scene.world_physics

        return prompt

    def generate_chapter_prompt(self, chapter: int, verbose: bool = False) -> Dict:
        """Generate a writing prompt for an entire chapter"""
        chapter_info = self.ncp.get_chapter_info(chapter)
        checkpoints = self.ncp.get_thematic_checkpoints(chapter)

        # Get all scenes for this chapter
        scenes = []
        for scene_data in self.ncp.structural_framework.get('scenes', []):
            if scene_data.get('chapter') == chapter:
                scenes.append({
                    'scene_id': scene_data.get('scene_id'),
                    'title': scene_data.get('title'),
                    'location': scene_data.get('location'),
                    'pov': scene_data.get('pov_character')
                })

        return {
            'chapter': chapter,
            'act': chapter_info.get('act'),
            'act_title': chapter_info.get('act_title'),
            'thematic_focus': chapter_info.get('thematic_focus'),
            'protagonist_state': chapter_info.get('protagonist_state'),
            'scenes': scenes,
            'checkpoints': checkpoints if verbose else [],
            'style_guidance': self._get_style_guidance(chapter, None)
        }

    def generate_voice_sample(self, character: str, chapter: int) -> Dict:
        """Generate character voice samples and writing guidance"""
        state = self.ncp.get_character_state(character, chapter)

        if not state:
            return {'error': f'Character {character} not found'}

        voice_profile = self._build_voice_profile(state)

        return {
            'character': state.name,
            'chapter': state.chapter,
            'type': state.type,
            'function': state.function,
            'arc_state': state.arc_state,
            'voice_profile': voice_profile,
            'dialogue_samples': self._generate_dialogue_samples(state),
            'internal_voice_samples': self._generate_internal_samples(state),
            'relationships': state.relationships
        }

    def _get_style_guidance(self, chapter: int, prose_style: Optional[str]) -> Dict:
        """Get prose style guidance based on Act"""
        if chapter <= 13:
            act = 1
            guidance = {
                'act': 'Act I: Fragmentation',
                'sentence_structure': 'Short, fragmented. Use interruptions, parenthetical intrusions.',
                'perspective': 'Fragmented POV. Multiple voices interrupting each other.',
                'pacing': 'Disjointed. Jumps in time/space. Confusion and disorientation.',
                'emotional_tone': 'Fear, confusion, dissociation. Characters avoid emotional content.',
                'key_techniques': [
                    'Use em-dashes for sudden breaks',
                    'Parenthetical intrusions from other alters',
                    'Incomplete thoughts trailing off',
                    'Present tense for immediacy',
                    'No clear pronoun consistency (I/we/they blur)'
                ]
            }
        elif chapter <= 26:
            act = 2
            guidance = {
                'act': 'Act II: Cooperation',
                'sentence_structure': 'Transitional. Mix of fragments and complete sentences.',
                'perspective': 'Beginning to integrate. "We" starts appearing.',
                'pacing': 'More controlled, but still unstable moments.',
                'emotional_tone': 'Tentative hope mixed with setbacks. Emerging trust.',
                'key_techniques': [
                    'Alternate between fragmented and fluid prose',
                    'Show negotiation between alters',
                    'Use "we" occasionally but not consistently',
                    'Balance logic (Lex) with emotion (Rhys)',
                    'Show moments of cooperation breaking down'
                ]
            }
        else:
            act = 3
            guidance = {
                'act': 'Act III: Integration',
                'sentence_structure': 'Polyphonic. Complex sentences holding multiple perspectives.',
                'perspective': 'Integrated "we" voice. All alters present simultaneously.',
                'pacing': 'Fluid and purposeful. Control with intention.',
                'emotional_tone': 'Acceptance, strength, wholeness. Pain acknowledged but not overwhelming.',
                'key_techniques': [
                    'Complex sentences weaving multiple viewpoints',
                    'Consistent "we" as primary pronoun',
                    'Show all alters contributing simultaneously',
                    'Parentheticals become collaborative, not intrusive',
                    'Confident, purposeful pacing'
                ]
            }

        if prose_style:
            guidance['scene_specific_style'] = prose_style

        return guidance

    def _get_sensory_keywords(self, location: str) -> Dict:
        """Get sensory keywords for a location"""
        location_lower = location.lower()

        if 'logos-prime' in location_lower or 'kw1' in location_lower:
            return {
                'realm': 'KW1: Logos-Prime',
                'visual': ['white', 'sterile', 'geometric', 'perfect angles', 'shadowless light', 'clean lines'],
                'tactile': ['smooth', 'temperature-neutral', 'synthetic', 'precise'],
                'auditory': ['silent', 'mechanical hum', 'precise footsteps', 'digital ping'],
                'emotional': ['numb', 'controlled', 'empty', 'logical', 'dissociated'],
                'physics': 'Rigid. Reality is fixed and predictable. Emotion is suppressed.'
            }
        elif 'mnemosyne' in location_lower or 'kw2' in location_lower:
            return {
                'realm': 'KW2: Mnemosyne-Archipel',
                'visual': ['dark water', 'mist', 'bruised sky', 'shifting islands', 'pale roots'],
                'tactile': ['wet', 'cold', 'drowning', 'heavy', 'pulling'],
                'auditory': ['echo', 'whisper', 'waves', 'sobbing', 'distant crying'],
                'emotional': ['grief', 'longing', 'overwhelm', 'memory', 'loss'],
                'physics': 'Fluid. Time is non-linear. Memory loops. Emotion shapes reality.'
            }
        elif 'cerberus' in location_lower or 'kw3' in location_lower:
            return {
                'realm': 'KW3: Cerberus-Labyrinth',
                'visual': ['concrete', 'steel', 'sharp edges', 'bunker', 'paranoid architecture'],
                'tactile': ['cold metal', 'rough concrete', 'barbed', 'pressure'],
                'auditory': ['alarm', 'footsteps echoing', 'locks clicking', 'threat'],
                'emotional': ['fear', 'paranoia', 'defensive', 'trapped', 'vigilant'],
                'physics': 'Defensive. Walls shift to protect. Paths loop to confuse invaders.'
            }
        elif 'kairos' in location_lower or 'kw4' in location_lower:
            return {
                'realm': 'KW4: Kairos-Potentialis',
                'visual': ['fractal gardens', 'growth', 'bioluminescence', 'emerging patterns'],
                'tactile': ['organic', 'warm', 'growing', 'alive', 'potential'],
                'auditory': ['rustling', 'breathing', 'growing', 'emergence'],
                'emotional': ['hope', 'possibility', 'creative', 'wonder', 'becoming'],
                'physics': 'Emergent. Potential becomes real. Imagination shapes matter.'
            }
        else:
            return {
                'realm': 'Unknown location',
                'note': 'No specific sensory profile available'
            }

    def _generate_opening_hooks(self, scene) -> List[str]:
        """Generate potential opening lines for a scene"""
        hooks = []

        # Action hook
        hooks.append(f"The {scene.location.split()[0]} doesn't wait for Kael to be ready.")

        # Sensory hook
        if 'mnemosyne' in scene.location.lower():
            hooks.append("The water remembers. Even when Kael doesn't.")
        elif 'logos' in scene.location.lower():
            hooks.append("The walls are perfect. Perfectly wrong.")
        elif 'cerberus' in scene.location.lower():
            hooks.append("Three corridors. Three choices. All of them traps.")

        # Character hook (POV character)
        pov_name = scene.pov_character.split()[0]  # Extract name
        hooks.append(f"{pov_name} finds the answer in the place no one thought to look.")

        # Thematic hook
        if scene.thematic_checkpoints:
            first_checkpoint = scene.thematic_checkpoints[0].get('checkpoint', '')
            if 'trauma' in first_checkpoint.lower():
                hooks.append("Some memories don't fade. They wait.")
            elif 'cooperation' in first_checkpoint.lower():
                hooks.append("Working together requires trust. Trust requires risk.")

        # Conflict hook
        if scene.conflict:
            hooks.append(f"The plan was simple. Until it wasn't.")

        return hooks

    def _build_voice_profile(self, state) -> Dict:
        """Build a voice profile for a character"""
        profiles = {
            'Kael': {
                'speech_patterns': 'Confused, questioning, short sentences. Often asks for help from others.',
                'vocabulary': 'Simple, direct. Technical when influenced by Lex.',
                'internal_voice': 'Fragmented thoughts. Constantly interrupted by other alters.',
                'emotional_register': 'Numb → Confused → Emerging awareness (across arc)',
                'typical_phrases': [
                    '"I don\'t understand."',
                    '"Lex, what is this?"',
                    '"Why can\'t I remember?"'
                ]
            },
            'Lex': {
                'speech_patterns': 'Logical, analytical, precise. Full sentences with technical detail.',
                'vocabulary': 'Scientific, technical, controlling. Uses statistics and facts.',
                'internal_voice': 'Calculating. Always analyzing. Struggles with emotion.',
                'emotional_register': 'Controlled → Afraid (when logic fails) → Accepting (late arc)',
                'typical_phrases': [
                    '"The data suggests..."',
                    '"This is inefficient."',
                    '"Control your emotional response."'
                ]
            },
            'Rhys': {
                'speech_patterns': 'Gentle, empathetic, complete sentences. Warm and caring.',
                'vocabulary': 'Emotional, compassionate. Names feelings.',
                'internal_voice': 'Concerned for others. Carries grief but remains kind.',
                'emotional_register': 'Sad compassion → Protective warmth → Healing presence',
                'typical_phrases': [
                    '"You\'re safe now."',
                    '"It\'s okay to feel this."',
                    '"I\'ve got you."'
                ]
            },
            'Kiko': {
                'speech_patterns': 'Childlike, simple words, short sentences. Sometimes non-verbal.',
                'vocabulary': 'Simple, concrete. Struggles with abstract concepts.',
                'internal_voice': 'Scared, hurt, but resilient. Holds trauma.',
                'emotional_register': 'Terrified → Tentatively trusting → Healing',
                'typical_phrases': [
                    '"I\'m sorry."',
                    '"Please don\'t leave."',
                    '"It hurts."'
                ]
            },
            'Nyx': {
                'speech_patterns': 'Short, aggressive, protective. Commands not questions.',
                'vocabulary': 'Blunt, confrontational. Military precision.',
                'internal_voice': 'Vigilant. Always scanning for threats.',
                'emotional_register': 'Aggressive defense → Calculated protection → Purposeful strength',
                'typical_phrases': [
                    '"Get back."',
                    '"I won\'t let them hurt us."',
                    '"Run."'
                ]
            },
            'Alex': {
                'speech_patterns': 'Adaptive, social, smooth. Diplomatic.',
                'vocabulary': 'Flexible. Mirrors others to fit in.',
                'internal_voice': 'Strategic. Maintains facade while protecting system.',
                'emotional_register': 'Performed confidence → Authentic connection → Integrated diplomat',
                'typical_phrases': [
                    '"Everything is fine."',
                    '"I can handle this."',
                    '"Let me manage this."'
                ]
            }
        }

        profile = profiles.get(state.name, {
            'speech_patterns': f'{state.type} alter - {state.function}',
            'note': 'Custom voice profile - see character arc details'
        })

        # Add arc-specific modifications
        profile['current_arc_state'] = state.arc_state

        return profile

    def _generate_dialogue_samples(self, state) -> List[str]:
        """Generate sample dialogue for a character"""
        samples = {
            'Kael': [
                '"Lex? I need... I need help understanding this."',
                '"Why does this feel familiar? Like I\'ve been here before?"',
                '"Is this real? Tell me this is real."'
            ],
            'Lex': [
                '"Your emotional response is counterproductive. Focus on the data."',
                '"I\'ve calculated seventeen potential outcomes. None are optimal."',
                '"This is a Riss. A flaw in the system architecture. We need to report it."'
            ],
            'Rhys': [
                '"Hey, it\'s okay. You\'re allowed to be scared."',
                '"I know it hurts. But you\'re not alone in this. I\'m here."',
                '"Let\'s take this slowly. One step at a time."'
            ],
            'Kiko': [
                '"I don\'t want to remember. Please don\'t make me remember."',
                '"Are we safe here? Really safe?"',
                '"I\'m sorry I\'m scared. I\'m trying to be brave."'
            ],
            'Nyx': [
                '"Back off. Now."',
                '"If they come for us again, I\'m ready."',
                '"Trust isn\'t free. Earn it."'
            ],
            'Alex': [
                '"Of course I\'m fine. Why wouldn\'t I be?"',
                '"I\'ve handled worse than this. We all have."',
                '"Let me talk to them. I know how to make this work."'
            ]
        }

        return samples.get(state.name, [f'"[{state.name} would say something fitting their function: {state.function}]"'])

    def _generate_internal_samples(self, state) -> List[str]:
        """Generate internal voice samples (thoughts)"""
        samples = {
            'Kael': [
                '(Why can\'t I remember? There\'s something wrong with me. Something broken.)',
                '(Lex is talking again. Numbers and logic. But none of it makes me feel better.)',
                '(Someone else is here. Watching. I can feel them.)'
            ],
            'Lex': [
                '(Kael\'s emotional dysregulation is increasing. I need to intervene before—)',
                '(This doesn\'t make sense. The variables don\'t align. Something\'s missing from the equation.)',
                '(If I lose control, we all lose control. I have to stay focused.)'
            ],
            'Rhys': [
                '(He\'s hurting so much. I wish I could take it from him.)',
                '(Kiko is crying again. In the background. Always in the background.)',
                '(We carry this together. That\'s what we do.)'
            ],
            'Kiko': [
                '(It\'s dark here. I don\'t like the dark.)',
                '(Maybe if I\'m very quiet, he won\'t find me.)',
                '(I remember. I don\'t want to remember. But I do.)'
            ],
            'Nyx': [
                '(Threat assessment: unclear. Trust level: zero.)',
                '(I\'m ready. Always ready. They won\'t catch us again.)',
                '(Kael doesn\'t see the danger. But I do.)'
            ],
            'Alex': [
                '(Smile. Nod. Pretend everything is normal.)',
                '(They can\'t know what we are. They\'d use it against us.)',
                '(I can hold this together. I always do.)'
            ]
        }

        return samples.get(state.name, [f'({state.name} thinks about {state.function.lower()})'])


def print_scene_prompt(prompt: Dict, verbose: bool = False):
    """Print scene prompt in human-readable format"""
    print(f"\n{'='*60}")
    print(f"WRITING PROMPT: SCENE {prompt['scene_id']}")
    print(f"{'='*60}")
    print(f"Title: {prompt.get('title', 'Untitled')}")
    print(f"Chapter: {prompt['chapter']} (Act {prompt['act']})")
    print(f"Location: {prompt['location']}")
    print(f"POV: {prompt['pov']}")
    print(f"Prose Style: {prompt['prose_style']}")

    print(f"\n{'─'*60}")
    print(f"SCENE STRUCTURE")
    print(f"{'─'*60}")
    print(f"Goal: {prompt['structure']['goal']}")
    print(f"Conflict: {prompt['structure']['conflict']}")
    print(f"Outcome: {prompt['structure']['outcome']}")

    print(f"\n{'─'*60}")
    print(f"ACTIVE ALTERS")
    print(f"{'─'*60}")
    for alter in prompt['active_alters']:
        print(f"\n{alter['name']} ({alter['type']})")
        print(f"  Function: {alter['function']}")
        print(f"  Arc State: {alter['arc_state']}")

    print(f"\n{'─'*60}")
    print(f"STYLE GUIDANCE: {prompt['style_guidance']['act']}")
    print(f"{'─'*60}")
    print(f"Sentence Structure: {prompt['style_guidance']['sentence_structure']}")
    print(f"Perspective: {prompt['style_guidance']['perspective']}")
    print(f"Pacing: {prompt['style_guidance']['pacing']}")
    print(f"Emotional Tone: {prompt['style_guidance']['emotional_tone']}")

    if verbose:
        print(f"\nKey Techniques:")
        for technique in prompt['style_guidance']['key_techniques']:
            print(f"  • {technique}")

    print(f"\n{'─'*60}")
    print(f"SENSORY KEYWORDS: {prompt['sensory_keywords']['realm']}")
    print(f"{'─'*60}")
    if 'visual' in prompt['sensory_keywords']:
        print(f"Visual: {', '.join(prompt['sensory_keywords']['visual'][:5])}")
        print(f"Tactile: {', '.join(prompt['sensory_keywords']['tactile'][:5])}")
        print(f"Emotional: {', '.join(prompt['sensory_keywords']['emotional'][:5])}")
        print(f"Physics: {prompt['sensory_keywords']['physics']}")

    print(f"\n{'─'*60}")
    print(f"OPENING HOOKS (Choose one)")
    print(f"{'─'*60}")
    for i, hook in enumerate(prompt['opening_hooks'], 1):
        print(f"{i}. {hook}")

    if verbose and prompt['thematic_checkpoints']:
        print(f"\n{'─'*60}")
        print(f"THEMATIC CHECKPOINTS")
        print(f"{'─'*60}")
        for cp in prompt['thematic_checkpoints']:
            print(f"\n• {cp['checkpoint']}")
            print(f"  Validation: {cp['validation_question']}")

    if verbose and 'world_physics' in prompt:
        print(f"\n{'─'*60}")
        print(f"WORLD PHYSICS")
        print(f"{'─'*60}")
        print(f"{prompt['world_physics']['description']}")

    print(f"\n{'='*60}\n")


def print_chapter_prompt(prompt: Dict, verbose: bool = False):
    """Print chapter prompt in human-readable format"""
    print(f"\n{'='*60}")
    print(f"WRITING PROMPT: CHAPTER {prompt['chapter']}")
    print(f"{'='*60}")
    print(f"Act: {prompt['act']} - {prompt['act_title']}")
    print(f"Thematic Focus: {prompt['thematic_focus']}")
    print(f"Protagonist State: {prompt['protagonist_state']}")

    print(f"\n{'─'*60}")
    print(f"SCENES IN THIS CHAPTER")
    print(f"{'─'*60}")
    for scene in prompt['scenes']:
        print(f"\n[{scene['scene_id']}] {scene['title']}")
        print(f"  Location: {scene['location']}")
        print(f"  POV: {scene['pov']}")

    print(f"\n{'─'*60}")
    print(f"STYLE GUIDANCE: {prompt['style_guidance']['act']}")
    print(f"{'─'*60}")
    print(f"Sentence Structure: {prompt['style_guidance']['sentence_structure']}")
    print(f"Perspective: {prompt['style_guidance']['perspective']}")
    print(f"Emotional Tone: {prompt['style_guidance']['emotional_tone']}")

    if verbose and prompt['checkpoints']:
        print(f"\n{'─'*60}")
        print(f"THEMATIC CHECKPOINTS")
        print(f"{'─'*60}")
        for cp in prompt['checkpoints']:
            print(f"\n[{cp['scene_id']}] {cp['checkpoint']}")
            print(f"  → {cp['validation_question']}")

    print(f"\n{'='*60}\n")


def print_voice_sample(voice: Dict, verbose: bool = False):
    """Print character voice sample in human-readable format"""
    print(f"\n{'='*60}")
    print(f"CHARACTER VOICE: {voice['character']} (Chapter {voice['chapter']})")
    print(f"{'='*60}")
    print(f"Type: {voice['type']}")
    print(f"Function: {voice['function']}")
    print(f"Current Arc State: {voice['arc_state']}")

    print(f"\n{'─'*60}")
    print(f"VOICE PROFILE")
    print(f"{'─'*60}")
    profile = voice['voice_profile']
    print(f"Speech Patterns: {profile.get('speech_patterns', 'N/A')}")
    print(f"Vocabulary: {profile.get('vocabulary', 'N/A')}")
    print(f"Internal Voice: {profile.get('internal_voice', 'N/A')}")
    print(f"Emotional Register: {profile.get('emotional_register', 'N/A')}")

    if 'typical_phrases' in profile:
        print(f"\nTypical Phrases:")
        for phrase in profile['typical_phrases']:
            print(f"  • {phrase}")

    print(f"\n{'─'*60}")
    print(f"DIALOGUE SAMPLES")
    print(f"{'─'*60}")
    for sample in voice['dialogue_samples']:
        print(f"  {sample}")

    print(f"\n{'─'*60}")
    print(f"INTERNAL VOICE SAMPLES")
    print(f"{'─'*60}")
    for sample in voice['internal_voice_samples']:
        print(f"  {sample}")

    if verbose and voice['relationships']:
        print(f"\n{'─'*60}")
        print(f"RELATIONSHIPS")
        print(f"{'─'*60}")
        for rel in voice['relationships']:
            print(f"\n→ {rel.get('target')}: {rel.get('type')}")
            print(f"  {rel.get('description')}")

    print(f"\n{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description='NCP Writing Assistant - Generate prompts and character voices',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate scene writing prompt
  python ncp_assist.py --scene 1.4 --prompt

  # Generate chapter overview prompt
  python ncp_assist.py --chapter 4 --prompt

  # Get character voice sample
  python ncp_assist.py --character Lex --voice-sample

  # Get character voice at specific chapter
  python ncp_assist.py --character Lex --chapter 4 --voice-sample

  # Verbose output with all details
  python ncp_assist.py --scene 1.4 --prompt --verbose

  # Get style guidance for a chapter
  python ncp_assist.py --chapter 15 --style-guide
        """
    )

    parser.add_argument('--ncp', type=Path,
                        default=Path(__file__).parent.parent / 'ncp' / 'kohaerenz_protokoll.ncp.json',
                        help='Path to NCP JSON file')
    parser.add_argument('--chapter', type=int, help='Chapter number')
    parser.add_argument('--scene', type=str, help='Scene ID (e.g., 1.4)')
    parser.add_argument('--character', type=str, help='Character name for voice sample')
    parser.add_argument('--prompt', action='store_true', help='Generate writing prompt')
    parser.add_argument('--voice-sample', action='store_true', help='Generate character voice sample')
    parser.add_argument('--style-guide', action='store_true', help='Show style guidance for chapter')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    # Load NCP
    try:
        ncp = NCPManager(args.ncp)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    assistant = WritingAssistant(ncp)

    # Execute command
    if args.prompt:
        if args.scene:
            prompt = assistant.generate_scene_prompt(args.scene, args.verbose)
            if 'error' in prompt:
                print(f"Error: {prompt['error']}", file=sys.stderr)
                sys.exit(1)
            if args.json:
                import json
                print(json.dumps(prompt, indent=2))
            else:
                print_scene_prompt(prompt, args.verbose)
        elif args.chapter:
            prompt = assistant.generate_chapter_prompt(args.chapter, args.verbose)
            if args.json:
                import json
                print(json.dumps(prompt, indent=2))
            else:
                print_chapter_prompt(prompt, args.verbose)
        else:
            print("Error: --prompt requires either --scene or --chapter", file=sys.stderr)
            sys.exit(1)

    elif args.voice_sample:
        if not args.character:
            print("Error: --voice-sample requires --character", file=sys.stderr)
            sys.exit(1)

        chapter = args.chapter or 1
        voice = assistant.generate_voice_sample(args.character, chapter)

        if 'error' in voice:
            print(f"Error: {voice['error']}", file=sys.stderr)
            sys.exit(1)

        if args.json:
            import json
            print(json.dumps(voice, indent=2))
        else:
            print_voice_sample(voice, args.verbose)

    elif args.style_guide:
        if not args.chapter:
            print("Error: --style-guide requires --chapter", file=sys.stderr)
            sys.exit(1)

        guidance = assistant._get_style_guidance(args.chapter, None)

        print(f"\n{'='*60}")
        print(f"STYLE GUIDE: {guidance['act']}")
        print(f"{'='*60}")
        print(f"\nSentence Structure: {guidance['sentence_structure']}")
        print(f"Perspective: {guidance['perspective']}")
        print(f"Pacing: {guidance['pacing']}")
        print(f"Emotional Tone: {guidance['emotional_tone']}")
        print(f"\nKey Techniques:")
        for technique in guidance['key_techniques']:
            print(f"  • {technique}")
        print(f"\n{'='*60}\n")

    else:
        print("\nNCP Writing Assistant")
        print("=" * 60)
        print("\nAvailable commands:")
        print("  --prompt --scene X.Y       Generate scene writing prompt")
        print("  --prompt --chapter N       Generate chapter overview")
        print("  --voice-sample --character NAME   Generate character voice sample")
        print("  --style-guide --chapter N  Show style guidance")
        print("\nUse --help for more details and examples")
        print()


if __name__ == '__main__':
    main()
