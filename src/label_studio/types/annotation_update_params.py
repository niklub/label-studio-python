# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AnnotationUpdateParams"]


class AnnotationUpdateParams(TypedDict, total=False):
    completed_by: int

    draft_created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Draft creation time"""

    ground_truth: bool
    """This annotation is a Ground Truth (ground_truth)"""

    import_id: Optional[int]
    """
    Original annotation ID that was at the import step or NULL if this annotation
    wasn't imported
    """

    last_action: Optional[
        Literal[
            "prediction",
            "propagated_annotation",
            "imported",
            "submitted",
            "updated",
            "skipped",
            "accepted",
            "rejected",
            "fixed_and_accepted",
            "deleted_review",
        ]
    ]
    """Action which was performed in the last annotation history item"""

    last_created_by: Optional[int]
    """User who created the last annotation history item"""

    lead_time: Optional[float]
    """How much time it took to annotate the task"""

    parent_annotation: Optional[int]
    """Points to the parent annotation from which this annotation was created"""

    parent_prediction: Optional[int]
    """Points to the prediction from which this annotation was created"""

    project: Optional[int]
    """Project ID for this annotation"""

    result: Optional[object]
    """The main value of annotator work - labeling result in JSON format"""

    task: Optional[int]
    """Corresponding task for this annotation"""

    unique_id: str

    updated_by: Optional[int]
    """Last user who updated this annotation"""

    was_cancelled: bool
    """User skipped the task"""
