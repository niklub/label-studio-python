# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .columns import (
    ColumnsResource,
    AsyncColumnsResource,
    ColumnsResourceWithRawResponse,
    AsyncColumnsResourceWithRawResponse,
    ColumnsResourceWithStreamingResponse,
    AsyncColumnsResourceWithStreamingResponse,
)
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
from .....types.api.dataset_storages import (
    azure_list_params,
    azure_create_params,
    azure_update_params,
    azure_validate_params,
    azure_check_for_records_params,
)
from .....types.api.dataset_storages.azure_list_response import AzureListResponse
from .....types.api.dataset_storages.azure_dataset_storage import AzureDatasetStorage

__all__ = ["AzureResource", "AsyncAzureResource"]


class AzureResource(SyncAPIResource):
    @cached_property
    def columns(self) -> ColumnsResource:
        return ColumnsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AzureResourceWithRawResponse:
        return AzureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AzureResourceWithStreamingResponse:
        return AzureResourceWithStreamingResponse(self)

    def create(
        self,
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
        Create a new Azure import storage connection.

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
        return self._post(
            "/api/dataset-storages/azure/",
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
                azure_create_params.AzureCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AzureDatasetStorage,
        )

    def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AzureDatasetStorage:
        """
        Get a specific Azure import storage connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/dataset-storages/azure/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AzureDatasetStorage,
        )

    def update(
        self,
        id: int,
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
        Update a specific Azure import storage connection.

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
        return self._patch(
            f"/api/dataset-storages/azure/{id}/",
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
                azure_update_params.AzureUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AzureDatasetStorage,
        )

    def list(
        self,
        *,
        dataset: int | NotGiven = NOT_GIVEN,
        ordering: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AzureListResponse:
        """
        Get a list of all Azure import storage connections.

        Args:
          dataset: Dataset ID

          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/dataset-storages/azure/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset": dataset,
                        "ordering": ordering,
                    },
                    azure_list_params.AzureListParams,
                ),
            ),
            cast_to=AzureListResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a specific Azure import storage connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/dataset-storages/azure/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def check_for_records(
        self,
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
        Checks for existence of records matching the file pattern in the bucket/prefix

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
        return self._post(
            "/api/dataset-storages/azure/check-for-records/",
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
                azure_check_for_records_params.AzureCheckForRecordsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AzureDatasetStorage,
        )

    def validate(
        self,
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
        Validate a specific Azure import storage connection.

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
        return self._post(
            "/api/dataset-storages/azure/validate/",
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
                azure_validate_params.AzureValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AzureDatasetStorage,
        )


class AsyncAzureResource(AsyncAPIResource):
    @cached_property
    def columns(self) -> AsyncColumnsResource:
        return AsyncColumnsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAzureResourceWithRawResponse:
        return AsyncAzureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAzureResourceWithStreamingResponse:
        return AsyncAzureResourceWithStreamingResponse(self)

    async def create(
        self,
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
        Create a new Azure import storage connection.

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
        return await self._post(
            "/api/dataset-storages/azure/",
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
                azure_create_params.AzureCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AzureDatasetStorage,
        )

    async def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AzureDatasetStorage:
        """
        Get a specific Azure import storage connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/dataset-storages/azure/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AzureDatasetStorage,
        )

    async def update(
        self,
        id: int,
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
        Update a specific Azure import storage connection.

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
        return await self._patch(
            f"/api/dataset-storages/azure/{id}/",
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
                azure_update_params.AzureUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AzureDatasetStorage,
        )

    async def list(
        self,
        *,
        dataset: int | NotGiven = NOT_GIVEN,
        ordering: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AzureListResponse:
        """
        Get a list of all Azure import storage connections.

        Args:
          dataset: Dataset ID

          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/dataset-storages/azure/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dataset": dataset,
                        "ordering": ordering,
                    },
                    azure_list_params.AzureListParams,
                ),
            ),
            cast_to=AzureListResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a specific Azure import storage connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/dataset-storages/azure/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def check_for_records(
        self,
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
        Checks for existence of records matching the file pattern in the bucket/prefix

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
        return await self._post(
            "/api/dataset-storages/azure/check-for-records/",
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
                azure_check_for_records_params.AzureCheckForRecordsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AzureDatasetStorage,
        )

    async def validate(
        self,
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
        Validate a specific Azure import storage connection.

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
        return await self._post(
            "/api/dataset-storages/azure/validate/",
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
                azure_validate_params.AzureValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AzureDatasetStorage,
        )


class AzureResourceWithRawResponse:
    def __init__(self, azure: AzureResource) -> None:
        self._azure = azure

        self.create = to_raw_response_wrapper(
            azure.create,
        )
        self.retrieve = to_raw_response_wrapper(
            azure.retrieve,
        )
        self.update = to_raw_response_wrapper(
            azure.update,
        )
        self.list = to_raw_response_wrapper(
            azure.list,
        )
        self.delete = to_raw_response_wrapper(
            azure.delete,
        )
        self.check_for_records = to_raw_response_wrapper(
            azure.check_for_records,
        )
        self.validate = to_raw_response_wrapper(
            azure.validate,
        )

    @cached_property
    def columns(self) -> ColumnsResourceWithRawResponse:
        return ColumnsResourceWithRawResponse(self._azure.columns)


class AsyncAzureResourceWithRawResponse:
    def __init__(self, azure: AsyncAzureResource) -> None:
        self._azure = azure

        self.create = async_to_raw_response_wrapper(
            azure.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            azure.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            azure.update,
        )
        self.list = async_to_raw_response_wrapper(
            azure.list,
        )
        self.delete = async_to_raw_response_wrapper(
            azure.delete,
        )
        self.check_for_records = async_to_raw_response_wrapper(
            azure.check_for_records,
        )
        self.validate = async_to_raw_response_wrapper(
            azure.validate,
        )

    @cached_property
    def columns(self) -> AsyncColumnsResourceWithRawResponse:
        return AsyncColumnsResourceWithRawResponse(self._azure.columns)


class AzureResourceWithStreamingResponse:
    def __init__(self, azure: AzureResource) -> None:
        self._azure = azure

        self.create = to_streamed_response_wrapper(
            azure.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            azure.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            azure.update,
        )
        self.list = to_streamed_response_wrapper(
            azure.list,
        )
        self.delete = to_streamed_response_wrapper(
            azure.delete,
        )
        self.check_for_records = to_streamed_response_wrapper(
            azure.check_for_records,
        )
        self.validate = to_streamed_response_wrapper(
            azure.validate,
        )

    @cached_property
    def columns(self) -> ColumnsResourceWithStreamingResponse:
        return ColumnsResourceWithStreamingResponse(self._azure.columns)


class AsyncAzureResourceWithStreamingResponse:
    def __init__(self, azure: AsyncAzureResource) -> None:
        self._azure = azure

        self.create = async_to_streamed_response_wrapper(
            azure.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            azure.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            azure.update,
        )
        self.list = async_to_streamed_response_wrapper(
            azure.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            azure.delete,
        )
        self.check_for_records = async_to_streamed_response_wrapper(
            azure.check_for_records,
        )
        self.validate = async_to_streamed_response_wrapper(
            azure.validate,
        )

    @cached_property
    def columns(self) -> AsyncColumnsResourceWithStreamingResponse:
        return AsyncColumnsResourceWithStreamingResponse(self._azure.columns)
