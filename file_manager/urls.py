from django.urls import path
from .views import FilePostView

app_name = 'file_manager'

urlpatterns = [
    path('api/create/file/', FilePostView.as_view(), name='file_post')
]