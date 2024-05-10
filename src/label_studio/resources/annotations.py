# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import annotation_update_params
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
from .._base_client import (
    make_request_options,
)
from ..types.annotation import Annotation

__all__ = ["AnnotationsResource", "AsyncAnnotationsResource"]


class AnnotationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnnotationsResourceWithRawResponse:
        return AnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnnotationsResourceWithStreamingResponse:
        return AnnotationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Annotation:
        """
        Retrieve a specific annotation for a task using the annotation result ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/annotations/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Annotation,
        )

    def update(
        self,
        id: int,
        *,
        completed_by: int | NotGiven = NOT_GIVEN,
        draft_created_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        ground_truth: bool | NotGiven = NOT_GIVEN,
        import_id: Optional[int] | NotGiven = NOT_GIVEN,
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
        ]
        | NotGiven = NOT_GIVEN,
        last_created_by: Optional[int] | NotGiven = NOT_GIVEN,
        lead_time: Optional[float] | NotGiven = NOT_GIVEN,
        parent_annotation: Optional[int] | NotGiven = NOT_GIVEN,
        parent_prediction: Optional[int] | NotGiven = NOT_GIVEN,
        project: Optional[int] | NotGiven = NOT_GIVEN,
        result: Optional[object] | NotGiven = NOT_GIVEN,
        task: Optional[int] | NotGiven = NOT_GIVEN,
        unique_id: str | NotGiven = NOT_GIVEN,
        updated_by: Optional[int] | NotGiven = NOT_GIVEN,
        was_cancelled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Annotation:
        """
        Update existing attributes on an annotation.

        Args:
          draft_created_at: Draft creation time

          ground_truth: This annotation is a Ground Truth (ground_truth)

          import_id: Original annotation ID that was at the import step or NULL if this annotation
              wasn't imported

          last_action: Action which was performed in the last annotation history item

          last_created_by: User who created the last annotation history item

          lead_time: How much time it took to annotate the task

          parent_annotation: Points to the parent annotation from which this annotation was created

          parent_prediction: Points to the prediction from which this annotation was created

          project: Project ID for this annotation

          result: The main value of annotator work - labeling result in JSON format

          task: Corresponding task for this annotation

          updated_by: Last user who updated this annotation

          was_cancelled: User skipped the task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/api/annotations/{id}/",
            body=maybe_transform(
                {
                    "completed_by": completed_by,
                    "draft_created_at": draft_created_at,
                    "ground_truth": ground_truth,
                    "import_id": import_id,
                    "last_action": last_action,
                    "last_created_by": last_created_by,
                    "lead_time": lead_time,
                    "parent_annotation": parent_annotation,
                    "parent_prediction": parent_prediction,
                    "project": project,
                    "result": result,
                    "task": task,
                    "unique_id": unique_id,
                    "updated_by": updated_by,
                    "was_cancelled": was_cancelled,
                },
                annotation_update_params.AnnotationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Annotation,
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
        """Delete an annotation.

        This action can't be undone!

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/annotations/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAnnotationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnnotationsResourceWithRawResponse:
        return AsyncAnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnnotationsResourceWithStreamingResponse:
        return AsyncAnnotationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Annotation:
        """
        Retrieve a specific annotation for a task using the annotation result ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/annotations/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Annotation,
        )

    async def update(
        self,
        id: int,
        *,
        completed_by: int | NotGiven = NOT_GIVEN,
        draft_created_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        ground_truth: bool | NotGiven = NOT_GIVEN,
        import_id: Optional[int] | NotGiven = NOT_GIVEN,
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
        ]
        | NotGiven = NOT_GIVEN,
        last_created_by: Optional[int] | NotGiven = NOT_GIVEN,
        lead_time: Optional[float] | NotGiven = NOT_GIVEN,
        parent_annotation: Optional[int] | NotGiven = NOT_GIVEN,
        parent_prediction: Optional[int] | NotGiven = NOT_GIVEN,
        project: Optional[int] | NotGiven = NOT_GIVEN,
        result: Optional[object] | NotGiven = NOT_GIVEN,
        task: Optional[int] | NotGiven = NOT_GIVEN,
        unique_id: str | NotGiven = NOT_GIVEN,
        updated_by: Optional[int] | NotGiven = NOT_GIVEN,
        was_cancelled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Annotation:
        """
        Update existing attributes on an annotation.

        Args:
          draft_created_at: Draft creation time

          ground_truth: This annotation is a Ground Truth (ground_truth)

          import_id: Original annotation ID that was at the import step or NULL if this annotation
              wasn't imported

          last_action: Action which was performed in the last annotation history item

          last_created_by: User who created the last annotation history item

          lead_time: How much time it took to annotate the task

          parent_annotation: Points to the parent annotation from which this annotation was created

          parent_prediction: Points to the prediction from which this annotation was created

          project: Project ID for this annotation

          result: The main value of annotator work - labeling result in JSON format

          task: Corresponding task for this annotation

          updated_by: Last user who updated this annotation

          was_cancelled: User skipped the task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/api/annotations/{id}/",
            body=await async_maybe_transform(
                {
                    "completed_by": completed_by,
                    "draft_created_at": draft_created_at,
                    "ground_truth": ground_truth,
                    "import_id": import_id,
                    "last_action": last_action,
                    "last_created_by": last_created_by,
                    "lead_time": lead_time,
                    "parent_annotation": parent_annotation,
                    "parent_prediction": parent_prediction,
                    "project": project,
                    "result": result,
                    "task": task,
                    "unique_id": unique_id,
                    "updated_by": updated_by,
                    "was_cancelled": was_cancelled,
                },
                annotation_update_params.AnnotationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Annotation,
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
        """Delete an annotation.

        This action can't be undone!

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/annotations/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

        self.retrieve = to_raw_response_wrapper(
            annotations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            annotations.update,
        )
        self.delete = to_raw_response_wrapper(
            annotations.delete,
        )


class AsyncAnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

        self.retrieve = async_to_raw_response_wrapper(
            annotations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            annotations.update,
        )
        self.delete = async_to_raw_response_wrapper(
            annotations.delete,
        )


class AnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

        self.retrieve = to_streamed_response_wrapper(
            annotations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            annotations.update,
        )
        self.delete = to_streamed_response_wrapper(
            annotations.delete,
        )


class AsyncAnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

        self.retrieve = async_to_streamed_response_wrapper(
            annotations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            annotations.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            annotations.delete,
        )
