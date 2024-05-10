# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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

__all__ = ["DatasetStoragesTypesResource", "AsyncDatasetStoragesTypesResource"]


class DatasetStoragesTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetStoragesTypesResourceWithRawResponse:
        return DatasetStoragesTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetStoragesTypesResourceWithStreamingResponse:
        return DatasetStoragesTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Retrieve a list of the dataset storages types."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/dataset-storages/types/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDatasetStoragesTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetStoragesTypesResourceWithRawResponse:
        return AsyncDatasetStoragesTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetStoragesTypesResourceWithStreamingResponse:
        return AsyncDatasetStoragesTypesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Retrieve a list of the dataset storages types."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/dataset-storages/types/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DatasetStoragesTypesResourceWithRawResponse:
    def __init__(self, dataset_storages_types: DatasetStoragesTypesResource) -> None:
        self._dataset_storages_types = dataset_storages_types

        self.list = to_raw_response_wrapper(
            dataset_storages_types.list,
        )


class AsyncDatasetStoragesTypesResourceWithRawResponse:
    def __init__(self, dataset_storages_types: AsyncDatasetStoragesTypesResource) -> None:
        self._dataset_storages_types = dataset_storages_types

        self.list = async_to_raw_response_wrapper(
            dataset_storages_types.list,
        )


class DatasetStoragesTypesResourceWithStreamingResponse:
    def __init__(self, dataset_storages_types: DatasetStoragesTypesResource) -> None:
        self._dataset_storages_types = dataset_storages_types

        self.list = to_streamed_response_wrapper(
            dataset_storages_types.list,
        )


class AsyncDatasetStoragesTypesResourceWithStreamingResponse:
    def __init__(self, dataset_storages_types: AsyncDatasetStoragesTypesResource) -> None:
        self._dataset_storages_types = dataset_storages_types

        self.list = async_to_streamed_response_wrapper(
            dataset_storages_types.list,
        )
