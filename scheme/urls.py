from django.urls import path
from .views import upload_file_view, index, dataset_home, dataset_download

urlpatterns = [
    path('', index, name='homepage'),
    path('upload/', upload_file_view, name='upload-view'),
    path("dataset/<str:name>", dataset_home, name='dataset-home'),
    path("download/<str:name>", dataset_download, name='dataset-download')
]