# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .charts import (
    ChartsResource,
    AsyncChartsResource,
    ChartsResourceWithRawResponse,
    AsyncChartsResourceWithRawResponse,
    ChartsResourceWithStreamingResponse,
    AsyncChartsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .charts.charts import ChartsResource, AsyncChartsResource

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def charts(self) -> ChartsResource:
        return ChartsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self)


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def charts(self) -> AsyncChartsResource:
        return AsyncChartsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self)


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

    @cached_property
    def charts(self) -> ChartsResourceWithRawResponse:
        return ChartsResourceWithRawResponse(self._organizations.charts)


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

    @cached_property
    def charts(self) -> AsyncChartsResourceWithRawResponse:
        return AsyncChartsResourceWithRawResponse(self._organizations.charts)


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

    @cached_property
    def charts(self) -> ChartsResourceWithStreamingResponse:
        return ChartsResourceWithStreamingResponse(self._organizations.charts)


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

    @cached_property
    def charts(self) -> AsyncChartsResourceWithStreamingResponse:
        return AsyncChartsResourceWithStreamingResponse(self._organizations.charts)
