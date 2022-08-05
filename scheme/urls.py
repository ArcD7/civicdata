from django.urls import path
from .views import upload_file_view, index, dataset_home

urlpatterns = [
    path('', index),
    path('upload/', upload_file_view, name='upload-view'),
    path("<str:name>", dataset_home, name='dataset-home'),
]