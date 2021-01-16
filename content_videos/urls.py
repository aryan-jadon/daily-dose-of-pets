from django.urls import path
from content_videos.views import index_page, shared_video, explore_videos


urlpatterns = [
    path('', index_page, name="index"),
    path('explore/', explore_videos, name="explore"),
    path('shared/<slug:video>/', shared_video, name="video_shared_link"),
]