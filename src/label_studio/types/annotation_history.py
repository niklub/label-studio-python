# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AnnotationHistory"]


class AnnotationHistory(BaseModel):
    id: Optional[int] = None

    action: Optional[
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

    annotation_id: Optional[int] = None
    """Corresponding annotation for this historical annotation"""

    comment: Optional[str] = None

    comment_id: Optional[int] = None
    """Comment id sent with result"""

    created_at: Optional[datetime] = None

    created_by: Optional[int] = None
    """Created by user id"""

    draft_id: Optional[int] = None
    """Corresponding draft for this historical annotation"""

    organization_id: Optional[int] = None
    """Organization for this annotation history"""

    project_id: Optional[int] = None
    """Project for this annotation history"""

    result: Optional[object] = None
    """Labeling result"""

    review_id: Optional[int] = None
    """AnnotationReview ID, using with review field"""

    task_id: Optional[int] = None
    """Task id"""
