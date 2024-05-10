# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Annotation"]


class Annotation(BaseModel):
    id: Optional[int] = None

    completed_by: Optional[int] = None

    created_ago: Optional[str] = None
    """Time delta from creation time"""

    created_at: Optional[datetime] = None
    """Creation time"""

    created_username: Optional[str] = None
    """Username string"""

    draft_created_at: Optional[datetime] = None
    """Draft creation time"""

    ground_truth: Optional[bool] = None
    """This annotation is a Ground Truth (ground_truth)"""

    import_id: Optional[int] = None
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
    ] = None
    """Action which was performed in the last annotation history item"""

    last_created_by: Optional[int] = None
    """User who created the last annotation history item"""

    lead_time: Optional[float] = None
    """How much time it took to annotate the task"""

    parent_annotation: Optional[int] = None
    """Points to the parent annotation from which this annotation was created"""

    parent_prediction: Optional[int] = None
    """Points to the prediction from which this annotation was created"""

    project: Optional[int] = None
    """Project ID for this annotation"""

    result: Optional[object] = None
    """The main value of annotator work - labeling result in JSON format"""

    task: Optional[int] = None
    """Corresponding task for this annotation"""

    unique_id: Optional[str] = None

    updated_at: Optional[datetime] = None
    """Last updated time"""

    updated_by: Optional[int] = None
    """Last user who updated this annotation"""

    was_cancelled: Optional[bool] = None
    """User skipped the task"""
