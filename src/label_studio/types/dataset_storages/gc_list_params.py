# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GcListParams"]


class GcListParams(TypedDict, total=False):
    dataset: int
    """Dataset ID"""

    ordering: str
    """Which field to use when ordering the results."""
