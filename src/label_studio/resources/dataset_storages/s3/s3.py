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
    s3_list_params,
    s3_sync_params,
    s3_create_params,
    s3_update_params,
    s3_validate_params,
    s3_check_for_records_params,
)
from ....types.dataset_storages.s3_list_response import S3ListResponse
from ....types.api.dataset_storages.s3_dataset_storage import S3DatasetStorage

__all__ = ["S3Resource", "AsyncS3Resource"]


class S3Resource(SyncAPIResource):
    @cached_property
    def columns(self) -> ColumnsResource:
        return ColumnsResource(self._client)

    @cached_property
    def with_raw_response(self) -> S3ResourceWithRawResponse:
        return S3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> S3ResourceWithStreamingResponse:
        return S3ResourceWithStreamingResponse(self)

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
                s3_create_params.S3CreateParams,
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
                s3_update_params.S3UpdateParams,
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
    ) -> S3ListResponse:
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
                    s3_list_params.S3ListParams,
                ),
            ),
            cast_to=S3ListResponse,
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
                s3_check_for_records_params.S3CheckForRecordsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
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
                s3_sync_params.S3SyncParams,
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
                s3_validate_params.S3ValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
        )


class AsyncS3Resource(AsyncAPIResource):
    @cached_property
    def columns(self) -> AsyncColumnsResource:
        return AsyncColumnsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncS3ResourceWithRawResponse:
        return AsyncS3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncS3ResourceWithStreamingResponse:
        return AsyncS3ResourceWithStreamingResponse(self)

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
                s3_create_params.S3CreateParams,
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
                s3_update_params.S3UpdateParams,
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
    ) -> S3ListResponse:
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
                    s3_list_params.S3ListParams,
                ),
            ),
            cast_to=S3ListResponse,
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
                s3_check_for_records_params.S3CheckForRecordsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
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
                s3_sync_params.S3SyncParams,
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
                s3_validate_params.S3ValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=S3DatasetStorage,
        )


class S3ResourceWithRawResponse:
    def __init__(self, s3: S3Resource) -> None:
        self._s3 = s3

        self.create = to_raw_response_wrapper(
            s3.create,
        )
        self.retrieve = to_raw_response_wrapper(
            s3.retrieve,
        )
        self.update = to_raw_response_wrapper(
            s3.update,
        )
        self.list = to_raw_response_wrapper(
            s3.list,
        )
        self.delete = to_raw_response_wrapper(
            s3.delete,
        )
        self.check_for_records = to_raw_response_wrapper(
            s3.check_for_records,
        )
        self.sync = to_raw_response_wrapper(
            s3.sync,
        )
        self.validate = to_raw_response_wrapper(
            s3.validate,
        )

    @cached_property
    def columns(self) -> ColumnsResourceWithRawResponse:
        return ColumnsResourceWithRawResponse(self._s3.columns)


class AsyncS3ResourceWithRawResponse:
    def __init__(self, s3: AsyncS3Resource) -> None:
        self._s3 = s3

        self.create = async_to_raw_response_wrapper(
            s3.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            s3.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            s3.update,
        )
        self.list = async_to_raw_response_wrapper(
            s3.list,
        )
        self.delete = async_to_raw_response_wrapper(
            s3.delete,
        )
        self.check_for_records = async_to_raw_response_wrapper(
            s3.check_for_records,
        )
        self.sync = async_to_raw_response_wrapper(
            s3.sync,
        )
        self.validate = async_to_raw_response_wrapper(
            s3.validate,
        )

    @cached_property
    def columns(self) -> AsyncColumnsResourceWithRawResponse:
        return AsyncColumnsResourceWithRawResponse(self._s3.columns)


class S3ResourceWithStreamingResponse:
    def __init__(self, s3: S3Resource) -> None:
        self._s3 = s3

        self.create = to_streamed_response_wrapper(
            s3.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            s3.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            s3.update,
        )
        self.list = to_streamed_response_wrapper(
            s3.list,
        )
        self.delete = to_streamed_response_wrapper(
            s3.delete,
        )
        self.check_for_records = to_streamed_response_wrapper(
            s3.check_for_records,
        )
        self.sync = to_streamed_response_wrapper(
            s3.sync,
        )
        self.validate = to_streamed_response_wrapper(
            s3.validate,
        )

    @cached_property
    def columns(self) -> ColumnsResourceWithStreamingResponse:
        return ColumnsResourceWithStreamingResponse(self._s3.columns)


class AsyncS3ResourceWithStreamingResponse:
    def __init__(self, s3: AsyncS3Resource) -> None:
        self._s3 = s3

        self.create = async_to_streamed_response_wrapper(
            s3.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            s3.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            s3.update,
        )
        self.list = async_to_streamed_response_wrapper(
            s3.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            s3.delete,
        )
        self.check_for_records = async_to_streamed_response_wrapper(
            s3.check_for_records,
        )
        self.sync = async_to_streamed_response_wrapper(
            s3.sync,
        )
        self.validate = async_to_streamed_response_wrapper(
            s3.validate,
        )

    @cached_property
    def columns(self) -> AsyncColumnsResourceWithStreamingResponse:
        return AsyncColumnsResourceWithStreamingResponse(self._s3.columns)
