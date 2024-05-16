# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from label_studio import LabelStudio, AsyncLabelStudio
from label_studio._utils import parse_datetime
from label_studio.types.dataset_storages import (
    GcListResponse,
)
from label_studio.types.api.dataset_storages import GcsDatasetStorage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGcs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.create(
            dataset=0,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.create(
            dataset=0,
            bucket="string",
            description="string",
            glob_pattern="string",
            google_application_credentials="string",
            google_project_id="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            regex_filter="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LabelStudio) -> None:
        response = client.dataset_storages.gcs.with_raw_response.create(
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = response.parse()
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LabelStudio) -> None:
        with client.dataset_storages.gcs.with_streaming_response.create(
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = response.parse()
            assert_matches_type(GcsDatasetStorage, gc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.retrieve(
            0,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LabelStudio) -> None:
        response = client.dataset_storages.gcs.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = response.parse()
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LabelStudio) -> None:
        with client.dataset_storages.gcs.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = response.parse()
            assert_matches_type(GcsDatasetStorage, gc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.update(
            0,
            dataset=0,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.update(
            0,
            dataset=0,
            bucket="string",
            description="string",
            glob_pattern="string",
            google_application_credentials="string",
            google_project_id="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            regex_filter="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: LabelStudio) -> None:
        response = client.dataset_storages.gcs.with_raw_response.update(
            0,
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = response.parse()
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: LabelStudio) -> None:
        with client.dataset_storages.gcs.with_streaming_response.update(
            0,
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = response.parse()
            assert_matches_type(GcsDatasetStorage, gc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.list()
        assert_matches_type(GcListResponse, gc, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.list(
            dataset=0,
            ordering="string",
        )
        assert_matches_type(GcListResponse, gc, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LabelStudio) -> None:
        response = client.dataset_storages.gcs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = response.parse()
        assert_matches_type(GcListResponse, gc, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LabelStudio) -> None:
        with client.dataset_storages.gcs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = response.parse()
            assert_matches_type(GcListResponse, gc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.delete(
            0,
        )
        assert gc is None

    @parametrize
    def test_raw_response_delete(self, client: LabelStudio) -> None:
        response = client.dataset_storages.gcs.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = response.parse()
        assert gc is None

    @parametrize
    def test_streaming_response_delete(self, client: LabelStudio) -> None:
        with client.dataset_storages.gcs.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = response.parse()
            assert gc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_check_for_records(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.check_for_records(
            dataset=0,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_method_check_for_records_with_all_params(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.check_for_records(
            dataset=0,
            bucket="string",
            description="string",
            glob_pattern="string",
            google_application_credentials="string",
            google_project_id="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            regex_filter="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_raw_response_check_for_records(self, client: LabelStudio) -> None:
        response = client.dataset_storages.gcs.with_raw_response.check_for_records(
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = response.parse()
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_streaming_response_check_for_records(self, client: LabelStudio) -> None:
        with client.dataset_storages.gcs.with_streaming_response.check_for_records(
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = response.parse()
            assert_matches_type(GcsDatasetStorage, gc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_sync(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.sync(
            "string",
            dataset=0,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_method_sync_with_all_params(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.sync(
            "string",
            dataset=0,
            bucket="string",
            description="string",
            glob_pattern="string",
            google_application_credentials="string",
            google_project_id="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            regex_filter="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_raw_response_sync(self, client: LabelStudio) -> None:
        response = client.dataset_storages.gcs.with_raw_response.sync(
            "string",
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = response.parse()
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_streaming_response_sync(self, client: LabelStudio) -> None:
        with client.dataset_storages.gcs.with_streaming_response.sync(
            "string",
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = response.parse()
            assert_matches_type(GcsDatasetStorage, gc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_sync(self, client: LabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.dataset_storages.gcs.with_raw_response.sync(
                "",
                dataset=0,
            )

    @parametrize
    def test_method_validate(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.validate(
            dataset=0,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_method_validate_with_all_params(self, client: LabelStudio) -> None:
        gc = client.dataset_storages.gcs.validate(
            dataset=0,
            bucket="string",
            description="string",
            glob_pattern="string",
            google_application_credentials="string",
            google_project_id="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            regex_filter="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_raw_response_validate(self, client: LabelStudio) -> None:
        response = client.dataset_storages.gcs.with_raw_response.validate(
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = response.parse()
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    def test_streaming_response_validate(self, client: LabelStudio) -> None:
        with client.dataset_storages.gcs.with_streaming_response.validate(
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = response.parse()
            assert_matches_type(GcsDatasetStorage, gc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGcs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.create(
            dataset=0,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.create(
            dataset=0,
            bucket="string",
            description="string",
            glob_pattern="string",
            google_application_credentials="string",
            google_project_id="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            regex_filter="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages.gcs.with_raw_response.create(
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = await response.parse()
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages.gcs.with_streaming_response.create(
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = await response.parse()
            assert_matches_type(GcsDatasetStorage, gc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.retrieve(
            0,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages.gcs.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = await response.parse()
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages.gcs.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = await response.parse()
            assert_matches_type(GcsDatasetStorage, gc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.update(
            0,
            dataset=0,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.update(
            0,
            dataset=0,
            bucket="string",
            description="string",
            glob_pattern="string",
            google_application_credentials="string",
            google_project_id="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            regex_filter="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages.gcs.with_raw_response.update(
            0,
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = await response.parse()
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages.gcs.with_streaming_response.update(
            0,
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = await response.parse()
            assert_matches_type(GcsDatasetStorage, gc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.list()
        assert_matches_type(GcListResponse, gc, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.list(
            dataset=0,
            ordering="string",
        )
        assert_matches_type(GcListResponse, gc, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages.gcs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = await response.parse()
        assert_matches_type(GcListResponse, gc, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages.gcs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = await response.parse()
            assert_matches_type(GcListResponse, gc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.delete(
            0,
        )
        assert gc is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages.gcs.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = await response.parse()
        assert gc is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages.gcs.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = await response.parse()
            assert gc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_check_for_records(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.check_for_records(
            dataset=0,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_method_check_for_records_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.check_for_records(
            dataset=0,
            bucket="string",
            description="string",
            glob_pattern="string",
            google_application_credentials="string",
            google_project_id="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            regex_filter="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_raw_response_check_for_records(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages.gcs.with_raw_response.check_for_records(
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = await response.parse()
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_streaming_response_check_for_records(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages.gcs.with_streaming_response.check_for_records(
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = await response.parse()
            assert_matches_type(GcsDatasetStorage, gc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_sync(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.sync(
            "string",
            dataset=0,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_method_sync_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.sync(
            "string",
            dataset=0,
            bucket="string",
            description="string",
            glob_pattern="string",
            google_application_credentials="string",
            google_project_id="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            regex_filter="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_raw_response_sync(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages.gcs.with_raw_response.sync(
            "string",
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = await response.parse()
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_streaming_response_sync(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages.gcs.with_streaming_response.sync(
            "string",
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = await response.parse()
            assert_matches_type(GcsDatasetStorage, gc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_sync(self, async_client: AsyncLabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.dataset_storages.gcs.with_raw_response.sync(
                "",
                dataset=0,
            )

    @parametrize
    async def test_method_validate(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.validate(
            dataset=0,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        gc = await async_client.dataset_storages.gcs.validate(
            dataset=0,
            bucket="string",
            description="string",
            glob_pattern="string",
            google_application_credentials="string",
            google_project_id="string",
            last_sync=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_sync_count=0,
            last_sync_job="string",
            meta={},
            prefix="string",
            presign=True,
            presign_ttl=0,
            regex_filter="string",
            status="initialized",
            synced=True,
            synchronizable=True,
            title="string",
            traceback="string",
            use_blob_urls=True,
        )
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages.gcs.with_raw_response.validate(
            dataset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gc = await response.parse()
        assert_matches_type(GcsDatasetStorage, gc, path=["response"])

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages.gcs.with_streaming_response.validate(
            dataset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gc = await response.parse()
            assert_matches_type(GcsDatasetStorage, gc, path=["response"])

        assert cast(Any, response.is_closed) is True
