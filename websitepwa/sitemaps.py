from django.contrib.sitemaps import Sitemap
from content_videos.models import VideoEntry


class VideosSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return VideoEntry.objects.all()

    def lastmod(self, obj):
        return obj.updated
