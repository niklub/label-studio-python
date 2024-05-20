# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MlUpdateParams"]


class MlUpdateParams(TypedDict, total=False):
    project: Required[int]

    url: Required[str]
    """URL for the machine learning model server"""

    auth_method: Literal["NONE", "BASIC_AUTH"]

    auto_update: bool
    """
    If false, model version is set by the user, if true - getting latest version
    from backend.
    """

    basic_auth_pass: Optional[str]

    basic_auth_user: Optional[str]
    """HTTP Basic Auth user"""

    description: Optional[str]
    """Description for the machine learning backend"""

    error_message: Optional[str]
    """Error message in error state"""

    extra_params: Optional[object]
    """Any extra parameters passed to the ML Backend during the setup"""

    is_interactive: bool
    """Used to interactively annotate tasks.

    If true, model returns one list with results
    """

    model_version: Optional[str]
    """Current model version associated with this machine learning backend"""

    state: Literal["CO", "DI", "ER", "TR", "PR"]

    title: Optional[str]
    """Name of the machine learning backend"""
