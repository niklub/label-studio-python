# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["S3SyncParams"]


class S3SyncParams(TypedDict, total=False):
    dataset: Required[int]
    """A unique integer value identifying this dataset."""

    aws_access_key_id: Optional[str]
    """AWS_ACCESS_KEY_ID"""

    aws_secret_access_key: Optional[str]
    """AWS_SECRET_ACCESS_KEY"""

    aws_session_token: Optional[str]
    """AWS_SESSION_TOKEN"""

    aws_sse_kms_key_id: Optional[str]
    """AWS SSE KMS Key ID"""

    bucket: Optional[str]
    """S3 bucket name"""

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
    """S3 bucket prefix"""

    presign: bool

    presign_ttl: int
    """Presigned URLs TTL (in minutes)"""

    recursive_scan: bool
    """Perform recursive scan over the bucket content"""

    regex_filter: Optional[str]
    """Cloud storage regex for filtering objects"""

    region_name: Optional[str]
    """AWS Region"""

    s3_endpoint: Optional[str]
    """S3 Endpoint"""

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
