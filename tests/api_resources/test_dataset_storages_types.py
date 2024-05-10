# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from label_studio import LabelStudio, AsyncLabelStudio

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasetStoragesTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: LabelStudio) -> None:
        dataset_storages_type = client.dataset_storages_types.list()
        assert dataset_storages_type is None

    @parametrize
    def test_raw_response_list(self, client: LabelStudio) -> None:
        response = client.dataset_storages_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_type = response.parse()
        assert dataset_storages_type is None

    @parametrize
    def test_streaming_response_list(self, client: LabelStudio) -> None:
        with client.dataset_storages_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_type = response.parse()
            assert dataset_storages_type is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasetStoragesTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLabelStudio) -> None:
        dataset_storages_type = await async_client.dataset_storages_types.list()
        assert dataset_storages_type is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.dataset_storages_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset_storages_type = await response.parse()
        assert dataset_storages_type is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.dataset_storages_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset_storages_type = await response.parse()
            assert dataset_storages_type is None

        assert cast(Any, response.is_closed) is True