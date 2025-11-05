"""
Zettelkasten Tools MCP Server

This module implements a Model Context Protocol (MCP) server that provides all
file system operations for the Zettelkasten agent. It enforces the note taxonomy
through schema validation and handles all CRUD operations on the knowledge vault.

Architecture: This server acts as a "secure gatekeeper" between the LLM and the
file system, ensuring all operations conform to Zettelkasten principles.
"""

import asyncio
import json
import os
import re
import yaml
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Literal

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from schemas.note_schemas import (
    SourceNoteMetadata,
    ZettelNoteMetadata,
    MocNoteMetadata,
    Note,
    generate_note_id,
    generate_filename,
    NoteMetadata
)


# Configuration
VAULT_PATH = Path(__file__).parent / "vault"
INDEX_FILE = VAULT_PATH / "_INDEX.md"
LOG_FILE = VAULT_PATH / "_LOG.md"


class ZettelkastenToolsServer:
    """MCP Server implementation for Zettelkasten tools."""

    def __init__(self):
        self.server = Server("zettelkasten-tools")
        self._setup_tools()

    def _setup_tools(self):
        """Register all tools with the MCP server."""

        @self.server.list_tools()
        async def list_tools() -> List[Tool]:
            """Return the list of available tools."""
            return [
                Tool(
                    name="create_note",
                    description=(
                        "Creates a new note file (.md) in the Zettelkasten vault. "
                        "Use this for all note creation (SRC, ZTL, or MOC). "
                        "The function handles correct filename conventions and YAML "
                        "metadata based on note_type."
                    ),
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "note_type": {
                                "type": "string",
                                "enum": ["SRC", "ZTL", "MOC"],
                                "description": "Type of note to create"
                            },
                            "content": {
                                "type": "string",
                                "description": "The body content of the note"
                            },
                            "title": {
                                "type": "string",
                                "description": "Required for ZTL notes"
                            },
                            "tags": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "Optional list of tags"
                            },
                            "links": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "Optional list of note IDs to link"
                            },
                            "source_uri": {
                                "type": "string",
                                "description": "Required for SRC notes"
                            },
                            "topic": {
                                "type": "string",
                                "description": "Required for MOC notes"
                            }
                        },
                        "required": ["note_type", "content"]
                    }
                ),
                Tool(
                    name="read_note_content",
                    description=(
                        "Reads and returns the full content (body and YAML) "
                        "of a single specified note file."
                    ),
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "file_path": {
                                "type": "string",
                                "description": "Path to the note file to read"
                            }
                        },
                        "required": ["file_path"]
                    }
                ),
                Tool(
                    name="get_note_metadata",
                    description=(
                        "A low-cost tool to read and return only the YAML frontmatter "
                        "of a note. Use this for quick analysis without loading the "
                        "full note content."
                    ),
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "file_path": {
                                "type": "string",
                                "description": "Path to the note file"
                            }
                        },
                        "required": ["file_path"]
                    }
                ),
                Tool(
                    name="append_link",
                    description=(
                        "Adds a contextual link from a source note to a target note. "
                        "This automatically creates a reciprocal backlink in the target note. "
                        "Use for all linking operations."
                    ),
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "source_note_path": {
                                "type": "string",
                                "description": "Path to the source note"
                            },
                            "target_note_path": {
                                "type": "string",
                                "description": "Path to the target note"
                            },
                            "context_sentence": {
                                "type": "string",
                                "description": "Sentence explaining the link's context"
                            }
                        },
                        "required": ["source_note_path", "target_note_path", "context_sentence"]
                    }
                ),
                Tool(
                    name="find_notes",
                    description=(
                        "Searches the knowledge base for notes relevant to a query. "
                        "Can perform keyword or semantic search."
                    ),
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Search query"
                            },
                            "search_type": {
                                "type": "string",
                                "enum": ["keyword", "semantic"],
                                "default": "keyword",
                                "description": "Type of search to perform"
                            }
                        },
                        "required": ["query"]
                    }
                ),
                Tool(
                    name="list_files",
                    description=(
                        "Lists all files in the vault, optionally filtered by note type "
                        "(SRC, ZTL, MOC). Useful for getting an overview or finding "
                        "unprocessed notes."
                    ),
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "note_type": {
                                "type": "string",
                                "enum": ["all", "SRC", "ZTL", "MOC"],
                                "default": "all",
                                "description": "Filter by note type"
                            }
                        }
                    }
                ),
                Tool(
                    name="log_action",
                    description=(
                        "Appends a timestamped entry to the _LOG.md file. "
                        "Use this to record completed actions, decisions, or "
                        "identified knowledge gaps."
                    ),
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "message": {
                                "type": "string",
                                "description": "Log message to append"
                            }
                        },
                        "required": ["message"]
                    }
                )
            ]

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
            """Handle tool invocations."""

            if name == "create_note":
                return await self._create_note(**arguments)
            elif name == "read_note_content":
                return await self._read_note_content(**arguments)
            elif name == "get_note_metadata":
                return await self._get_note_metadata(**arguments)
            elif name == "append_link":
                return await self._append_link(**arguments)
            elif name == "find_notes":
                return await self._find_notes(**arguments)
            elif name == "list_files":
                return await self._list_files(**arguments)
            elif name == "log_action":
                return await self._log_action(**arguments)
            else:
                raise ValueError(f"Unknown tool: {name}")

    async def _create_note(
        self,
        note_type: Literal["SRC", "ZTL", "MOC"],
        content: str,
        title: Optional[str] = None,
        tags: Optional[List[str]] = None,
        links: Optional[List[str]] = None,
        source_uri: Optional[str] = None,
        topic: Optional[str] = None
    ) -> List[TextContent]:
        """Create a new note with proper metadata and filename."""

        try:
            # Ensure vault directory exists
            VAULT_PATH.mkdir(parents=True, exist_ok=True)

            # Generate note ID
            note_id = generate_note_id(note_type, topic)
            created = datetime.now().isoformat()

            # Build metadata based on note type
            metadata: NoteMetadata
            if note_type == "SRC":
                if not source_uri:
                    raise ValueError("source_uri is required for SRC notes")
                metadata = SourceNoteMetadata(
                    id=note_id,
                    created=created,
                    source_uri=source_uri,
                    tags=tags or [],
                    links=links or []
                )
            elif note_type == "ZTL":
                if not title:
                    raise ValueError("title is required for ZTL notes")
                metadata = ZettelNoteMetadata(
                    id=note_id,
                    created=created,
                    title=title,
                    tags=tags or [],
                    links=links or []
                )
            elif note_type == "MOC":
                if not topic:
                    raise ValueError("topic is required for MOC notes")
                metadata = MocNoteMetadata(
                    id=note_id,
                    created=created,
                    topic=topic,
                    tags=tags or [],
                    links=links or []
                )
            else:
                raise ValueError(f"Invalid note_type: {note_type}")

            # Validate the complete note
            note = Note(metadata=metadata, content=content)

            # Generate filename and full path
            filename = generate_filename(note_id)
            file_path = VAULT_PATH / filename

            # Format the note content with YAML frontmatter
            yaml_metadata = yaml.dump(
                metadata.model_dump(exclude_none=True),
                default_flow_style=False,
                sort_keys=False
            )
            full_content = f"---\n{yaml_metadata}---\n\n{content}\n"

            # Write to file
            file_path.write_text(full_content, encoding='utf-8')

            result = {
                "status": "success",
                "file_path": str(file_path),
                "note_id": note_id
            }

            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]

        except Exception as e:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "status": "error",
                    "error": str(e)
                }, indent=2)
            )]

    async def _read_note_content(self, file_path: str) -> List[TextContent]:
        """Read and return the full content of a note."""

        try:
            path = Path(file_path)
            if not path.exists():
                raise FileNotFoundError(f"Note not found: {file_path}")

            content = path.read_text(encoding='utf-8')

            return [TextContent(
                type="text",
                text=json.dumps({
                    "status": "success",
                    "content": content
                }, indent=2)
            )]

        except Exception as e:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "status": "error",
                    "error": str(e)
                }, indent=2)
            )]

    async def _get_note_metadata(self, file_path: str) -> List[TextContent]:
        """Extract and return only the YAML frontmatter from a note."""

        try:
            path = Path(file_path)
            if not path.exists():
                raise FileNotFoundError(f"Note not found: {file_path}")

            content = path.read_text(encoding='utf-8')

            # Extract YAML frontmatter
            match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not match:
                raise ValueError("No YAML frontmatter found")

            yaml_content = match.group(1)
            metadata = yaml.safe_load(yaml_content)

            return [TextContent(
                type="text",
                text=json.dumps({
                    "status": "success",
                    "metadata": metadata
                }, indent=2)
            )]

        except Exception as e:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "status": "error",
                    "error": str(e)
                }, indent=2)
            )]

    async def _append_link(
        self,
        source_note_path: str,
        target_note_path: str,
        context_sentence: str
    ) -> List[TextContent]:
        """Add a contextual link and create reciprocal backlink."""

        try:
            source_path = Path(source_note_path)
            target_path = Path(target_note_path)

            if not source_path.exists():
                raise FileNotFoundError(f"Source note not found: {source_note_path}")
            if not target_path.exists():
                raise FileNotFoundError(f"Target note not found: {target_note_path}")

            # Get note IDs from filenames
            source_id = source_path.stem
            target_id = target_path.stem

            # Append link to source note
            source_content = source_path.read_text(encoding='utf-8')
            link_line = f"\n- {context_sentence} → [{target_id}]({target_path.name})\n"
            source_path.write_text(source_content + link_line, encoding='utf-8')

            # Create reciprocal backlink in target note
            target_content = target_path.read_text(encoding='utf-8')
            backlink_section = "\n## Backlinks\n\n" if "## Backlinks" not in target_content else ""
            backlink_line = f"- Referenced by [{source_id}]({source_path.name})\n"
            target_path.write_text(target_content + backlink_section + backlink_line, encoding='utf-8')

            return [TextContent(
                type="text",
                text=json.dumps({
                    "status": "success",
                    "source_updated": True,
                    "target_updated": True
                }, indent=2)
            )]

        except Exception as e:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "status": "error",
                    "error": str(e)
                }, indent=2)
            )]

    async def _find_notes(
        self,
        query: str,
        search_type: str = "keyword"
    ) -> List[TextContent]:
        """Search for notes matching a query."""

        try:
            if not VAULT_PATH.exists():
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "status": "success",
                        "results": []
                    }, indent=2)
                )]

            results = []
            query_lower = query.lower()

            # Simple keyword search for MVP
            for note_file in VAULT_PATH.glob("*.md"):
                if note_file.name.startswith("_"):
                    continue

                content = note_file.read_text(encoding='utf-8')

                # Search in content
                if query_lower in content.lower():
                    # Extract title from metadata if available
                    match = re.search(r'title:\s*(.+)', content)
                    title = match.group(1).strip() if match else note_file.stem

                    # Simple scoring based on frequency
                    score = content.lower().count(query_lower) / len(content)

                    results.append({
                        "file_path": str(note_file),
                        "title": title,
                        "score": score
                    })

            # Sort by score descending
            results.sort(key=lambda x: x["score"], reverse=True)

            return [TextContent(
                type="text",
                text=json.dumps({
                    "status": "success",
                    "results": results
                }, indent=2)
            )]

        except Exception as e:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "status": "error",
                    "error": str(e)
                }, indent=2)
            )]

    async def _list_files(self, note_type: str = "all") -> List[TextContent]:
        """List all files in the vault, optionally filtered by type."""

        try:
            if not VAULT_PATH.exists():
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "status": "success",
                        "files": []
                    }, indent=2)
                )]

            files = []

            for note_file in VAULT_PATH.glob("*.md"):
                # Skip special files unless requested
                if note_file.name.startswith("_") and note_type != "all":
                    continue

                # Filter by type if specified
                if note_type != "all":
                    if not note_file.stem.startswith(note_type):
                        continue

                files.append(str(note_file))

            files.sort()

            return [TextContent(
                type="text",
                text=json.dumps({
                    "status": "success",
                    "files": files,
                    "count": len(files)
                }, indent=2)
            )]

        except Exception as e:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "status": "error",
                    "error": str(e)
                }, indent=2)
            )]

    async def _log_action(self, message: str) -> List[TextContent]:
        """Append a timestamped entry to the _LOG.md file."""

        try:
            # Ensure vault exists
            VAULT_PATH.mkdir(parents=True, exist_ok=True)

            # Create log file if it doesn't exist
            if not LOG_FILE.exists():
                LOG_FILE.write_text("# Agent Action Log\n\n", encoding='utf-8')

            # Append log entry
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"**{timestamp}**: {message}\n\n"

            with LOG_FILE.open('a', encoding='utf-8') as f:
                f.write(log_entry)

            return [TextContent(
                type="text",
                text=json.dumps({
                    "status": "success",
                    "logged": True
                }, indent=2)
            )]

        except Exception as e:
            return [TextContent(
                type="text",
                text=json.dumps({
                    "status": "error",
                    "error": str(e)
                }, indent=2)
            )]

    async def run(self):
        """Run the MCP server."""
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options()
            )


def main():
    """Entry point for the MCP server."""
    server = ZettelkastenToolsServer()
    asyncio.run(server.run())


if __name__ == "__main__":
    main()
