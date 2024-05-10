# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.dataset_storages import azure_sync_params
from ...types.api.dataset_storages.azure_dataset_storage import AzureDatasetStorage

__all__ = ["AzureResource", "AsyncAzureResource"]


class AzureResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AzureResourceWithRawResponse:
        return AzureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AzureResourceWithStreamingResponse:
        return AzureResourceWithStreamingResponse(self)

    def sync(
        self,
        id: str,
        *,
        dataset: int,
        account_key: Optional[str] | NotGiven = NOT_GIVEN,
        account_name: Optional[str] | NotGiven = NOT_GIVEN,
        container: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        last_sync: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_sync_count: Optional[int] | NotGiven = NOT_GIVEN,
        last_sync_job: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        presign: bool | NotGiven = NOT_GIVEN,
        presign_ttl: int | NotGiven = NOT_GIVEN,
        regex_filter: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["initialized", "queued", "in_progress", "failed", "completed"] | NotGiven = NOT_GIVEN,
        synced: bool | NotGiven = NOT_GIVEN,
        synchronizable: bool | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        traceback: Optional[str] | NotGiven = NOT_GIVEN,
        use_blob_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AzureDatasetStorage:
        """
        Sync tasks from an Azure import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          account_key: Azure Blob account key

          account_name: Azure Blob account name

          container: Azure blob container

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: Azure blob prefix name

          presign_ttl: Presigned URLs TTL (in minutes)

          regex_filter: Cloud storage regex for filtering objects

          synced: Flag if dataset has been previously synced or not

          title: Cloud storage title

          traceback: Traceback report for the last failed sync

          use_blob_urls: Interpret objects as BLOBs and generate URLs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/dataset-storages/azure/{id}/sync/",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "account_key": account_key,
                    "account_name": account_name,
                    "container": container,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "last_sync": last_sync,
                    "last_sync_count": last_sync_count,
                    "last_sync_job": last_sync_job,
                    "meta": meta,
                    "prefix": prefix,
                    "presign": presign,
                    "presign_ttl": presign_ttl,
                    "regex_filter": regex_filter,
                    "status": status,
                    "synced": synced,
                    "synchronizable": synchronizable,
                    "title": title,
                    "traceback": traceback,
                    "use_blob_urls": use_blob_urls,
                },
                azure_sync_params.AzureSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AzureDatasetStorage,
        )


class AsyncAzureResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAzureResourceWithRawResponse:
        return AsyncAzureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAzureResourceWithStreamingResponse:
        return AsyncAzureResourceWithStreamingResponse(self)

    async def sync(
        self,
        id: str,
        *,
        dataset: int,
        account_key: Optional[str] | NotGiven = NOT_GIVEN,
        account_name: Optional[str] | NotGiven = NOT_GIVEN,
        container: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        last_sync: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_sync_count: Optional[int] | NotGiven = NOT_GIVEN,
        last_sync_job: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        presign: bool | NotGiven = NOT_GIVEN,
        presign_ttl: int | NotGiven = NOT_GIVEN,
        regex_filter: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["initialized", "queued", "in_progress", "failed", "completed"] | NotGiven = NOT_GIVEN,
        synced: bool | NotGiven = NOT_GIVEN,
        synchronizable: bool | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        traceback: Optional[str] | NotGiven = NOT_GIVEN,
        use_blob_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AzureDatasetStorage:
        """
        Sync tasks from an Azure import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          account_key: Azure Blob account key

          account_name: Azure Blob account name

          container: Azure blob container

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: Azure blob prefix name

          presign_ttl: Presigned URLs TTL (in minutes)

          regex_filter: Cloud storage regex for filtering objects

          synced: Flag if dataset has been previously synced or not

          title: Cloud storage title

          traceback: Traceback report for the last failed sync

          use_blob_urls: Interpret objects as BLOBs and generate URLs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/dataset-storages/azure/{id}/sync/",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "account_key": account_key,
                    "account_name": account_name,
                    "container": container,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "last_sync": last_sync,
                    "last_sync_count": last_sync_count,
                    "last_sync_job": last_sync_job,
                    "meta": meta,
                    "prefix": prefix,
                    "presign": presign,
                    "presign_ttl": presign_ttl,
                    "regex_filter": regex_filter,
                    "status": status,
                    "synced": synced,
                    "synchronizable": synchronizable,
                    "title": title,
                    "traceback": traceback,
                    "use_blob_urls": use_blob_urls,
                },
                azure_sync_params.AzureSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AzureDatasetStorage,
        )


class AzureResourceWithRawResponse:
    def __init__(self, azure: AzureResource) -> None:
        self._azure = azure

        self.sync = to_raw_response_wrapper(
            azure.sync,
        )


class AsyncAzureResourceWithRawResponse:
    def __init__(self, azure: AsyncAzureResource) -> None:
        self._azure = azure

        self.sync = async_to_raw_response_wrapper(
            azure.sync,
        )


class AzureResourceWithStreamingResponse:
    def __init__(self, azure: AzureResource) -> None:
        self._azure = azure

        self.sync = to_streamed_response_wrapper(
            azure.sync,
        )


class AsyncAzureResourceWithStreamingResponse:
    def __init__(self, azure: AsyncAzureResource) -> None:
        self._azure = azure

        self.sync = async_to_streamed_response_wrapper(
            azure.sync,
        )
