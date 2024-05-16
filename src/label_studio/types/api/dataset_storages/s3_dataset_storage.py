# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["S3DatasetStorage"]


class S3DatasetStorage(BaseModel):
    dataset: int
    """A unique integer value identifying this dataset."""

    id: Optional[int] = None

    aws_access_key_id: Optional[str] = None
    """AWS_ACCESS_KEY_ID"""

    aws_secret_access_key: Optional[str] = None
    """AWS_SECRET_ACCESS_KEY"""

    aws_session_token: Optional[str] = None
    """AWS_SESSION_TOKEN"""

    aws_sse_kms_key_id: Optional[str] = None
    """AWS SSE KMS Key ID"""

    bucket: Optional[str] = None
    """S3 bucket name"""

    created_at: Optional[datetime] = None
    """Creation time"""

    description: Optional[str] = None
    """Cloud storage description"""

    glob_pattern: Optional[str] = None
    """Glob pattern for syncing from bucket"""

    job_id: Optional[str] = None

    last_sync: Optional[datetime] = None
    """Last sync finished time"""

    last_sync_count: Optional[int] = None
    """Count of tasks synced last time"""

    last_sync_job: Optional[str] = None
    """Last sync job ID"""

    meta: Optional[object] = None
    """Meta and debug information about storage processes"""

    prefix: Optional[str] = None
    """S3 bucket prefix"""

    presign: Optional[bool] = None

    presign_ttl: Optional[int] = None
    """Presigned URLs TTL (in minutes)"""

    recursive_scan: Optional[bool] = None
    """Perform recursive scan over the bucket content"""

    regex_filter: Optional[str] = None
    """Cloud storage regex for filtering objects"""

    region_name: Optional[str] = None
    """AWS Region"""

    s3_endpoint: Optional[str] = None
    """S3 Endpoint"""

    status: Optional[Literal["initialized", "queued", "in_progress", "failed", "completed"]] = None

    synced: Optional[bool] = None
    """Flag if dataset has been previously synced or not"""

    synchronizable: Optional[bool] = None

    title: Optional[str] = None
    """Cloud storage title"""

    traceback: Optional[str] = None
    """Traceback report for the last failed sync"""

    type: Optional[str] = None

    use_blob_urls: Optional[bool] = None
    """Interpret objects as BLOBs and generate URLs"""
