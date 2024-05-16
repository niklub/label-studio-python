# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.lse_user import LseUser
from ..types.current_user_reset_token_response import CurrentUserResetTokenResponse

__all__ = ["CurrentUserResource", "AsyncCurrentUserResource"]


class CurrentUserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CurrentUserResourceWithRawResponse:
        return CurrentUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrentUserResourceWithStreamingResponse:
        return CurrentUserResourceWithStreamingResponse(self)

    def reset_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CurrentUserResetTokenResponse:
        """Reset the user token for the current user."""
        return self._post(
            "/api/current-user/reset-token/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrentUserResetTokenResponse,
        )

    def token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get a user token to authenticate to the API as the current user."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/current-user/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def whoami(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LseUser:
        """Retrieve details of the account that you are using to access the API."""
        return self._get(
            "/api/current-user/whoami",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LseUser,
        )


class AsyncCurrentUserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCurrentUserResourceWithRawResponse:
        return AsyncCurrentUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrentUserResourceWithStreamingResponse:
        return AsyncCurrentUserResourceWithStreamingResponse(self)

    async def reset_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CurrentUserResetTokenResponse:
        """Reset the user token for the current user."""
        return await self._post(
            "/api/current-user/reset-token/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrentUserResetTokenResponse,
        )

    async def token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get a user token to authenticate to the API as the current user."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/current-user/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def whoami(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LseUser:
        """Retrieve details of the account that you are using to access the API."""
        return await self._get(
            "/api/current-user/whoami",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LseUser,
        )


class CurrentUserResourceWithRawResponse:
    def __init__(self, current_user: CurrentUserResource) -> None:
        self._current_user = current_user

        self.reset_token = to_raw_response_wrapper(
            current_user.reset_token,
        )
        self.token = to_raw_response_wrapper(
            current_user.token,
        )
        self.whoami = to_raw_response_wrapper(
            current_user.whoami,
        )


class AsyncCurrentUserResourceWithRawResponse:
    def __init__(self, current_user: AsyncCurrentUserResource) -> None:
        self._current_user = current_user

        self.reset_token = async_to_raw_response_wrapper(
            current_user.reset_token,
        )
        self.token = async_to_raw_response_wrapper(
            current_user.token,
        )
        self.whoami = async_to_raw_response_wrapper(
            current_user.whoami,
        )


class CurrentUserResourceWithStreamingResponse:
    def __init__(self, current_user: CurrentUserResource) -> None:
        self._current_user = current_user

        self.reset_token = to_streamed_response_wrapper(
            current_user.reset_token,
        )
        self.token = to_streamed_response_wrapper(
            current_user.token,
        )
        self.whoami = to_streamed_response_wrapper(
            current_user.whoami,
        )


class AsyncCurrentUserResourceWithStreamingResponse:
    def __init__(self, current_user: AsyncCurrentUserResource) -> None:
        self._current_user = current_user

        self.reset_token = async_to_streamed_response_wrapper(
            current_user.reset_token,
        )
        self.token = async_to_streamed_response_wrapper(
            current_user.token,
        )
        self.whoami = async_to_streamed_response_wrapper(
            current_user.whoami,
        )
