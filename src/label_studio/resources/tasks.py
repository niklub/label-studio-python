# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime

import httpx

from ..types import task_list_params, task_create_params, task_update_params
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
from ..types.task_get_response import TaskGetResponse
from ..types.task_list_response import TaskListResponse
from ..types.task_create_response import TaskCreateResponse
from ..types.task_update_response import TaskUpdateResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        data: object,
        cancelled_annotations: int | NotGiven = NOT_GIVEN,
        comment_authors: Iterable[int] | NotGiven = NOT_GIVEN,
        comment_count: int | NotGiven = NOT_GIVEN,
        file_upload: Optional[int] | NotGiven = NOT_GIVEN,
        inner_id: Optional[int] | NotGiven = NOT_GIVEN,
        is_labeled: bool | NotGiven = NOT_GIVEN,
        last_comment_updated_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        overlap: int | NotGiven = NOT_GIVEN,
        project: Optional[int] | NotGiven = NOT_GIVEN,
        total_annotations: int | NotGiven = NOT_GIVEN,
        total_predictions: int | NotGiven = NOT_GIVEN,
        unresolved_comment_count: int | NotGiven = NOT_GIVEN,
        updated_by: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Create a new labeling task in Label Studio.

        Args:
          data: User imported or uploaded data for a task. Data is formatted according to the
              project label config. You can find examples of data for your project on the
              Import page in the Label Studio Data Manager UI.

          cancelled_annotations: Number of total cancelled annotations for the current task

          comment_authors: Users who wrote comments

          comment_count: Number of comments in the task including all annotations

          file_upload: Uploaded file used as data source for this task

          inner_id: Internal task ID in the project, starts with 1

          is_labeled: True if the number of annotations for this task is greater than or equal to the
              number of maximum_completions for the project

          last_comment_updated_at: When the last comment was updated

          meta: Meta is user imported (uploaded) data and can be useful as input for an ML
              Backend for embeddings, advanced vectors, and other info. It is passed to ML
              during training/predicting steps.

          overlap: Number of distinct annotators that processed the current task

          project: Project ID for this task

          total_annotations: Number of total annotations for the current task except cancelled annotations

          total_predictions: Number of total predictions for the current task

          unresolved_comment_count: Number of unresolved comments in the task including all annotations

          updated_by: Last annotator or reviewer who updated this task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/tasks/",
            body=maybe_transform(
                {
                    "data": data,
                    "cancelled_annotations": cancelled_annotations,
                    "comment_authors": comment_authors,
                    "comment_count": comment_count,
                    "file_upload": file_upload,
                    "inner_id": inner_id,
                    "is_labeled": is_labeled,
                    "last_comment_updated_at": last_comment_updated_at,
                    "meta": meta,
                    "overlap": overlap,
                    "project": project,
                    "total_annotations": total_annotations,
                    "total_predictions": total_predictions,
                    "unresolved_comment_count": unresolved_comment_count,
                    "updated_by": updated_by,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        data: object,
        cancelled_annotations: int | NotGiven = NOT_GIVEN,
        comment_authors: Iterable[int] | NotGiven = NOT_GIVEN,
        comment_count: int | NotGiven = NOT_GIVEN,
        file_upload: Optional[int] | NotGiven = NOT_GIVEN,
        inner_id: Optional[int] | NotGiven = NOT_GIVEN,
        is_labeled: bool | NotGiven = NOT_GIVEN,
        last_comment_updated_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        overlap: int | NotGiven = NOT_GIVEN,
        project: Optional[int] | NotGiven = NOT_GIVEN,
        total_annotations: int | NotGiven = NOT_GIVEN,
        total_predictions: int | NotGiven = NOT_GIVEN,
        unresolved_comment_count: int | NotGiven = NOT_GIVEN,
        updated_by: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskUpdateResponse:
        """
        Update the attributes of an existing labeling task.

        Args:
          data: User imported or uploaded data for a task. Data is formatted according to the
              project label config. You can find examples of data for your project on the
              Import page in the Label Studio Data Manager UI.

          cancelled_annotations: Number of total cancelled annotations for the current task

          comment_authors: Users who wrote comments

          comment_count: Number of comments in the task including all annotations

          file_upload: Uploaded file used as data source for this task

          inner_id: Internal task ID in the project, starts with 1

          is_labeled: True if the number of annotations for this task is greater than or equal to the
              number of maximum_completions for the project

          last_comment_updated_at: When the last comment was updated

          meta: Meta is user imported (uploaded) data and can be useful as input for an ML
              Backend for embeddings, advanced vectors, and other info. It is passed to ML
              during training/predicting steps.

          overlap: Number of distinct annotators that processed the current task

          project: Project ID for this task

          total_annotations: Number of total annotations for the current task except cancelled annotations

          total_predictions: Number of total predictions for the current task

          unresolved_comment_count: Number of unresolved comments in the task including all annotations

          updated_by: Last annotator or reviewer who updated this task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/tasks/{id}/",
            body=maybe_transform(
                {
                    "data": data,
                    "cancelled_annotations": cancelled_annotations,
                    "comment_authors": comment_authors,
                    "comment_count": comment_count,
                    "file_upload": file_upload,
                    "inner_id": inner_id,
                    "is_labeled": is_labeled,
                    "last_comment_updated_at": last_comment_updated_at,
                    "meta": meta,
                    "overlap": overlap,
                    "project": project,
                    "total_annotations": total_annotations,
                    "total_predictions": total_predictions,
                    "unresolved_comment_count": unresolved_comment_count,
                    "updated_by": updated_by,
                },
                task_update_params.TaskUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        project: int | NotGiven = NOT_GIVEN,
        resolve_uri: bool | NotGiven = NOT_GIVEN,
        view: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncLsOffsetPage[TaskListResponse]:
        """
        Retrieve a list of tasks with pagination for a specific view or project, by
        using filters and ordering.

        Args:
          page: A page number within the paginated result set.

          page_size: Number of results to return per page.

          project: Project ID

          resolve_uri: Resolve task data URIs using Cloud Storage

          view: View ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/tasks/",
            page=SyncLsOffsetPage[TaskListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "project": project,
                        "resolve_uri": resolve_uri,
                        "view": view,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            model=TaskListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete a task in Label Studio.

        This action cannot be undone!

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/tasks/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskGetResponse:
        """
        Get task data, metadata, annotations and other attributes for a specific
        labeling task by task ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/tasks/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        data: object,
        cancelled_annotations: int | NotGiven = NOT_GIVEN,
        comment_authors: Iterable[int] | NotGiven = NOT_GIVEN,
        comment_count: int | NotGiven = NOT_GIVEN,
        file_upload: Optional[int] | NotGiven = NOT_GIVEN,
        inner_id: Optional[int] | NotGiven = NOT_GIVEN,
        is_labeled: bool | NotGiven = NOT_GIVEN,
        last_comment_updated_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        overlap: int | NotGiven = NOT_GIVEN,
        project: Optional[int] | NotGiven = NOT_GIVEN,
        total_annotations: int | NotGiven = NOT_GIVEN,
        total_predictions: int | NotGiven = NOT_GIVEN,
        unresolved_comment_count: int | NotGiven = NOT_GIVEN,
        updated_by: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Create a new labeling task in Label Studio.

        Args:
          data: User imported or uploaded data for a task. Data is formatted according to the
              project label config. You can find examples of data for your project on the
              Import page in the Label Studio Data Manager UI.

          cancelled_annotations: Number of total cancelled annotations for the current task

          comment_authors: Users who wrote comments

          comment_count: Number of comments in the task including all annotations

          file_upload: Uploaded file used as data source for this task

          inner_id: Internal task ID in the project, starts with 1

          is_labeled: True if the number of annotations for this task is greater than or equal to the
              number of maximum_completions for the project

          last_comment_updated_at: When the last comment was updated

          meta: Meta is user imported (uploaded) data and can be useful as input for an ML
              Backend for embeddings, advanced vectors, and other info. It is passed to ML
              during training/predicting steps.

          overlap: Number of distinct annotators that processed the current task

          project: Project ID for this task

          total_annotations: Number of total annotations for the current task except cancelled annotations

          total_predictions: Number of total predictions for the current task

          unresolved_comment_count: Number of unresolved comments in the task including all annotations

          updated_by: Last annotator or reviewer who updated this task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/tasks/",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "cancelled_annotations": cancelled_annotations,
                    "comment_authors": comment_authors,
                    "comment_count": comment_count,
                    "file_upload": file_upload,
                    "inner_id": inner_id,
                    "is_labeled": is_labeled,
                    "last_comment_updated_at": last_comment_updated_at,
                    "meta": meta,
                    "overlap": overlap,
                    "project": project,
                    "total_annotations": total_annotations,
                    "total_predictions": total_predictions,
                    "unresolved_comment_count": unresolved_comment_count,
                    "updated_by": updated_by,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        data: object,
        cancelled_annotations: int | NotGiven = NOT_GIVEN,
        comment_authors: Iterable[int] | NotGiven = NOT_GIVEN,
        comment_count: int | NotGiven = NOT_GIVEN,
        file_upload: Optional[int] | NotGiven = NOT_GIVEN,
        inner_id: Optional[int] | NotGiven = NOT_GIVEN,
        is_labeled: bool | NotGiven = NOT_GIVEN,
        last_comment_updated_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        overlap: int | NotGiven = NOT_GIVEN,
        project: Optional[int] | NotGiven = NOT_GIVEN,
        total_annotations: int | NotGiven = NOT_GIVEN,
        total_predictions: int | NotGiven = NOT_GIVEN,
        unresolved_comment_count: int | NotGiven = NOT_GIVEN,
        updated_by: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskUpdateResponse:
        """
        Update the attributes of an existing labeling task.

        Args:
          data: User imported or uploaded data for a task. Data is formatted according to the
              project label config. You can find examples of data for your project on the
              Import page in the Label Studio Data Manager UI.

          cancelled_annotations: Number of total cancelled annotations for the current task

          comment_authors: Users who wrote comments

          comment_count: Number of comments in the task including all annotations

          file_upload: Uploaded file used as data source for this task

          inner_id: Internal task ID in the project, starts with 1

          is_labeled: True if the number of annotations for this task is greater than or equal to the
              number of maximum_completions for the project

          last_comment_updated_at: When the last comment was updated

          meta: Meta is user imported (uploaded) data and can be useful as input for an ML
              Backend for embeddings, advanced vectors, and other info. It is passed to ML
              during training/predicting steps.

          overlap: Number of distinct annotators that processed the current task

          project: Project ID for this task

          total_annotations: Number of total annotations for the current task except cancelled annotations

          total_predictions: Number of total predictions for the current task

          unresolved_comment_count: Number of unresolved comments in the task including all annotations

          updated_by: Last annotator or reviewer who updated this task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/tasks/{id}/",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "cancelled_annotations": cancelled_annotations,
                    "comment_authors": comment_authors,
                    "comment_count": comment_count,
                    "file_upload": file_upload,
                    "inner_id": inner_id,
                    "is_labeled": is_labeled,
                    "last_comment_updated_at": last_comment_updated_at,
                    "meta": meta,
                    "overlap": overlap,
                    "project": project,
                    "total_annotations": total_annotations,
                    "total_predictions": total_predictions,
                    "unresolved_comment_count": unresolved_comment_count,
                    "updated_by": updated_by,
                },
                task_update_params.TaskUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        project: int | NotGiven = NOT_GIVEN,
        resolve_uri: bool | NotGiven = NOT_GIVEN,
        view: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TaskListResponse, AsyncLsOffsetPage[TaskListResponse]]:
        """
        Retrieve a list of tasks with pagination for a specific view or project, by
        using filters and ordering.

        Args:
          page: A page number within the paginated result set.

          page_size: Number of results to return per page.

          project: Project ID

          resolve_uri: Resolve task data URIs using Cloud Storage

          view: View ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/tasks/",
            page=AsyncLsOffsetPage[TaskListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "project": project,
                        "resolve_uri": resolve_uri,
                        "view": view,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            model=TaskListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete a task in Label Studio.

        This action cannot be undone!

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/tasks/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskGetResponse:
        """
        Get task data, metadata, annotations and other attributes for a specific
        labeling task by task ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/tasks/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetResponse,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_raw_response_wrapper(
            tasks.create,
        )
        self.update = to_raw_response_wrapper(
            tasks.update,
        )
        self.list = to_raw_response_wrapper(
            tasks.list,
        )
        self.delete = to_raw_response_wrapper(
            tasks.delete,
        )
        self.get = to_raw_response_wrapper(
            tasks.get,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
        self.update = async_to_raw_response_wrapper(
            tasks.update,
        )
        self.list = async_to_raw_response_wrapper(
            tasks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tasks.delete,
        )
        self.get = async_to_raw_response_wrapper(
            tasks.get,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_streamed_response_wrapper(
            tasks.create,
        )
        self.update = to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = to_streamed_response_wrapper(
            tasks.list,
        )
        self.delete = to_streamed_response_wrapper(
            tasks.delete,
        )
        self.get = to_streamed_response_wrapper(
            tasks.get,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
        self.update = async_to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tasks.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            tasks.get,
        )
