# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .series_key import (
    SeriesKeyResource,
    AsyncSeriesKeyResource,
    SeriesKeyResourceWithRawResponse,
    AsyncSeriesKeyResourceWithRawResponse,
    SeriesKeyResourceWithStreamingResponse,
    AsyncSeriesKeyResourceWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ChartsResource", "AsyncChartsResource"]


class ChartsResource(SyncAPIResource):
    @cached_property
    def series_key(self) -> SeriesKeyResource:
        return SeriesKeyResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChartsResourceWithRawResponse:
        return ChartsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChartsResourceWithStreamingResponse:
        return ChartsResourceWithStreamingResponse(self)


class AsyncChartsResource(AsyncAPIResource):
    @cached_property
    def series_key(self) -> AsyncSeriesKeyResource:
        return AsyncSeriesKeyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChartsResourceWithRawResponse:
        return AsyncChartsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChartsResourceWithStreamingResponse:
        return AsyncChartsResourceWithStreamingResponse(self)


class ChartsResourceWithRawResponse:
    def __init__(self, charts: ChartsResource) -> None:
        self._charts = charts

    @cached_property
    def series_key(self) -> SeriesKeyResourceWithRawResponse:
        return SeriesKeyResourceWithRawResponse(self._charts.series_key)


class AsyncChartsResourceWithRawResponse:
    def __init__(self, charts: AsyncChartsResource) -> None:
        self._charts = charts

    @cached_property
    def series_key(self) -> AsyncSeriesKeyResourceWithRawResponse:
        return AsyncSeriesKeyResourceWithRawResponse(self._charts.series_key)


class ChartsResourceWithStreamingResponse:
    def __init__(self, charts: ChartsResource) -> None:
        self._charts = charts

    @cached_property
    def series_key(self) -> SeriesKeyResourceWithStreamingResponse:
        return SeriesKeyResourceWithStreamingResponse(self._charts.series_key)


class AsyncChartsResourceWithStreamingResponse:
    def __init__(self, charts: AsyncChartsResource) -> None:
        self._charts = charts

    @cached_property
    def series_key(self) -> AsyncSeriesKeyResourceWithStreamingResponse:
        return AsyncSeriesKeyResourceWithStreamingResponse(self._charts.series_key)
