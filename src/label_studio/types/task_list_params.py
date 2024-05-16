# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    page: int
    """A page number within the paginated result set."""

    page_size: int
    """Number of results to return per page."""

    project: int
    """Project ID"""

    resolve_uri: bool
    """Resolve task data URIs using Cloud Storage"""

    view: int
    """View ID"""
