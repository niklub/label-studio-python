# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["TaskListResponse", "Result"]


class Result(BaseModel):
    data: object
    """User imported or uploaded data for a task.

    Data is formatted according to the project label config. You can find examples
    of data for your project on the Import page in the Label Studio Data Manager UI.
    """

    id: Optional[int] = None

    agreement: Optional[str] = None

    cancelled_annotations: Optional[int] = None
    """Number of total cancelled annotations for the current task"""

    comment_authors: Optional[List[int]] = None
    """Users who wrote comments"""

    comment_count: Optional[int] = None
    """Number of comments in the task including all annotations"""

    created_at: Optional[datetime] = None
    """Time a task was created"""

    file_upload: Optional[int] = None
    """Uploaded file used as data source for this task"""

    inner_id: Optional[int] = None
    """Internal task ID in the project, starts with 1"""

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

    project: Optional[int] = None
    """Project ID for this task"""

    total_annotations: Optional[int] = None
    """Number of total annotations for the current task except cancelled annotations"""

    total_predictions: Optional[int] = None
    """Number of total predictions for the current task"""

    unresolved_comment_count: Optional[int] = None
    """Number of unresolved comments in the task including all annotations"""

    updated_at: Optional[datetime] = None
    """Last time a task was updated"""

    updated_by: Optional[int] = None
    """Last annotator or reviewer who updated this task"""


class TaskListResponse(BaseModel):
    count: int

    results: List[Result]

    next: Optional[str] = None

    previous: Optional[str] = None
