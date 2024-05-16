# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProjectListParams"]


class ProjectListParams(TypedDict, total=False):
    ids: str
    """ids"""

    ordering: str
    """Which field to use when ordering the results."""

    page: int
    """A page number within the paginated result set."""

    page_size: int
    """Number of results to return per page."""

    title: str
    """title"""

    workspaces: str
    """workspaces"""
