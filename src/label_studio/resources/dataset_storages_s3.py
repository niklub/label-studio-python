# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    dataset_storages_s3_list_params,
    dataset_storages_s3_sync_params,
    dataset_storages_s3_create_params,
    dataset_storages_s3_update_params,
    dataset_storages_s3_columns_params,
    dataset_storages_s3_validate_params,
    dataset_storages_s3_check_for_records_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ..types.dataset_storages_s3_list_response import DatasetStoragesS3ListResponse
from ..types.api.dataset_storages.s3_dataset_storage import S3DatasetStorage

__all__ = ["DatasetStoragesS3Resource", "AsyncDatasetStoragesS3Resource"]


class DatasetStoragesS3Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetStoragesS3ResourceWithRawResponse:
        return DatasetStoragesS3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetStoragesS3ResourceWithStreamingResponse:
        return DatasetStoragesS3ResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        dataset: int,
        aws_access_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        aws_secret_access_key: Optional[str] | NotGiven = NOT_GIVEN,
        aws_session_token: Optional[str] | NotGiven = NOT_GIVEN,
        aws_sse_kms_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        last_sync: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_sync_count: Optional[int] | NotGiven = NOT_GIVEN,
        last_sync_job: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        presign: bool | NotGiven = NOT_GIVEN,
        presign_ttl: int | NotGiven = NOT_GIVEN,
        recursive_scan: bool | NotGiven = NOT_GIVEN,
        regex_filter: Optional[str] | NotGiven = NOT_GIVEN,
        region_name: Optional[str] | NotGiven = NOT_GIVEN,
        s3_endpoint: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> S3DatasetStorage:
        """
        Create a new S3 import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          aws_access_key_id: AWS_ACCESS_KEY_ID

          aws_secret_access_key: AWS_SECRET_ACCESS_KEY

          aws_session_token: AWS_SESSION_TOKEN

          aws_sse_kms_key_id: AWS SSE KMS Key ID

          bucket: S3 bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: S3 bucket prefix

          presign_ttl: Presigned URLs TTL (in minutes)

          recursive_scan: Perform recursive scan over the bucket content

          regex_filter: Cloud storage regex for filtering objects

          region_name: AWS Region

          s3_endpoint: S3 Endpoint

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
            "/api/dataset-storages/s3/",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "aws_access_key_id": aws_access_key_id,
                    "aws_secret_access_key": aws_secret_access_key,
                    "aws_session_token": aws_session_token,
                    "aws_sse_kms_key_id": aws_sse_kms_key_id,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "last_sync": last_sync,
                    "last_sync_count": last_sync_count,
                    "last_sync_job": last_sync_job,
                    "meta": meta,
                    "prefix": prefix,
                    "presign": presign,
                    "presign_ttl": presign_ttl,
                    "recursive_scan": recursive_scan,
                    "regex_filter": regex_filter,
                    "region_name": region_name,
                    "s3_endpoint": s3_endpoint,
                    "status": status,
                    "synced": synced,
                    "synchronizable": synchronizable,
                    "title": title,
                    "traceback": traceback,
                    "use_blob_urls": use_blob_urls,
                },
                dataset_storages_s3_create_params.DatasetStoragesS3CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
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
    ) -> S3DatasetStorage:
        """
        Get a specific S3 import storage connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/dataset-storages/s3/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
        )

    def update(
        self,
        id: int,
        *,
        dataset: int,
        aws_access_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        aws_secret_access_key: Optional[str] | NotGiven = NOT_GIVEN,
        aws_session_token: Optional[str] | NotGiven = NOT_GIVEN,
        aws_sse_kms_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        last_sync: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_sync_count: Optional[int] | NotGiven = NOT_GIVEN,
        last_sync_job: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        presign: bool | NotGiven = NOT_GIVEN,
        presign_ttl: int | NotGiven = NOT_GIVEN,
        recursive_scan: bool | NotGiven = NOT_GIVEN,
        regex_filter: Optional[str] | NotGiven = NOT_GIVEN,
        region_name: Optional[str] | NotGiven = NOT_GIVEN,
        s3_endpoint: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> S3DatasetStorage:
        """
        Update a specific S3 import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          aws_access_key_id: AWS_ACCESS_KEY_ID

          aws_secret_access_key: AWS_SECRET_ACCESS_KEY

          aws_session_token: AWS_SESSION_TOKEN

          aws_sse_kms_key_id: AWS SSE KMS Key ID

          bucket: S3 bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: S3 bucket prefix

          presign_ttl: Presigned URLs TTL (in minutes)

          recursive_scan: Perform recursive scan over the bucket content

          regex_filter: Cloud storage regex for filtering objects

          region_name: AWS Region

          s3_endpoint: S3 Endpoint

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
            f"/api/dataset-storages/s3/{id}/",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "aws_access_key_id": aws_access_key_id,
                    "aws_secret_access_key": aws_secret_access_key,
                    "aws_session_token": aws_session_token,
                    "aws_sse_kms_key_id": aws_sse_kms_key_id,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "last_sync": last_sync,
                    "last_sync_count": last_sync_count,
                    "last_sync_job": last_sync_job,
                    "meta": meta,
                    "prefix": prefix,
                    "presign": presign,
                    "presign_ttl": presign_ttl,
                    "recursive_scan": recursive_scan,
                    "regex_filter": regex_filter,
                    "region_name": region_name,
                    "s3_endpoint": s3_endpoint,
                    "status": status,
                    "synced": synced,
                    "synchronizable": synchronizable,
                    "title": title,
                    "traceback": traceback,
                    "use_blob_urls": use_blob_urls,
                },
                dataset_storages_s3_update_params.DatasetStoragesS3UpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
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
    ) -> DatasetStoragesS3ListResponse:
        """
        Get a list of all S3 import storage connections.

        Args:
          dataset: Dataset ID

          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/dataset-storages/s3/",
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
                    dataset_storages_s3_list_params.DatasetStoragesS3ListParams,
                ),
            ),
            cast_to=DatasetStoragesS3ListResponse,
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
        Delete a specific S3 import storage connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/dataset-storages/s3/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def check_for_records(
        self,
        *,
        dataset: int,
        aws_access_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        aws_secret_access_key: Optional[str] | NotGiven = NOT_GIVEN,
        aws_session_token: Optional[str] | NotGiven = NOT_GIVEN,
        aws_sse_kms_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        last_sync: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_sync_count: Optional[int] | NotGiven = NOT_GIVEN,
        last_sync_job: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        presign: bool | NotGiven = NOT_GIVEN,
        presign_ttl: int | NotGiven = NOT_GIVEN,
        recursive_scan: bool | NotGiven = NOT_GIVEN,
        regex_filter: Optional[str] | NotGiven = NOT_GIVEN,
        region_name: Optional[str] | NotGiven = NOT_GIVEN,
        s3_endpoint: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> S3DatasetStorage:
        """
        Checks for existence of records matching the file pattern in the bucket/prefix

        Args:
          dataset: A unique integer value identifying this dataset.

          aws_access_key_id: AWS_ACCESS_KEY_ID

          aws_secret_access_key: AWS_SECRET_ACCESS_KEY

          aws_session_token: AWS_SESSION_TOKEN

          aws_sse_kms_key_id: AWS SSE KMS Key ID

          bucket: S3 bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: S3 bucket prefix

          presign_ttl: Presigned URLs TTL (in minutes)

          recursive_scan: Perform recursive scan over the bucket content

          regex_filter: Cloud storage regex for filtering objects

          region_name: AWS Region

          s3_endpoint: S3 Endpoint

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
            "/api/dataset-storages/s3/check-for-records/",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "aws_access_key_id": aws_access_key_id,
                    "aws_secret_access_key": aws_secret_access_key,
                    "aws_session_token": aws_session_token,
                    "aws_sse_kms_key_id": aws_sse_kms_key_id,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "last_sync": last_sync,
                    "last_sync_count": last_sync_count,
                    "last_sync_job": last_sync_job,
                    "meta": meta,
                    "prefix": prefix,
                    "presign": presign,
                    "presign_ttl": presign_ttl,
                    "recursive_scan": recursive_scan,
                    "regex_filter": regex_filter,
                    "region_name": region_name,
                    "s3_endpoint": s3_endpoint,
                    "status": status,
                    "synced": synced,
                    "synchronizable": synchronizable,
                    "title": title,
                    "traceback": traceback,
                    "use_blob_urls": use_blob_urls,
                },
                dataset_storages_s3_check_for_records_params.DatasetStoragesS3CheckForRecordsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
        )

    def columns(
        self,
        id: int,
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
        Retrieves column names from users JSON/blob data in bucket

        Args:
          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/dataset-storages/s3/{id}/columns/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"ordering": ordering}, dataset_storages_s3_columns_params.DatasetStoragesS3ColumnsParams
                ),
            ),
            cast_to=NoneType,
        )

    def sync(
        self,
        id: str,
        *,
        dataset: int,
        aws_access_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        aws_secret_access_key: Optional[str] | NotGiven = NOT_GIVEN,
        aws_session_token: Optional[str] | NotGiven = NOT_GIVEN,
        aws_sse_kms_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        last_sync: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_sync_count: Optional[int] | NotGiven = NOT_GIVEN,
        last_sync_job: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        presign: bool | NotGiven = NOT_GIVEN,
        presign_ttl: int | NotGiven = NOT_GIVEN,
        recursive_scan: bool | NotGiven = NOT_GIVEN,
        regex_filter: Optional[str] | NotGiven = NOT_GIVEN,
        region_name: Optional[str] | NotGiven = NOT_GIVEN,
        s3_endpoint: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> S3DatasetStorage:
        """
        Sync tasks from an S3 import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          aws_access_key_id: AWS_ACCESS_KEY_ID

          aws_secret_access_key: AWS_SECRET_ACCESS_KEY

          aws_session_token: AWS_SESSION_TOKEN

          aws_sse_kms_key_id: AWS SSE KMS Key ID

          bucket: S3 bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: S3 bucket prefix

          presign_ttl: Presigned URLs TTL (in minutes)

          recursive_scan: Perform recursive scan over the bucket content

          regex_filter: Cloud storage regex for filtering objects

          region_name: AWS Region

          s3_endpoint: S3 Endpoint

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
            f"/api/dataset-storages/s3/{id}/sync/",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "aws_access_key_id": aws_access_key_id,
                    "aws_secret_access_key": aws_secret_access_key,
                    "aws_session_token": aws_session_token,
                    "aws_sse_kms_key_id": aws_sse_kms_key_id,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "last_sync": last_sync,
                    "last_sync_count": last_sync_count,
                    "last_sync_job": last_sync_job,
                    "meta": meta,
                    "prefix": prefix,
                    "presign": presign,
                    "presign_ttl": presign_ttl,
                    "recursive_scan": recursive_scan,
                    "regex_filter": regex_filter,
                    "region_name": region_name,
                    "s3_endpoint": s3_endpoint,
                    "status": status,
                    "synced": synced,
                    "synchronizable": synchronizable,
                    "title": title,
                    "traceback": traceback,
                    "use_blob_urls": use_blob_urls,
                },
                dataset_storages_s3_sync_params.DatasetStoragesS3SyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
        )

    def validate(
        self,
        *,
        dataset: int,
        aws_access_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        aws_secret_access_key: Optional[str] | NotGiven = NOT_GIVEN,
        aws_session_token: Optional[str] | NotGiven = NOT_GIVEN,
        aws_sse_kms_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        last_sync: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_sync_count: Optional[int] | NotGiven = NOT_GIVEN,
        last_sync_job: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        presign: bool | NotGiven = NOT_GIVEN,
        presign_ttl: int | NotGiven = NOT_GIVEN,
        recursive_scan: bool | NotGiven = NOT_GIVEN,
        regex_filter: Optional[str] | NotGiven = NOT_GIVEN,
        region_name: Optional[str] | NotGiven = NOT_GIVEN,
        s3_endpoint: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> S3DatasetStorage:
        """
        Validate a specific S3 import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          aws_access_key_id: AWS_ACCESS_KEY_ID

          aws_secret_access_key: AWS_SECRET_ACCESS_KEY

          aws_session_token: AWS_SESSION_TOKEN

          aws_sse_kms_key_id: AWS SSE KMS Key ID

          bucket: S3 bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: S3 bucket prefix

          presign_ttl: Presigned URLs TTL (in minutes)

          recursive_scan: Perform recursive scan over the bucket content

          regex_filter: Cloud storage regex for filtering objects

          region_name: AWS Region

          s3_endpoint: S3 Endpoint

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
            "/api/dataset-storages/s3/validate/",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "aws_access_key_id": aws_access_key_id,
                    "aws_secret_access_key": aws_secret_access_key,
                    "aws_session_token": aws_session_token,
                    "aws_sse_kms_key_id": aws_sse_kms_key_id,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "last_sync": last_sync,
                    "last_sync_count": last_sync_count,
                    "last_sync_job": last_sync_job,
                    "meta": meta,
                    "prefix": prefix,
                    "presign": presign,
                    "presign_ttl": presign_ttl,
                    "recursive_scan": recursive_scan,
                    "regex_filter": regex_filter,
                    "region_name": region_name,
                    "s3_endpoint": s3_endpoint,
                    "status": status,
                    "synced": synced,
                    "synchronizable": synchronizable,
                    "title": title,
                    "traceback": traceback,
                    "use_blob_urls": use_blob_urls,
                },
                dataset_storages_s3_validate_params.DatasetStoragesS3ValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
        )


class AsyncDatasetStoragesS3Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetStoragesS3ResourceWithRawResponse:
        return AsyncDatasetStoragesS3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetStoragesS3ResourceWithStreamingResponse:
        return AsyncDatasetStoragesS3ResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        dataset: int,
        aws_access_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        aws_secret_access_key: Optional[str] | NotGiven = NOT_GIVEN,
        aws_session_token: Optional[str] | NotGiven = NOT_GIVEN,
        aws_sse_kms_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        last_sync: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_sync_count: Optional[int] | NotGiven = NOT_GIVEN,
        last_sync_job: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        presign: bool | NotGiven = NOT_GIVEN,
        presign_ttl: int | NotGiven = NOT_GIVEN,
        recursive_scan: bool | NotGiven = NOT_GIVEN,
        regex_filter: Optional[str] | NotGiven = NOT_GIVEN,
        region_name: Optional[str] | NotGiven = NOT_GIVEN,
        s3_endpoint: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> S3DatasetStorage:
        """
        Create a new S3 import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          aws_access_key_id: AWS_ACCESS_KEY_ID

          aws_secret_access_key: AWS_SECRET_ACCESS_KEY

          aws_session_token: AWS_SESSION_TOKEN

          aws_sse_kms_key_id: AWS SSE KMS Key ID

          bucket: S3 bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: S3 bucket prefix

          presign_ttl: Presigned URLs TTL (in minutes)

          recursive_scan: Perform recursive scan over the bucket content

          regex_filter: Cloud storage regex for filtering objects

          region_name: AWS Region

          s3_endpoint: S3 Endpoint

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
            "/api/dataset-storages/s3/",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "aws_access_key_id": aws_access_key_id,
                    "aws_secret_access_key": aws_secret_access_key,
                    "aws_session_token": aws_session_token,
                    "aws_sse_kms_key_id": aws_sse_kms_key_id,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "last_sync": last_sync,
                    "last_sync_count": last_sync_count,
                    "last_sync_job": last_sync_job,
                    "meta": meta,
                    "prefix": prefix,
                    "presign": presign,
                    "presign_ttl": presign_ttl,
                    "recursive_scan": recursive_scan,
                    "regex_filter": regex_filter,
                    "region_name": region_name,
                    "s3_endpoint": s3_endpoint,
                    "status": status,
                    "synced": synced,
                    "synchronizable": synchronizable,
                    "title": title,
                    "traceback": traceback,
                    "use_blob_urls": use_blob_urls,
                },
                dataset_storages_s3_create_params.DatasetStoragesS3CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
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
    ) -> S3DatasetStorage:
        """
        Get a specific S3 import storage connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/dataset-storages/s3/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
        )

    async def update(
        self,
        id: int,
        *,
        dataset: int,
        aws_access_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        aws_secret_access_key: Optional[str] | NotGiven = NOT_GIVEN,
        aws_session_token: Optional[str] | NotGiven = NOT_GIVEN,
        aws_sse_kms_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        last_sync: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_sync_count: Optional[int] | NotGiven = NOT_GIVEN,
        last_sync_job: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        presign: bool | NotGiven = NOT_GIVEN,
        presign_ttl: int | NotGiven = NOT_GIVEN,
        recursive_scan: bool | NotGiven = NOT_GIVEN,
        regex_filter: Optional[str] | NotGiven = NOT_GIVEN,
        region_name: Optional[str] | NotGiven = NOT_GIVEN,
        s3_endpoint: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> S3DatasetStorage:
        """
        Update a specific S3 import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          aws_access_key_id: AWS_ACCESS_KEY_ID

          aws_secret_access_key: AWS_SECRET_ACCESS_KEY

          aws_session_token: AWS_SESSION_TOKEN

          aws_sse_kms_key_id: AWS SSE KMS Key ID

          bucket: S3 bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: S3 bucket prefix

          presign_ttl: Presigned URLs TTL (in minutes)

          recursive_scan: Perform recursive scan over the bucket content

          regex_filter: Cloud storage regex for filtering objects

          region_name: AWS Region

          s3_endpoint: S3 Endpoint

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
            f"/api/dataset-storages/s3/{id}/",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "aws_access_key_id": aws_access_key_id,
                    "aws_secret_access_key": aws_secret_access_key,
                    "aws_session_token": aws_session_token,
                    "aws_sse_kms_key_id": aws_sse_kms_key_id,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "last_sync": last_sync,
                    "last_sync_count": last_sync_count,
                    "last_sync_job": last_sync_job,
                    "meta": meta,
                    "prefix": prefix,
                    "presign": presign,
                    "presign_ttl": presign_ttl,
                    "recursive_scan": recursive_scan,
                    "regex_filter": regex_filter,
                    "region_name": region_name,
                    "s3_endpoint": s3_endpoint,
                    "status": status,
                    "synced": synced,
                    "synchronizable": synchronizable,
                    "title": title,
                    "traceback": traceback,
                    "use_blob_urls": use_blob_urls,
                },
                dataset_storages_s3_update_params.DatasetStoragesS3UpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
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
    ) -> DatasetStoragesS3ListResponse:
        """
        Get a list of all S3 import storage connections.

        Args:
          dataset: Dataset ID

          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/dataset-storages/s3/",
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
                    dataset_storages_s3_list_params.DatasetStoragesS3ListParams,
                ),
            ),
            cast_to=DatasetStoragesS3ListResponse,
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
        Delete a specific S3 import storage connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/dataset-storages/s3/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def check_for_records(
        self,
        *,
        dataset: int,
        aws_access_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        aws_secret_access_key: Optional[str] | NotGiven = NOT_GIVEN,
        aws_session_token: Optional[str] | NotGiven = NOT_GIVEN,
        aws_sse_kms_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        last_sync: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_sync_count: Optional[int] | NotGiven = NOT_GIVEN,
        last_sync_job: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        presign: bool | NotGiven = NOT_GIVEN,
        presign_ttl: int | NotGiven = NOT_GIVEN,
        recursive_scan: bool | NotGiven = NOT_GIVEN,
        regex_filter: Optional[str] | NotGiven = NOT_GIVEN,
        region_name: Optional[str] | NotGiven = NOT_GIVEN,
        s3_endpoint: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> S3DatasetStorage:
        """
        Checks for existence of records matching the file pattern in the bucket/prefix

        Args:
          dataset: A unique integer value identifying this dataset.

          aws_access_key_id: AWS_ACCESS_KEY_ID

          aws_secret_access_key: AWS_SECRET_ACCESS_KEY

          aws_session_token: AWS_SESSION_TOKEN

          aws_sse_kms_key_id: AWS SSE KMS Key ID

          bucket: S3 bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: S3 bucket prefix

          presign_ttl: Presigned URLs TTL (in minutes)

          recursive_scan: Perform recursive scan over the bucket content

          regex_filter: Cloud storage regex for filtering objects

          region_name: AWS Region

          s3_endpoint: S3 Endpoint

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
            "/api/dataset-storages/s3/check-for-records/",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "aws_access_key_id": aws_access_key_id,
                    "aws_secret_access_key": aws_secret_access_key,
                    "aws_session_token": aws_session_token,
                    "aws_sse_kms_key_id": aws_sse_kms_key_id,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "last_sync": last_sync,
                    "last_sync_count": last_sync_count,
                    "last_sync_job": last_sync_job,
                    "meta": meta,
                    "prefix": prefix,
                    "presign": presign,
                    "presign_ttl": presign_ttl,
                    "recursive_scan": recursive_scan,
                    "regex_filter": regex_filter,
                    "region_name": region_name,
                    "s3_endpoint": s3_endpoint,
                    "status": status,
                    "synced": synced,
                    "synchronizable": synchronizable,
                    "title": title,
                    "traceback": traceback,
                    "use_blob_urls": use_blob_urls,
                },
                dataset_storages_s3_check_for_records_params.DatasetStoragesS3CheckForRecordsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
        )

    async def columns(
        self,
        id: int,
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
        Retrieves column names from users JSON/blob data in bucket

        Args:
          ordering: Which field to use when ordering the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/dataset-storages/s3/{id}/columns/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"ordering": ordering}, dataset_storages_s3_columns_params.DatasetStoragesS3ColumnsParams
                ),
            ),
            cast_to=NoneType,
        )

    async def sync(
        self,
        id: str,
        *,
        dataset: int,
        aws_access_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        aws_secret_access_key: Optional[str] | NotGiven = NOT_GIVEN,
        aws_session_token: Optional[str] | NotGiven = NOT_GIVEN,
        aws_sse_kms_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        last_sync: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_sync_count: Optional[int] | NotGiven = NOT_GIVEN,
        last_sync_job: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        presign: bool | NotGiven = NOT_GIVEN,
        presign_ttl: int | NotGiven = NOT_GIVEN,
        recursive_scan: bool | NotGiven = NOT_GIVEN,
        regex_filter: Optional[str] | NotGiven = NOT_GIVEN,
        region_name: Optional[str] | NotGiven = NOT_GIVEN,
        s3_endpoint: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> S3DatasetStorage:
        """
        Sync tasks from an S3 import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          aws_access_key_id: AWS_ACCESS_KEY_ID

          aws_secret_access_key: AWS_SECRET_ACCESS_KEY

          aws_session_token: AWS_SESSION_TOKEN

          aws_sse_kms_key_id: AWS SSE KMS Key ID

          bucket: S3 bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: S3 bucket prefix

          presign_ttl: Presigned URLs TTL (in minutes)

          recursive_scan: Perform recursive scan over the bucket content

          regex_filter: Cloud storage regex for filtering objects

          region_name: AWS Region

          s3_endpoint: S3 Endpoint

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
            f"/api/dataset-storages/s3/{id}/sync/",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "aws_access_key_id": aws_access_key_id,
                    "aws_secret_access_key": aws_secret_access_key,
                    "aws_session_token": aws_session_token,
                    "aws_sse_kms_key_id": aws_sse_kms_key_id,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "last_sync": last_sync,
                    "last_sync_count": last_sync_count,
                    "last_sync_job": last_sync_job,
                    "meta": meta,
                    "prefix": prefix,
                    "presign": presign,
                    "presign_ttl": presign_ttl,
                    "recursive_scan": recursive_scan,
                    "regex_filter": regex_filter,
                    "region_name": region_name,
                    "s3_endpoint": s3_endpoint,
                    "status": status,
                    "synced": synced,
                    "synchronizable": synchronizable,
                    "title": title,
                    "traceback": traceback,
                    "use_blob_urls": use_blob_urls,
                },
                dataset_storages_s3_sync_params.DatasetStoragesS3SyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
        )

    async def validate(
        self,
        *,
        dataset: int,
        aws_access_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        aws_secret_access_key: Optional[str] | NotGiven = NOT_GIVEN,
        aws_session_token: Optional[str] | NotGiven = NOT_GIVEN,
        aws_sse_kms_key_id: Optional[str] | NotGiven = NOT_GIVEN,
        bucket: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        glob_pattern: Optional[str] | NotGiven = NOT_GIVEN,
        last_sync: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_sync_count: Optional[int] | NotGiven = NOT_GIVEN,
        last_sync_job: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        presign: bool | NotGiven = NOT_GIVEN,
        presign_ttl: int | NotGiven = NOT_GIVEN,
        recursive_scan: bool | NotGiven = NOT_GIVEN,
        regex_filter: Optional[str] | NotGiven = NOT_GIVEN,
        region_name: Optional[str] | NotGiven = NOT_GIVEN,
        s3_endpoint: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> S3DatasetStorage:
        """
        Validate a specific S3 import storage connection.

        Args:
          dataset: A unique integer value identifying this dataset.

          aws_access_key_id: AWS_ACCESS_KEY_ID

          aws_secret_access_key: AWS_SECRET_ACCESS_KEY

          aws_session_token: AWS_SESSION_TOKEN

          aws_sse_kms_key_id: AWS SSE KMS Key ID

          bucket: S3 bucket name

          description: Cloud storage description

          glob_pattern: Glob pattern for syncing from bucket

          last_sync: Last sync finished time

          last_sync_count: Count of tasks synced last time

          last_sync_job: Last sync job ID

          meta: Meta and debug information about storage processes

          prefix: S3 bucket prefix

          presign_ttl: Presigned URLs TTL (in minutes)

          recursive_scan: Perform recursive scan over the bucket content

          regex_filter: Cloud storage regex for filtering objects

          region_name: AWS Region

          s3_endpoint: S3 Endpoint

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
            "/api/dataset-storages/s3/validate/",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "aws_access_key_id": aws_access_key_id,
                    "aws_secret_access_key": aws_secret_access_key,
                    "aws_session_token": aws_session_token,
                    "aws_sse_kms_key_id": aws_sse_kms_key_id,
                    "bucket": bucket,
                    "description": description,
                    "glob_pattern": glob_pattern,
                    "last_sync": last_sync,
                    "last_sync_count": last_sync_count,
                    "last_sync_job": last_sync_job,
                    "meta": meta,
                    "prefix": prefix,
                    "presign": presign,
                    "presign_ttl": presign_ttl,
                    "recursive_scan": recursive_scan,
                    "regex_filter": regex_filter,
                    "region_name": region_name,
                    "s3_endpoint": s3_endpoint,
                    "status": status,
                    "synced": synced,
                    "synchronizable": synchronizable,
                    "title": title,
                    "traceback": traceback,
                    "use_blob_urls": use_blob_urls,
                },
                dataset_storages_s3_validate_params.DatasetStoragesS3ValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
        )


class DatasetStoragesS3ResourceWithRawResponse:
    def __init__(self, dataset_storages_s3: DatasetStoragesS3Resource) -> None:
        self._dataset_storages_s3 = dataset_storages_s3

        self.create = to_raw_response_wrapper(
            dataset_storages_s3.create,
        )
        self.retrieve = to_raw_response_wrapper(
            dataset_storages_s3.retrieve,
        )
        self.update = to_raw_response_wrapper(
            dataset_storages_s3.update,
        )
        self.list = to_raw_response_wrapper(
            dataset_storages_s3.list,
        )
        self.delete = to_raw_response_wrapper(
            dataset_storages_s3.delete,
        )
        self.check_for_records = to_raw_response_wrapper(
            dataset_storages_s3.check_for_records,
        )
        self.columns = to_raw_response_wrapper(
            dataset_storages_s3.columns,
        )
        self.sync = to_raw_response_wrapper(
            dataset_storages_s3.sync,
        )
        self.validate = to_raw_response_wrapper(
            dataset_storages_s3.validate,
        )


class AsyncDatasetStoragesS3ResourceWithRawResponse:
    def __init__(self, dataset_storages_s3: AsyncDatasetStoragesS3Resource) -> None:
        self._dataset_storages_s3 = dataset_storages_s3

        self.create = async_to_raw_response_wrapper(
            dataset_storages_s3.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            dataset_storages_s3.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            dataset_storages_s3.update,
        )
        self.list = async_to_raw_response_wrapper(
            dataset_storages_s3.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dataset_storages_s3.delete,
        )
        self.check_for_records = async_to_raw_response_wrapper(
            dataset_storages_s3.check_for_records,
        )
        self.columns = async_to_raw_response_wrapper(
            dataset_storages_s3.columns,
        )
        self.sync = async_to_raw_response_wrapper(
            dataset_storages_s3.sync,
        )
        self.validate = async_to_raw_response_wrapper(
            dataset_storages_s3.validate,
        )


class DatasetStoragesS3ResourceWithStreamingResponse:
    def __init__(self, dataset_storages_s3: DatasetStoragesS3Resource) -> None:
        self._dataset_storages_s3 = dataset_storages_s3

        self.create = to_streamed_response_wrapper(
            dataset_storages_s3.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            dataset_storages_s3.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            dataset_storages_s3.update,
        )
        self.list = to_streamed_response_wrapper(
            dataset_storages_s3.list,
        )
        self.delete = to_streamed_response_wrapper(
            dataset_storages_s3.delete,
        )
        self.check_for_records = to_streamed_response_wrapper(
            dataset_storages_s3.check_for_records,
        )
        self.columns = to_streamed_response_wrapper(
            dataset_storages_s3.columns,
        )
        self.sync = to_streamed_response_wrapper(
            dataset_storages_s3.sync,
        )
        self.validate = to_streamed_response_wrapper(
            dataset_storages_s3.validate,
        )


class AsyncDatasetStoragesS3ResourceWithStreamingResponse:
    def __init__(self, dataset_storages_s3: AsyncDatasetStoragesS3Resource) -> None:
        self._dataset_storages_s3 = dataset_storages_s3

        self.create = async_to_streamed_response_wrapper(
            dataset_storages_s3.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            dataset_storages_s3.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            dataset_storages_s3.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dataset_storages_s3.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dataset_storages_s3.delete,
        )
        self.check_for_records = async_to_streamed_response_wrapper(
            dataset_storages_s3.check_for_records,
        )
        self.columns = async_to_streamed_response_wrapper(
            dataset_storages_s3.columns,
        )
        self.sync = async_to_streamed_response_wrapper(
            dataset_storages_s3.sync,
        )
        self.validate = async_to_streamed_response_wrapper(
            dataset_storages_s3.validate,
        )
