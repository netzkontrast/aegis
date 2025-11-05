"""
Pydantic schemas for Zettelkasten note validation.

This module implements the note taxonomy from Section 2.3 of the architectural blueprint.
It enforces structural integrity through programmatic validation, ensuring that:
- Source notes (SRC) contain required source_uri metadata
- Atomic notes (ZTL) contain required id and title
- Maps of Content (MOC) contain required topic
"""

from datetime import datetime
from typing import List, Optional, Literal
from pydantic import BaseModel, Field, field_validator


class BaseNoteMetadata(BaseModel):
    """Base metadata common to all note types."""

    id: str = Field(description="Unique identifier for the note")
    created: str = Field(description="ISO timestamp of creation")
    tags: List[str] = Field(default_factory=list, description="List of tags")
    links: List[str] = Field(default_factory=list, description="List of linked note IDs")


class SourceNoteMetadata(BaseNoteMetadata):
    """Metadata schema for Source Notes (SRC).

    Source notes represent raw, unprocessed information from external sources.
    They MUST include a source_uri and status field.
    """

    note_type: Literal["SRC"] = "SRC"
    source_uri: str = Field(description="URI or reference to the original source")
    status: Literal["unprocessed", "processing", "processed"] = Field(
        default="unprocessed",
        description="Processing status of the source"
    )
    author: Optional[str] = Field(default=None, description="Author of the source material")
    date_published: Optional[str] = Field(default=None, description="Publication date")


class ZettelNoteMetadata(BaseNoteMetadata):
    """Metadata schema for Atomic Notes (Zettel/ZTL).

    Zettel notes are atomic, self-contained ideas.
    They MUST include a title and should link to their sources.
    """

    note_type: Literal["ZTL"] = "ZTL"
    title: str = Field(description="Declarative title of the atomic idea")
    source_notes: List[str] = Field(
        default_factory=list,
        description="List of source note IDs this Zettel was derived from"
    )


class MocNoteMetadata(BaseNoteMetadata):
    """Metadata schema for Maps of Content (MOC).

    MOCs organize and provide structure to collections of related notes.
    They MUST include a topic and description.
    """

    note_type: Literal["MOC"] = "MOC"
    topic: str = Field(description="The main topic this MOC organizes")
    description: Optional[str] = Field(
        default=None,
        description="Brief description of what this MOC contains"
    )
    last_tended: Optional[str] = Field(
        default=None,
        description="ISO date of last maintenance by MOC_Tender agent"
    )


class Note(BaseModel):
    """Complete note model including metadata and content."""

    metadata: SourceNoteMetadata | ZettelNoteMetadata | MocNoteMetadata
    content: str = Field(description="The body content of the note in Markdown")

    @field_validator('content')
    @classmethod
    def content_not_empty(cls, v: str) -> str:
        """Ensure note content is not empty."""
        if not v or v.strip() == "":
            raise ValueError("Note content cannot be empty")
        return v


def generate_note_id(note_type: Literal["SRC", "ZTL", "MOC"], topic: Optional[str] = None) -> str:
    """
    Generate a unique note ID following the naming conventions.

    - SRC notes: SRC-<YYYYMMDDHHMMSS>
    - ZTL notes: ZTL-<YYYYMMDDHHMMSS>
    - MOC notes: MOC-<Topic>

    Args:
        note_type: The type of note (SRC, ZTL, or MOC)
        topic: Required for MOC notes, the topic name

    Returns:
        A properly formatted note ID

    Raises:
        ValueError: If topic is not provided for MOC notes
    """
    if note_type == "MOC":
        if not topic:
            raise ValueError("topic is required for MOC note IDs")
        # Sanitize topic for filename (replace spaces with underscores, remove special chars)
        sanitized_topic = "".join(c if c.isalnum() or c in ('-', '_') else '_' for c in topic)
        return f"MOC-{sanitized_topic}"
    else:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{note_type}-{timestamp}"


def generate_filename(note_id: str) -> str:
    """
    Generate the filename for a note based on its ID.

    Args:
        note_id: The note's unique identifier

    Returns:
        Filename with .md extension
    """
    return f"{note_id}.md"


# Type alias for convenience
NoteMetadata = SourceNoteMetadata | ZettelNoteMetadata | MocNoteMetadata
