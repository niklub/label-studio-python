# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from label_studio import LabelStudio, AsyncLabelStudio
from label_studio.types import (
    AnnotationReview,
    AnnotationReviewListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnnotationReviews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LabelStudio) -> None:
        annotation_review = client.annotation_reviews.create(
            annotation=0,
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LabelStudio) -> None:
        annotation_review = client.annotation_reviews.create(
            annotation=0,
            accepted=True,
            comment="x",
            last_annotation_history=0,
            result={},
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LabelStudio) -> None:
        response = client.annotation_reviews.with_raw_response.create(
            annotation=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_review = response.parse()
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LabelStudio) -> None:
        with client.annotation_reviews.with_streaming_response.create(
            annotation=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_review = response.parse()
            assert_matches_type(AnnotationReview, annotation_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LabelStudio) -> None:
        annotation_review = client.annotation_reviews.retrieve(
            0,
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LabelStudio) -> None:
        response = client.annotation_reviews.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_review = response.parse()
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LabelStudio) -> None:
        with client.annotation_reviews.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_review = response.parse()
            assert_matches_type(AnnotationReview, annotation_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: LabelStudio) -> None:
        annotation_review = client.annotation_reviews.update(
            0,
            annotation=0,
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: LabelStudio) -> None:
        annotation_review = client.annotation_reviews.update(
            0,
            annotation=0,
            accepted=True,
            comment="x",
            last_annotation_history=0,
            result={},
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: LabelStudio) -> None:
        response = client.annotation_reviews.with_raw_response.update(
            0,
            annotation=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_review = response.parse()
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: LabelStudio) -> None:
        with client.annotation_reviews.with_streaming_response.update(
            0,
            annotation=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_review = response.parse()
            assert_matches_type(AnnotationReview, annotation_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: LabelStudio) -> None:
        annotation_review = client.annotation_reviews.list()
        assert_matches_type(AnnotationReviewListResponse, annotation_review, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LabelStudio) -> None:
        annotation_review = client.annotation_reviews.list(
            annotation="string",
            annotation_task_project="string",
            ordering="string",
        )
        assert_matches_type(AnnotationReviewListResponse, annotation_review, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LabelStudio) -> None:
        response = client.annotation_reviews.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_review = response.parse()
        assert_matches_type(AnnotationReviewListResponse, annotation_review, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LabelStudio) -> None:
        with client.annotation_reviews.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_review = response.parse()
            assert_matches_type(AnnotationReviewListResponse, annotation_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LabelStudio) -> None:
        annotation_review = client.annotation_reviews.delete(
            0,
        )
        assert annotation_review is None

    @parametrize
    def test_raw_response_delete(self, client: LabelStudio) -> None:
        response = client.annotation_reviews.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_review = response.parse()
        assert annotation_review is None

    @parametrize
    def test_streaming_response_delete(self, client: LabelStudio) -> None:
        with client.annotation_reviews.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_review = response.parse()
            assert annotation_review is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_overwrite(self, client: LabelStudio) -> None:
        annotation_review = client.annotation_reviews.overwrite(
            0,
            annotation=0,
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    def test_method_overwrite_with_all_params(self, client: LabelStudio) -> None:
        annotation_review = client.annotation_reviews.overwrite(
            0,
            annotation=0,
            accepted=True,
            comment="x",
            last_annotation_history=0,
            result={},
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    def test_raw_response_overwrite(self, client: LabelStudio) -> None:
        response = client.annotation_reviews.with_raw_response.overwrite(
            0,
            annotation=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_review = response.parse()
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    def test_streaming_response_overwrite(self, client: LabelStudio) -> None:
        with client.annotation_reviews.with_streaming_response.overwrite(
            0,
            annotation=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_review = response.parse()
            assert_matches_type(AnnotationReview, annotation_review, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnnotationReviews:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLabelStudio) -> None:
        annotation_review = await async_client.annotation_reviews.create(
            annotation=0,
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        annotation_review = await async_client.annotation_reviews.create(
            annotation=0,
            accepted=True,
            comment="x",
            last_annotation_history=0,
            result={},
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.annotation_reviews.with_raw_response.create(
            annotation=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_review = await response.parse()
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.annotation_reviews.with_streaming_response.create(
            annotation=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_review = await response.parse()
            assert_matches_type(AnnotationReview, annotation_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLabelStudio) -> None:
        annotation_review = await async_client.annotation_reviews.retrieve(
            0,
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.annotation_reviews.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_review = await response.parse()
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.annotation_reviews.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_review = await response.parse()
            assert_matches_type(AnnotationReview, annotation_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncLabelStudio) -> None:
        annotation_review = await async_client.annotation_reviews.update(
            0,
            annotation=0,
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        annotation_review = await async_client.annotation_reviews.update(
            0,
            annotation=0,
            accepted=True,
            comment="x",
            last_annotation_history=0,
            result={},
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.annotation_reviews.with_raw_response.update(
            0,
            annotation=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_review = await response.parse()
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.annotation_reviews.with_streaming_response.update(
            0,
            annotation=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_review = await response.parse()
            assert_matches_type(AnnotationReview, annotation_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncLabelStudio) -> None:
        annotation_review = await async_client.annotation_reviews.list()
        assert_matches_type(AnnotationReviewListResponse, annotation_review, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        annotation_review = await async_client.annotation_reviews.list(
            annotation="string",
            annotation_task_project="string",
            ordering="string",
        )
        assert_matches_type(AnnotationReviewListResponse, annotation_review, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.annotation_reviews.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_review = await response.parse()
        assert_matches_type(AnnotationReviewListResponse, annotation_review, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.annotation_reviews.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_review = await response.parse()
            assert_matches_type(AnnotationReviewListResponse, annotation_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLabelStudio) -> None:
        annotation_review = await async_client.annotation_reviews.delete(
            0,
        )
        assert annotation_review is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.annotation_reviews.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_review = await response.parse()
        assert annotation_review is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.annotation_reviews.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_review = await response.parse()
            assert annotation_review is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_overwrite(self, async_client: AsyncLabelStudio) -> None:
        annotation_review = await async_client.annotation_reviews.overwrite(
            0,
            annotation=0,
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    async def test_method_overwrite_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        annotation_review = await async_client.annotation_reviews.overwrite(
            0,
            annotation=0,
            accepted=True,
            comment="x",
            last_annotation_history=0,
            result={},
        )
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    async def test_raw_response_overwrite(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.annotation_reviews.with_raw_response.overwrite(
            0,
            annotation=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation_review = await response.parse()
        assert_matches_type(AnnotationReview, annotation_review, path=["response"])

    @parametrize
    async def test_streaming_response_overwrite(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.annotation_reviews.with_streaming_response.overwrite(
            0,
            annotation=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation_review = await response.parse()
            assert_matches_type(AnnotationReview, annotation_review, path=["response"])

        assert cast(Any, response.is_closed) is True
