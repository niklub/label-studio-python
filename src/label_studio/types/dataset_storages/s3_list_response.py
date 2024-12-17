# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..api.dataset_storages.s3_dataset_storage import S3DatasetStorage

__all__ = ["S3ListResponse"]

S3ListResponse: TypeAlias = List[S3DatasetStorage]
