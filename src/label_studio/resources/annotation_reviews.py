# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    annotation_review_list_params,
    annotation_review_create_params,
    annotation_review_update_params,
    annotation_review_overwrite_params,
)
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
from ..types.annotation_review import AnnotationReview
from ..types.annotation_review_list_response import AnnotationReviewListResponse

__all__ = ["AnnotationReviewsResource", "AsyncAnnotationReviewsResource"]


class AnnotationReviewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnnotationReviewsResourceWithRawResponse:
        return AnnotationReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnnotationReviewsResourceWithStreamingResponse:
        return AnnotationReviewsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        annotation: int,
        accepted: bool | NotGiven = NOT_GIVEN,
        comment: Optional[str] | NotGiven = NOT_GIVEN,
        last_annotation_history: Optional[int] | NotGiven = NOT_GIVEN,
        result: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationReview:
        """
        Create a review for a specific annotation ID.

        Args:
          annotation: Corresponding annotation

          accepted: Accepted or rejected (if false) flag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/annotation-reviews/",
            body=maybe_transform(
                {
                    "annotation": annotation,
                    "accepted": accepted,
                    "comment": comment,
                    "last_annotation_history": last_annotation_history,
                    "result": result,
                },
                annotation_review_create_params.AnnotationReviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationReview,
        )

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
    ) -> AnnotationReview:
        """
        Retrieve a specific review by ID for an annotation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/annotation-reviews/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationReview,
        )

    def update(
        self,
        id: int,
        *,
        annotation: int,
        accepted: bool | NotGiven = NOT_GIVEN,
        comment: Optional[str] | NotGiven = NOT_GIVEN,
        last_annotation_history: Optional[int] | NotGiven = NOT_GIVEN,
        result: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationReview:
        """
        Update a specific review by ID.

        Args:
          annotation: Corresponding annotation

          accepted: Accepted or rejected (if false) flag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/api/annotation-reviews/{id}/",
            body=maybe_transform(
                {
                    "annotation": annotation,
                    "accepted": accepted,
                    "comment": comment,
                    "last_annotation_history": last_annotation_history,
                    "result": result,
                },
                annotation_review_update_params.AnnotationReviewUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationReview,
        )

    def list(
        self,
        *,
        annotation: str | NotGiven = NOT_GIVEN,
        annotation_task_project: str | NotGiven = NOT_GIVEN,
        ordering: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationReviewListResponse:
        """
        List all reviews for a specific annotation ID.

        Args:
          annotation: annotation

          annotation_task_project: annotation**task**project

          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/annotation-reviews/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "annotation": annotation,
                        "annotation_task_project": annotation_task_project,
                        "ordering": ordering,
                    },
                    annotation_review_list_params.AnnotationReviewListParams,
                ),
            ),
            cast_to=AnnotationReviewListResponse,
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
        Delete a review by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/annotation-reviews/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def overwrite(
        self,
        id: int,
        *,
        annotation: int,
        accepted: bool | NotGiven = NOT_GIVEN,
        comment: Optional[str] | NotGiven = NOT_GIVEN,
        last_annotation_history: Optional[int] | NotGiven = NOT_GIVEN,
        result: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationReview:
        """
        Overwrite a specific review by ID.

        Args:
          annotation: Corresponding annotation

          accepted: Accepted or rejected (if false) flag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/api/annotation-reviews/{id}/",
            body=maybe_transform(
                {
                    "annotation": annotation,
                    "accepted": accepted,
                    "comment": comment,
                    "last_annotation_history": last_annotation_history,
                    "result": result,
                },
                annotation_review_overwrite_params.AnnotationReviewOverwriteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationReview,
        )


class AsyncAnnotationReviewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnnotationReviewsResourceWithRawResponse:
        return AsyncAnnotationReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnnotationReviewsResourceWithStreamingResponse:
        return AsyncAnnotationReviewsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        annotation: int,
        accepted: bool | NotGiven = NOT_GIVEN,
        comment: Optional[str] | NotGiven = NOT_GIVEN,
        last_annotation_history: Optional[int] | NotGiven = NOT_GIVEN,
        result: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationReview:
        """
        Create a review for a specific annotation ID.

        Args:
          annotation: Corresponding annotation

          accepted: Accepted or rejected (if false) flag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/annotation-reviews/",
            body=await async_maybe_transform(
                {
                    "annotation": annotation,
                    "accepted": accepted,
                    "comment": comment,
                    "last_annotation_history": last_annotation_history,
                    "result": result,
                },
                annotation_review_create_params.AnnotationReviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationReview,
        )

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
    ) -> AnnotationReview:
        """
        Retrieve a specific review by ID for an annotation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/annotation-reviews/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationReview,
        )

    async def update(
        self,
        id: int,
        *,
        annotation: int,
        accepted: bool | NotGiven = NOT_GIVEN,
        comment: Optional[str] | NotGiven = NOT_GIVEN,
        last_annotation_history: Optional[int] | NotGiven = NOT_GIVEN,
        result: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationReview:
        """
        Update a specific review by ID.

        Args:
          annotation: Corresponding annotation

          accepted: Accepted or rejected (if false) flag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/api/annotation-reviews/{id}/",
            body=await async_maybe_transform(
                {
                    "annotation": annotation,
                    "accepted": accepted,
                    "comment": comment,
                    "last_annotation_history": last_annotation_history,
                    "result": result,
                },
                annotation_review_update_params.AnnotationReviewUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationReview,
        )

    async def list(
        self,
        *,
        annotation: str | NotGiven = NOT_GIVEN,
        annotation_task_project: str | NotGiven = NOT_GIVEN,
        ordering: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationReviewListResponse:
        """
        List all reviews for a specific annotation ID.

        Args:
          annotation: annotation

          annotation_task_project: annotation**task**project

          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/annotation-reviews/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "annotation": annotation,
                        "annotation_task_project": annotation_task_project,
                        "ordering": ordering,
                    },
                    annotation_review_list_params.AnnotationReviewListParams,
                ),
            ),
            cast_to=AnnotationReviewListResponse,
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
        Delete a review by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/annotation-reviews/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def overwrite(
        self,
        id: int,
        *,
        annotation: int,
        accepted: bool | NotGiven = NOT_GIVEN,
        comment: Optional[str] | NotGiven = NOT_GIVEN,
        last_annotation_history: Optional[int] | NotGiven = NOT_GIVEN,
        result: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationReview:
        """
        Overwrite a specific review by ID.

        Args:
          annotation: Corresponding annotation

          accepted: Accepted or rejected (if false) flag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/api/annotation-reviews/{id}/",
            body=await async_maybe_transform(
                {
                    "annotation": annotation,
                    "accepted": accepted,
                    "comment": comment,
                    "last_annotation_history": last_annotation_history,
                    "result": result,
                },
                annotation_review_overwrite_params.AnnotationReviewOverwriteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotationReview,
        )


class AnnotationReviewsResourceWithRawResponse:
    def __init__(self, annotation_reviews: AnnotationReviewsResource) -> None:
        self._annotation_reviews = annotation_reviews

        self.create = to_raw_response_wrapper(
            annotation_reviews.create,
        )
        self.retrieve = to_raw_response_wrapper(
            annotation_reviews.retrieve,
        )
        self.update = to_raw_response_wrapper(
            annotation_reviews.update,
        )
        self.list = to_raw_response_wrapper(
            annotation_reviews.list,
        )
        self.delete = to_raw_response_wrapper(
            annotation_reviews.delete,
        )
        self.overwrite = to_raw_response_wrapper(
            annotation_reviews.overwrite,
        )


class AsyncAnnotationReviewsResourceWithRawResponse:
    def __init__(self, annotation_reviews: AsyncAnnotationReviewsResource) -> None:
        self._annotation_reviews = annotation_reviews

        self.create = async_to_raw_response_wrapper(
            annotation_reviews.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            annotation_reviews.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            annotation_reviews.update,
        )
        self.list = async_to_raw_response_wrapper(
            annotation_reviews.list,
        )
        self.delete = async_to_raw_response_wrapper(
            annotation_reviews.delete,
        )
        self.overwrite = async_to_raw_response_wrapper(
            annotation_reviews.overwrite,
        )


class AnnotationReviewsResourceWithStreamingResponse:
    def __init__(self, annotation_reviews: AnnotationReviewsResource) -> None:
        self._annotation_reviews = annotation_reviews

        self.create = to_streamed_response_wrapper(
            annotation_reviews.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            annotation_reviews.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            annotation_reviews.update,
        )
        self.list = to_streamed_response_wrapper(
            annotation_reviews.list,
        )
        self.delete = to_streamed_response_wrapper(
            annotation_reviews.delete,
        )
        self.overwrite = to_streamed_response_wrapper(
            annotation_reviews.overwrite,
        )


class AsyncAnnotationReviewsResourceWithStreamingResponse:
    def __init__(self, annotation_reviews: AsyncAnnotationReviewsResource) -> None:
        self._annotation_reviews = annotation_reviews

        self.create = async_to_streamed_response_wrapper(
            annotation_reviews.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            annotation_reviews.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            annotation_reviews.update,
        )
        self.list = async_to_streamed_response_wrapper(
            annotation_reviews.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            annotation_reviews.delete,
        )
        self.overwrite = async_to_streamed_response_wrapper(
            annotation_reviews.overwrite,
        )
