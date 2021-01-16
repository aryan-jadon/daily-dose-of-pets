from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from content_videos.models import VideoEntry
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import random


CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)


def index_page(request):
    webpush = {"group": "users"}
    if not cache.get("todays_video_list"):
        video_list = VideoEntry.objects.all()
        cache.set("todays_video_list", video_list)

    current_video_list = list(cache.get("todays_video_list"))
    random.shuffle(current_video_list)
    paginator = Paginator(current_video_list, 12)
    page = request.GET.get('page')

    try:
        page_videos = paginator.page(page)
    except PageNotAnInteger:
        page_videos = paginator.page(1)
    except EmptyPage:
        page_videos = paginator.page(paginator.num_pages)

    context = {
        "webpush": webpush,
        'page': page,
        "page_videos": page_videos
    }

    return render(request, 'website/index.html', context)


def shared_video(request, video):
    webpush = {"group": "users"}
    if cache.get(video):
        page_video = cache.get(video)
    else:
        page_video = get_object_or_404(VideoEntry, slug=video)
        cache.set(video, page_video)

    context = {
        "webpush": webpush,
        'page_video': page_video
    }

    return render(request, "website/shared_video.html", context)


def explore_videos(request):
    return render(request, "website/explore_videos.html")
