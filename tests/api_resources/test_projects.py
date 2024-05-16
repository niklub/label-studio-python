# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from label_studio import LabelStudio, AsyncLabelStudio
from label_studio.types import (
    ProjectGetResponse,
    ProjectListResponse,
    ProjectCreateResponse,
    ProjectUpdateResponse,
)
from label_studio._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LabelStudio) -> None:
        project = client.projects.create()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LabelStudio) -> None:
        project = client.projects.create(
            color="string",
            control_weights={},
            created_by={
                "first_name": "string",
                "last_name": "string",
                "email": "dev@stainlessapi.com",
            },
            description="string",
            enable_empty_annotation=True,
            evaluate_predictions_automatically=True,
            expert_instruction="string",
            is_draft=True,
            is_published=True,
            label_config="string",
            maximum_annotations=-2147483648,
            min_annotations_to_start_training=-2147483648,
            model_version="string",
            organization=0,
            overlap_cohort_percentage=-2147483648,
            pinned_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            reveal_preannotations_interactively=True,
            sampling="Sequential sampling",
            show_annotation_history=True,
            show_collab_predictions=True,
            show_ground_truth_first=True,
            show_instruction=True,
            show_overlap_first=True,
            show_skip_button=True,
            skip_queue="REQUEUE_FOR_ME",
            task_data_login="string",
            task_data_password="string",
            title="xxx",
            workspace=0,
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LabelStudio) -> None:
        response = client.projects.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LabelStudio) -> None:
        with client.projects.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: LabelStudio) -> None:
        project = client.projects.update(
            0,
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: LabelStudio) -> None:
        project = client.projects.update(
            0,
            color="string",
            control_weights={},
            created_by={
                "first_name": "string",
                "last_name": "string",
                "email": "dev@stainlessapi.com",
            },
            description="string",
            enable_empty_annotation=True,
            evaluate_predictions_automatically=True,
            expert_instruction="string",
            is_draft=True,
            is_published=True,
            label_config="string",
            maximum_annotations=-2147483648,
            min_annotations_to_start_training=-2147483648,
            model_version="string",
            organization=0,
            overlap_cohort_percentage=-2147483648,
            pinned_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            reveal_preannotations_interactively=True,
            sampling="Sequential sampling",
            show_annotation_history=True,
            show_collab_predictions=True,
            show_ground_truth_first=True,
            show_instruction=True,
            show_overlap_first=True,
            show_skip_button=True,
            skip_queue="REQUEUE_FOR_ME",
            task_data_login="string",
            task_data_password="string",
            title="xxx",
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: LabelStudio) -> None:
        response = client.projects.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: LabelStudio) -> None:
        with client.projects.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: LabelStudio) -> None:
        project = client.projects.list()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LabelStudio) -> None:
        project = client.projects.list(
            ids="string",
            ordering="string",
            page=0,
            page_size=0,
            title="string",
            workspaces="string",
        )
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LabelStudio) -> None:
        response = client.projects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LabelStudio) -> None:
        with client.projects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LabelStudio) -> None:
        project = client.projects.delete(
            0,
        )
        assert project is None

    @parametrize
    def test_raw_response_delete(self, client: LabelStudio) -> None:
        response = client.projects.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @parametrize
    def test_streaming_response_delete(self, client: LabelStudio) -> None:
        with client.projects.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: LabelStudio) -> None:
        project = client.projects.get(
            0,
        )
        assert_matches_type(ProjectGetResponse, project, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: LabelStudio) -> None:
        response = client.projects.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectGetResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: LabelStudio) -> None:
        with client.projects.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectGetResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProjects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLabelStudio) -> None:
        project = await async_client.projects.create()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        project = await async_client.projects.create(
            color="string",
            control_weights={},
            created_by={
                "first_name": "string",
                "last_name": "string",
                "email": "dev@stainlessapi.com",
            },
            description="string",
            enable_empty_annotation=True,
            evaluate_predictions_automatically=True,
            expert_instruction="string",
            is_draft=True,
            is_published=True,
            label_config="string",
            maximum_annotations=-2147483648,
            min_annotations_to_start_training=-2147483648,
            model_version="string",
            organization=0,
            overlap_cohort_percentage=-2147483648,
            pinned_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            reveal_preannotations_interactively=True,
            sampling="Sequential sampling",
            show_annotation_history=True,
            show_collab_predictions=True,
            show_ground_truth_first=True,
            show_instruction=True,
            show_overlap_first=True,
            show_skip_button=True,
            skip_queue="REQUEUE_FOR_ME",
            task_data_login="string",
            task_data_password="string",
            title="xxx",
            workspace=0,
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.projects.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.projects.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncLabelStudio) -> None:
        project = await async_client.projects.update(
            0,
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        project = await async_client.projects.update(
            0,
            color="string",
            control_weights={},
            created_by={
                "first_name": "string",
                "last_name": "string",
                "email": "dev@stainlessapi.com",
            },
            description="string",
            enable_empty_annotation=True,
            evaluate_predictions_automatically=True,
            expert_instruction="string",
            is_draft=True,
            is_published=True,
            label_config="string",
            maximum_annotations=-2147483648,
            min_annotations_to_start_training=-2147483648,
            model_version="string",
            organization=0,
            overlap_cohort_percentage=-2147483648,
            pinned_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            reveal_preannotations_interactively=True,
            sampling="Sequential sampling",
            show_annotation_history=True,
            show_collab_predictions=True,
            show_ground_truth_first=True,
            show_instruction=True,
            show_overlap_first=True,
            show_skip_button=True,
            skip_queue="REQUEUE_FOR_ME",
            task_data_login="string",
            task_data_password="string",
            title="xxx",
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.projects.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.projects.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncLabelStudio) -> None:
        project = await async_client.projects.list()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLabelStudio) -> None:
        project = await async_client.projects.list(
            ids="string",
            ordering="string",
            page=0,
            page_size=0,
            title="string",
            workspaces="string",
        )
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.projects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.projects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLabelStudio) -> None:
        project = await async_client.projects.delete(
            0,
        )
        assert project is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.projects.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.projects.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncLabelStudio) -> None:
        project = await async_client.projects.get(
            0,
        )
        assert_matches_type(ProjectGetResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.projects.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectGetResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.projects.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectGetResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True
