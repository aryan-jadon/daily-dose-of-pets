from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from content_videos.models import VideoEntry
import random


def index_page(request):
    webpush = {"group": "users"}
    video_list = VideoEntry.objects.all()
    paginator = Paginator(video_list, 3)
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
    page_video = get_object_or_404(VideoEntry, slug=video)
    context = {
        "webpush": webpush,
        'page_video': page_video
    }

    return render(request, "website/shared_video.html", context)


def explore_videos(request):
    return render(request, "website/explore_videos.html")
