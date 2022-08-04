from django.urls import path
from .views import upload_file_view, index

urlpatterns = [
    path('', index),
    path('upload/', upload_file_view, name='upload-view'),
]