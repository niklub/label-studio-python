# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .annotation import Annotation

__all__ = ["TaskGetResponse"]


class TaskGetResponse(BaseModel):
    data: object
    """User imported or uploaded data for a task.

    Data is formatted according to the project label config. You can find examples
    of data for your project on the Import page in the Label Studio Data Manager UI.
    """

    id: Optional[int] = None

    agreement: Optional[str] = None

    annotations: Optional[List[Annotation]] = None

    annotations_ids: Optional[str] = None

    annotations_results: Optional[str] = None

    annotators: Optional[str] = None

    avg_lead_time: Optional[float] = None

    cancelled_annotations: Optional[int] = None

    comment_authors: Optional[List[int]] = None
    """Users who wrote comments"""

    comment_count: Optional[int] = None
    """Number of comments in the task including all annotations"""

    completed_at: Optional[datetime] = None

    created_at: Optional[datetime] = None
    """Time a task was created"""

    draft_exists: Optional[bool] = None

    drafts: Optional[str] = None

    file_upload: Optional[str] = None

    inner_id: Optional[int] = None

    is_labeled: Optional[bool] = None
    """
    True if the number of annotations for this task is greater than or equal to the
    number of maximum_completions for the project
    """

    last_comment_updated_at: Optional[datetime] = None
    """When the last comment was updated"""

    meta: Optional[object] = None
    """
    Meta is user imported (uploaded) data and can be useful as input for an ML
    Backend for embeddings, advanced vectors, and other info. It is passed to ML
    during training/predicting steps.
    """

    overlap: Optional[int] = None
    """Number of distinct annotators that processed the current task"""

    predictions: Optional[str] = None

    predictions_model_versions: Optional[str] = None

    predictions_results: Optional[str] = None

    predictions_score: Optional[float] = None

    project: Optional[int] = None
    """Project ID for this task"""

    storage_filename: Optional[str] = None

    total_annotations: Optional[int] = None

    total_predictions: Optional[int] = None

    unresolved_comment_count: Optional[int] = None
    """Number of unresolved comments in the task including all annotations"""

    updated_at: Optional[datetime] = None
    """Last time a task was updated"""

    updated_by: Optional[str] = None
