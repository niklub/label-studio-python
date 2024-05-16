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
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)
from ....types.dataset_storages import (
    gc_list_params,
    gc_sync_params,
    gc_create_params,
    gc_update_params,
    gc_validate_params,
    gc_check_for_records_params,
)
from ....types.dataset_storages.gc_list_response import GcListResponse
from ....types.api.dataset_storages.gcs_dataset_storage import GcsDatasetStorage

__all__ = ["GcsResource", "AsyncGcsResource"]


class GcsResource(SyncAPIResource):
    @cached_property
    def columns(self) -> ColumnsResource:
        return ColumnsResource(self._client)

    @cached_property
    def with_raw_response(self) -> GcsResourceWithRawResponse:
        return GcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GcsResourceWithStreamingResponse:
        return GcsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        dataset: int,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        google_application_credentials: Optional[str] | NotGiven = NOT_GIVEN,
        google_project_id: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> GcsDatasetStorage:
        """
        Create a new GCS import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          bucket: GCS bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          google_application_credentials: The content of GOOGLE_APPLICATION_CREDENTIALS json file

          google_project_id: Google project ID

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: GCS bucket prefix

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
            "/api/dataset-storages/gcs/",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "google_application_credentials": google_application_credentials,
                    "google_project_id": google_project_id,
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
                gc_create_params.GcCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GcsDatasetStorage,
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
    ) -> GcsDatasetStorage:
        """
        Get a specific GCS import storage connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/dataset-storages/gcs/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GcsDatasetStorage,
        )

    def update(
        self,
        id: int,
        *,
        dataset: int,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        google_application_credentials: Optional[str] | NotGiven = NOT_GIVEN,
        google_project_id: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> GcsDatasetStorage:
        """
        Update a specific GCS import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          bucket: GCS bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          google_application_credentials: The content of GOOGLE_APPLICATION_CREDENTIALS json file

          google_project_id: Google project ID

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: GCS bucket prefix

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
            f"/api/dataset-storages/gcs/{id}/",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "google_application_credentials": google_application_credentials,
                    "google_project_id": google_project_id,
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
                gc_update_params.GcUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GcsDatasetStorage,
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
    ) -> GcListResponse:
        """
        Get a list of all GCS import storage connections.

        Args:
          dataset: Dataset ID

          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/dataset-storages/gcs/",
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
                    gc_list_params.GcListParams,
                ),
            ),
            cast_to=GcListResponse,
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
        Delete a specific GCS import storage connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/dataset-storages/gcs/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def check_for_records(
        self,
        *,
        dataset: int,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        google_application_credentials: Optional[str] | NotGiven = NOT_GIVEN,
        google_project_id: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> GcsDatasetStorage:
        """
        Checks for existence of records matching the file pattern in the bucket/prefix

        Args:
          dataset: A unique integer value identifying this dataset.

          bucket: GCS bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          google_application_credentials: The content of GOOGLE_APPLICATION_CREDENTIALS json file

          google_project_id: Google project ID

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: GCS bucket prefix

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
            "/api/dataset-storages/gcs/check-for-records/",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "google_application_credentials": google_application_credentials,
                    "google_project_id": google_project_id,
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
                gc_check_for_records_params.GcCheckForRecordsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GcsDatasetStorage,
        )

    def sync(
        self,
        id: str,
        *,
        dataset: int,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        google_application_credentials: Optional[str] | NotGiven = NOT_GIVEN,
        google_project_id: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> GcsDatasetStorage:
        """
        Sync tasks from an GCS import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          bucket: GCS bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          google_application_credentials: The content of GOOGLE_APPLICATION_CREDENTIALS json file

          google_project_id: Google project ID

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: GCS bucket prefix

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
            f"/api/dataset-storages/gcs/{id}/sync/",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "google_application_credentials": google_application_credentials,
                    "google_project_id": google_project_id,
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
                gc_sync_params.GcSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GcsDatasetStorage,
        )

    def validate(
        self,
        *,
        dataset: int,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        google_application_credentials: Optional[str] | NotGiven = NOT_GIVEN,
        google_project_id: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> GcsDatasetStorage:
        """
        Validate a specific GCS import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          bucket: GCS bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          google_application_credentials: The content of GOOGLE_APPLICATION_CREDENTIALS json file

          google_project_id: Google project ID

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: GCS bucket prefix

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
            "/api/dataset-storages/gcs/validate/",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "google_application_credentials": google_application_credentials,
                    "google_project_id": google_project_id,
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
                gc_validate_params.GcValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GcsDatasetStorage,
        )


class AsyncGcsResource(AsyncAPIResource):
    @cached_property
    def columns(self) -> AsyncColumnsResource:
        return AsyncColumnsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGcsResourceWithRawResponse:
        return AsyncGcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGcsResourceWithStreamingResponse:
        return AsyncGcsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        dataset: int,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        google_application_credentials: Optional[str] | NotGiven = NOT_GIVEN,
        google_project_id: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> GcsDatasetStorage:
        """
        Create a new GCS import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          bucket: GCS bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          google_application_credentials: The content of GOOGLE_APPLICATION_CREDENTIALS json file

          google_project_id: Google project ID

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: GCS bucket prefix

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
            "/api/dataset-storages/gcs/",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "google_application_credentials": google_application_credentials,
                    "google_project_id": google_project_id,
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
                gc_create_params.GcCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GcsDatasetStorage,
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
    ) -> GcsDatasetStorage:
        """
        Get a specific GCS import storage connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/dataset-storages/gcs/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GcsDatasetStorage,
        )

    async def update(
        self,
        id: int,
        *,
        dataset: int,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        google_application_credentials: Optional[str] | NotGiven = NOT_GIVEN,
        google_project_id: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> GcsDatasetStorage:
        """
        Update a specific GCS import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          bucket: GCS bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          google_application_credentials: The content of GOOGLE_APPLICATION_CREDENTIALS json file

          google_project_id: Google project ID

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: GCS bucket prefix

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
            f"/api/dataset-storages/gcs/{id}/",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "google_application_credentials": google_application_credentials,
                    "google_project_id": google_project_id,
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
                gc_update_params.GcUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GcsDatasetStorage,
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
    ) -> GcListResponse:
        """
        Get a list of all GCS import storage connections.

        Args:
          dataset: Dataset ID

          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/dataset-storages/gcs/",
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
                    gc_list_params.GcListParams,
                ),
            ),
            cast_to=GcListResponse,
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
        Delete a specific GCS import storage connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/dataset-storages/gcs/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def check_for_records(
        self,
        *,
        dataset: int,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        google_application_credentials: Optional[str] | NotGiven = NOT_GIVEN,
        google_project_id: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> GcsDatasetStorage:
        """
        Checks for existence of records matching the file pattern in the bucket/prefix

        Args:
          dataset: A unique integer value identifying this dataset.

          bucket: GCS bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          google_application_credentials: The content of GOOGLE_APPLICATION_CREDENTIALS json file

          google_project_id: Google project ID

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: GCS bucket prefix

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
            "/api/dataset-storages/gcs/check-for-records/",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "google_application_credentials": google_application_credentials,
                    "google_project_id": google_project_id,
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
                gc_check_for_records_params.GcCheckForRecordsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GcsDatasetStorage,
        )

    async def sync(
        self,
        id: str,
        *,
        dataset: int,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        google_application_credentials: Optional[str] | NotGiven = NOT_GIVEN,
        google_project_id: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> GcsDatasetStorage:
        """
        Sync tasks from an GCS import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          bucket: GCS bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          google_application_credentials: The content of GOOGLE_APPLICATION_CREDENTIALS json file

          google_project_id: Google project ID

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: GCS bucket prefix

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
            f"/api/dataset-storages/gcs/{id}/sync/",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "google_application_credentials": google_application_credentials,
                    "google_project_id": google_project_id,
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
                gc_sync_params.GcSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GcsDatasetStorage,
        )

    async def validate(
        self,
        *,
        dataset: int,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        google_application_credentials: Optional[str] | NotGiven = NOT_GIVEN,
        google_project_id: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> GcsDatasetStorage:
        """
        Validate a specific GCS import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          bucket: GCS bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          google_application_credentials: The content of GOOGLE_APPLICATION_CREDENTIALS json file

          google_project_id: Google project ID

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: GCS bucket prefix

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
            "/api/dataset-storages/gcs/validate/",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "google_application_credentials": google_application_credentials,
                    "google_project_id": google_project_id,
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
                gc_validate_params.GcValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GcsDatasetStorage,
        )


class GcsResourceWithRawResponse:
    def __init__(self, gcs: GcsResource) -> None:
        self._gcs = gcs

        self.create = to_raw_response_wrapper(
            gcs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            gcs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            gcs.update,
        )
        self.list = to_raw_response_wrapper(
            gcs.list,
        )
        self.delete = to_raw_response_wrapper(
            gcs.delete,
        )
        self.check_for_records = to_raw_response_wrapper(
            gcs.check_for_records,
        )
        self.sync = to_raw_response_wrapper(
            gcs.sync,
        )
        self.validate = to_raw_response_wrapper(
            gcs.validate,
        )

    @cached_property
    def columns(self) -> ColumnsResourceWithRawResponse:
        return ColumnsResourceWithRawResponse(self._gcs.columns)


class AsyncGcsResourceWithRawResponse:
    def __init__(self, gcs: AsyncGcsResource) -> None:
        self._gcs = gcs

        self.create = async_to_raw_response_wrapper(
            gcs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            gcs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            gcs.update,
        )
        self.list = async_to_raw_response_wrapper(
            gcs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            gcs.delete,
        )
        self.check_for_records = async_to_raw_response_wrapper(
            gcs.check_for_records,
        )
        self.sync = async_to_raw_response_wrapper(
            gcs.sync,
        )
        self.validate = async_to_raw_response_wrapper(
            gcs.validate,
        )

    @cached_property
    def columns(self) -> AsyncColumnsResourceWithRawResponse:
        return AsyncColumnsResourceWithRawResponse(self._gcs.columns)


class GcsResourceWithStreamingResponse:
    def __init__(self, gcs: GcsResource) -> None:
        self._gcs = gcs

        self.create = to_streamed_response_wrapper(
            gcs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            gcs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            gcs.update,
        )
        self.list = to_streamed_response_wrapper(
            gcs.list,
        )
        self.delete = to_streamed_response_wrapper(
            gcs.delete,
        )
        self.check_for_records = to_streamed_response_wrapper(
            gcs.check_for_records,
        )
        self.sync = to_streamed_response_wrapper(
            gcs.sync,
        )
        self.validate = to_streamed_response_wrapper(
            gcs.validate,
        )

    @cached_property
    def columns(self) -> ColumnsResourceWithStreamingResponse:
        return ColumnsResourceWithStreamingResponse(self._gcs.columns)


class AsyncGcsResourceWithStreamingResponse:
    def __init__(self, gcs: AsyncGcsResource) -> None:
        self._gcs = gcs

        self.create = async_to_streamed_response_wrapper(
            gcs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            gcs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            gcs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            gcs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            gcs.delete,
        )
        self.check_for_records = async_to_streamed_response_wrapper(
            gcs.check_for_records,
        )
        self.sync = async_to_streamed_response_wrapper(
            gcs.sync,
        )
        self.validate = async_to_streamed_response_wrapper(
            gcs.validate,
        )

    @cached_property
    def columns(self) -> AsyncColumnsResourceWithStreamingResponse:
        return AsyncColumnsResourceWithStreamingResponse(self._gcs.columns)
