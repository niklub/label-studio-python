# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from label_studio import LabelStudio, AsyncLabelStudio
from label_studio.types import LseUser, CurrentUserResetTokenResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCurrentUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LabelStudio) -> None:
        current_user = client.current_user.retrieve()
        assert_matches_type(LseUser, current_user, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LabelStudio) -> None:
        response = client.current_user.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        current_user = response.parse()
        assert_matches_type(LseUser, current_user, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LabelStudio) -> None:
        with client.current_user.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            current_user = response.parse()
            assert_matches_type(LseUser, current_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reset_token(self, client: LabelStudio) -> None:
        current_user = client.current_user.reset_token()
        assert_matches_type(CurrentUserResetTokenResponse, current_user, path=["response"])

    @parametrize
    def test_raw_response_reset_token(self, client: LabelStudio) -> None:
        response = client.current_user.with_raw_response.reset_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        current_user = response.parse()
        assert_matches_type(CurrentUserResetTokenResponse, current_user, path=["response"])

    @parametrize
    def test_streaming_response_reset_token(self, client: LabelStudio) -> None:
        with client.current_user.with_streaming_response.reset_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            current_user = response.parse()
            assert_matches_type(CurrentUserResetTokenResponse, current_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_token(self, client: LabelStudio) -> None:
        current_user = client.current_user.retrieve_token()
        assert current_user is None

    @parametrize
    def test_raw_response_retrieve_token(self, client: LabelStudio) -> None:
        response = client.current_user.with_raw_response.retrieve_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        current_user = response.parse()
        assert current_user is None

    @parametrize
    def test_streaming_response_retrieve_token(self, client: LabelStudio) -> None:
        with client.current_user.with_streaming_response.retrieve_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            current_user = response.parse()
            assert current_user is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCurrentUser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLabelStudio) -> None:
        current_user = await async_client.current_user.retrieve()
        assert_matches_type(LseUser, current_user, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.current_user.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        current_user = await response.parse()
        assert_matches_type(LseUser, current_user, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.current_user.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            current_user = await response.parse()
            assert_matches_type(LseUser, current_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reset_token(self, async_client: AsyncLabelStudio) -> None:
        current_user = await async_client.current_user.reset_token()
        assert_matches_type(CurrentUserResetTokenResponse, current_user, path=["response"])

    @parametrize
    async def test_raw_response_reset_token(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.current_user.with_raw_response.reset_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        current_user = await response.parse()
        assert_matches_type(CurrentUserResetTokenResponse, current_user, path=["response"])

    @parametrize
    async def test_streaming_response_reset_token(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.current_user.with_streaming_response.reset_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            current_user = await response.parse()
            assert_matches_type(CurrentUserResetTokenResponse, current_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_token(self, async_client: AsyncLabelStudio) -> None:
        current_user = await async_client.current_user.retrieve_token()
        assert current_user is None

    @parametrize
    async def test_raw_response_retrieve_token(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.current_user.with_raw_response.retrieve_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        current_user = await response.parse()
        assert current_user is None

    @parametrize
    async def test_streaming_response_retrieve_token(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.current_user.with_streaming_response.retrieve_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            current_user = await response.parse()
            assert current_user is None

        assert cast(Any, response.is_closed) is True
