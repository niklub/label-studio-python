# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProjectUpdateParams", "CreatedBy"]


class ProjectUpdateParams(TypedDict, total=False):
    color: Optional[str]

    control_weights: Optional[object]
    """Dict of weights for each control tag in metric calculation.

    Each control tag (e.g. label or choice) will have it's own key in control weight
    dict with weight for each label and overall weight.For example, if bounding box
    annotation with control tag named my_bbox should be included with 0.33 weight in
    agreement calculation, and the first label Car should be twice more important
    than Airplaine, then you have to need the specify: {'my_bbox': {'type':
    'RectangleLabels', 'labels': {'Car': 1.0, 'Airplaine': 0.5}, 'overall': 0.33}
    """

    created_by: CreatedBy
    """User who created Dataset"""

    description: Optional[str]
    """Project description"""

    enable_empty_annotation: bool
    """Allow annotators to submit empty annotations"""

    evaluate_predictions_automatically: bool
    """Retrieve and display predictions when loading a task"""

    expert_instruction: Optional[str]
    """Labeling instructions in HTML format"""

    is_draft: bool
    """Whether or not the project is in the middle of being created"""

    is_published: bool
    """Whether or not the project is published to annotators"""

    label_config: Optional[str]
    """Label config in XML format. See more about it in documentation"""

    maximum_annotations: int
    """Maximum number of annotations for one task.

    If the number of annotations per task is equal or greater to this value, the
    task is completed (is_labeled=True)
    """

    min_annotations_to_start_training: int
    """Minimum number of completed tasks after which model training is started"""

    model_version: Optional[str]
    """Machine learning model version"""

    organization: Optional[int]

    overlap_cohort_percentage: int

    pinned_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Pinned date and time"""

    reveal_preannotations_interactively: bool
    """Reveal pre-annotations interactively"""

    sampling: Optional[Literal["Sequential sampling", "Uniform sampling", "Uncertainty sampling"]]

    show_annotation_history: bool
    """Show annotation history to annotator"""

    show_collab_predictions: bool
    """If set, the annotator can view model predictions"""

    show_ground_truth_first: bool

    show_instruction: bool
    """Show instructions to the annotator before they start"""

    show_overlap_first: bool

    show_skip_button: bool
    """Show a skip button in interface and allow annotators to skip the task"""

    skip_queue: Optional[Literal["REQUEUE_FOR_ME", "REQUEUE_FOR_OTHERS", "IGNORE_SKIPPED"]]

    task_data_login: Optional[str]
    """Task data credentials: login"""

    task_data_password: Optional[str]
    """Task data credentials: password"""

    title: Optional[str]
    """Project name. Must be between 3 and 50 characters long."""


class CreatedBy(TypedDict, total=False):
    email: str

    first_name: str

    last_name: str
