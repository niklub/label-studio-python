# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectGetResponse", "AssignmentSettings", "Member", "ReviewSettings", "CreatedBy"]


class AssignmentSettings(BaseModel):
    id: Optional[int] = None

    label_stream_task_distribution: Optional[Literal["auto_distribution", "assigned_only"]] = None
    """Modes for distributing tasks to annotators"""

    project: Optional[int] = None


class Member(BaseModel):
    user: Optional[str] = None


class ReviewSettings(BaseModel):
    id: Optional[int] = None

    anonymize_annotations: Optional[bool] = None
    """Hide annotator names from annotations while review"""

    instruction: Optional[str] = None
    """Reviewer instructions in HTML format"""

    only_finished_tasks: Optional[bool] = None
    """Show only finished tasks in the review stream"""

    project: Optional[int] = None

    requeue_rejected_tasks_to_annotator: Optional[bool] = None
    """If set, the rejected task is requeued to the annotator"""

    require_comment_on_reject: Optional[bool] = None
    """If set, the reviewer must leave a comment on reject"""

    review_criteria: Optional[Literal["all", "one"]] = None
    """Criteria to mark task as reviewed"""

    review_only_manual_assignments: Optional[bool] = None
    """When set True, review queue is built only from manually assigned tasks"""

    show_agreement_to_reviewers: Optional[bool] = None
    """Show the agreement column to reviewers"""

    show_data_manager_to_reviewers: Optional[bool] = None
    """Show the data manager to reviewers"""

    show_instruction: Optional[bool] = None
    """Show instructions to the reviewers before they start"""


class CreatedBy(BaseModel):
    id: Optional[int] = None

    avatar: Optional[str] = None

    email: Optional[str] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None


class ProjectGetResponse(BaseModel):
    assignment_settings: AssignmentSettings

    members: List[Member]

    review_settings: ReviewSettings

    id: Optional[int] = None

    color: Optional[str] = None

    config_has_control_tags: Optional[str] = None
    """Flag to detect is project ready for labeling"""

    control_weights: Optional[object] = None
    """Dict of weights for each control tag in metric calculation.

    Each control tag (e.g. label or choice) will have it's own key in control weight
    dict with weight for each label and overall weight.For example, if bounding box
    annotation with control tag named my_bbox should be included with 0.33 weight in
    agreement calculation, and the first label Car should be twice more important
    than Airplaine, then you have to need the specify: {'my_bbox': {'type':
    'RectangleLabels', 'labels': {'Car': 1.0, 'Airplaine': 0.5}, 'overall': 0.33}
    """

    created_at: Optional[datetime] = None

    created_by: Optional[CreatedBy] = None
    """User who created Dataset"""

    data_types: Optional[object] = None

    description: Optional[str] = None
    """Project description"""

    duplication_done: Optional[bool] = None

    enable_empty_annotation: Optional[bool] = None
    """Allow annotators to submit empty annotations"""

    evaluate_predictions_automatically: Optional[bool] = None
    """Retrieve and display predictions when loading a task"""

    expert_instruction: Optional[str] = None
    """Labeling instructions in HTML format"""

    finished_task_number: Optional[int] = None
    """Finished tasks"""

    ground_truth_number: Optional[int] = None
    """Honeypot annotation number in project"""

    is_draft: Optional[bool] = None
    """Whether or not the project is in the middle of being created"""

    is_published: Optional[bool] = None
    """Whether or not the project is published to annotators"""

    label_config: Optional[str] = None
    """Label config in XML format. See more about it in documentation"""

    maximum_annotations: Optional[int] = None
    """Maximum number of annotations for one task.

    If the number of annotations per task is equal or greater to this value, the
    task is completed (is_labeled=True)
    """

    min_annotations_to_start_training: Optional[int] = None
    """Minimum number of completed tasks after which model training is started"""

    api_model_version: Optional[str] = FieldInfo(alias="model_version", default=None)
    """Machine learning model version"""

    num_tasks_with_annotations: Optional[int] = None
    """Tasks with annotations count"""

    organization: Optional[int] = None

    overlap_cohort_percentage: Optional[int] = None

    parsed_label_config: Optional[str] = None
    """JSON-formatted labeling configuration"""

    pinned_at: Optional[datetime] = None
    """Pinned date and time"""

    queue_done: Optional[str] = None

    queue_left: Optional[str] = None

    queue_total: Optional[str] = None

    require_comment_on_skip: Optional[bool] = None

    reveal_preannotations_interactively: Optional[bool] = None
    """Reveal pre-annotations interactively"""

    reviewer_queue_total: Optional[str] = None

    sampling: Optional[Literal["Sequential sampling", "Uniform sampling", "Uncertainty sampling"]] = None

    show_annotation_history: Optional[bool] = None
    """Show annotation history to annotator"""

    show_collab_predictions: Optional[bool] = None
    """If set, the annotator can view model predictions"""

    show_ground_truth_first: Optional[bool] = None

    show_instruction: Optional[bool] = None
    """Show instructions to the annotator before they start"""

    show_overlap_first: Optional[bool] = None

    show_skip_button: Optional[bool] = None
    """Show a skip button in interface and allow annotators to skip the task"""

    skip_queue: Optional[Literal["REQUEUE_FOR_ME", "REQUEUE_FOR_OTHERS", "IGNORE_SKIPPED"]] = None

    skipped_annotations_number: Optional[int] = None
    """Skipped by collaborators annotation number in project"""

    start_training_on_annotation_update: Optional[str] = None
    """Start model training after any annotations are submitted or updated"""

    task_data_login: Optional[str] = None
    """Task data credentials: login"""

    task_data_password: Optional[str] = None
    """Task data credentials: password"""

    task_number: Optional[int] = None
    """Total task number in project"""

    title: Optional[str] = None
    """Project name. Must be between 3 and 50 characters long."""

    total_annotations_number: Optional[int] = None
    """
    Total annotations number in project including skipped_annotations_number and
    ground_truth_number.
    """

    total_predictions_number: Optional[int] = None
    """
    Total predictions number in project including skipped_annotations_number,
    ground_truth_number, and useful_annotation_number.
    """

    useful_annotation_number: Optional[int] = None
    """
    Useful annotation number in project not including skipped_annotations_number and
    ground_truth_number. Total annotations = annotation_number +
    skipped_annotations_number + ground_truth_number
    """

    workspace: Optional[str] = None
