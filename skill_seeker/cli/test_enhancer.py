#!/usr/bin/env python3
"""
Test Enhancement System Refactoring
"""

import unittest
from unittest.mock import MagicMock, patch, mock_open
import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cli.skill_enhancer import SkillEnhancer, APIEnhancer, LocalEnhancer, create_enhancer

class TestSkillEnhancer(unittest.TestCase):

    def setUp(self):
        self.skill_dir = Path("test_skill")
        self.skill_dir.mkdir(exist_ok=True)
        (self.skill_dir / "references").mkdir(exist_ok=True)
        (self.skill_dir / "SKILL.md").write_text("Old Content")
        (self.skill_dir / "references/ref1.md").write_text("Ref Content")

    def tearDown(self):
        import shutil
        if self.skill_dir.exists():
            shutil.rmtree(self.skill_dir)

    def test_factory(self):
        enhancer = create_enhancer('api', self.skill_dir, api_key="test")
        self.assertIsInstance(enhancer, APIEnhancer)

        enhancer = create_enhancer('local', self.skill_dir)
        self.assertIsInstance(enhancer, LocalEnhancer)

        with self.assertRaises(ValueError):
            create_enhancer('unknown', self.skill_dir)

    @patch('cli.skill_enhancer.read_reference_files')
    @patch('anthropic.Anthropic')
    def test_api_enhancer(self, MockAnthropic, mock_read_refs):
        mock_read_refs.return_value = {"ref1.md": "Ref Content"}

        mock_client = MagicMock()
        MockAnthropic.return_value = mock_client
        mock_message = MagicMock()
        mock_message.content = [MagicMock(text="Enhanced Content")]
        mock_client.messages.create.return_value = mock_message

        enhancer = APIEnhancer(self.skill_dir, api_key="test_key")
        result = enhancer.enhance()

        self.assertEqual(result, "Enhanced Content")
        mock_client.messages.create.assert_called_once()

    @patch('cli.skill_enhancer.read_reference_files')
    @patch('tempfile.NamedTemporaryFile')
    @patch('subprocess.Popen')
    @patch('os.chmod')
    def test_local_enhancer(self, mock_chmod, mock_popen, mock_temp, mock_read_refs):
        mock_read_refs.return_value = {"ref1.md": "Ref Content"}

        # Mock temp file context manager
        mock_file = MagicMock()
        mock_file.name = "temp_prompt.txt"
        mock_temp.return_value.__enter__.return_value = mock_file

        enhancer = LocalEnhancer(self.skill_dir)

        # Mock sys.platform to linux (default in this env)
        # In linux it just prints, doesn't call Popen
        with patch('sys.platform', 'linux'):
            result = enhancer.enhance()
            self.assertIsNone(result)
            mock_popen.assert_not_called()

        # Mock sys.platform to darwin
        with patch('sys.platform', 'darwin'):
            result = enhancer.enhance()
            self.assertIsNone(result)
            mock_popen.assert_called() # Should call open -a Terminal

    @patch('cli.skill_enhancer.SkillEnhancer.enhance')
    def test_run_method(self, mock_enhance):
        # Case 1: enhance returns content
        mock_enhance.return_value = "Enhanced Content"

        class ConcreteEnhancer(SkillEnhancer):
            def enhance(self): return super().enhance()

        enhancer = ConcreteEnhancer(self.skill_dir)
        enhancer.enhance = MagicMock(return_value="Enhanced Content")

        success = enhancer.run()
        self.assertTrue(success)
        self.assertEqual((self.skill_dir / "SKILL.md").read_text(), "Enhanced Content")

        # Case 2: enhance returns None (handled externally)
        enhancer.enhance = MagicMock(return_value=None)
        # Reset SKILL.md
        (self.skill_dir / "SKILL.md").write_text("Old Content")

        success = enhancer.run()
        self.assertTrue(success)
        # Should NOT update SKILL.md (as enhance returned None)
        self.assertEqual((self.skill_dir / "SKILL.md").read_text(), "Old Content")

if __name__ == '__main__':
    unittest.main()
