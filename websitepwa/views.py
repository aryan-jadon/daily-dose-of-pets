from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.templatetags.static import static
from django.urls import reverse


def page_not_found_view(request, exception):
    return render(request, '404.html')


def error_view(request):
    return render(request, '500.html')


def bad_request_view(request, exception):
    return render(request, '400.html')


def offline(request):
    return render(request, 'website/offline.html')


class ServiceWorkerView(TemplateView):
    template_name = 'service_worker.js'
    content_type = 'application/javascript'
    name = 'service_worker.js'

    def get_context_data(self, **kwargs):
        return {
            'icon_url': static('assets/pwa/icons/manifest-icon-512.png'),
            'manifest_url': static('assets/pwa/manifest.json'),
            'home_url': reverse('index'),
            'offline_url': reverse('offline'),
        }
