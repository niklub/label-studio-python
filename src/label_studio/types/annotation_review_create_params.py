# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AnnotationReviewCreateParams"]


class AnnotationReviewCreateParams(TypedDict, total=False):
    annotation: Required[int]
    """Corresponding annotation"""

    accepted: bool
    """Accepted or rejected (if false) flag"""

    comment: Optional[str]

    last_annotation_history: Optional[int]

    result: Optional[object]
