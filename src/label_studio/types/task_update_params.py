# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TaskUpdateParams"]


class TaskUpdateParams(TypedDict, total=False):
    data: Required[object]
    """User imported or uploaded data for a task.

    Data is formatted according to the project label config. You can find examples
    of data for your project on the Import page in the Label Studio Data Manager UI.
    """

    cancelled_annotations: int
    """Number of total cancelled annotations for the current task"""

    comment_authors: Iterable[int]
    """Users who wrote comments"""

    comment_count: int
    """Number of comments in the task including all annotations"""

    file_upload: Optional[int]
    """Uploaded file used as data source for this task"""

    inner_id: Optional[int]
    """Internal task ID in the project, starts with 1"""

    is_labeled: bool
    """
    True if the number of annotations for this task is greater than or equal to the
    number of maximum_completions for the project
    """

    last_comment_updated_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """When the last comment was updated"""

    meta: Optional[object]
    """
    Meta is user imported (uploaded) data and can be useful as input for an ML
    Backend for embeddings, advanced vectors, and other info. It is passed to ML
    during training/predicting steps.
    """

    overlap: int
    """Number of distinct annotators that processed the current task"""

    project: Optional[int]
    """Project ID for this task"""

    total_annotations: int
    """Number of total annotations for the current task except cancelled annotations"""

    total_predictions: int
    """Number of total predictions for the current task"""

    unresolved_comment_count: int
    """Number of unresolved comments in the task including all annotations"""

    updated_by: Optional[int]
    """Last annotator or reviewer who updated this task"""
