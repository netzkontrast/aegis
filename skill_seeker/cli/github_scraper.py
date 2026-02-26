#!/usr/bin/env python3
"""
GitHub Repository to Claude Skill Converter (Tasks C1.1-C1.12)

Converts GitHub repositories into Claude AI skills by extracting:
- README and documentation
- Code structure and signatures
- GitHub Issues, Changelog, and Releases
- Usage examples from tests

Usage:
    python3 cli/github_scraper.py --repo facebook/react
    python3 cli/github_scraper.py --config configs/react_github.json
    python3 cli/github_scraper.py --repo owner/repo --token $GITHUB_TOKEN
"""

import os
import sys
import json
import re
import argparse
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
from bs4 import BeautifulSoup

try:
    from github import Github, GithubException, Repository
    from github.GithubException import RateLimitExceededException
except ImportError:
    print("Error: PyGithub not installed. Run: pip install PyGithub")
    sys.exit(1)

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cli.base_scraper import BaseScraper

# Import code analyzer for deep code analysis
try:
    from cli.code_analyzer import CodeAnalyzer
    CODE_ANALYZER_AVAILABLE = True
except ImportError:
    # Try importing from local if running as script
    try:
        from code_analyzer import CodeAnalyzer
        CODE_ANALYZER_AVAILABLE = True
    except ImportError:
        CODE_ANALYZER_AVAILABLE = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class GitHubScraper(BaseScraper):
    """
    GitHub Repository Scraper (C1.1-C1.9)
    """

    def __init__(self, config: Dict[str, Any]):
        """Initialize GitHub scraper with configuration."""
        super().__init__(config)
        self.repo_name = config['repo']
        self.name = config.get('name', self.repo_name.split('/')[-1])
        self.description = config.get('description', f'Skill for {self.repo_name}')

        # GitHub client setup (C1.1)
        token = self._get_token()
        self.github = Github(token) if token else Github()
        self.repo: Optional[Repository.Repository] = None

        # Options
        self.include_issues = config.get('include_issues', True)
        self.max_issues = config.get('max_issues', 100)
        self.include_changelog = config.get('include_changelog', True)
        self.include_releases = config.get('include_releases', True)
        self.include_code = config.get('include_code', False)
        self.code_analysis_depth = config.get('code_analysis_depth', 'surface')  # 'surface', 'deep', 'full'
        self.file_patterns = config.get('file_patterns', [])

        # Initialize code analyzer if deep analysis requested
        self.code_analyzer = None
        if self.code_analysis_depth != 'surface' and CODE_ANALYZER_AVAILABLE:
            self.code_analyzer = CodeAnalyzer(depth=self.code_analysis_depth)
            logger.info(f"Code analysis depth: {self.code_analysis_depth}")

        # Output paths
        self.skill_dir = f"output/{self.name}"
        self.data_file = f"output/{self.name}_github_data.json"

        # Extracted data storage
        self.extracted_data = {
            'repo_info': {},
            'readme': '',
            'file_tree': [],
            'languages': {},
            'signatures': [],
            'test_examples': [],
            'issues': [],
            'changelog': '',
            'releases': []
        }

    def validate_url(self, url: str) -> bool:
        """Validate if URL is a GitHub repo"""
        return "github.com" in url or not url.startswith("http") # Allow "owner/repo" format

    def extract_content(self, url: str) -> Dict[str, Any]:
        """Extract content (wrapper for scrape)"""
        # If url looks like a full URL, extract owner/repo
        if "github.com/" in url:
            parts = url.split("github.com/")[-1].strip("/").split("/")
            if len(parts) >= 2:
                self.repo_name = f"{parts[0]}/{parts[1]}"
        elif "/" in url and not url.startswith("http"):
            self.repo_name = url

        return self.scrape()

    def apply_selectors(self, soup: BeautifulSoup) -> str:
        """Not applicable for GitHub API scraper"""
        return ""

    def _get_token(self) -> Optional[str]:
        """
        Get GitHub token from env var or config (both options supported).
        Priority: GITHUB_TOKEN env var > config file > None
        """
        # Try environment variable first (recommended)
        token = os.getenv('GITHUB_TOKEN')
        if token:
            logger.info("Using GitHub token from GITHUB_TOKEN environment variable")
            return token

        # Fall back to config file
        token = self.config.get('github_token')
        if token:
            logger.warning("Using GitHub token from config file (less secure)")
            return token

        logger.warning("No GitHub token provided - using unauthenticated access (lower rate limits)")
        return None

    def scrape(self) -> Dict[str, Any]:
        """
        Main scraping entry point.
        Executes all C1 tasks in sequence.
        """
        try:
            logger.info(f"Starting GitHub scrape for: {self.repo_name}")

            # C1.1: Fetch repository
            self._fetch_repository()

            # C1.2: Extract README
            self._extract_readme()

            # C1.3-C1.6: Extract code structure
            self._extract_code_structure()

            # C1.7: Extract Issues
            if self.include_issues:
                self._extract_issues()

            # C1.8: Extract CHANGELOG
            if self.include_changelog:
                self._extract_changelog()

            # C1.9: Extract Releases
            if self.include_releases:
                self._extract_releases()

            # Save extracted data
            self._save_data()

            logger.info(f"✅ Scraping complete! Data saved to: {self.data_file}")
            return self.extracted_data

        except RateLimitExceededException:
            logger.error("GitHub API rate limit exceeded. Please wait or use authentication token.")
            raise
        except GithubException as e:
            logger.error(f"GitHub API error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during scraping: {e}")
            raise

    # ... (Keep existing methods: _fetch_repository, _extract_readme, etc.)
    # I need to include them to keep the file valid.

    def _fetch_repository(self):
        logger.info(f"Fetching repository: {self.repo_name}")
        try:
            self.repo = self.github.get_repo(self.repo_name)
            self.extracted_data['repo_info'] = {
                'name': self.repo.name,
                'full_name': self.repo.full_name,
                'description': self.repo.description,
                'url': self.repo.html_url,
                'homepage': self.repo.homepage,
                'stars': self.repo.stargazers_count,
                'forks': self.repo.forks_count,
                'open_issues': self.repo.open_issues_count,
                'default_branch': self.repo.default_branch,
                'created_at': self.repo.created_at.isoformat() if self.repo.created_at else None,
                'updated_at': self.repo.updated_at.isoformat() if self.repo.updated_at else None,
                'language': self.repo.language,
                'license': self.repo.license.name if self.repo.license else None,
                'topics': self.repo.get_topics()
            }
            logger.info(f"Repository fetched: {self.repo.full_name} ({self.repo.stargazers_count} stars)")
        except GithubException as e:
            if e.status == 404: raise ValueError(f"Repository not found: {self.repo_name}")
            raise

    def _extract_readme(self):
        logger.info("Extracting README...")
        readme_files = ['README.md', 'README.rst', 'README.txt', 'README', 'docs/README.md', '.github/README.md']
        for readme_path in readme_files:
            try:
                content = self.repo.get_contents(readme_path)
                if content:
                    self.extracted_data['readme'] = content.decoded_content.decode('utf-8')
                    logger.info(f"README found: {readme_path}")
                    return
            except GithubException: continue
        logger.warning("No README found in repository")

    def _extract_code_structure(self):
        logger.info("Extracting code structure...")
        self._extract_languages()
        self._extract_file_tree()
        if self.include_code: self._extract_signatures_and_tests()

    def _extract_languages(self):
        logger.info("Detecting programming languages...")
        try:
            languages = self.repo.get_languages()
            total_bytes = sum(languages.values())
            self.extracted_data['languages'] = {
                lang: {'bytes': bytes_count, 'percentage': round((bytes_count / total_bytes) * 100, 2) if total_bytes > 0 else 0}
                for lang, bytes_count in languages.items()
            }
            logger.info(f"Languages detected: {', '.join(languages.keys())}")
        except GithubException as e: logger.warning(f"Could not fetch languages: {e}")

    def _extract_file_tree(self):
        logger.info("Building file tree...")
        try:
            contents = self.repo.get_contents("")
            file_tree = []
            while contents:
                file_content = contents.pop(0)
                file_info = {'path': file_content.path, 'type': file_content.type, 'size': file_content.size if file_content.type == 'file' else None}
                file_tree.append(file_info)
                if file_content.type == "dir":
                    try: contents.extend(self.repo.get_contents(file_content.path))
                    except GithubException: pass
            self.extracted_data['file_tree'] = file_tree
            logger.info(f"File tree built: {len(file_tree)} items")
        except GithubException as e: logger.warning(f"Could not build file tree: {e}")

    def _extract_signatures_and_tests(self):
        if self.code_analysis_depth == 'surface':
            logger.info("Code extraction: Surface level (file tree only)")
            return
        if not self.code_analyzer:
            logger.warning("Code analyzer not available - skipping deep analysis")
            return
        logger.info(f"Extracting code signatures ({self.code_analysis_depth} analysis)...")
        languages = self.extracted_data.get('languages', {})
        if not languages:
            logger.warning("No languages detected - skipping code analysis")
            return
        primary_language = max(languages.items(), key=lambda x: x[1]['bytes'])[0]
        logger.info(f"Primary language: {primary_language}")
        extension_map = {'Python': ['.py'], 'JavaScript': ['.js', '.jsx'], 'TypeScript': ['.ts', '.tsx'], 'C': ['.c', '.h'], 'C++': ['.cpp', '.hpp', '.cc', '.hh', '.cxx']}
        extensions = extension_map.get(primary_language, [])
        if not extensions:
            logger.warning(f"No file extensions mapped for {primary_language}")
            return
        analyzed_files = []
        file_tree = self.extracted_data.get('file_tree', [])
        for file_info in file_tree:
            file_path = file_info['path']
            if not any(file_path.endswith(ext) for ext in extensions): continue
            if self.file_patterns:
                import fnmatch
                if not any(fnmatch.fnmatch(file_path, pattern) for pattern in self.file_patterns): continue
            try:
                file_content = self.repo.get_contents(file_path)
                content = file_content.decoded_content.decode('utf-8')
                analysis_result = self.code_analyzer.analyze_file(file_path, content, primary_language)
                if analysis_result and (analysis_result.get('classes') or analysis_result.get('functions')):
                    analyzed_files.append({'file': file_path, 'language': primary_language, **analysis_result})
            except Exception as e: logger.debug(f"Could not analyze {file_path}: {e}")
            if len(analyzed_files) >= 50:
                logger.info(f"Reached analysis limit (50 files)")
                break
        self.extracted_data['code_analysis'] = {'depth': self.code_analysis_depth, 'language': primary_language, 'files_analyzed': len(analyzed_files), 'files': analyzed_files}
        total_classes = sum(len(f.get('classes', [])) for f in analyzed_files)
        total_functions = sum(len(f.get('functions', [])) for f in analyzed_files)
        logger.info(f"Code analysis complete: {len(analyzed_files)} files, {total_classes} classes, {total_functions} functions")

    def _extract_issues(self):
        logger.info(f"Extracting GitHub Issues (max {self.max_issues})...")
        try:
            issues = self.repo.get_issues(state='all', sort='updated', direction='desc')
            issue_list = []
            for issue in issues[:self.max_issues]:
                if issue.pull_request: continue
                issue_data = {
                    'number': issue.number, 'title': issue.title, 'state': issue.state,
                    'labels': [label.name for label in issue.labels],
                    'milestone': issue.milestone.title if issue.milestone else None,
                    'created_at': issue.created_at.isoformat() if issue.created_at else None,
                    'updated_at': issue.updated_at.isoformat() if issue.updated_at else None,
                    'closed_at': issue.closed_at.isoformat() if issue.closed_at else None,
                    'url': issue.html_url,
                    'body': issue.body[:500] if issue.body else None
                }
                issue_list.append(issue_data)
            self.extracted_data['issues'] = issue_list
            logger.info(f"Extracted {len(issue_list)} issues")
        except GithubException as e: logger.warning(f"Could not fetch issues: {e}")

    def _extract_changelog(self):
        logger.info("Extracting CHANGELOG...")
        changelog_files = ['CHANGELOG.md', 'CHANGES.md', 'HISTORY.md', 'CHANGELOG.rst', 'CHANGELOG.txt', 'CHANGELOG', 'docs/CHANGELOG.md', '.github/CHANGELOG.md']
        for changelog_path in changelog_files:
            try:
                content = self.repo.get_contents(changelog_path)
                if content:
                    self.extracted_data['changelog'] = content.decoded_content.decode('utf-8')
                    logger.info(f"CHANGELOG found: {changelog_path}")
                    return
            except GithubException: continue
        logger.warning("No CHANGELOG found in repository")

    def _extract_releases(self):
        logger.info("Extracting GitHub Releases...")
        try:
            releases = self.repo.get_releases()
            release_list = []
            for release in releases:
                release_data = {
                    'tag_name': release.tag_name, 'name': release.title, 'body': release.body,
                    'draft': release.draft, 'prerelease': release.prerelease,
                    'created_at': release.created_at.isoformat() if release.created_at else None,
                    'published_at': release.published_at.isoformat() if release.published_at else None,
                    'url': release.html_url, 'tarball_url': release.tarball_url, 'zipball_url': release.zipball_url
                }
                release_list.append(release_data)
            self.extracted_data['releases'] = release_list
            logger.info(f"Extracted {len(release_list)} releases")
        except GithubException as e: logger.warning(f"Could not fetch releases: {e}")

    def _save_data(self):
        os.makedirs('output', exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.extracted_data, f, indent=2, ensure_ascii=False)
        logger.info(f"Data saved to: {self.data_file}")


# ... (Keep GitHubToSkillConverter class and main function)

class GitHubToSkillConverter:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.name = config.get('name', config['repo'].split('/')[-1])
        self.description = config.get('description', f'Skill for {config["repo"]}')
        self.data_file = f"output/{self.name}_github_data.json"
        self.skill_dir = f"output/{self.name}"
        self.data = self._load_data()

    def _load_data(self) -> Dict[str, Any]:
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Data file not found: {self.data_file}")
        with open(self.data_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def build_skill(self):
        logger.info(f"Building skill for: {self.name}")
        os.makedirs(self.skill_dir, exist_ok=True)
        os.makedirs(f"{self.skill_dir}/references", exist_ok=True)
        os.makedirs(f"{self.skill_dir}/scripts", exist_ok=True)
        os.makedirs(f"{self.skill_dir}/assets", exist_ok=True)
        self._generate_skill_md()
        self._generate_references()
        logger.info(f"✅ Skill built successfully: {self.skill_dir}/")

    def _generate_skill_md(self):
        repo_info = self.data.get('repo_info', {})
        skill_content = f"""# {repo_info.get('name', self.name)}

{self.description}

## Description

{repo_info.get('description', 'GitHub repository skill')}

**Repository:** [{repo_info.get('full_name', 'N/A')}]({repo_info.get('url', '#')})
**Language:** {repo_info.get('language', 'N/A')}
**Stars:** {repo_info.get('stars', 0):,}
**License:** {repo_info.get('license', 'N/A')}

## When to Use This Skill

Use this skill when you need to:
- Understand how to use {self.name}
- Look up API documentation
- Find usage examples
- Check for known issues or recent changes
- Review release history

## Quick Reference

### Repository Info
- **Homepage:** {repo_info.get('homepage', 'N/A')}
- **Topics:** {', '.join(repo_info.get('topics', []))}
- **Open Issues:** {repo_info.get('open_issues', 0)}
- **Last Updated:** {repo_info.get('updated_at', 'N/A')[:10]}

### Languages
{self._format_languages()}

### Recent Releases
{self._format_recent_releases()}

## Available References

- `references/README.md` - Complete README documentation
- `references/CHANGELOG.md` - Version history and changes
- `references/issues.md` - Recent GitHub issues
- `references/releases.md` - Release notes
- `references/file_structure.md` - Repository structure

## Usage

See README.md for complete usage instructions and examples.

---

**Generated by Skill Seeker** | GitHub Repository Scraper
"""
        skill_path = f"{self.skill_dir}/SKILL.md"
        with open(skill_path, 'w', encoding='utf-8') as f:
            f.write(skill_content)
        logger.info(f"Generated: {skill_path}")

    def _format_languages(self) -> str:
        languages = self.data.get('languages', {})
        if not languages: return "No language data available"
        lines = []
        for lang, info in sorted(languages.items(), key=lambda x: x[1]['bytes'], reverse=True):
            lines.append(f"- **{lang}:** {info['percentage']:.1f}%")
        return '\n'.join(lines)

    def _format_recent_releases(self) -> str:
        releases = self.data.get('releases', [])
        if not releases: return "No releases available"
        lines = []
        for release in releases[:3]:
            lines.append(f"- **{release['tag_name']}** ({release['published_at'][:10]}): {release['name']}")
        return '\n'.join(lines)

    def _generate_references(self):
        if self.data.get('readme'):
            readme_path = f"{self.skill_dir}/references/README.md"
            with open(readme_path, 'w', encoding='utf-8') as f: f.write(self.data['readme'])
            logger.info(f"Generated: {readme_path}")
        if self.data.get('changelog'):
            changelog_path = f"{self.skill_dir}/references/CHANGELOG.md"
            with open(changelog_path, 'w', encoding='utf-8') as f: f.write(self.data['changelog'])
            logger.info(f"Generated: {changelog_path}")
        if self.data.get('issues'): self._generate_issues_reference()
        if self.data.get('releases'): self._generate_releases_reference()
        if self.data.get('file_tree'): self._generate_file_structure_reference()

    def _generate_issues_reference(self):
        issues = self.data['issues']
        content = f"# GitHub Issues\n\nRecent issues from the repository ({len(issues)} total).\n\n"
        open_issues = [i for i in issues if i['state'] == 'open']
        closed_issues = [i for i in issues if i['state'] == 'closed']
        content += f"## Open Issues ({len(open_issues)})\n\n"
        for issue in open_issues[:20]:
            labels = ', '.join(issue['labels']) if issue['labels'] else 'No labels'
            content += f"### #{issue['number']}: {issue['title']}\n"
            content += f"**Labels:** {labels} | **Created:** {issue['created_at'][:10]}\n"
            content += f"[View on GitHub]({issue['url']})\n\n"
        content += f"\n## Recently Closed Issues ({len(closed_issues)})\n\n"
        for issue in closed_issues[:10]:
            labels = ', '.join(issue['labels']) if issue['labels'] else 'No labels'
            content += f"### #{issue['number']}: {issue['title']}\n"
            content += f"**Labels:** {labels} | **Closed:** {issue['closed_at'][:10]}\n"
            content += f"[View on GitHub]({issue['url']})\n\n"
        issues_path = f"{self.skill_dir}/references/issues.md"
        with open(issues_path, 'w', encoding='utf-8') as f: f.write(content)
        logger.info(f"Generated: {issues_path}")

    def _generate_releases_reference(self):
        releases = self.data['releases']
        content = f"# Releases\n\nVersion history for this repository ({len(releases)} releases).\n\n"
        for release in releases:
            content += f"## {release['tag_name']}: {release['name']}\n"
            content += f"**Published:** {release['published_at'][:10]}\n"
            if release['prerelease']: content += f"**Pre-release**\n"
            content += f"\n{release['body']}\n\n"
            content += f"[View on GitHub]({release['url']})\n\n---\n\n"
        releases_path = f"{self.skill_dir}/references/releases.md"
        with open(releases_path, 'w', encoding='utf-8') as f: f.write(content)
        logger.info(f"Generated: {releases_path}")

    def _generate_file_structure_reference(self):
        file_tree = self.data['file_tree']
        content = f"# Repository File Structure\n\n"
        content += f"Total items: {len(file_tree)}\n\n"
        content += "```\n"
        for item in file_tree:
            indent = "  " * item['path'].count('/')
            icon = "📁" if item['type'] == 'dir' else "📄"
            content += f"{indent}{icon} {os.path.basename(item['path'])}\n"
        content += "```\n"
        structure_path = f"{self.skill_dir}/references/file_structure.md"
        with open(structure_path, 'w', encoding='utf-8') as f: f.write(content)
        logger.info(f"Generated: {structure_path}")

def main():
    parser = argparse.ArgumentParser(
        description='GitHub Repository to Claude Skill Converter',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--repo', help='GitHub repository (owner/repo)')
    parser.add_argument('--config', help='Path to config JSON file')
    parser.add_argument('--token', help='GitHub personal access token')
    parser.add_argument('--name', help='Skill name (default: repo name)')
    parser.add_argument('--description', help='Skill description')
    parser.add_argument('--no-issues', action='store_true', help='Skip GitHub issues')
    parser.add_argument('--no-changelog', action='store_true', help='Skip CHANGELOG')
    parser.add_argument('--no-releases', action='store_true', help='Skip releases')
    parser.add_argument('--max-issues', type=int, default=100, help='Max issues to fetch')
    parser.add_argument('--scrape-only', action='store_true', help='Only scrape, don\'t build skill')
    args = parser.parse_args()
    if args.config:
        with open(args.config, 'r') as f: config = json.load(f)
    elif args.repo:
        config = {
            'repo': args.repo,
            'name': args.name or args.repo.split('/')[-1],
            'description': args.description or f'GitHub repository skill for {args.repo}',
            'github_token': args.token,
            'include_issues': not args.no_issues,
            'include_changelog': not args.no_changelog,
            'include_releases': not args.no_releases,
            'max_issues': args.max_issues
        }
    else: parser.error('Either --repo or --config is required')
    try:
        scraper = GitHubScraper(config)
        scraper.scrape()
        if args.scrape_only:
            logger.info("Scrape complete (--scrape-only mode)")
            return
        converter = GitHubToSkillConverter(config)
        converter.build_skill()
        logger.info(f"\n✅ Success! Skill created at: output/{config.get('name', config['repo'].split('/')[-1])}/")
        logger.info(f"Next step: python3 cli/package_skill.py output/{config.get('name', config['repo'].split('/')[-1])}/")
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
