#!/usr/bin/env python3
"""
Test Base Scraper
"""

import unittest
from unittest.mock import MagicMock, patch, mock_open
import sys
import os
from pathlib import Path
from typing import Dict, Any

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cli.base_scraper import BaseScraper, BeautifulSoup

class ConcreteScraper(BaseScraper):
    def validate_url(self, url: str) -> bool:
        return True

    def extract_content(self, url: str) -> Dict[str, Any]:
        return {"content": "test"}

    def apply_selectors(self, soup: BeautifulSoup) -> str:
        return "test"

class TestBaseScraper(unittest.TestCase):

    def setUp(self):
        self.config = {
            "name": "test_scraper",
            "base_url": "https://example.com",
            "cache_dir": "test_cache",
            "rate_limit": 0.1
        }
        self.scraper = ConcreteScraper(self.config)

    def tearDown(self):
        import shutil
        if Path("test_cache").exists():
            shutil.rmtree("test_cache")

    @patch('requests.get')
    def test_fetch_url(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = "<html></html>"
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        html = self.scraper.fetch_url("https://example.com")
        self.assertEqual(html, "<html></html>")
        mock_get.assert_called_with("https://example.com", headers={'User-Agent': 'Mozilla/5.0 (Base Scraper)'}, timeout=30)

    @patch('time.sleep')
    def test_rate_limit(self, mock_sleep):
        self.scraper._apply_rate_limit()
        mock_sleep.assert_called_with(0.1)

    def test_caching(self):
        self.scraper.cache_data("test_key", {"key": "value"})

        # Check if file exists
        cache_file = Path("test_cache/test_key.json")
        self.assertTrue(cache_file.exists())

        # Check load
        data = self.scraper.load_cached("test_key")
        self.assertEqual(data, {"key": "value"})

        # Check load missing
        data = self.scraper.load_cached("missing_key")
        self.assertIsNone(data)

    def test_parse_html(self):
        html = "<html><body><h1>Test</h1></body></html>"
        soup = self.scraper.parse_html(html)
        self.assertIsInstance(soup, BeautifulSoup)
        self.assertEqual(soup.h1.text, "Test")

if __name__ == '__main__':
    unittest.main()
