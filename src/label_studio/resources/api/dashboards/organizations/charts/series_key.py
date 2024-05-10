# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import (
    make_request_options,
)

__all__ = ["SeriesKeyResource", "AsyncSeriesKeyResource"]


class SeriesKeyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SeriesKeyResourceWithRawResponse:
        return SeriesKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeriesKeyResourceWithStreamingResponse:
        return SeriesKeyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        series_key: str,
        *,
        id: str,
        chart_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not chart_key:
            raise ValueError(f"Expected a non-empty value for `chart_key` but received {chart_key!r}")
        if not series_key:
            raise ValueError(f"Expected a non-empty value for `series_key` but received {series_key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/dashboards/organizations/{id}/charts/{chart_key}/{series_key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSeriesKeyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSeriesKeyResourceWithRawResponse:
        return AsyncSeriesKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeriesKeyResourceWithStreamingResponse:
        return AsyncSeriesKeyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        series_key: str,
        *,
        id: str,
        chart_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not chart_key:
            raise ValueError(f"Expected a non-empty value for `chart_key` but received {chart_key!r}")
        if not series_key:
            raise ValueError(f"Expected a non-empty value for `series_key` but received {series_key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/dashboards/organizations/{id}/charts/{chart_key}/{series_key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SeriesKeyResourceWithRawResponse:
    def __init__(self, series_key: SeriesKeyResource) -> None:
        self._series_key = series_key

        self.retrieve = to_raw_response_wrapper(
            series_key.retrieve,
        )


class AsyncSeriesKeyResourceWithRawResponse:
    def __init__(self, series_key: AsyncSeriesKeyResource) -> None:
        self._series_key = series_key

        self.retrieve = async_to_raw_response_wrapper(
            series_key.retrieve,
        )


class SeriesKeyResourceWithStreamingResponse:
    def __init__(self, series_key: SeriesKeyResource) -> None:
        self._series_key = series_key

        self.retrieve = to_streamed_response_wrapper(
            series_key.retrieve,
        )


class AsyncSeriesKeyResourceWithStreamingResponse:
    def __init__(self, series_key: AsyncSeriesKeyResource) -> None:
        self._series_key = series_key

        self.retrieve = async_to_streamed_response_wrapper(
            series_key.retrieve,
        )
