# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..api.dataset_storages.gcs_dataset_storage import GcsDatasetStorage

__all__ = ["GcListResponse"]

GcListResponse: TypeAlias = List[GcsDatasetStorage]
