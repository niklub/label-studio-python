# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from label_studio import LabelStudio, AsyncLabelStudio
from label_studio.types import (
    Comment,
    CommentListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LabelStudio) -> None:
        comment = client.comments.create()
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LabelStudio) -> None:
        comment = client.comments.create(
            annotation=0,
            draft=0,
            is_resolved=True,
            text="string",
        )
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LabelStudio) -> None:
        response = client.comments.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LabelStudio) -> None:
        with client.comments.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(Comment, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LabelStudio) -> None:
        comment = client.comments.retrieve(
            "string",
        )
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LabelStudio) -> None:
        response = client.comments.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LabelStudio) -> None:
        with client.comments.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(Comment, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.comments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: LabelStudio) -> None:
        comment = client.comments.update(
            "string",
        )
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: LabelStudio) -> None:
        comment = client.comments.update(
            "string",
            annotation=0,
            draft=0,
            is_resolved=True,
            text="string",
        )
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: LabelStudio) -> None:
        response = client.comments.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: LabelStudio) -> None:
        with client.comments.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(Comment, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: LabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.comments.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: LabelStudio) -> None:
        comment = client.comments.list()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LabelStudio) -> None:
        comment = client.comments.list(
            ordering="string",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LabelStudio) -> None:
        response = client.comments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LabelStudio) -> None:
        with client.comments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentListResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LabelStudio) -> None:
        comment = client.comments.delete(
            "string",
        )
        assert comment is None

    @parametrize
    def test_raw_response_delete(self, client: LabelStudio) -> None:
        response = client.comments.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert comment is None

    @parametrize
    def test_streaming_response_delete(self, client: LabelStudio) -> None:
        with client.comments.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert comment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: LabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.comments.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_overwrite(self, client: LabelStudio) -> None:
        comment = client.comments.overwrite(
            "string",
        )
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    def test_method_overwrite_with_all_params(self, client: LabelStudio) -> None:
        comment = client.comments.overwrite(
            "string",
            annotation=0,
            draft=0,
            is_resolved=True,
            text="string",
        )
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    def test_raw_response_overwrite(self, client: LabelStudio) -> None:
        response = client.comments.with_raw_response.overwrite(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    def test_streaming_response_overwrite(self, client: LabelStudio) -> None:
        with client.comments.with_streaming_response.overwrite(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(Comment, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_overwrite(self, client: LabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.comments.with_raw_response.overwrite(
                "",
            )


class TestAsyncComments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLabelStudio) -> None:
        comment = await async_client.comments.create()
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        comment = await async_client.comments.create(
            annotation=0,
            draft=0,
            is_resolved=True,
            text="string",
        )
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.comments.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.comments.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(Comment, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLabelStudio) -> None:
        comment = await async_client.comments.retrieve(
            "string",
        )
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.comments.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.comments.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(Comment, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.comments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLabelStudio) -> None:
        comment = await async_client.comments.update(
            "string",
        )
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        comment = await async_client.comments.update(
            "string",
            annotation=0,
            draft=0,
            is_resolved=True,
            text="string",
        )
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.comments.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.comments.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(Comment, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.comments.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLabelStudio) -> None:
        comment = await async_client.comments.list()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        comment = await async_client.comments.list(
            ordering="string",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.comments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.comments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentListResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLabelStudio) -> None:
        comment = await async_client.comments.delete(
            "string",
        )
        assert comment is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.comments.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert comment is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.comments.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert comment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.comments.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_overwrite(self, async_client: AsyncLabelStudio) -> None:
        comment = await async_client.comments.overwrite(
            "string",
        )
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    async def test_method_overwrite_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        comment = await async_client.comments.overwrite(
            "string",
            annotation=0,
            draft=0,
            is_resolved=True,
            text="string",
        )
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    async def test_raw_response_overwrite(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.comments.with_raw_response.overwrite(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(Comment, comment, path=["response"])

    @parametrize
    async def test_streaming_response_overwrite(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.comments.with_streaming_response.overwrite(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(Comment, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_overwrite(self, async_client: AsyncLabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.comments.with_raw_response.overwrite(
                "",
            )
