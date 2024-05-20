# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import project_list_params, project_create_params, project_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncLsOffsetPage, AsyncLsOffsetPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ..types.project_get_response import ProjectGetResponse
from ..types.project_list_response import ProjectListResponse
from ..types.project_create_response import ProjectCreateResponse
from ..types.project_update_response import ProjectUpdateResponse

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        color: Optional[str] | NotGiven = NOT_GIVEN,
        control_weights: Optional[object] | NotGiven = NOT_GIVEN,
        created_by: project_create_params.CreatedBy | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enable_empty_annotation: bool | NotGiven = NOT_GIVEN,
        evaluate_predictions_automatically: bool | NotGiven = NOT_GIVEN,
        expert_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        is_draft: bool | NotGiven = NOT_GIVEN,
        is_published: bool | NotGiven = NOT_GIVEN,
        label_config: Optional[str] | NotGiven = NOT_GIVEN,
        maximum_annotations: int | NotGiven = NOT_GIVEN,
        min_annotations_to_start_training: int | NotGiven = NOT_GIVEN,
        model_version: Optional[str] | NotGiven = NOT_GIVEN,
        organization: Optional[int] | NotGiven = NOT_GIVEN,
        overlap_cohort_percentage: int | NotGiven = NOT_GIVEN,
        pinned_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        reveal_preannotations_interactively: bool | NotGiven = NOT_GIVEN,
        sampling: Optional[Literal["Sequential sampling", "Uniform sampling", "Uncertainty sampling"]]
        | NotGiven = NOT_GIVEN,
        show_annotation_history: bool | NotGiven = NOT_GIVEN,
        show_collab_predictions: bool | NotGiven = NOT_GIVEN,
        show_ground_truth_first: bool | NotGiven = NOT_GIVEN,
        show_instruction: bool | NotGiven = NOT_GIVEN,
        show_overlap_first: bool | NotGiven = NOT_GIVEN,
        show_skip_button: bool | NotGiven = NOT_GIVEN,
        skip_queue: Optional[Literal["REQUEUE_FOR_ME", "REQUEUE_FOR_OTHERS", "IGNORE_SKIPPED"]] | NotGiven = NOT_GIVEN,
        task_data_login: Optional[str] | NotGiven = NOT_GIVEN,
        task_data_password: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        workspace: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectCreateResponse:
        """
        Create a project and set up the labeling interface in Label Studio using the
        API.

        ```bash
        curl -H Content-Type:application/json -H 'Authorization: Token abc123' -X POST 'https://app.heartex.com/api/projects'     --data '{"label_config": "<View>[...]</View>"}'
        ```

        Args:
          control_weights: Dict of weights for each control tag in metric calculation. Each control tag
              (e.g. label or choice) will have it's own key in control weight dict with weight
              for each label and overall weight.For example, if bounding box annotation with
              control tag named my_bbox should be included with 0.33 weight in agreement
              calculation, and the first label Car should be twice more important than
              Airplaine, then you have to need the specify: {'my_bbox': {'type':
              'RectangleLabels', 'labels': {'Car': 1.0, 'Airplaine': 0.5}, 'overall': 0.33}

          created_by: User who created Dataset

          description: Project description

          enable_empty_annotation: Allow annotators to submit empty annotations

          evaluate_predictions_automatically: Retrieve and display predictions when loading a task

          expert_instruction: Labeling instructions in HTML format

          is_draft: Whether or not the project is in the middle of being created

          is_published: Whether or not the project is published to annotators

          label_config: Label config in XML format. See more about it in documentation

          maximum_annotations: Maximum number of annotations for one task. If the number of annotations per
              task is equal or greater to this value, the task is completed (is_labeled=True)

          min_annotations_to_start_training: Minimum number of completed tasks after which model training is started

          model_version: Machine learning model version

          pinned_at: Pinned date and time

          reveal_preannotations_interactively: Reveal pre-annotations interactively

          show_annotation_history: Show annotation history to annotator

          show_collab_predictions: If set, the annotator can view model predictions

          show_instruction: Show instructions to the annotator before they start

          show_skip_button: Show a skip button in interface and allow annotators to skip the task

          task_data_login: Task data credentials: login

          task_data_password: Task data credentials: password

          title: Project name. Must be between 3 and 50 characters long.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/projects/",
            body=maybe_transform(
                {
                    "color": color,
                    "control_weights": control_weights,
                    "created_by": created_by,
                    "description": description,
                    "enable_empty_annotation": enable_empty_annotation,
                    "evaluate_predictions_automatically": evaluate_predictions_automatically,
                    "expert_instruction": expert_instruction,
                    "is_draft": is_draft,
                    "is_published": is_published,
                    "label_config": label_config,
                    "maximum_annotations": maximum_annotations,
                    "min_annotations_to_start_training": min_annotations_to_start_training,
                    "model_version": model_version,
                    "organization": organization,
                    "overlap_cohort_percentage": overlap_cohort_percentage,
                    "pinned_at": pinned_at,
                    "reveal_preannotations_interactively": reveal_preannotations_interactively,
                    "sampling": sampling,
                    "show_annotation_history": show_annotation_history,
                    "show_collab_predictions": show_collab_predictions,
                    "show_ground_truth_first": show_ground_truth_first,
                    "show_instruction": show_instruction,
                    "show_overlap_first": show_overlap_first,
                    "show_skip_button": show_skip_button,
                    "skip_queue": skip_queue,
                    "task_data_login": task_data_login,
                    "task_data_password": task_data_password,
                    "title": title,
                    "workspace": workspace,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateResponse,
        )

    def update(
        self,
        id: int,
        *,
        color: Optional[str] | NotGiven = NOT_GIVEN,
        control_weights: Optional[object] | NotGiven = NOT_GIVEN,
        created_by: project_update_params.CreatedBy | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enable_empty_annotation: bool | NotGiven = NOT_GIVEN,
        evaluate_predictions_automatically: bool | NotGiven = NOT_GIVEN,
        expert_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        is_draft: bool | NotGiven = NOT_GIVEN,
        is_published: bool | NotGiven = NOT_GIVEN,
        label_config: Optional[str] | NotGiven = NOT_GIVEN,
        maximum_annotations: int | NotGiven = NOT_GIVEN,
        min_annotations_to_start_training: int | NotGiven = NOT_GIVEN,
        model_version: Optional[str] | NotGiven = NOT_GIVEN,
        organization: Optional[int] | NotGiven = NOT_GIVEN,
        overlap_cohort_percentage: int | NotGiven = NOT_GIVEN,
        pinned_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        reveal_preannotations_interactively: bool | NotGiven = NOT_GIVEN,
        sampling: Optional[Literal["Sequential sampling", "Uniform sampling", "Uncertainty sampling"]]
        | NotGiven = NOT_GIVEN,
        show_annotation_history: bool | NotGiven = NOT_GIVEN,
        show_collab_predictions: bool | NotGiven = NOT_GIVEN,
        show_ground_truth_first: bool | NotGiven = NOT_GIVEN,
        show_instruction: bool | NotGiven = NOT_GIVEN,
        show_overlap_first: bool | NotGiven = NOT_GIVEN,
        show_skip_button: bool | NotGiven = NOT_GIVEN,
        skip_queue: Optional[Literal["REQUEUE_FOR_ME", "REQUEUE_FOR_OTHERS", "IGNORE_SKIPPED"]] | NotGiven = NOT_GIVEN,
        task_data_login: Optional[str] | NotGiven = NOT_GIVEN,
        task_data_password: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectUpdateResponse:
        """
        Update the project settings for a specific project.

        Args:
          control_weights: Dict of weights for each control tag in metric calculation. Each control tag
              (e.g. label or choice) will have it's own key in control weight dict with weight
              for each label and overall weight.For example, if bounding box annotation with
              control tag named my_bbox should be included with 0.33 weight in agreement
              calculation, and the first label Car should be twice more important than
              Airplaine, then you have to need the specify: {'my_bbox': {'type':
              'RectangleLabels', 'labels': {'Car': 1.0, 'Airplaine': 0.5}, 'overall': 0.33}

          created_by: User who created Dataset

          description: Project description

          enable_empty_annotation: Allow annotators to submit empty annotations

          evaluate_predictions_automatically: Retrieve and display predictions when loading a task

          expert_instruction: Labeling instructions in HTML format

          is_draft: Whether or not the project is in the middle of being created

          is_published: Whether or not the project is published to annotators

          label_config: Label config in XML format. See more about it in documentation

          maximum_annotations: Maximum number of annotations for one task. If the number of annotations per
              task is equal or greater to this value, the task is completed (is_labeled=True)

          min_annotations_to_start_training: Minimum number of completed tasks after which model training is started

          model_version: Machine learning model version

          pinned_at: Pinned date and time

          reveal_preannotations_interactively: Reveal pre-annotations interactively

          show_annotation_history: Show annotation history to annotator

          show_collab_predictions: If set, the annotator can view model predictions

          show_instruction: Show instructions to the annotator before they start

          show_skip_button: Show a skip button in interface and allow annotators to skip the task

          task_data_login: Task data credentials: login

          task_data_password: Task data credentials: password

          title: Project name. Must be between 3 and 50 characters long.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/api/projects/{id}/",
            body=maybe_transform(
                {
                    "color": color,
                    "control_weights": control_weights,
                    "created_by": created_by,
                    "description": description,
                    "enable_empty_annotation": enable_empty_annotation,
                    "evaluate_predictions_automatically": evaluate_predictions_automatically,
                    "expert_instruction": expert_instruction,
                    "is_draft": is_draft,
                    "is_published": is_published,
                    "label_config": label_config,
                    "maximum_annotations": maximum_annotations,
                    "min_annotations_to_start_training": min_annotations_to_start_training,
                    "model_version": model_version,
                    "organization": organization,
                    "overlap_cohort_percentage": overlap_cohort_percentage,
                    "pinned_at": pinned_at,
                    "reveal_preannotations_interactively": reveal_preannotations_interactively,
                    "sampling": sampling,
                    "show_annotation_history": show_annotation_history,
                    "show_collab_predictions": show_collab_predictions,
                    "show_ground_truth_first": show_ground_truth_first,
                    "show_instruction": show_instruction,
                    "show_overlap_first": show_overlap_first,
                    "show_skip_button": show_skip_button,
                    "skip_queue": skip_queue,
                    "task_data_login": task_data_login,
                    "task_data_password": task_data_password,
                    "title": title,
                },
                project_update_params.ProjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectUpdateResponse,
        )

    def list(
        self,
        *,
        ids: str | NotGiven = NOT_GIVEN,
        ordering: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        workspaces: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncLsOffsetPage[ProjectListResponse]:
        """
        Return a list of the projects that you've created.

        To perform most tasks with the Label Studio API, you must specify the project
        ID, sometimes referred to as the `pk`. To retrieve a list of your Label Studio
        projects, update the following command to match your own environment. Replace
        the domain name, port, and authorization token, then run the following from the
        command line:

        ```bash
        curl -X GET https://app.heartex.com/api/projects/ -H 'Authorization: Token abc123'
        ```

        Args:
          ids: ids

          ordering: Which field to use when ordering the results.

          page: A page number within the paginated result set.

          page_size: Number of results to return per page.

          title: title

          workspaces: workspaces

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/projects/",
            page=SyncLsOffsetPage[ProjectListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "ordering": ordering,
                        "page": page,
                        "page_size": page_size,
                        "title": title,
                        "workspaces": workspaces,
                    },
                    project_list_params.ProjectListParams,
                ),
            ),
            model=ProjectListResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a project by specified project ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/projects/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectGetResponse:
        """
        Retrieve information about a project by project ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/projects/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectGetResponse,
        )


class AsyncProjectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        color: Optional[str] | NotGiven = NOT_GIVEN,
        control_weights: Optional[object] | NotGiven = NOT_GIVEN,
        created_by: project_create_params.CreatedBy | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enable_empty_annotation: bool | NotGiven = NOT_GIVEN,
        evaluate_predictions_automatically: bool | NotGiven = NOT_GIVEN,
        expert_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        is_draft: bool | NotGiven = NOT_GIVEN,
        is_published: bool | NotGiven = NOT_GIVEN,
        label_config: Optional[str] | NotGiven = NOT_GIVEN,
        maximum_annotations: int | NotGiven = NOT_GIVEN,
        min_annotations_to_start_training: int | NotGiven = NOT_GIVEN,
        model_version: Optional[str] | NotGiven = NOT_GIVEN,
        organization: Optional[int] | NotGiven = NOT_GIVEN,
        overlap_cohort_percentage: int | NotGiven = NOT_GIVEN,
        pinned_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        reveal_preannotations_interactively: bool | NotGiven = NOT_GIVEN,
        sampling: Optional[Literal["Sequential sampling", "Uniform sampling", "Uncertainty sampling"]]
        | NotGiven = NOT_GIVEN,
        show_annotation_history: bool | NotGiven = NOT_GIVEN,
        show_collab_predictions: bool | NotGiven = NOT_GIVEN,
        show_ground_truth_first: bool | NotGiven = NOT_GIVEN,
        show_instruction: bool | NotGiven = NOT_GIVEN,
        show_overlap_first: bool | NotGiven = NOT_GIVEN,
        show_skip_button: bool | NotGiven = NOT_GIVEN,
        skip_queue: Optional[Literal["REQUEUE_FOR_ME", "REQUEUE_FOR_OTHERS", "IGNORE_SKIPPED"]] | NotGiven = NOT_GIVEN,
        task_data_login: Optional[str] | NotGiven = NOT_GIVEN,
        task_data_password: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        workspace: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectCreateResponse:
        """
        Create a project and set up the labeling interface in Label Studio using the
        API.

        ```bash
        curl -H Content-Type:application/json -H 'Authorization: Token abc123' -X POST 'https://app.heartex.com/api/projects'     --data '{"label_config": "<View>[...]</View>"}'
        ```

        Args:
          control_weights: Dict of weights for each control tag in metric calculation. Each control tag
              (e.g. label or choice) will have it's own key in control weight dict with weight
              for each label and overall weight.For example, if bounding box annotation with
              control tag named my_bbox should be included with 0.33 weight in agreement
              calculation, and the first label Car should be twice more important than
              Airplaine, then you have to need the specify: {'my_bbox': {'type':
              'RectangleLabels', 'labels': {'Car': 1.0, 'Airplaine': 0.5}, 'overall': 0.33}

          created_by: User who created Dataset

          description: Project description

          enable_empty_annotation: Allow annotators to submit empty annotations

          evaluate_predictions_automatically: Retrieve and display predictions when loading a task

          expert_instruction: Labeling instructions in HTML format

          is_draft: Whether or not the project is in the middle of being created

          is_published: Whether or not the project is published to annotators

          label_config: Label config in XML format. See more about it in documentation

          maximum_annotations: Maximum number of annotations for one task. If the number of annotations per
              task is equal or greater to this value, the task is completed (is_labeled=True)

          min_annotations_to_start_training: Minimum number of completed tasks after which model training is started

          model_version: Machine learning model version

          pinned_at: Pinned date and time

          reveal_preannotations_interactively: Reveal pre-annotations interactively

          show_annotation_history: Show annotation history to annotator

          show_collab_predictions: If set, the annotator can view model predictions

          show_instruction: Show instructions to the annotator before they start

          show_skip_button: Show a skip button in interface and allow annotators to skip the task

          task_data_login: Task data credentials: login

          task_data_password: Task data credentials: password

          title: Project name. Must be between 3 and 50 characters long.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/projects/",
            body=await async_maybe_transform(
                {
                    "color": color,
                    "control_weights": control_weights,
                    "created_by": created_by,
                    "description": description,
                    "enable_empty_annotation": enable_empty_annotation,
                    "evaluate_predictions_automatically": evaluate_predictions_automatically,
                    "expert_instruction": expert_instruction,
                    "is_draft": is_draft,
                    "is_published": is_published,
                    "label_config": label_config,
                    "maximum_annotations": maximum_annotations,
                    "min_annotations_to_start_training": min_annotations_to_start_training,
                    "model_version": model_version,
                    "organization": organization,
                    "overlap_cohort_percentage": overlap_cohort_percentage,
                    "pinned_at": pinned_at,
                    "reveal_preannotations_interactively": reveal_preannotations_interactively,
                    "sampling": sampling,
                    "show_annotation_history": show_annotation_history,
                    "show_collab_predictions": show_collab_predictions,
                    "show_ground_truth_first": show_ground_truth_first,
                    "show_instruction": show_instruction,
                    "show_overlap_first": show_overlap_first,
                    "show_skip_button": show_skip_button,
                    "skip_queue": skip_queue,
                    "task_data_login": task_data_login,
                    "task_data_password": task_data_password,
                    "title": title,
                    "workspace": workspace,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateResponse,
        )

    async def update(
        self,
        id: int,
        *,
        color: Optional[str] | NotGiven = NOT_GIVEN,
        control_weights: Optional[object] | NotGiven = NOT_GIVEN,
        created_by: project_update_params.CreatedBy | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enable_empty_annotation: bool | NotGiven = NOT_GIVEN,
        evaluate_predictions_automatically: bool | NotGiven = NOT_GIVEN,
        expert_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        is_draft: bool | NotGiven = NOT_GIVEN,
        is_published: bool | NotGiven = NOT_GIVEN,
        label_config: Optional[str] | NotGiven = NOT_GIVEN,
        maximum_annotations: int | NotGiven = NOT_GIVEN,
        min_annotations_to_start_training: int | NotGiven = NOT_GIVEN,
        model_version: Optional[str] | NotGiven = NOT_GIVEN,
        organization: Optional[int] | NotGiven = NOT_GIVEN,
        overlap_cohort_percentage: int | NotGiven = NOT_GIVEN,
        pinned_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        reveal_preannotations_interactively: bool | NotGiven = NOT_GIVEN,
        sampling: Optional[Literal["Sequential sampling", "Uniform sampling", "Uncertainty sampling"]]
        | NotGiven = NOT_GIVEN,
        show_annotation_history: bool | NotGiven = NOT_GIVEN,
        show_collab_predictions: bool | NotGiven = NOT_GIVEN,
        show_ground_truth_first: bool | NotGiven = NOT_GIVEN,
        show_instruction: bool | NotGiven = NOT_GIVEN,
        show_overlap_first: bool | NotGiven = NOT_GIVEN,
        show_skip_button: bool | NotGiven = NOT_GIVEN,
        skip_queue: Optional[Literal["REQUEUE_FOR_ME", "REQUEUE_FOR_OTHERS", "IGNORE_SKIPPED"]] | NotGiven = NOT_GIVEN,
        task_data_login: Optional[str] | NotGiven = NOT_GIVEN,
        task_data_password: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectUpdateResponse:
        """
        Update the project settings for a specific project.

        Args:
          control_weights: Dict of weights for each control tag in metric calculation. Each control tag
              (e.g. label or choice) will have it's own key in control weight dict with weight
              for each label and overall weight.For example, if bounding box annotation with
              control tag named my_bbox should be included with 0.33 weight in agreement
              calculation, and the first label Car should be twice more important than
              Airplaine, then you have to need the specify: {'my_bbox': {'type':
              'RectangleLabels', 'labels': {'Car': 1.0, 'Airplaine': 0.5}, 'overall': 0.33}

          created_by: User who created Dataset

          description: Project description

          enable_empty_annotation: Allow annotators to submit empty annotations

          evaluate_predictions_automatically: Retrieve and display predictions when loading a task

          expert_instruction: Labeling instructions in HTML format

          is_draft: Whether or not the project is in the middle of being created

          is_published: Whether or not the project is published to annotators

          label_config: Label config in XML format. See more about it in documentation

          maximum_annotations: Maximum number of annotations for one task. If the number of annotations per
              task is equal or greater to this value, the task is completed (is_labeled=True)

          min_annotations_to_start_training: Minimum number of completed tasks after which model training is started

          model_version: Machine learning model version

          pinned_at: Pinned date and time

          reveal_preannotations_interactively: Reveal pre-annotations interactively

          show_annotation_history: Show annotation history to annotator

          show_collab_predictions: If set, the annotator can view model predictions

          show_instruction: Show instructions to the annotator before they start

          show_skip_button: Show a skip button in interface and allow annotators to skip the task

          task_data_login: Task data credentials: login

          task_data_password: Task data credentials: password

          title: Project name. Must be between 3 and 50 characters long.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/api/projects/{id}/",
            body=await async_maybe_transform(
                {
                    "color": color,
                    "control_weights": control_weights,
                    "created_by": created_by,
                    "description": description,
                    "enable_empty_annotation": enable_empty_annotation,
                    "evaluate_predictions_automatically": evaluate_predictions_automatically,
                    "expert_instruction": expert_instruction,
                    "is_draft": is_draft,
                    "is_published": is_published,
                    "label_config": label_config,
                    "maximum_annotations": maximum_annotations,
                    "min_annotations_to_start_training": min_annotations_to_start_training,
                    "model_version": model_version,
                    "organization": organization,
                    "overlap_cohort_percentage": overlap_cohort_percentage,
                    "pinned_at": pinned_at,
                    "reveal_preannotations_interactively": reveal_preannotations_interactively,
                    "sampling": sampling,
                    "show_annotation_history": show_annotation_history,
                    "show_collab_predictions": show_collab_predictions,
                    "show_ground_truth_first": show_ground_truth_first,
                    "show_instruction": show_instruction,
                    "show_overlap_first": show_overlap_first,
                    "show_skip_button": show_skip_button,
                    "skip_queue": skip_queue,
                    "task_data_login": task_data_login,
                    "task_data_password": task_data_password,
                    "title": title,
                },
                project_update_params.ProjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectUpdateResponse,
        )

    def list(
        self,
        *,
        ids: str | NotGiven = NOT_GIVEN,
        ordering: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        workspaces: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ProjectListResponse, AsyncLsOffsetPage[ProjectListResponse]]:
        """
        Return a list of the projects that you've created.

        To perform most tasks with the Label Studio API, you must specify the project
        ID, sometimes referred to as the `pk`. To retrieve a list of your Label Studio
        projects, update the following command to match your own environment. Replace
        the domain name, port, and authorization token, then run the following from the
        command line:

        ```bash
        curl -X GET https://app.heartex.com/api/projects/ -H 'Authorization: Token abc123'
        ```

        Args:
          ids: ids

          ordering: Which field to use when ordering the results.

          page: A page number within the paginated result set.

          page_size: Number of results to return per page.

          title: title

          workspaces: workspaces

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/projects/",
            page=AsyncLsOffsetPage[ProjectListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "ordering": ordering,
                        "page": page,
                        "page_size": page_size,
                        "title": title,
                        "workspaces": workspaces,
                    },
                    project_list_params.ProjectListParams,
                ),
            ),
            model=ProjectListResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a project by specified project ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/projects/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectGetResponse:
        """
        Retrieve information about a project by project ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/projects/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectGetResponse,
        )


class ProjectsResourceWithRawResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.create = to_raw_response_wrapper(
            projects.create,
        )
        self.update = to_raw_response_wrapper(
            projects.update,
        )
        self.list = to_raw_response_wrapper(
            projects.list,
        )
        self.delete = to_raw_response_wrapper(
            projects.delete,
        )
        self.get = to_raw_response_wrapper(
            projects.get,
        )


class AsyncProjectsResourceWithRawResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create = async_to_raw_response_wrapper(
            projects.create,
        )
        self.update = async_to_raw_response_wrapper(
            projects.update,
        )
        self.list = async_to_raw_response_wrapper(
            projects.list,
        )
        self.delete = async_to_raw_response_wrapper(
            projects.delete,
        )
        self.get = async_to_raw_response_wrapper(
            projects.get,
        )


class ProjectsResourceWithStreamingResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.create = to_streamed_response_wrapper(
            projects.create,
        )
        self.update = to_streamed_response_wrapper(
            projects.update,
        )
        self.list = to_streamed_response_wrapper(
            projects.list,
        )
        self.delete = to_streamed_response_wrapper(
            projects.delete,
        )
        self.get = to_streamed_response_wrapper(
            projects.get,
        )


class AsyncProjectsResourceWithStreamingResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create = async_to_streamed_response_wrapper(
            projects.create,
        )
        self.update = async_to_streamed_response_wrapper(
            projects.update,
        )
        self.list = async_to_streamed_response_wrapper(
            projects.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            projects.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            projects.get,
        )
