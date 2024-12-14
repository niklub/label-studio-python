# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, LabelStudioError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "LabelStudio",
    "AsyncLabelStudio",
    "Client",
    "AsyncClient",
]


class LabelStudio(SyncAPIClient):
    annotation_history: resources.AnnotationHistoryResource
    annotation_reviews: resources.AnnotationReviewsResource
    annotations: resources.AnnotationsResource
    comments: resources.CommentsResource
    current_user: resources.CurrentUserResource
    ml: resources.MlResource
    projects: resources.ProjectsResource
    tasks: resources.TasksResource
    api: resources.APIResource
    dataset_storages: resources.DatasetStoragesResource
    with_raw_response: LabelStudioWithRawResponse
    with_streaming_response: LabelStudioWithStreamedResponse

    # client options
    token: str

    def __init__(
        self,
        *,
        token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous label-studio client instance.

        This automatically infers the `token` argument from the `LABEL_STUDIO_TOKEN` environment variable if it is not provided.
        """
        if token is None:
            token = os.environ.get("LABEL_STUDIO_TOKEN")
        if token is None:
            raise LabelStudioError(
                "The token client option must be set either by passing token to the client or by setting the LABEL_STUDIO_TOKEN environment variable"
            )
        self.token = token

        if base_url is None:
            base_url = os.environ.get("LABEL_STUDIO_BASE_URL")
        if base_url is None:
            base_url = f"https://app.heartex.com/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.annotation_history = resources.AnnotationHistoryResource(self)
        self.annotation_reviews = resources.AnnotationReviewsResource(self)
        self.annotations = resources.AnnotationsResource(self)
        self.comments = resources.CommentsResource(self)
        self.current_user = resources.CurrentUserResource(self)
        self.ml = resources.MlResource(self)
        self.projects = resources.ProjectsResource(self)
        self.tasks = resources.TasksResource(self)
        self.api = resources.APIResource(self)
        self.dataset_storages = resources.DatasetStoragesResource(self)
        self.with_raw_response = LabelStudioWithRawResponse(self)
        self.with_streaming_response = LabelStudioWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        token = self.token
        return {"Authorization": token}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            token=token or self.token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLabelStudio(AsyncAPIClient):
    annotation_history: resources.AsyncAnnotationHistoryResource
    annotation_reviews: resources.AsyncAnnotationReviewsResource
    annotations: resources.AsyncAnnotationsResource
    comments: resources.AsyncCommentsResource
    current_user: resources.AsyncCurrentUserResource
    ml: resources.AsyncMlResource
    projects: resources.AsyncProjectsResource
    tasks: resources.AsyncTasksResource
    api: resources.AsyncAPIResource
    dataset_storages: resources.AsyncDatasetStoragesResource
    with_raw_response: AsyncLabelStudioWithRawResponse
    with_streaming_response: AsyncLabelStudioWithStreamedResponse

    # client options
    token: str

    def __init__(
        self,
        *,
        token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async label-studio client instance.

        This automatically infers the `token` argument from the `LABEL_STUDIO_TOKEN` environment variable if it is not provided.
        """
        if token is None:
            token = os.environ.get("LABEL_STUDIO_TOKEN")
        if token is None:
            raise LabelStudioError(
                "The token client option must be set either by passing token to the client or by setting the LABEL_STUDIO_TOKEN environment variable"
            )
        self.token = token

        if base_url is None:
            base_url = os.environ.get("LABEL_STUDIO_BASE_URL")
        if base_url is None:
            base_url = f"https://app.heartex.com/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.annotation_history = resources.AsyncAnnotationHistoryResource(self)
        self.annotation_reviews = resources.AsyncAnnotationReviewsResource(self)
        self.annotations = resources.AsyncAnnotationsResource(self)
        self.comments = resources.AsyncCommentsResource(self)
        self.current_user = resources.AsyncCurrentUserResource(self)
        self.ml = resources.AsyncMlResource(self)
        self.projects = resources.AsyncProjectsResource(self)
        self.tasks = resources.AsyncTasksResource(self)
        self.api = resources.AsyncAPIResource(self)
        self.dataset_storages = resources.AsyncDatasetStoragesResource(self)
        self.with_raw_response = AsyncLabelStudioWithRawResponse(self)
        self.with_streaming_response = AsyncLabelStudioWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        token = self.token
        return {"Authorization": token}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            token=token or self.token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LabelStudioWithRawResponse:
    def __init__(self, client: LabelStudio) -> None:
        self.annotation_history = resources.AnnotationHistoryResourceWithRawResponse(client.annotation_history)
        self.annotation_reviews = resources.AnnotationReviewsResourceWithRawResponse(client.annotation_reviews)
        self.annotations = resources.AnnotationsResourceWithRawResponse(client.annotations)
        self.comments = resources.CommentsResourceWithRawResponse(client.comments)
        self.current_user = resources.CurrentUserResourceWithRawResponse(client.current_user)
        self.ml = resources.MlResourceWithRawResponse(client.ml)
        self.projects = resources.ProjectsResourceWithRawResponse(client.projects)
        self.tasks = resources.TasksResourceWithRawResponse(client.tasks)
        self.api = resources.APIResourceWithRawResponse(client.api)
        self.dataset_storages = resources.DatasetStoragesResourceWithRawResponse(client.dataset_storages)


class AsyncLabelStudioWithRawResponse:
    def __init__(self, client: AsyncLabelStudio) -> None:
        self.annotation_history = resources.AsyncAnnotationHistoryResourceWithRawResponse(client.annotation_history)
        self.annotation_reviews = resources.AsyncAnnotationReviewsResourceWithRawResponse(client.annotation_reviews)
        self.annotations = resources.AsyncAnnotationsResourceWithRawResponse(client.annotations)
        self.comments = resources.AsyncCommentsResourceWithRawResponse(client.comments)
        self.current_user = resources.AsyncCurrentUserResourceWithRawResponse(client.current_user)
        self.ml = resources.AsyncMlResourceWithRawResponse(client.ml)
        self.projects = resources.AsyncProjectsResourceWithRawResponse(client.projects)
        self.tasks = resources.AsyncTasksResourceWithRawResponse(client.tasks)
        self.api = resources.AsyncAPIResourceWithRawResponse(client.api)
        self.dataset_storages = resources.AsyncDatasetStoragesResourceWithRawResponse(client.dataset_storages)


class LabelStudioWithStreamedResponse:
    def __init__(self, client: LabelStudio) -> None:
        self.annotation_history = resources.AnnotationHistoryResourceWithStreamingResponse(client.annotation_history)
        self.annotation_reviews = resources.AnnotationReviewsResourceWithStreamingResponse(client.annotation_reviews)
        self.annotations = resources.AnnotationsResourceWithStreamingResponse(client.annotations)
        self.comments = resources.CommentsResourceWithStreamingResponse(client.comments)
        self.current_user = resources.CurrentUserResourceWithStreamingResponse(client.current_user)
        self.ml = resources.MlResourceWithStreamingResponse(client.ml)
        self.projects = resources.ProjectsResourceWithStreamingResponse(client.projects)
        self.tasks = resources.TasksResourceWithStreamingResponse(client.tasks)
        self.api = resources.APIResourceWithStreamingResponse(client.api)
        self.dataset_storages = resources.DatasetStoragesResourceWithStreamingResponse(client.dataset_storages)


class AsyncLabelStudioWithStreamedResponse:
    def __init__(self, client: AsyncLabelStudio) -> None:
        self.annotation_history = resources.AsyncAnnotationHistoryResourceWithStreamingResponse(
            client.annotation_history
        )
        self.annotation_reviews = resources.AsyncAnnotationReviewsResourceWithStreamingResponse(
            client.annotation_reviews
        )
        self.annotations = resources.AsyncAnnotationsResourceWithStreamingResponse(client.annotations)
        self.comments = resources.AsyncCommentsResourceWithStreamingResponse(client.comments)
        self.current_user = resources.AsyncCurrentUserResourceWithStreamingResponse(client.current_user)
        self.ml = resources.AsyncMlResourceWithStreamingResponse(client.ml)
        self.projects = resources.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.tasks = resources.AsyncTasksResourceWithStreamingResponse(client.tasks)
        self.api = resources.AsyncAPIResourceWithStreamingResponse(client.api)
        self.dataset_storages = resources.AsyncDatasetStoragesResourceWithStreamingResponse(client.dataset_storages)


Client = LabelStudio

AsyncClient = AsyncLabelStudio
