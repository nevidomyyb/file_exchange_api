from django.urls import path
from .views import FilePostView, FileDownloadView

app_name = 'file_manager'

urlpatterns = [
    path('api/create/file/', FilePostView.as_view(), name='file_post'),
    path('api/file/<str:code>/', FileDownloadView.as_view(), name='file_download')
]