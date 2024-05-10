# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .azure import (
    AzureResource,
    AsyncAzureResource,
    AzureResourceWithRawResponse,
    AsyncAzureResourceWithRawResponse,
    AzureResourceWithStreamingResponse,
    AsyncAzureResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .azure.azure import AzureResource, AsyncAzureResource
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.api import dataset_storage_list_params
from ...._base_client import (
    make_request_options,
)

__all__ = ["DatasetStoragesResource", "AsyncDatasetStoragesResource"]


class DatasetStoragesResource(SyncAPIResource):
    @cached_property
    def azure(self) -> AzureResource:
        return AzureResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetStoragesResourceWithRawResponse:
        return DatasetStoragesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetStoragesResourceWithStreamingResponse:
        return DatasetStoragesResourceWithStreamingResponse(self)

    def list(
        self,
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
        Retrieve a list of the dataset storages of all types with their IDs.

        Args:
          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/dataset-storages/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ordering": ordering}, dataset_storage_list_params.DatasetStorageListParams),
            ),
            cast_to=NoneType,
        )


class AsyncDatasetStoragesResource(AsyncAPIResource):
    @cached_property
    def azure(self) -> AsyncAzureResource:
        return AsyncAzureResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetStoragesResourceWithRawResponse:
        return AsyncDatasetStoragesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetStoragesResourceWithStreamingResponse:
        return AsyncDatasetStoragesResourceWithStreamingResponse(self)

    async def list(
        self,
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
        Retrieve a list of the dataset storages of all types with their IDs.

        Args:
          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/dataset-storages/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"ordering": ordering}, dataset_storage_list_params.DatasetStorageListParams
                ),
            ),
            cast_to=NoneType,
        )


class DatasetStoragesResourceWithRawResponse:
    def __init__(self, dataset_storages: DatasetStoragesResource) -> None:
        self._dataset_storages = dataset_storages

        self.list = to_raw_response_wrapper(
            dataset_storages.list,
        )

    @cached_property
    def azure(self) -> AzureResourceWithRawResponse:
        return AzureResourceWithRawResponse(self._dataset_storages.azure)


class AsyncDatasetStoragesResourceWithRawResponse:
    def __init__(self, dataset_storages: AsyncDatasetStoragesResource) -> None:
        self._dataset_storages = dataset_storages

        self.list = async_to_raw_response_wrapper(
            dataset_storages.list,
        )

    @cached_property
    def azure(self) -> AsyncAzureResourceWithRawResponse:
        return AsyncAzureResourceWithRawResponse(self._dataset_storages.azure)


class DatasetStoragesResourceWithStreamingResponse:
    def __init__(self, dataset_storages: DatasetStoragesResource) -> None:
        self._dataset_storages = dataset_storages

        self.list = to_streamed_response_wrapper(
            dataset_storages.list,
        )

    @cached_property
    def azure(self) -> AzureResourceWithStreamingResponse:
        return AzureResourceWithStreamingResponse(self._dataset_storages.azure)


class AsyncDatasetStoragesResourceWithStreamingResponse:
    def __init__(self, dataset_storages: AsyncDatasetStoragesResource) -> None:
        self._dataset_storages = dataset_storages

        self.list = async_to_streamed_response_wrapper(
            dataset_storages.list,
        )

    @cached_property
    def azure(self) -> AsyncAzureResourceWithStreamingResponse:
        return AsyncAzureResourceWithStreamingResponse(self._dataset_storages.azure)
