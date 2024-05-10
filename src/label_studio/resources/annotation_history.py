# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import annotation_history_list_params, annotation_history_delete_params
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
from ..types.annotation_history_list_response import AnnotationHistoryListResponse

__all__ = ["AnnotationHistoryResource", "AsyncAnnotationHistoryResource"]


class AnnotationHistoryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnnotationHistoryResourceWithRawResponse:
        return AnnotationHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnnotationHistoryResourceWithStreamingResponse:
        return AnnotationHistoryResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        annotation: int | NotGiven = NOT_GIVEN,
        ordering: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationHistoryListResponse:
        """List annotation history items for an annotation.

        Annotation history logs all
        actions performed with annotations, such as: imports, submits, updates, reviews,
        and more. Users can view annotation history items in the Annotation History
        panel during labeling.

        Args:
          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/annotation-history/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "annotation": annotation,
                        "ordering": ordering,
                    },
                    annotation_history_list_params.AnnotationHistoryListParams,
                ),
            ),
            cast_to=AnnotationHistoryListResponse,
        )

    def delete(
        self,
        *,
        annotation: int | NotGiven = NOT_GIVEN,
        project: int | NotGiven = NOT_GIVEN,
        task: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete all annotation history items for a specific annotation, task or project.
        This method is available only for users with administrator roles.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/api/annotation-history/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "annotation": annotation,
                        "project": project,
                        "task": task,
                    },
                    annotation_history_delete_params.AnnotationHistoryDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncAnnotationHistoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnnotationHistoryResourceWithRawResponse:
        return AsyncAnnotationHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnnotationHistoryResourceWithStreamingResponse:
        return AsyncAnnotationHistoryResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        annotation: int | NotGiven = NOT_GIVEN,
        ordering: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationHistoryListResponse:
        """List annotation history items for an annotation.

        Annotation history logs all
        actions performed with annotations, such as: imports, submits, updates, reviews,
        and more. Users can view annotation history items in the Annotation History
        panel during labeling.

        Args:
          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/annotation-history/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "annotation": annotation,
                        "ordering": ordering,
                    },
                    annotation_history_list_params.AnnotationHistoryListParams,
                ),
            ),
            cast_to=AnnotationHistoryListResponse,
        )

    async def delete(
        self,
        *,
        annotation: int | NotGiven = NOT_GIVEN,
        project: int | NotGiven = NOT_GIVEN,
        task: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete all annotation history items for a specific annotation, task or project.
        This method is available only for users with administrator roles.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/api/annotation-history/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "annotation": annotation,
                        "project": project,
                        "task": task,
                    },
                    annotation_history_delete_params.AnnotationHistoryDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class AnnotationHistoryResourceWithRawResponse:
    def __init__(self, annotation_history: AnnotationHistoryResource) -> None:
        self._annotation_history = annotation_history

        self.list = to_raw_response_wrapper(
            annotation_history.list,
        )
        self.delete = to_raw_response_wrapper(
            annotation_history.delete,
        )


class AsyncAnnotationHistoryResourceWithRawResponse:
    def __init__(self, annotation_history: AsyncAnnotationHistoryResource) -> None:
        self._annotation_history = annotation_history

        self.list = async_to_raw_response_wrapper(
            annotation_history.list,
        )
        self.delete = async_to_raw_response_wrapper(
            annotation_history.delete,
        )


class AnnotationHistoryResourceWithStreamingResponse:
    def __init__(self, annotation_history: AnnotationHistoryResource) -> None:
        self._annotation_history = annotation_history

        self.list = to_streamed_response_wrapper(
            annotation_history.list,
        )
        self.delete = to_streamed_response_wrapper(
            annotation_history.delete,
        )


class AsyncAnnotationHistoryResourceWithStreamingResponse:
    def __init__(self, annotation_history: AsyncAnnotationHistoryResource) -> None:
        self._annotation_history = annotation_history

        self.list = async_to_streamed_response_wrapper(
            annotation_history.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            annotation_history.delete,
        )
