# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AnnotationReview"]


class AnnotationReview(BaseModel):
    annotation: int
    """Corresponding annotation"""

    id: Optional[int] = None

    accepted: Optional[bool] = None
    """Accepted or rejected (if false) flag"""

    comment: Optional[str] = None

    created_at: Optional[datetime] = None
    """Creation time"""

    created_by: Optional[int] = None
    """User who made this review"""

    fixed_annotation_history: Optional[int] = None
    """Fixed annotation history item by the reviewer"""

    last_annotation_history: Optional[int] = None

    previous_annotation_history: Optional[int] = None
    """Previous annotation history item by the annotator"""

    result: Optional[object] = None
