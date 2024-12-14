# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .charts.charts import (
    ChartsResource,
    AsyncChartsResource,
    ChartsResourceWithRawResponse,
    AsyncChartsResourceWithRawResponse,
    ChartsResourceWithStreamingResponse,
    AsyncChartsResourceWithStreamingResponse,
)

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def charts(self) -> ChartsResource:
        return ChartsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/niklub/label-studio-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/niklub/label-studio-python#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def charts(self) -> AsyncChartsResource:
        return AsyncChartsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/niklub/label-studio-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/niklub/label-studio-python#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

    @cached_property
    def charts(self) -> ChartsResourceWithRawResponse:
        return ChartsResourceWithRawResponse(self._organizations.charts)


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

    @cached_property
    def charts(self) -> AsyncChartsResourceWithRawResponse:
        return AsyncChartsResourceWithRawResponse(self._organizations.charts)


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

    @cached_property
    def charts(self) -> ChartsResourceWithStreamingResponse:
        return ChartsResourceWithStreamingResponse(self._organizations.charts)


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

    @cached_property
    def charts(self) -> AsyncChartsResourceWithStreamingResponse:
        return AsyncChartsResourceWithStreamingResponse(self._organizations.charts)
