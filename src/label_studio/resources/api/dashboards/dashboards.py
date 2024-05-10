# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)
from .organizations.organizations import OrganizationsResource, AsyncOrganizationsResource

__all__ = ["DashboardsResource", "AsyncDashboardsResource"]


class DashboardsResource(SyncAPIResource):
    @cached_property
    def organizations(self) -> OrganizationsResource:
        return OrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DashboardsResourceWithRawResponse:
        return DashboardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DashboardsResourceWithStreamingResponse:
        return DashboardsResourceWithStreamingResponse(self)


class AsyncDashboardsResource(AsyncAPIResource):
    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDashboardsResourceWithRawResponse:
        return AsyncDashboardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDashboardsResourceWithStreamingResponse:
        return AsyncDashboardsResourceWithStreamingResponse(self)


class DashboardsResourceWithRawResponse:
    def __init__(self, dashboards: DashboardsResource) -> None:
        self._dashboards = dashboards

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._dashboards.organizations)


class AsyncDashboardsResourceWithRawResponse:
    def __init__(self, dashboards: AsyncDashboardsResource) -> None:
        self._dashboards = dashboards

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._dashboards.organizations)


class DashboardsResourceWithStreamingResponse:
    def __init__(self, dashboards: DashboardsResource) -> None:
        self._dashboards = dashboards

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._dashboards.organizations)


class AsyncDashboardsResourceWithStreamingResponse:
    def __init__(self, dashboards: AsyncDashboardsResource) -> None:
        self._dashboards = dashboards

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._dashboards.organizations)
