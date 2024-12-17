# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .azure_dataset_storage import AzureDatasetStorage

__all__ = ["AzureListResponse"]

AzureListResponse: TypeAlias = List[AzureDatasetStorage]
