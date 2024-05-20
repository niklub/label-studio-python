# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import ml_list_params, ml_create_params, ml_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ..types.ml_get_response import MlGetResponse
from ..types.ml_list_response import MlListResponse
from ..types.ml_create_response import MlCreateResponse
from ..types.ml_update_response import MlUpdateResponse

__all__ = ["MlResource", "AsyncMlResource"]


class MlResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MlResourceWithRawResponse:
        return MlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MlResourceWithStreamingResponse:
        return MlResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project: int | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MlCreateResponse:
        """
        Add an ML backend to a project using the Label Studio UI or by sending a POST
        request using the following cURL command:

        ```bash
        curl -X POST -H 'Content-type: application/json' https://app.heartex.com/api/ml -H 'Authorization: Token abc123'\\
        --data '{"url": "http://localhost:9090", "project": {project_id}}'
        ```

        Args:
          project: Project ID

          url: ML backend URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/ml/",
            body=maybe_transform(
                {
                    "project": project,
                    "url": url,
                },
                ml_create_params.MlCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MlCreateResponse,
        )

    def update(
        self,
        id: int,
        *,
        project: int,
        url: str,
        auth_method: Literal["NONE", "BASIC_AUTH"] | NotGiven = NOT_GIVEN,
        auto_update: bool | NotGiven = NOT_GIVEN,
        basic_auth_pass: Optional[str] | NotGiven = NOT_GIVEN,
        basic_auth_user: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        error_message: Optional[str] | NotGiven = NOT_GIVEN,
        extra_params: Optional[object] | NotGiven = NOT_GIVEN,
        is_interactive: bool | NotGiven = NOT_GIVEN,
        model_version: Optional[str] | NotGiven = NOT_GIVEN,
        state: Literal["CO", "DI", "ER", "TR", "PR"] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MlUpdateResponse:
        """
        Update ML backend parameters using the Label Studio UI or by sending a PATCH
        request using the following cURL command:

        ```bash
        curl -X PATCH -H 'Content-type: application/json' https://app.heartex.com/api/ml/{ml_backend_ID} -H 'Authorization: Token abc123'\\
        --data '{"url": "http://localhost:9091"}'
        ```

        Args:
          url: URL for the machine learning model server

          auto_update: If false, model version is set by the user, if true - getting latest version
              from backend.

          basic_auth_user: HTTP Basic Auth user

          description: Description for the machine learning backend

          error_message: Error message in error state

          extra_params: Any extra parameters passed to the ML Backend during the setup

          is_interactive: Used to interactively annotate tasks. If true, model returns one list with
              results

          model_version: Current model version associated with this machine learning backend

          title: Name of the machine learning backend

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/api/ml/{id}",
            body=maybe_transform(
                {
                    "project": project,
                    "url": url,
                    "auth_method": auth_method,
                    "auto_update": auto_update,
                    "basic_auth_pass": basic_auth_pass,
                    "basic_auth_user": basic_auth_user,
                    "description": description,
                    "error_message": error_message,
                    "extra_params": extra_params,
                    "is_interactive": is_interactive,
                    "model_version": model_version,
                    "state": state,
                    "title": title,
                },
                ml_update_params.MlUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MlUpdateResponse,
        )

    def list(
        self,
        *,
        project: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MlListResponse:
        """List all configured ML backends for a specific project by ID.

        Use the following
        cURL command:

        ```bash
        curl https://app.heartex.com/api/ml?project={project_id} -H 'Authorization: Token abc123'
        ```

        Args:
          project: Project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/ml/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project": project}, ml_list_params.MlListParams),
            ),
            cast_to=MlListResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Remove an existing ML backend connection by ID.

        For example, use the following
        cURL command:

        ```bash
        curl -X DELETE https://app.heartex.com/api/ml/{ml_backend_ID} -H 'Authorization: Token abc123'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/ml/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MlGetResponse:
        """Get details about a specific ML backend connection by ID.

        For example, make a
        GET request using the following cURL command:

        ```bash
        curl https://app.heartex.com/api/ml/{ml_backend_ID} -H 'Authorization: Token abc123'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/ml/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MlGetResponse,
        )


class AsyncMlResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMlResourceWithRawResponse:
        return AsyncMlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMlResourceWithStreamingResponse:
        return AsyncMlResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project: int | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MlCreateResponse:
        """
        Add an ML backend to a project using the Label Studio UI or by sending a POST
        request using the following cURL command:

        ```bash
        curl -X POST -H 'Content-type: application/json' https://app.heartex.com/api/ml -H 'Authorization: Token abc123'\\
        --data '{"url": "http://localhost:9090", "project": {project_id}}'
        ```

        Args:
          project: Project ID

          url: ML backend URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/ml/",
            body=await async_maybe_transform(
                {
                    "project": project,
                    "url": url,
                },
                ml_create_params.MlCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MlCreateResponse,
        )

    async def update(
        self,
        id: int,
        *,
        project: int,
        url: str,
        auth_method: Literal["NONE", "BASIC_AUTH"] | NotGiven = NOT_GIVEN,
        auto_update: bool | NotGiven = NOT_GIVEN,
        basic_auth_pass: Optional[str] | NotGiven = NOT_GIVEN,
        basic_auth_user: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        error_message: Optional[str] | NotGiven = NOT_GIVEN,
        extra_params: Optional[object] | NotGiven = NOT_GIVEN,
        is_interactive: bool | NotGiven = NOT_GIVEN,
        model_version: Optional[str] | NotGiven = NOT_GIVEN,
        state: Literal["CO", "DI", "ER", "TR", "PR"] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MlUpdateResponse:
        """
        Update ML backend parameters using the Label Studio UI or by sending a PATCH
        request using the following cURL command:

        ```bash
        curl -X PATCH -H 'Content-type: application/json' https://app.heartex.com/api/ml/{ml_backend_ID} -H 'Authorization: Token abc123'\\
        --data '{"url": "http://localhost:9091"}'
        ```

        Args:
          url: URL for the machine learning model server

          auto_update: If false, model version is set by the user, if true - getting latest version
              from backend.

          basic_auth_user: HTTP Basic Auth user

          description: Description for the machine learning backend

          error_message: Error message in error state

          extra_params: Any extra parameters passed to the ML Backend during the setup

          is_interactive: Used to interactively annotate tasks. If true, model returns one list with
              results

          model_version: Current model version associated with this machine learning backend

          title: Name of the machine learning backend

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/api/ml/{id}",
            body=await async_maybe_transform(
                {
                    "project": project,
                    "url": url,
                    "auth_method": auth_method,
                    "auto_update": auto_update,
                    "basic_auth_pass": basic_auth_pass,
                    "basic_auth_user": basic_auth_user,
                    "description": description,
                    "error_message": error_message,
                    "extra_params": extra_params,
                    "is_interactive": is_interactive,
                    "model_version": model_version,
                    "state": state,
                    "title": title,
                },
                ml_update_params.MlUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MlUpdateResponse,
        )

    async def list(
        self,
        *,
        project: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MlListResponse:
        """List all configured ML backends for a specific project by ID.

        Use the following
        cURL command:

        ```bash
        curl https://app.heartex.com/api/ml?project={project_id} -H 'Authorization: Token abc123'
        ```

        Args:
          project: Project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/ml/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project": project}, ml_list_params.MlListParams),
            ),
            cast_to=MlListResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Remove an existing ML backend connection by ID.

        For example, use the following
        cURL command:

        ```bash
        curl -X DELETE https://app.heartex.com/api/ml/{ml_backend_ID} -H 'Authorization: Token abc123'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/ml/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MlGetResponse:
        """Get details about a specific ML backend connection by ID.

        For example, make a
        GET request using the following cURL command:

        ```bash
        curl https://app.heartex.com/api/ml/{ml_backend_ID} -H 'Authorization: Token abc123'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/ml/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MlGetResponse,
        )


class MlResourceWithRawResponse:
    def __init__(self, ml: MlResource) -> None:
        self._ml = ml

        self.create = to_raw_response_wrapper(
            ml.create,
        )
        self.update = to_raw_response_wrapper(
            ml.update,
        )
        self.list = to_raw_response_wrapper(
            ml.list,
        )
        self.delete = to_raw_response_wrapper(
            ml.delete,
        )
        self.get = to_raw_response_wrapper(
            ml.get,
        )


class AsyncMlResourceWithRawResponse:
    def __init__(self, ml: AsyncMlResource) -> None:
        self._ml = ml

        self.create = async_to_raw_response_wrapper(
            ml.create,
        )
        self.update = async_to_raw_response_wrapper(
            ml.update,
        )
        self.list = async_to_raw_response_wrapper(
            ml.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ml.delete,
        )
        self.get = async_to_raw_response_wrapper(
            ml.get,
        )


class MlResourceWithStreamingResponse:
    def __init__(self, ml: MlResource) -> None:
        self._ml = ml

        self.create = to_streamed_response_wrapper(
            ml.create,
        )
        self.update = to_streamed_response_wrapper(
            ml.update,
        )
        self.list = to_streamed_response_wrapper(
            ml.list,
        )
        self.delete = to_streamed_response_wrapper(
            ml.delete,
        )
        self.get = to_streamed_response_wrapper(
            ml.get,
        )


class AsyncMlResourceWithStreamingResponse:
    def __init__(self, ml: AsyncMlResource) -> None:
        self._ml = ml

        self.create = async_to_streamed_response_wrapper(
            ml.create,
        )
        self.update = async_to_streamed_response_wrapper(
            ml.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ml.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ml.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            ml.get,
        )
