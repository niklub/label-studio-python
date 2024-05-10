# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from label_studio import LabelStudio, AsyncLabelStudio
from label_studio.types import (
    DatasetStoragesS3ListResponse,
)
from label_studio._utils import parse_datetime
from label_studio.types.api.dataset_storages import S3DatasetStorage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasetStoragesS3:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.create(
            dataset=0,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.create(
            dataset=0,
            aws_access_key_id="string",
            aws_secret_access_key="string",
            aws_session_token="string",
            aws_sse_kms_key_id="string",
            bucket="string",
            description="string",
            glob_pattern="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            recursive_scan=True,
            regex_filter="string",
            region_name="string",
            s3_endpoint="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LabelStudio) -> None:
        response = client.dataset_storages_s3.with_raw_response.create(
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = response.parse()
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LabelStudio) -> None:
        with client.dataset_storages_s3.with_streaming_response.create(
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = response.parse()
            assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.retrieve(
            0,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LabelStudio) -> None:
        response = client.dataset_storages_s3.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = response.parse()
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LabelStudio) -> None:
        with client.dataset_storages_s3.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = response.parse()
            assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.update(
            0,
            dataset=0,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.update(
            0,
            dataset=0,
            aws_access_key_id="string",
            aws_secret_access_key="string",
            aws_session_token="string",
            aws_sse_kms_key_id="string",
            bucket="string",
            description="string",
            glob_pattern="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            recursive_scan=True,
            regex_filter="string",
            region_name="string",
            s3_endpoint="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: LabelStudio) -> None:
        response = client.dataset_storages_s3.with_raw_response.update(
            0,
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = response.parse()
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: LabelStudio) -> None:
        with client.dataset_storages_s3.with_streaming_response.update(
            0,
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = response.parse()
            assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.list()
        assert_matches_type(DatasetStoragesS3ListResponse, dataset_storages_s3, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.list(
            dataset=0,
            ordering="string",
        )
        assert_matches_type(DatasetStoragesS3ListResponse, dataset_storages_s3, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LabelStudio) -> None:
        response = client.dataset_storages_s3.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = response.parse()
        assert_matches_type(DatasetStoragesS3ListResponse, dataset_storages_s3, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LabelStudio) -> None:
        with client.dataset_storages_s3.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = response.parse()
            assert_matches_type(DatasetStoragesS3ListResponse, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.delete(
            0,
        )
        assert dataset_storages_s3 is None

    @parametrize
    def test_raw_response_delete(self, client: LabelStudio) -> None:
        response = client.dataset_storages_s3.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = response.parse()
        assert dataset_storages_s3 is None

    @parametrize
    def test_streaming_response_delete(self, client: LabelStudio) -> None:
        with client.dataset_storages_s3.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = response.parse()
            assert dataset_storages_s3 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_check_for_records(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.check_for_records(
            dataset=0,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_method_check_for_records_with_all_params(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.check_for_records(
            dataset=0,
            aws_access_key_id="string",
            aws_secret_access_key="string",
            aws_session_token="string",
            aws_sse_kms_key_id="string",
            bucket="string",
            description="string",
            glob_pattern="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            recursive_scan=True,
            regex_filter="string",
            region_name="string",
            s3_endpoint="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_raw_response_check_for_records(self, client: LabelStudio) -> None:
        response = client.dataset_storages_s3.with_raw_response.check_for_records(
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = response.parse()
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_streaming_response_check_for_records(self, client: LabelStudio) -> None:
        with client.dataset_storages_s3.with_streaming_response.check_for_records(
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = response.parse()
            assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_columns(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.columns(
            0,
        )
        assert dataset_storages_s3 is None

    @parametrize
    def test_method_columns_with_all_params(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.columns(
            0,
            ordering="string",
        )
        assert dataset_storages_s3 is None

    @parametrize
    def test_raw_response_columns(self, client: LabelStudio) -> None:
        response = client.dataset_storages_s3.with_raw_response.columns(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = response.parse()
        assert dataset_storages_s3 is None

    @parametrize
    def test_streaming_response_columns(self, client: LabelStudio) -> None:
        with client.dataset_storages_s3.with_streaming_response.columns(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = response.parse()
            assert dataset_storages_s3 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_sync(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.sync(
            "string",
            dataset=0,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_method_sync_with_all_params(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.sync(
            "string",
            dataset=0,
            aws_access_key_id="string",
            aws_secret_access_key="string",
            aws_session_token="string",
            aws_sse_kms_key_id="string",
            bucket="string",
            description="string",
            glob_pattern="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            recursive_scan=True,
            regex_filter="string",
            region_name="string",
            s3_endpoint="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_raw_response_sync(self, client: LabelStudio) -> None:
        response = client.dataset_storages_s3.with_raw_response.sync(
            "string",
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = response.parse()
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_streaming_response_sync(self, client: LabelStudio) -> None:
        with client.dataset_storages_s3.with_streaming_response.sync(
            "string",
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = response.parse()
            assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_sync(self, client: LabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.dataset_storages_s3.with_raw_response.sync(
                "",
                dataset=0,
            )

    @parametrize
    def test_method_validate(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.validate(
            dataset=0,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_method_validate_with_all_params(self, client: LabelStudio) -> None:
        dataset_storages_s3 = client.dataset_storages_s3.validate(
            dataset=0,
            aws_access_key_id="string",
            aws_secret_access_key="string",
            aws_session_token="string",
            aws_sse_kms_key_id="string",
            bucket="string",
            description="string",
            glob_pattern="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            recursive_scan=True,
            regex_filter="string",
            region_name="string",
            s3_endpoint="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_raw_response_validate(self, client: LabelStudio) -> None:
        response = client.dataset_storages_s3.with_raw_response.validate(
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = response.parse()
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    def test_streaming_response_validate(self, client: LabelStudio) -> None:
        with client.dataset_storages_s3.with_streaming_response.validate(
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = response.parse()
            assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasetStoragesS3:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.create(
            dataset=0,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.create(
            dataset=0,
            aws_access_key_id="string",
            aws_secret_access_key="string",
            aws_session_token="string",
            aws_sse_kms_key_id="string",
            bucket="string",
            description="string",
            glob_pattern="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            recursive_scan=True,
            regex_filter="string",
            region_name="string",
            s3_endpoint="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages_s3.with_raw_response.create(
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = await response.parse()
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages_s3.with_streaming_response.create(
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = await response.parse()
            assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.retrieve(
            0,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages_s3.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = await response.parse()
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages_s3.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = await response.parse()
            assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.update(
            0,
            dataset=0,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.update(
            0,
            dataset=0,
            aws_access_key_id="string",
            aws_secret_access_key="string",
            aws_session_token="string",
            aws_sse_kms_key_id="string",
            bucket="string",
            description="string",
            glob_pattern="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            recursive_scan=True,
            regex_filter="string",
            region_name="string",
            s3_endpoint="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages_s3.with_raw_response.update(
            0,
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = await response.parse()
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages_s3.with_streaming_response.update(
            0,
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = await response.parse()
            assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.list()
        assert_matches_type(DatasetStoragesS3ListResponse, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.list(
            dataset=0,
            ordering="string",
        )
        assert_matches_type(DatasetStoragesS3ListResponse, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages_s3.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = await response.parse()
        assert_matches_type(DatasetStoragesS3ListResponse, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages_s3.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = await response.parse()
            assert_matches_type(DatasetStoragesS3ListResponse, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.delete(
            0,
        )
        assert dataset_storages_s3 is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages_s3.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = await response.parse()
        assert dataset_storages_s3 is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages_s3.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = await response.parse()
            assert dataset_storages_s3 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_check_for_records(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.check_for_records(
            dataset=0,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_method_check_for_records_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.check_for_records(
            dataset=0,
            aws_access_key_id="string",
            aws_secret_access_key="string",
            aws_session_token="string",
            aws_sse_kms_key_id="string",
            bucket="string",
            description="string",
            glob_pattern="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            recursive_scan=True,
            regex_filter="string",
            region_name="string",
            s3_endpoint="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_raw_response_check_for_records(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages_s3.with_raw_response.check_for_records(
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = await response.parse()
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_streaming_response_check_for_records(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages_s3.with_streaming_response.check_for_records(
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = await response.parse()
            assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_columns(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.columns(
            0,
        )
        assert dataset_storages_s3 is None

    @parametrize
    async def test_method_columns_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.columns(
            0,
            ordering="string",
        )
        assert dataset_storages_s3 is None

    @parametrize
    async def test_raw_response_columns(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages_s3.with_raw_response.columns(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = await response.parse()
        assert dataset_storages_s3 is None

    @parametrize
    async def test_streaming_response_columns(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages_s3.with_streaming_response.columns(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = await response.parse()
            assert dataset_storages_s3 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_sync(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.sync(
            "string",
            dataset=0,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_method_sync_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.sync(
            "string",
            dataset=0,
            aws_access_key_id="string",
            aws_secret_access_key="string",
            aws_session_token="string",
            aws_sse_kms_key_id="string",
            bucket="string",
            description="string",
            glob_pattern="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            recursive_scan=True,
            regex_filter="string",
            region_name="string",
            s3_endpoint="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_raw_response_sync(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages_s3.with_raw_response.sync(
            "string",
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = await response.parse()
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_streaming_response_sync(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages_s3.with_streaming_response.sync(
            "string",
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = await response.parse()
            assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_sync(self, async_client: AsyncLabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.dataset_storages_s3.with_raw_response.sync(
                "",
                dataset=0,
            )

    @parametrize
    async def test_method_validate(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.validate(
            dataset=0,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_s3 = await async_client.dataset_storages_s3.validate(
            dataset=0,
            aws_access_key_id="string",
            aws_secret_access_key="string",
            aws_session_token="string",
            aws_sse_kms_key_id="string",
            bucket="string",
            description="string",
            glob_pattern="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            recursive_scan=True,
            regex_filter="string",
            region_name="string",
            s3_endpoint="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages_s3.with_raw_response.validate(
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_s3 = await response.parse()
        assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages_s3.with_streaming_response.validate(
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_s3 = await response.parse()
            assert_matches_type(S3DatasetStorage, dataset_storages_s3, path=["response"])

        assert cast(Any, response.is_closed) is True
