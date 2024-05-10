# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .dashboards import (
    DashboardsResource,
    AsyncDashboardsResource,
    DashboardsResourceWithRawResponse,
    AsyncDashboardsResourceWithRawResponse,
    DashboardsResourceWithStreamingResponse,
    AsyncDashboardsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .dataset_storages import (
    DatasetStoragesResource,
    AsyncDatasetStoragesResource,
    DatasetStoragesResourceWithRawResponse,
    AsyncDatasetStoragesResourceWithRawResponse,
    DatasetStoragesResourceWithStreamingResponse,
    AsyncDatasetStoragesResourceWithStreamingResponse,
)
from .dashboards.dashboards import DashboardsResource, AsyncDashboardsResource
from .dataset_storages.dataset_storages import DatasetStoragesResource, AsyncDatasetStoragesResource

__all__ = ["APIResource", "AsyncAPIResource"]


class APIResource(SyncAPIResource):
    @cached_property
    def dashboards(self) -> DashboardsResource:
        return DashboardsResource(self._client)

    @cached_property
    def dataset_storages(self) -> DatasetStoragesResource:
        return DatasetStoragesResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIResourceWithRawResponse:
        return APIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIResourceWithStreamingResponse:
        return APIResourceWithStreamingResponse(self)


class AsyncAPIResource(AsyncAPIResource):
    @cached_property
    def dashboards(self) -> AsyncDashboardsResource:
        return AsyncDashboardsResource(self._client)

    @cached_property
    def dataset_storages(self) -> AsyncDatasetStoragesResource:
        return AsyncDatasetStoragesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIResourceWithRawResponse:
        return AsyncAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIResourceWithStreamingResponse:
        return AsyncAPIResourceWithStreamingResponse(self)


class APIResourceWithRawResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

    @cached_property
    def dashboards(self) -> DashboardsResourceWithRawResponse:
        return DashboardsResourceWithRawResponse(self._api.dashboards)

    @cached_property
    def dataset_storages(self) -> DatasetStoragesResourceWithRawResponse:
        return DatasetStoragesResourceWithRawResponse(self._api.dataset_storages)


class AsyncAPIResourceWithRawResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

    @cached_property
    def dashboards(self) -> AsyncDashboardsResourceWithRawResponse:
        return AsyncDashboardsResourceWithRawResponse(self._api.dashboards)

    @cached_property
    def dataset_storages(self) -> AsyncDatasetStoragesResourceWithRawResponse:
        return AsyncDatasetStoragesResourceWithRawResponse(self._api.dataset_storages)


class APIResourceWithStreamingResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

    @cached_property
    def dashboards(self) -> DashboardsResourceWithStreamingResponse:
        return DashboardsResourceWithStreamingResponse(self._api.dashboards)

    @cached_property
    def dataset_storages(self) -> DatasetStoragesResourceWithStreamingResponse:
        return DatasetStoragesResourceWithStreamingResponse(self._api.dataset_storages)


class AsyncAPIResourceWithStreamingResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

    @cached_property
    def dashboards(self) -> AsyncDashboardsResourceWithStreamingResponse:
        return AsyncDashboardsResourceWithStreamingResponse(self._api.dashboards)

    @cached_property
    def dataset_storages(self) -> AsyncDatasetStoragesResourceWithStreamingResponse:
        return AsyncDatasetStoragesResourceWithStreamingResponse(self._api.dataset_storages)
