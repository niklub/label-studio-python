# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from label_studio import LabelStudio, AsyncLabelStudio
from label_studio.types import (
    MlGetResponse,
    MlListResponse,
    MlCreateResponse,
    MlUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMl:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LabelStudio) -> None:
        ml = client.ml.create()
        assert_matches_type(MlCreateResponse, ml, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LabelStudio) -> None:
        ml = client.ml.create(
            project=0,
            url="string",
        )
        assert_matches_type(MlCreateResponse, ml, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LabelStudio) -> None:
        response = client.ml.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ml = response.parse()
        assert_matches_type(MlCreateResponse, ml, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LabelStudio) -> None:
        with client.ml.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ml = response.parse()
            assert_matches_type(MlCreateResponse, ml, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: LabelStudio) -> None:
        ml = client.ml.update(
            0,
            project=0,
            url="x",
        )
        assert_matches_type(MlUpdateResponse, ml, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: LabelStudio) -> None:
        ml = client.ml.update(
            0,
            project=0,
            url="x",
            auth_method="NONE",
            auto_update=True,
            basic_auth_pass="string",
            basic_auth_user="string",
            description="string",
            error_message="string",
            extra_params={},
            is_interactive=True,
            model_version="string",
            state="CO",
            title="string",
        )
        assert_matches_type(MlUpdateResponse, ml, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: LabelStudio) -> None:
        response = client.ml.with_raw_response.update(
            0,
            project=0,
            url="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ml = response.parse()
        assert_matches_type(MlUpdateResponse, ml, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: LabelStudio) -> None:
        with client.ml.with_streaming_response.update(
            0,
            project=0,
            url="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ml = response.parse()
            assert_matches_type(MlUpdateResponse, ml, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: LabelStudio) -> None:
        ml = client.ml.list()
        assert_matches_type(MlListResponse, ml, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LabelStudio) -> None:
        ml = client.ml.list(
            project=0,
        )
        assert_matches_type(MlListResponse, ml, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LabelStudio) -> None:
        response = client.ml.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ml = response.parse()
        assert_matches_type(MlListResponse, ml, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LabelStudio) -> None:
        with client.ml.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ml = response.parse()
            assert_matches_type(MlListResponse, ml, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LabelStudio) -> None:
        ml = client.ml.delete(
            0,
        )
        assert ml is None

    @parametrize
    def test_raw_response_delete(self, client: LabelStudio) -> None:
        response = client.ml.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ml = response.parse()
        assert ml is None

    @parametrize
    def test_streaming_response_delete(self, client: LabelStudio) -> None:
        with client.ml.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ml = response.parse()
            assert ml is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: LabelStudio) -> None:
        ml = client.ml.get(
            0,
        )
        assert_matches_type(MlGetResponse, ml, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: LabelStudio) -> None:
        response = client.ml.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ml = response.parse()
        assert_matches_type(MlGetResponse, ml, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: LabelStudio) -> None:
        with client.ml.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ml = response.parse()
            assert_matches_type(MlGetResponse, ml, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMl:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLabelStudio) -> None:
        ml = await async_client.ml.create()
        assert_matches_type(MlCreateResponse, ml, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        ml = await async_client.ml.create(
            project=0,
            url="string",
        )
        assert_matches_type(MlCreateResponse, ml, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.ml.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ml = await response.parse()
        assert_matches_type(MlCreateResponse, ml, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.ml.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ml = await response.parse()
            assert_matches_type(MlCreateResponse, ml, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncLabelStudio) -> None:
        ml = await async_client.ml.update(
            0,
            project=0,
            url="x",
        )
        assert_matches_type(MlUpdateResponse, ml, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        ml = await async_client.ml.update(
            0,
            project=0,
            url="x",
            auth_method="NONE",
            auto_update=True,
            basic_auth_pass="string",
            basic_auth_user="string",
            description="string",
            error_message="string",
            extra_params={},
            is_interactive=True,
            model_version="string",
            state="CO",
            title="string",
        )
        assert_matches_type(MlUpdateResponse, ml, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.ml.with_raw_response.update(
            0,
            project=0,
            url="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ml = await response.parse()
        assert_matches_type(MlUpdateResponse, ml, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.ml.with_streaming_response.update(
            0,
            project=0,
            url="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ml = await response.parse()
            assert_matches_type(MlUpdateResponse, ml, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncLabelStudio) -> None:
        ml = await async_client.ml.list()
        assert_matches_type(MlListResponse, ml, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        ml = await async_client.ml.list(
            project=0,
        )
        assert_matches_type(MlListResponse, ml, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.ml.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ml = await response.parse()
        assert_matches_type(MlListResponse, ml, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.ml.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ml = await response.parse()
            assert_matches_type(MlListResponse, ml, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLabelStudio) -> None:
        ml = await async_client.ml.delete(
            0,
        )
        assert ml is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.ml.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ml = await response.parse()
        assert ml is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.ml.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ml = await response.parse()
            assert ml is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncLabelStudio) -> None:
        ml = await async_client.ml.get(
            0,
        )
        assert_matches_type(MlGetResponse, ml, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.ml.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ml = await response.parse()
        assert_matches_type(MlGetResponse, ml, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.ml.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ml = await response.parse()
            assert_matches_type(MlGetResponse, ml, path=["response"])

        assert cast(Any, response.is_closed) is True
