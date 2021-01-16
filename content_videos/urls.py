from django.urls import path
from content_videos.views import index_page, shared_video


urlpatterns = [
    path('', index_page, name="index"),
    path('shared/<slug:video>/', shared_video, name="video_shared_link"),
]