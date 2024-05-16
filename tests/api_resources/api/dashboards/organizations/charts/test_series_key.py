# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from label_studio import LabelStudio, AsyncLabelStudio

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeriesKey:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LabelStudio) -> None:
        series_key = client.api.dashboards.organizations.charts.series_key.retrieve(
            "string",
            id="string",
            chart_key="string",
        )
        assert series_key is None

    @parametrize
    def test_raw_response_retrieve(self, client: LabelStudio) -> None:
        response = client.api.dashboards.organizations.charts.series_key.with_raw_response.retrieve(
            "string",
            id="string",
            chart_key="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        series_key = response.parse()
        assert series_key is None

    @parametrize
    def test_streaming_response_retrieve(self, client: LabelStudio) -> None:
        with client.api.dashboards.organizations.charts.series_key.with_streaming_response.retrieve(
            "string",
            id="string",
            chart_key="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            series_key = response.parse()
            assert series_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.dashboards.organizations.charts.series_key.with_raw_response.retrieve(
                "string",
                id="",
                chart_key="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chart_key` but received ''"):
            client.api.dashboards.organizations.charts.series_key.with_raw_response.retrieve(
                "string",
                id="string",
                chart_key="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `series_key` but received ''"):
            client.api.dashboards.organizations.charts.series_key.with_raw_response.retrieve(
                "",
                id="string",
                chart_key="string",
            )


class TestAsyncSeriesKey:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLabelStudio) -> None:
        series_key = await async_client.api.dashboards.organizations.charts.series_key.retrieve(
            "string",
            id="string",
            chart_key="string",
        )
        assert series_key is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        response = await async_client.api.dashboards.organizations.charts.series_key.with_raw_response.retrieve(
            "string",
            id="string",
            chart_key="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        series_key = await response.parse()
        assert series_key is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLabelStudio) -> None:
        async with async_client.api.dashboards.organizations.charts.series_key.with_streaming_response.retrieve(
            "string",
            id="string",
            chart_key="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            series_key = await response.parse()
            assert series_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLabelStudio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.dashboards.organizations.charts.series_key.with_raw_response.retrieve(
                "string",
                id="",
                chart_key="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chart_key` but received ''"):
            await async_client.api.dashboards.organizations.charts.series_key.with_raw_response.retrieve(
                "string",
                id="string",
                chart_key="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `series_key` but received ''"):
            await async_client.api.dashboards.organizations.charts.series_key.with_raw_response.retrieve(
                "",
                id="string",
                chart_key="string",
            )
