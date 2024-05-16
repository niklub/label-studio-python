# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .s3 import (
    S3Resource,
    AsyncS3Resource,
    S3ResourceWithRawResponse,
    AsyncS3ResourceWithRawResponse,
    S3ResourceWithStreamingResponse,
    AsyncS3ResourceWithStreamingResponse,
)
from .gcs import (
    GcsResource,
    AsyncGcsResource,
    GcsResourceWithRawResponse,
    AsyncGcsResourceWithRawResponse,
    GcsResourceWithStreamingResponse,
    AsyncGcsResourceWithStreamingResponse,
)
from .azure import (
    AzureResource,
    AsyncAzureResource,
    AzureResourceWithRawResponse,
    AsyncAzureResourceWithRawResponse,
    AzureResourceWithStreamingResponse,
    AsyncAzureResourceWithStreamingResponse,
)
from .s3.s3 import S3Resource, AsyncS3Resource
from .types import (
    TypesResource,
    AsyncTypesResource,
    TypesResourceWithRawResponse,
    AsyncTypesResourceWithRawResponse,
    TypesResourceWithStreamingResponse,
    AsyncTypesResourceWithStreamingResponse,
)
from .gcs.gcs import GcsResource, AsyncGcsResource
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DatasetStoragesResource", "AsyncDatasetStoragesResource"]


class DatasetStoragesResource(SyncAPIResource):
    @cached_property
    def azure(self) -> AzureResource:
        return AzureResource(self._client)

    @cached_property
    def gcs(self) -> GcsResource:
        return GcsResource(self._client)

    @cached_property
    def s3(self) -> S3Resource:
        return S3Resource(self._client)

    @cached_property
    def types(self) -> TypesResource:
        return TypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetStoragesResourceWithRawResponse:
        return DatasetStoragesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetStoragesResourceWithStreamingResponse:
        return DatasetStoragesResourceWithStreamingResponse(self)


class AsyncDatasetStoragesResource(AsyncAPIResource):
    @cached_property
    def azure(self) -> AsyncAzureResource:
        return AsyncAzureResource(self._client)

    @cached_property
    def gcs(self) -> AsyncGcsResource:
        return AsyncGcsResource(self._client)

    @cached_property
    def s3(self) -> AsyncS3Resource:
        return AsyncS3Resource(self._client)

    @cached_property
    def types(self) -> AsyncTypesResource:
        return AsyncTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetStoragesResourceWithRawResponse:
        return AsyncDatasetStoragesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetStoragesResourceWithStreamingResponse:
        return AsyncDatasetStoragesResourceWithStreamingResponse(self)


class DatasetStoragesResourceWithRawResponse:
    def __init__(self, dataset_storages: DatasetStoragesResource) -> None:
        self._dataset_storages = dataset_storages

    @cached_property
    def azure(self) -> AzureResourceWithRawResponse:
        return AzureResourceWithRawResponse(self._dataset_storages.azure)

    @cached_property
    def gcs(self) -> GcsResourceWithRawResponse:
        return GcsResourceWithRawResponse(self._dataset_storages.gcs)

    @cached_property
    def s3(self) -> S3ResourceWithRawResponse:
        return S3ResourceWithRawResponse(self._dataset_storages.s3)

    @cached_property
    def types(self) -> TypesResourceWithRawResponse:
        return TypesResourceWithRawResponse(self._dataset_storages.types)


class AsyncDatasetStoragesResourceWithRawResponse:
    def __init__(self, dataset_storages: AsyncDatasetStoragesResource) -> None:
        self._dataset_storages = dataset_storages

    @cached_property
    def azure(self) -> AsyncAzureResourceWithRawResponse:
        return AsyncAzureResourceWithRawResponse(self._dataset_storages.azure)

    @cached_property
    def gcs(self) -> AsyncGcsResourceWithRawResponse:
        return AsyncGcsResourceWithRawResponse(self._dataset_storages.gcs)

    @cached_property
    def s3(self) -> AsyncS3ResourceWithRawResponse:
        return AsyncS3ResourceWithRawResponse(self._dataset_storages.s3)

    @cached_property
    def types(self) -> AsyncTypesResourceWithRawResponse:
        return AsyncTypesResourceWithRawResponse(self._dataset_storages.types)


class DatasetStoragesResourceWithStreamingResponse:
    def __init__(self, dataset_storages: DatasetStoragesResource) -> None:
        self._dataset_storages = dataset_storages

    @cached_property
    def azure(self) -> AzureResourceWithStreamingResponse:
        return AzureResourceWithStreamingResponse(self._dataset_storages.azure)

    @cached_property
    def gcs(self) -> GcsResourceWithStreamingResponse:
        return GcsResourceWithStreamingResponse(self._dataset_storages.gcs)

    @cached_property
    def s3(self) -> S3ResourceWithStreamingResponse:
        return S3ResourceWithStreamingResponse(self._dataset_storages.s3)

    @cached_property
    def types(self) -> TypesResourceWithStreamingResponse:
        return TypesResourceWithStreamingResponse(self._dataset_storages.types)


class AsyncDatasetStoragesResourceWithStreamingResponse:
    def __init__(self, dataset_storages: AsyncDatasetStoragesResource) -> None:
        self._dataset_storages = dataset_storages

    @cached_property
    def azure(self) -> AsyncAzureResourceWithStreamingResponse:
        return AsyncAzureResourceWithStreamingResponse(self._dataset_storages.azure)

    @cached_property
    def gcs(self) -> AsyncGcsResourceWithStreamingResponse:
        return AsyncGcsResourceWithStreamingResponse(self._dataset_storages.gcs)

    @cached_property
    def s3(self) -> AsyncS3ResourceWithStreamingResponse:
        return AsyncS3ResourceWithStreamingResponse(self._dataset_storages.s3)

    @cached_property
    def types(self) -> AsyncTypesResourceWithStreamingResponse:
        return AsyncTypesResourceWithStreamingResponse(self._dataset_storages.types)
