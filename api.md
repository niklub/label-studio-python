# AnnotationHistory

Types:

```python
from label_studio.types import AnnotationHistory, AnnotationHistoryListResponse
```

Methods:

- <code title="get /api/annotation-history/">client.annotation_history.<a href="./src/label_studio/resources/annotation_history.py">list</a>(\*\*<a href="src/label_studio/types/annotation_history_list_params.py">params</a>) -> <a href="./src/label_studio/types/annotation_history_list_response.py">AnnotationHistoryListResponse</a></code>
- <code title="delete /api/annotation-history/">client.annotation_history.<a href="./src/label_studio/resources/annotation_history.py">delete</a>(\*\*<a href="src/label_studio/types/annotation_history_delete_params.py">params</a>) -> None</code>

# AnnotationReviews

Types:

```python
from label_studio.types import AnnotationReview, AnnotationReviewListResponse
```

Methods:

- <code title="post /api/annotation-reviews/">client.annotation_reviews.<a href="./src/label_studio/resources/annotation_reviews.py">create</a>(\*\*<a href="src/label_studio/types/annotation_review_create_params.py">params</a>) -> <a href="./src/label_studio/types/annotation_review.py">AnnotationReview</a></code>
- <code title="get /api/annotation-reviews/{id}/">client.annotation_reviews.<a href="./src/label_studio/resources/annotation_reviews.py">retrieve</a>(id) -> <a href="./src/label_studio/types/annotation_review.py">AnnotationReview</a></code>
- <code title="patch /api/annotation-reviews/{id}/">client.annotation_reviews.<a href="./src/label_studio/resources/annotation_reviews.py">update</a>(id, \*\*<a href="src/label_studio/types/annotation_review_update_params.py">params</a>) -> <a href="./src/label_studio/types/annotation_review.py">AnnotationReview</a></code>
- <code title="get /api/annotation-reviews/">client.annotation_reviews.<a href="./src/label_studio/resources/annotation_reviews.py">list</a>(\*\*<a href="src/label_studio/types/annotation_review_list_params.py">params</a>) -> <a href="./src/label_studio/types/annotation_review_list_response.py">AnnotationReviewListResponse</a></code>
- <code title="delete /api/annotation-reviews/{id}/">client.annotation_reviews.<a href="./src/label_studio/resources/annotation_reviews.py">delete</a>(id) -> None</code>
- <code title="put /api/annotation-reviews/{id}/">client.annotation_reviews.<a href="./src/label_studio/resources/annotation_reviews.py">put</a>(id, \*\*<a href="src/label_studio/types/annotation_review_put_params.py">params</a>) -> <a href="./src/label_studio/types/annotation_review.py">AnnotationReview</a></code>

# Annotations

Types:

```python
from label_studio.types import Annotation
```

Methods:

- <code title="get /api/annotations/{id}/">client.annotations.<a href="./src/label_studio/resources/annotations.py">retrieve</a>(id) -> <a href="./src/label_studio/types/annotation.py">Annotation</a></code>
- <code title="patch /api/annotations/{id}/">client.annotations.<a href="./src/label_studio/resources/annotations.py">update</a>(id, \*\*<a href="src/label_studio/types/annotation_update_params.py">params</a>) -> <a href="./src/label_studio/types/annotation.py">Annotation</a></code>
- <code title="delete /api/annotations/{id}/">client.annotations.<a href="./src/label_studio/resources/annotations.py">delete</a>(id) -> None</code>

# Comments

Types:

```python
from label_studio.types import Comment, CommentListResponse
```

Methods:

- <code title="post /api/comments/">client.comments.<a href="./src/label_studio/resources/comments.py">create</a>(\*\*<a href="src/label_studio/types/comment_create_params.py">params</a>) -> <a href="./src/label_studio/types/comment.py">Comment</a></code>
- <code title="get /api/comments/{id}/">client.comments.<a href="./src/label_studio/resources/comments.py">retrieve</a>(id) -> <a href="./src/label_studio/types/comment.py">Comment</a></code>
- <code title="patch /api/comments/{id}/">client.comments.<a href="./src/label_studio/resources/comments.py">update</a>(id, \*\*<a href="src/label_studio/types/comment_update_params.py">params</a>) -> <a href="./src/label_studio/types/comment.py">Comment</a></code>
- <code title="get /api/comments/">client.comments.<a href="./src/label_studio/resources/comments.py">list</a>(\*\*<a href="src/label_studio/types/comment_list_params.py">params</a>) -> <a href="./src/label_studio/types/comment_list_response.py">CommentListResponse</a></code>
- <code title="delete /api/comments/{id}/">client.comments.<a href="./src/label_studio/resources/comments.py">delete</a>(id) -> None</code>

# CurrentUser

Types:

```python
from label_studio.types import LseUser, CurrentUserResetTokenResponse
```

Methods:

- <code title="post /api/current-user/reset-token/">client.current_user.<a href="./src/label_studio/resources/current_user.py">reset_token</a>() -> <a href="./src/label_studio/types/current_user_reset_token_response.py">CurrentUserResetTokenResponse</a></code>
- <code title="get /api/current-user/token">client.current_user.<a href="./src/label_studio/resources/current_user.py">token</a>() -> None</code>
- <code title="get /api/current-user/whoami">client.current_user.<a href="./src/label_studio/resources/current_user.py">whoami</a>() -> <a href="./src/label_studio/types/lse_user.py">LseUser</a></code>

# Ml

Types:

```python
from label_studio.types import MlCreateResponse, MlUpdateResponse, MlListResponse, MlGetResponse
```

Methods:

- <code title="post /api/ml/">client.ml.<a href="./src/label_studio/resources/ml.py">create</a>(\*\*<a href="src/label_studio/types/ml_create_params.py">params</a>) -> <a href="./src/label_studio/types/ml_create_response.py">MlCreateResponse</a></code>
- <code title="patch /api/ml/{id}">client.ml.<a href="./src/label_studio/resources/ml.py">update</a>(id, \*\*<a href="src/label_studio/types/ml_update_params.py">params</a>) -> <a href="./src/label_studio/types/ml_update_response.py">MlUpdateResponse</a></code>
- <code title="get /api/ml/">client.ml.<a href="./src/label_studio/resources/ml.py">list</a>(\*\*<a href="src/label_studio/types/ml_list_params.py">params</a>) -> <a href="./src/label_studio/types/ml_list_response.py">MlListResponse</a></code>
- <code title="delete /api/ml/{id}">client.ml.<a href="./src/label_studio/resources/ml.py">delete</a>(id) -> None</code>
- <code title="get /api/ml/{id}">client.ml.<a href="./src/label_studio/resources/ml.py">get</a>(id) -> <a href="./src/label_studio/types/ml_get_response.py">MlGetResponse</a></code>

# Projects

Types:

```python
from label_studio.types import (
    ProjectCreateResponse,
    ProjectUpdateResponse,
    ProjectListResponse,
    ProjectGetResponse,
)
```

Methods:

- <code title="post /api/projects/">client.projects.<a href="./src/label_studio/resources/projects.py">create</a>(\*\*<a href="src/label_studio/types/project_create_params.py">params</a>) -> <a href="./src/label_studio/types/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="patch /api/projects/{id}/">client.projects.<a href="./src/label_studio/resources/projects.py">update</a>(id, \*\*<a href="src/label_studio/types/project_update_params.py">params</a>) -> <a href="./src/label_studio/types/project_update_response.py">ProjectUpdateResponse</a></code>
- <code title="get /api/projects/">client.projects.<a href="./src/label_studio/resources/projects.py">list</a>(\*\*<a href="src/label_studio/types/project_list_params.py">params</a>) -> <a href="./src/label_studio/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /api/projects/{id}/">client.projects.<a href="./src/label_studio/resources/projects.py">delete</a>(id) -> None</code>
- <code title="get /api/projects/{id}/">client.projects.<a href="./src/label_studio/resources/projects.py">get</a>(id) -> <a href="./src/label_studio/types/project_get_response.py">ProjectGetResponse</a></code>

# Tasks

Types:

```python
from label_studio.types import (
    TaskCreateResponse,
    TaskUpdateResponse,
    TaskListResponse,
    TaskGetResponse,
)
```

Methods:

- <code title="post /api/tasks/">client.tasks.<a href="./src/label_studio/resources/tasks.py">create</a>(\*\*<a href="src/label_studio/types/task_create_params.py">params</a>) -> <a href="./src/label_studio/types/task_create_response.py">TaskCreateResponse</a></code>
- <code title="patch /api/tasks/{id}/">client.tasks.<a href="./src/label_studio/resources/tasks.py">update</a>(id, \*\*<a href="src/label_studio/types/task_update_params.py">params</a>) -> <a href="./src/label_studio/types/task_update_response.py">TaskUpdateResponse</a></code>
- <code title="get /api/tasks/">client.tasks.<a href="./src/label_studio/resources/tasks.py">list</a>(\*\*<a href="src/label_studio/types/task_list_params.py">params</a>) -> <a href="./src/label_studio/types/task_list_response.py">TaskListResponse</a></code>
- <code title="delete /api/tasks/{id}/">client.tasks.<a href="./src/label_studio/resources/tasks.py">delete</a>(id) -> None</code>
- <code title="get /api/tasks/{id}/">client.tasks.<a href="./src/label_studio/resources/tasks.py">get</a>(id) -> <a href="./src/label_studio/types/task_get_response.py">TaskGetResponse</a></code>

# API

## Dashboards

### Organizations

#### Charts

##### SeriesKey

Methods:

- <code title="get /api/dashboards/organizations/{id}/charts/{chart_key}/{series_key}">client.api.dashboards.organizations.charts.series_key.<a href="./src/label_studio/resources/api/dashboards/organizations/charts/series_key.py">retrieve</a>(series_key, \*, id, chart_key) -> None</code>

## DatasetStorages

Methods:

- <code title="get /api/dataset-storages/">client.api.dataset_storages.<a href="./src/label_studio/resources/api/dataset_storages/dataset_storages.py">list</a>(\*\*<a href="src/label_studio/types/api/dataset_storage_list_params.py">params</a>) -> None</code>

### Azure

Types:

```python
from label_studio.types.api.dataset_storages import AzureDatasetStorage, AzureListResponse
```

Methods:

- <code title="post /api/dataset-storages/azure/">client.api.dataset_storages.azure.<a href="./src/label_studio/resources/api/dataset_storages/azure/azure.py">create</a>(\*\*<a href="src/label_studio/types/api/dataset_storages/azure_create_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/azure_dataset_storage.py">AzureDatasetStorage</a></code>
- <code title="get /api/dataset-storages/azure/{id}/">client.api.dataset_storages.azure.<a href="./src/label_studio/resources/api/dataset_storages/azure/azure.py">retrieve</a>(id) -> <a href="./src/label_studio/types/api/dataset_storages/azure_dataset_storage.py">AzureDatasetStorage</a></code>
- <code title="patch /api/dataset-storages/azure/{id}/">client.api.dataset_storages.azure.<a href="./src/label_studio/resources/api/dataset_storages/azure/azure.py">update</a>(id, \*\*<a href="src/label_studio/types/api/dataset_storages/azure_update_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/azure_dataset_storage.py">AzureDatasetStorage</a></code>
- <code title="get /api/dataset-storages/azure/">client.api.dataset_storages.azure.<a href="./src/label_studio/resources/api/dataset_storages/azure/azure.py">list</a>(\*\*<a href="src/label_studio/types/api/dataset_storages/azure_list_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/azure_list_response.py">AzureListResponse</a></code>
- <code title="delete /api/dataset-storages/azure/{id}/">client.api.dataset_storages.azure.<a href="./src/label_studio/resources/api/dataset_storages/azure/azure.py">delete</a>(id) -> None</code>
- <code title="post /api/dataset-storages/azure/check-for-records/">client.api.dataset_storages.azure.<a href="./src/label_studio/resources/api/dataset_storages/azure/azure.py">check_for_records</a>(\*\*<a href="src/label_studio/types/api/dataset_storages/azure_check_for_records_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/azure_dataset_storage.py">AzureDatasetStorage</a></code>
- <code title="post /api/dataset-storages/azure/validate/">client.api.dataset_storages.azure.<a href="./src/label_studio/resources/api/dataset_storages/azure/azure.py">validate</a>(\*\*<a href="src/label_studio/types/api/dataset_storages/azure_validate_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/azure_dataset_storage.py">AzureDatasetStorage</a></code>

#### Columns

Methods:

- <code title="get /api/dataset-storages/azure/{id}/columns/">client.api.dataset_storages.azure.columns.<a href="./src/label_studio/resources/api/dataset_storages/azure/columns.py">retrieve</a>(id, \*\*<a href="src/label_studio/types/api/dataset_storages/azure/column_retrieve_params.py">params</a>) -> None</code>

### Gcs

Types:

```python
from label_studio.types.api.dataset_storages import GcsDatasetStorage
```

### S3

Types:

```python
from label_studio.types.api.dataset_storages import S3DatasetStorage
```

# DatasetStorages

## Azure

Methods:

- <code title="post /api/dataset-storages/azure/{id}/sync/">client.dataset_storages.azure.<a href="./src/label_studio/resources/dataset_storages/azure.py">sync</a>(id, \*\*<a href="src/label_studio/types/dataset_storages/azure_sync_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/azure_dataset_storage.py">AzureDatasetStorage</a></code>

## Gcs

Types:

```python
from label_studio.types.dataset_storages import GcListResponse
```

Methods:

- <code title="post /api/dataset-storages/gcs/">client.dataset_storages.gcs.<a href="./src/label_studio/resources/dataset_storages/gcs/gcs.py">create</a>(\*\*<a href="src/label_studio/types/dataset_storages/gc_create_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/gcs_dataset_storage.py">GcsDatasetStorage</a></code>
- <code title="get /api/dataset-storages/gcs/{id}/">client.dataset_storages.gcs.<a href="./src/label_studio/resources/dataset_storages/gcs/gcs.py">retrieve</a>(id) -> <a href="./src/label_studio/types/api/dataset_storages/gcs_dataset_storage.py">GcsDatasetStorage</a></code>
- <code title="patch /api/dataset-storages/gcs/{id}/">client.dataset_storages.gcs.<a href="./src/label_studio/resources/dataset_storages/gcs/gcs.py">update</a>(id, \*\*<a href="src/label_studio/types/dataset_storages/gc_update_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/gcs_dataset_storage.py">GcsDatasetStorage</a></code>
- <code title="get /api/dataset-storages/gcs/">client.dataset_storages.gcs.<a href="./src/label_studio/resources/dataset_storages/gcs/gcs.py">list</a>(\*\*<a href="src/label_studio/types/dataset_storages/gc_list_params.py">params</a>) -> <a href="./src/label_studio/types/dataset_storages/gc_list_response.py">GcListResponse</a></code>
- <code title="delete /api/dataset-storages/gcs/{id}/">client.dataset_storages.gcs.<a href="./src/label_studio/resources/dataset_storages/gcs/gcs.py">delete</a>(id) -> None</code>
- <code title="post /api/dataset-storages/gcs/check-for-records/">client.dataset_storages.gcs.<a href="./src/label_studio/resources/dataset_storages/gcs/gcs.py">check_for_records</a>(\*\*<a href="src/label_studio/types/dataset_storages/gc_check_for_records_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/gcs_dataset_storage.py">GcsDatasetStorage</a></code>
- <code title="post /api/dataset-storages/gcs/{id}/sync/">client.dataset_storages.gcs.<a href="./src/label_studio/resources/dataset_storages/gcs/gcs.py">sync</a>(id, \*\*<a href="src/label_studio/types/dataset_storages/gc_sync_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/gcs_dataset_storage.py">GcsDatasetStorage</a></code>
- <code title="post /api/dataset-storages/gcs/validate/">client.dataset_storages.gcs.<a href="./src/label_studio/resources/dataset_storages/gcs/gcs.py">validate</a>(\*\*<a href="src/label_studio/types/dataset_storages/gc_validate_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/gcs_dataset_storage.py">GcsDatasetStorage</a></code>

### Columns

Methods:

- <code title="get /api/dataset-storages/gcs/{id}/columns/">client.dataset_storages.gcs.columns.<a href="./src/label_studio/resources/dataset_storages/gcs/columns.py">list</a>(id, \*\*<a href="src/label_studio/types/dataset_storages/gcs/column_list_params.py">params</a>) -> None</code>

## S3

Types:

```python
from label_studio.types.dataset_storages import S3ListResponse
```

Methods:

- <code title="post /api/dataset-storages/s3/">client.dataset_storages.s3.<a href="./src/label_studio/resources/dataset_storages/s3/s3.py">create</a>(\*\*<a href="src/label_studio/types/dataset_storages/s3_create_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/s3_dataset_storage.py">S3DatasetStorage</a></code>
- <code title="get /api/dataset-storages/s3/{id}/">client.dataset_storages.s3.<a href="./src/label_studio/resources/dataset_storages/s3/s3.py">retrieve</a>(id) -> <a href="./src/label_studio/types/api/dataset_storages/s3_dataset_storage.py">S3DatasetStorage</a></code>
- <code title="patch /api/dataset-storages/s3/{id}/">client.dataset_storages.s3.<a href="./src/label_studio/resources/dataset_storages/s3/s3.py">update</a>(id, \*\*<a href="src/label_studio/types/dataset_storages/s3_update_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/s3_dataset_storage.py">S3DatasetStorage</a></code>
- <code title="get /api/dataset-storages/s3/">client.dataset_storages.s3.<a href="./src/label_studio/resources/dataset_storages/s3/s3.py">list</a>(\*\*<a href="src/label_studio/types/dataset_storages/s3_list_params.py">params</a>) -> <a href="./src/label_studio/types/dataset_storages/s3_list_response.py">S3ListResponse</a></code>
- <code title="delete /api/dataset-storages/s3/{id}/">client.dataset_storages.s3.<a href="./src/label_studio/resources/dataset_storages/s3/s3.py">delete</a>(id) -> None</code>
- <code title="post /api/dataset-storages/s3/check-for-records/">client.dataset_storages.s3.<a href="./src/label_studio/resources/dataset_storages/s3/s3.py">check_for_records</a>(\*\*<a href="src/label_studio/types/dataset_storages/s3_check_for_records_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/s3_dataset_storage.py">S3DatasetStorage</a></code>
- <code title="post /api/dataset-storages/s3/{id}/sync/">client.dataset_storages.s3.<a href="./src/label_studio/resources/dataset_storages/s3/s3.py">sync</a>(id, \*\*<a href="src/label_studio/types/dataset_storages/s3_sync_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/s3_dataset_storage.py">S3DatasetStorage</a></code>
- <code title="post /api/dataset-storages/s3/validate/">client.dataset_storages.s3.<a href="./src/label_studio/resources/dataset_storages/s3/s3.py">validate</a>(\*\*<a href="src/label_studio/types/dataset_storages/s3_validate_params.py">params</a>) -> <a href="./src/label_studio/types/api/dataset_storages/s3_dataset_storage.py">S3DatasetStorage</a></code>

### Columns

Methods:

- <code title="get /api/dataset-storages/s3/{id}/columns/">client.dataset_storages.s3.columns.<a href="./src/label_studio/resources/dataset_storages/s3/columns.py">retrieve</a>(id, \*\*<a href="src/label_studio/types/dataset_storages/s3/column_retrieve_params.py">params</a>) -> None</code>

## Types

Methods:

- <code title="get /api/dataset-storages/types/">client.dataset_storages.types.<a href="./src/label_studio/resources/dataset_storages/types.py">list</a>() -> None</code>
