# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from label_studio import LabelStudio, AsyncLabelStudio
from label_studio.types import (
    AnnotationHistoryListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnnotationHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: LabelStudio) -> None:
        annotation_history = client.annotation_history.list()
        assert_matches_type(AnnotationHistoryListResponse, annotation_history, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LabelStudio) -> None:
        annotation_history = client.annotation_history.list(
            annotation=0,
            ordering="string",
        )
        assert_matches_type(AnnotationHistoryListResponse, annotation_history, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LabelStudio) -> None:
        response = client.annotation_history.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_history = response.parse()
        assert_matches_type(AnnotationHistoryListResponse, annotation_history, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LabelStudio) -> None:
        with client.annotation_history.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_history = response.parse()
            assert_matches_type(AnnotationHistoryListResponse, annotation_history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LabelStudio) -> None:
        annotation_history = client.annotation_history.delete()
        assert annotation_history is None

    @parametrize
    def test_method_delete_with_all_params(self, client: LabelStudio) -> None:
        annotation_history = client.annotation_history.delete(
            annotation=0,
            project=0,
            task=0,
        )
        assert annotation_history is None

    @parametrize
    def test_raw_response_delete(self, client: LabelStudio) -> None:
        response = client.annotation_history.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_history = response.parse()
        assert annotation_history is None

    @parametrize
    def test_streaming_response_delete(self, client: LabelStudio) -> None:
        with client.annotation_history.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_history = response.parse()
            assert annotation_history is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAnnotationHistory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLabelStudio) -> None:
        annotation_history = await async_client.annotation_history.list()
        assert_matches_type(AnnotationHistoryListResponse, annotation_history, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        annotation_history = await async_client.annotation_history.list(
            annotation=0,
            ordering="string",
        )
        assert_matches_type(AnnotationHistoryListResponse, annotation_history, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.annotation_history.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_history = await response.parse()
        assert_matches_type(AnnotationHistoryListResponse, annotation_history, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.annotation_history.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_history = await response.parse()
            assert_matches_type(AnnotationHistoryListResponse, annotation_history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLabelStudio) -> None:
        annotation_history = await async_client.annotation_history.delete()
        assert annotation_history is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        annotation_history = await async_client.annotation_history.delete(
            annotation=0,
            project=0,
            task=0,
        )
        assert annotation_history is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.annotation_history.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_history = await response.parse()
        assert annotation_history is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.annotation_history.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_history = await response.parse()
            assert annotation_history is None

        assert cast(Any, response.is_closed) is True
