# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import (
    make_request_options,
)
from .....types.api.dataset_storages.azure import column_retrieve_params

__all__ = ["ColumnsResource", "AsyncColumnsResource"]


class ColumnsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ColumnsResourceWithRawResponse:
        return ColumnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ColumnsResourceWithStreamingResponse:
        return ColumnsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: int,
        *,
        ordering: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Retrieves column names from users JSON/blob data in bucket

        Args:
          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/dataset-storages/azure/{id}/columns/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ordering": ordering}, column_retrieve_params.ColumnRetrieveParams),
            ),
            cast_to=NoneType,
        )


class AsyncColumnsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncColumnsResourceWithRawResponse:
        return AsyncColumnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncColumnsResourceWithStreamingResponse:
        return AsyncColumnsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: int,
        *,
        ordering: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Retrieves column names from users JSON/blob data in bucket

        Args:
          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/dataset-storages/azure/{id}/columns/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ordering": ordering}, column_retrieve_params.ColumnRetrieveParams),
            ),
            cast_to=NoneType,
        )


class ColumnsResourceWithRawResponse:
    def __init__(self, columns: ColumnsResource) -> None:
        self._columns = columns

        self.retrieve = to_raw_response_wrapper(
            columns.retrieve,
        )


class AsyncColumnsResourceWithRawResponse:
    def __init__(self, columns: AsyncColumnsResource) -> None:
        self._columns = columns

        self.retrieve = async_to_raw_response_wrapper(
            columns.retrieve,
        )


class ColumnsResourceWithStreamingResponse:
    def __init__(self, columns: ColumnsResource) -> None:
        self._columns = columns

        self.retrieve = to_streamed_response_wrapper(
            columns.retrieve,
        )


class AsyncColumnsResourceWithStreamingResponse:
    def __init__(self, columns: AsyncColumnsResource) -> None:
        self._columns = columns

        self.retrieve = async_to_streamed_response_wrapper(
            columns.retrieve,
        )
