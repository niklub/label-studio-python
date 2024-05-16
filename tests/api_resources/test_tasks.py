# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from label_studio import LabelStudio, AsyncLabelStudio
from label_studio.types import (
    TaskGetResponse,
    TaskListResponse,
    TaskCreateResponse,
    TaskUpdateResponse,
)
from label_studio._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LabelStudio) -> None:
        task = client.tasks.create(
            data={},
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LabelStudio) -> None:
        task = client.tasks.create(
            data={},
            cancelled_annotations=-2147483648,
            comment_authors=[0],
            comment_count=-2147483648,
            file_upload=0,
            inner_id=-9223372036854776000,
            is_labeled=True,
            last_comment_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            meta={},
            overlap=-2147483648,
            project=0,
            total_annotations=-2147483648,
            total_predictions=-2147483648,
            unresolved_comment_count=-2147483648,
            updated_by=0,
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LabelStudio) -> None:
        response = client.tasks.with_raw_response.create(
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LabelStudio) -> None:
        with client.tasks.with_streaming_response.create(
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: LabelStudio) -> None:
        task = client.tasks.update(
            "string",
            data={},
        )
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: LabelStudio) -> None:
        task = client.tasks.update(
            "string",
            data={},
            cancelled_annotations=-2147483648,
            comment_authors=[0],
            comment_count=-2147483648,
            file_upload=0,
            inner_id=-9223372036854776000,
            is_labeled=True,
            last_comment_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            meta={},
            overlap=-2147483648,
            project=0,
            total_annotations=-2147483648,
            total_predictions=-2147483648,
            unresolved_comment_count=-2147483648,
            updated_by=0,
        )
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: LabelStudio) -> None:
        response = client.tasks.with_raw_response.update(
            "string",
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: LabelStudio) -> None:
        with client.tasks.with_streaming_response.update(
            "string",
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskUpdateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: LabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.with_raw_response.update(
                "",
                data={},
            )

    @parametrize
    def test_method_list(self, client: LabelStudio) -> None:
        task = client.tasks.list()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LabelStudio) -> None:
        task = client.tasks.list(
            page=0,
            page_size=0,
            project=0,
            resolve_uri=True,
            view=0,
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LabelStudio) -> None:
        response = client.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LabelStudio) -> None:
        with client.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LabelStudio) -> None:
        task = client.tasks.delete(
            "string",
        )
        assert task is None

    @parametrize
    def test_raw_response_delete(self, client: LabelStudio) -> None:
        response = client.tasks.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert task is None

    @parametrize
    def test_streaming_response_delete(self, client: LabelStudio) -> None:
        with client.tasks.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert task is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: LabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: LabelStudio) -> None:
        task = client.tasks.get(
            "string",
        )
        assert_matches_type(TaskGetResponse, task, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: LabelStudio) -> None:
        response = client.tasks.with_raw_response.get(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskGetResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: LabelStudio) -> None:
        with client.tasks.with_streaming_response.get(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskGetResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: LabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.with_raw_response.get(
                "",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLabelStudio) -> None:
        task = await async_client.tasks.create(
            data={},
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        task = await async_client.tasks.create(
            data={},
            cancelled_annotations=-2147483648,
            comment_authors=[0],
            comment_count=-2147483648,
            file_upload=0,
            inner_id=-9223372036854776000,
            is_labeled=True,
            last_comment_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            meta={},
            overlap=-2147483648,
            project=0,
            total_annotations=-2147483648,
            total_predictions=-2147483648,
            unresolved_comment_count=-2147483648,
            updated_by=0,
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.tasks.with_raw_response.create(
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.tasks.with_streaming_response.create(
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncLabelStudio) -> None:
        task = await async_client.tasks.update(
            "string",
            data={},
        )
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        task = await async_client.tasks.update(
            "string",
            data={},
            cancelled_annotations=-2147483648,
            comment_authors=[0],
            comment_count=-2147483648,
            file_upload=0,
            inner_id=-9223372036854776000,
            is_labeled=True,
            last_comment_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            meta={},
            overlap=-2147483648,
            project=0,
            total_annotations=-2147483648,
            total_predictions=-2147483648,
            unresolved_comment_count=-2147483648,
            updated_by=0,
        )
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.tasks.with_raw_response.update(
            "string",
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.tasks.with_streaming_response.update(
            "string",
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskUpdateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.with_raw_response.update(
                "",
                data={},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLabelStudio) -> None:
        task = await async_client.tasks.list()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        task = await async_client.tasks.list(
            page=0,
            page_size=0,
            project=0,
            resolve_uri=True,
            view=0,
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLabelStudio) -> None:
        task = await async_client.tasks.delete(
            "string",
        )
        assert task is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.tasks.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert task is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.tasks.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert task is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncLabelStudio) -> None:
        task = await async_client.tasks.get(
            "string",
        )
        assert_matches_type(TaskGetResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.tasks.with_raw_response.get(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskGetResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.tasks.with_streaming_response.get(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskGetResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncLabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.with_raw_response.get(
                "",
            )
