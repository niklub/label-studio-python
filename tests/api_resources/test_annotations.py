# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from label_studio import LabelStudio, AsyncLabelStudio
from label_studio.types import Annotation
from label_studio._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnnotations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LabelStudio) -> None:
        annotation = client.annotations.retrieve(
            0,
        )
        assert_matches_type(Annotation, annotation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LabelStudio) -> None:
        response = client.annotations.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = response.parse()
        assert_matches_type(Annotation, annotation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LabelStudio) -> None:
        with client.annotations.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = response.parse()
            assert_matches_type(Annotation, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: LabelStudio) -> None:
        annotation = client.annotations.update(
            0,
        )
        assert_matches_type(Annotation, annotation, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: LabelStudio) -> None:
        annotation = client.annotations.update(
            0,
            completed_by=0,
            draft_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            ground_truth=True,
            import_id=-9223372036854776000,
            last_action="prediction",
            last_created_by=0,
            lead_time=0,
            parent_annotation=0,
            parent_prediction=0,
            project=0,
            result={},
            task=0,
            unique_id="x",
            updated_by=0,
            was_cancelled=True,
        )
        assert_matches_type(Annotation, annotation, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: LabelStudio) -> None:
        response = client.annotations.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = response.parse()
        assert_matches_type(Annotation, annotation, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: LabelStudio) -> None:
        with client.annotations.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = response.parse()
            assert_matches_type(Annotation, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LabelStudio) -> None:
        annotation = client.annotations.delete(
            0,
        )
        assert annotation is None

    @parametrize
    def test_raw_response_delete(self, client: LabelStudio) -> None:
        response = client.annotations.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = response.parse()
        assert annotation is None

    @parametrize
    def test_streaming_response_delete(self, client: LabelStudio) -> None:
        with client.annotations.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = response.parse()
            assert annotation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAnnotations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLabelStudio) -> None:
        annotation = await async_client.annotations.retrieve(
            0,
        )
        assert_matches_type(Annotation, annotation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.annotations.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = await response.parse()
        assert_matches_type(Annotation, annotation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.annotations.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = await response.parse()
            assert_matches_type(Annotation, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncLabelStudio) -> None:
        annotation = await async_client.annotations.update(
            0,
        )
        assert_matches_type(Annotation, annotation, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        annotation = await async_client.annotations.update(
            0,
            completed_by=0,
            draft_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            ground_truth=True,
            import_id=-9223372036854776000,
            last_action="prediction",
            last_created_by=0,
            lead_time=0,
            parent_annotation=0,
            parent_prediction=0,
            project=0,
            result={},
            task=0,
            unique_id="x",
            updated_by=0,
            was_cancelled=True,
        )
        assert_matches_type(Annotation, annotation, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.annotations.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = await response.parse()
        assert_matches_type(Annotation, annotation, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.annotations.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = await response.parse()
            assert_matches_type(Annotation, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLabelStudio) -> None:
        annotation = await async_client.annotations.delete(
            0,
        )
        assert annotation is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.annotations.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = await response.parse()
        assert annotation is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.annotations.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = await response.parse()
            assert annotation is None

        assert cast(Any, response.is_closed) is True
