# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["GcsDatasetStorage"]


class GcsDatasetStorage(BaseModel):
    dataset: int
    """A unique integer value identifying this dataset."""

    id: Optional[int] = None

    bucket: Optional[str] = None
    """GCS bucket name"""

    created_at: Optional[datetime] = None
    """Creation time"""

    description: Optional[str] = None
    """Cloud storage description"""

    glob_pattern: Optional[str] = None
    """Glob pattern for syncing from bucket"""

    google_application_credentials: Optional[str] = None
    """The content of GOOGLE_APPLICATION_CREDENTIALS json file"""

    google_project_id: Optional[str] = None
    """Google project ID"""

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
    """GCS bucket prefix"""

    presign: Optional[bool] = None

    presign_ttl: Optional[int] = None
    """Presigned URLs TTL (in minutes)"""

    regex_filter: Optional[str] = None
    """Cloud storage regex for filtering objects"""

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
