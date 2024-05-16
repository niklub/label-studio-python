# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MlListResponse", "MlListResponseItem"]


class MlListResponseItem(BaseModel):
    project: int

    url: str
    """URL for the machine learning model server"""

    id: Optional[int] = None

    auth_method: Optional[Literal["NONE", "BASIC_AUTH"]] = None

    auto_update: Optional[bool] = None
    """
    If false, model version is set by the user, if true - getting latest version
    from backend.
    """

    basic_auth_pass: Optional[str] = None

    basic_auth_pass_is_set: Optional[str] = None

    basic_auth_user: Optional[str] = None
    """HTTP Basic Auth user"""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Description for the machine learning backend"""

    error_message: Optional[str] = None
    """Error message in error state"""

    extra_params: Optional[object] = None
    """Any extra parameters passed to the ML Backend during the setup"""

    is_interactive: Optional[bool] = None
    """Used to interactively annotate tasks.

    If true, model returns one list with results
    """

    api_model_version: Optional[str] = FieldInfo(alias="model_version", default=None)
    """Current model version associated with this machine learning backend"""

    readable_state: Optional[str] = None

    state: Optional[Literal["CO", "DI", "ER", "TR", "PR"]] = None

    timeout: Optional[float] = None
    """Response model timeout"""

    title: Optional[str] = None
    """Name of the machine learning backend"""

    updated_at: Optional[datetime] = None


MlListResponse = List[MlListResponseItem]
