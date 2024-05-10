# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CommentCreateParams"]


class CommentCreateParams(TypedDict, total=False):
    annotation: Optional[int]

    draft: Optional[int]

    is_resolved: bool
    """True if the comment is resolved"""

    text: Optional[str]
    """Reviewer or annotator comment"""
