# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Comment"]


class Comment(BaseModel):
    id: Optional[int] = None

    annotation: Optional[int] = None

    created_at: Optional[datetime] = None
    """Creation time"""

    created_by: Optional[int] = None
    """User who made this comment"""

    draft: Optional[int] = None

    is_resolved: Optional[bool] = None
    """True if the comment is resolved"""

    project: Optional[int] = None

    resolved_at: Optional[datetime] = None
    """Resolving time"""

    task: Optional[int] = None

    text: Optional[str] = None
    """Reviewer or annotator comment"""

    updated_at: Optional[datetime] = None
    """Last updated time"""
