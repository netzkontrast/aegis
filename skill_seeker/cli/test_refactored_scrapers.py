#!/usr/bin/env python3
"""
Test Refactored Scrapers
"""

import unittest
from unittest.mock import MagicMock, patch, mock_open
import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cli.base_scraper import BaseScraper
from cli.doc_scraper import DocToSkillConverter
from cli.github_scraper import GitHubScraper
from cli.pdf_scraper import PDFToSkillConverter

class TestRefactoredScrapers(unittest.TestCase):

    def test_doc_scraper_inheritance(self):
        config = {'name': 'test', 'base_url': 'https://example.com'}
        scraper = DocToSkillConverter(config, dry_run=True)
        self.assertIsInstance(scraper, BaseScraper)
        self.assertTrue(hasattr(scraper, 'fetch_url'))
        self.assertTrue(hasattr(scraper, 'validate_url'))
        self.assertTrue(scraper.validate_url('https://example.com/page'))
        self.assertFalse(scraper.validate_url('https://google.com'))

    @patch('github.Github')
    def test_github_scraper_inheritance(self, mock_github):
        config = {'repo': 'owner/repo'}
        scraper = GitHubScraper(config)
        self.assertIsInstance(scraper, BaseScraper)
        self.assertTrue(hasattr(scraper, 'validate_url'))
        self.assertTrue(scraper.validate_url('https://github.com/owner/repo'))
        self.assertTrue(scraper.validate_url('owner/repo'))

    def test_pdf_scraper_inheritance(self):
        config = {'name': 'test', 'pdf_path': 'test.pdf'}
        scraper = PDFToSkillConverter(config)
        self.assertIsInstance(scraper, BaseScraper)
        self.assertTrue(hasattr(scraper, 'validate_url'))
        self.assertTrue(scraper.validate_url('test.pdf'))
        self.assertFalse(scraper.validate_url('test.txt'))
        self.assertTrue(hasattr(scraper, 'extract_all'))

if __name__ == '__main__':
    unittest.main()
