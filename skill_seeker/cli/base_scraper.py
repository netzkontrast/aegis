from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
import time
import logging

# Configure logging
logger = logging.getLogger(__name__)

class BaseScraper(ABC):
    """Abstract base class for all scraping implementations"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.base_url = config.get('base_url', '')
        self.cache_dir = Path(config.get('cache_dir', './cache'))
        self.rate_limit = config.get('rate_limit', 1.0)
        self.name = config.get('name', 'unknown')

    # ===== ABSTRACT METHODS (must be implemented by subclasses) =====

    @abstractmethod
    def validate_url(self, url: str) -> bool:
        """Validate URL for this scraper type"""
        pass

    @abstractmethod
    def extract_content(self, url: str) -> Dict[str, Any]:
        """Extract content from URL (scraper-specific logic)"""
        pass

    @abstractmethod
    def apply_selectors(self, soup: BeautifulSoup) -> str:
        """Apply CSS selectors to extract content"""
        pass

    # ===== COMMON METHODS (shared across all scrapers) =====

    def fetch_url(self, url: str) -> str:
        """Fetch URL with error handling and rate limiting"""
        self._apply_rate_limit()

        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Base Scraper)'}
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            return self._handle_fetch_error(url, e)

    def cache_data(self, key: str, data: Any) -> None:
        """Cache data to disk"""
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        cache_file = self.cache_dir / f"{key}.json"

        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_cached(self, key: str) -> Optional[Dict[str, Any]]:
        """Load cached data from disk"""
        cache_file = self.cache_dir / f"{key}.json"

        if cache_file.exists():
            with open(cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None

    def _apply_rate_limit(self) -> None:
        """Apply rate limiting between requests"""
        if self.rate_limit > 0:
            time.sleep(self.rate_limit)

    def _handle_fetch_error(self, url: str, error: Exception) -> str:
        """Handle fetch errors with retry logic"""
        logger.error(f"Error fetching {url}: {error}")
        # In a real implementation, we might retry or return a specific error code
        # For now, return empty string or raise?
        # The existing scrapers raise or log.
        # Let's re-raise for now so the caller knows it failed.
        raise error

    def parse_html(self, html: str) -> BeautifulSoup:
        """Parse HTML with BeautifulSoup"""
        return BeautifulSoup(html, 'html.parser')
