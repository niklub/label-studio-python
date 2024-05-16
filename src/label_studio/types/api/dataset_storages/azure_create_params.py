# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AzureCreateParams"]


class AzureCreateParams(TypedDict, total=False):
    dataset: Required[int]
    """A unique integer value identifying this dataset."""

    account_key: Optional[str]
    """Azure Blob account key"""

    account_name: Optional[str]
    """Azure Blob account name"""

    container: Optional[str]
    """Azure blob container"""

    description: Optional[str]
    """Cloud storage description"""

    glob_pattern: Optional[str]
    """Glob pattern for syncing from bucket"""

    last_sync: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Last sync finished time"""

    last_sync_count: Optional[int]
    """Count of tasks synced last time"""

    last_sync_job: Optional[str]
    """Last sync job ID"""

    meta: Optional[object]
    """Meta and debug information about storage processes"""

    prefix: Optional[str]
    """Azure blob prefix name"""

    presign: bool

    presign_ttl: int
    """Presigned URLs TTL (in minutes)"""

    regex_filter: Optional[str]
    """Cloud storage regex for filtering objects"""

    status: Literal["initialized", "queued", "in_progress", "failed", "completed"]

    synced: bool
    """Flag if dataset has been previously synced or not"""

    synchronizable: bool

    title: Optional[str]
    """Cloud storage title"""

    traceback: Optional[str]
    """Traceback report for the last failed sync"""

    use_blob_urls: bool
    """Interpret objects as BLOBs and generate URLs"""
