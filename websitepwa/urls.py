from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
import websitepwa.views as pwa_views
from websitepwa.sitemaps import VideosSitemap
from django.contrib.sitemaps.views import sitemap
import websitepwa

sitemaps = {
    "videos": VideosSitemap,
}

handler404 = 'websitepwa.views.page_not_found_view'
handler500 = 'websitepwa.views.error_view'
handler400 = 'websitepwa.views.bad_request_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webpush/', include('webpush.urls')),
    path('offline/', pwa_views.offline, name='offline'),
    path('service_worker.js',
         pwa_views.ServiceWorkerView.as_view(),
         name=pwa_views.ServiceWorkerView.name,
         ),
    path('', include('content_videos.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
