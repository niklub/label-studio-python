# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ColumnListParams"]


class ColumnListParams(TypedDict, total=False):
    ordering: str
    """Which field to use when ordering the results."""
