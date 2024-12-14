# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
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
from .resources import ml, tasks, comments, projects, annotations, current_user, annotation_history, annotation_reviews
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, LabelStudioError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.api import api
from .resources.dataset_storages import dataset_storages

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "LabelStudio",
    "AsyncLabelStudio",
    "Client",
    "AsyncClient",
]


class LabelStudio(SyncAPIClient):
    annotation_history: annotation_history.AnnotationHistoryResource
    annotation_reviews: annotation_reviews.AnnotationReviewsResource
    annotations: annotations.AnnotationsResource
    comments: comments.CommentsResource
    current_user: current_user.CurrentUserResource
    ml: ml.MlResource
    projects: projects.ProjectsResource
    tasks: tasks.TasksResource
    api: api.APIResource
    dataset_storages: dataset_storages.DatasetStoragesResource
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

        self.annotation_history = annotation_history.AnnotationHistoryResource(self)
        self.annotation_reviews = annotation_reviews.AnnotationReviewsResource(self)
        self.annotations = annotations.AnnotationsResource(self)
        self.comments = comments.CommentsResource(self)
        self.current_user = current_user.CurrentUserResource(self)
        self.ml = ml.MlResource(self)
        self.projects = projects.ProjectsResource(self)
        self.tasks = tasks.TasksResource(self)
        self.api = api.APIResource(self)
        self.dataset_storages = dataset_storages.DatasetStoragesResource(self)
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
    annotation_history: annotation_history.AsyncAnnotationHistoryResource
    annotation_reviews: annotation_reviews.AsyncAnnotationReviewsResource
    annotations: annotations.AsyncAnnotationsResource
    comments: comments.AsyncCommentsResource
    current_user: current_user.AsyncCurrentUserResource
    ml: ml.AsyncMlResource
    projects: projects.AsyncProjectsResource
    tasks: tasks.AsyncTasksResource
    api: api.AsyncAPIResource
    dataset_storages: dataset_storages.AsyncDatasetStoragesResource
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

        self.annotation_history = annotation_history.AsyncAnnotationHistoryResource(self)
        self.annotation_reviews = annotation_reviews.AsyncAnnotationReviewsResource(self)
        self.annotations = annotations.AsyncAnnotationsResource(self)
        self.comments = comments.AsyncCommentsResource(self)
        self.current_user = current_user.AsyncCurrentUserResource(self)
        self.ml = ml.AsyncMlResource(self)
        self.projects = projects.AsyncProjectsResource(self)
        self.tasks = tasks.AsyncTasksResource(self)
        self.api = api.AsyncAPIResource(self)
        self.dataset_storages = dataset_storages.AsyncDatasetStoragesResource(self)
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
        self.annotation_history = annotation_history.AnnotationHistoryResourceWithRawResponse(client.annotation_history)
        self.annotation_reviews = annotation_reviews.AnnotationReviewsResourceWithRawResponse(client.annotation_reviews)
        self.annotations = annotations.AnnotationsResourceWithRawResponse(client.annotations)
        self.comments = comments.CommentsResourceWithRawResponse(client.comments)
        self.current_user = current_user.CurrentUserResourceWithRawResponse(client.current_user)
        self.ml = ml.MlResourceWithRawResponse(client.ml)
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.tasks = tasks.TasksResourceWithRawResponse(client.tasks)
        self.api = api.APIResourceWithRawResponse(client.api)
        self.dataset_storages = dataset_storages.DatasetStoragesResourceWithRawResponse(client.dataset_storages)


class AsyncLabelStudioWithRawResponse:
    def __init__(self, client: AsyncLabelStudio) -> None:
        self.annotation_history = annotation_history.AsyncAnnotationHistoryResourceWithRawResponse(
            client.annotation_history
        )
        self.annotation_reviews = annotation_reviews.AsyncAnnotationReviewsResourceWithRawResponse(
            client.annotation_reviews
        )
        self.annotations = annotations.AsyncAnnotationsResourceWithRawResponse(client.annotations)
        self.comments = comments.AsyncCommentsResourceWithRawResponse(client.comments)
        self.current_user = current_user.AsyncCurrentUserResourceWithRawResponse(client.current_user)
        self.ml = ml.AsyncMlResourceWithRawResponse(client.ml)
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.tasks = tasks.AsyncTasksResourceWithRawResponse(client.tasks)
        self.api = api.AsyncAPIResourceWithRawResponse(client.api)
        self.dataset_storages = dataset_storages.AsyncDatasetStoragesResourceWithRawResponse(client.dataset_storages)


class LabelStudioWithStreamedResponse:
    def __init__(self, client: LabelStudio) -> None:
        self.annotation_history = annotation_history.AnnotationHistoryResourceWithStreamingResponse(
            client.annotation_history
        )
        self.annotation_reviews = annotation_reviews.AnnotationReviewsResourceWithStreamingResponse(
            client.annotation_reviews
        )
        self.annotations = annotations.AnnotationsResourceWithStreamingResponse(client.annotations)
        self.comments = comments.CommentsResourceWithStreamingResponse(client.comments)
        self.current_user = current_user.CurrentUserResourceWithStreamingResponse(client.current_user)
        self.ml = ml.MlResourceWithStreamingResponse(client.ml)
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.tasks = tasks.TasksResourceWithStreamingResponse(client.tasks)
        self.api = api.APIResourceWithStreamingResponse(client.api)
        self.dataset_storages = dataset_storages.DatasetStoragesResourceWithStreamingResponse(client.dataset_storages)


class AsyncLabelStudioWithStreamedResponse:
    def __init__(self, client: AsyncLabelStudio) -> None:
        self.annotation_history = annotation_history.AsyncAnnotationHistoryResourceWithStreamingResponse(
            client.annotation_history
        )
        self.annotation_reviews = annotation_reviews.AsyncAnnotationReviewsResourceWithStreamingResponse(
            client.annotation_reviews
        )
        self.annotations = annotations.AsyncAnnotationsResourceWithStreamingResponse(client.annotations)
        self.comments = comments.AsyncCommentsResourceWithStreamingResponse(client.comments)
        self.current_user = current_user.AsyncCurrentUserResourceWithStreamingResponse(client.current_user)
        self.ml = ml.AsyncMlResourceWithStreamingResponse(client.ml)
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.tasks = tasks.AsyncTasksResourceWithStreamingResponse(client.tasks)
        self.api = api.AsyncAPIResourceWithStreamingResponse(client.api)
        self.dataset_storages = dataset_storages.AsyncDatasetStoragesResourceWithStreamingResponse(
            client.dataset_storages
        )


Client = LabelStudio

AsyncClient = AsyncLabelStudio
