# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AnnotationReviewListParams"]


class AnnotationReviewListParams(TypedDict, total=False):
    annotation: str
    """annotation"""

    annotation_task_project: Annotated[str, PropertyInfo(alias="annotation__task__project")]
    """annotation**task**project"""

    ordering: str
    """Which field to use when ordering the results."""
