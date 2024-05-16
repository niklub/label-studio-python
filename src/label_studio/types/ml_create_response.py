# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MlCreateResponse"]


class MlCreateResponse(BaseModel):
    project: Optional[int] = None
    """Project ID"""

    url: Optional[str] = None
    """ML backend URL"""
