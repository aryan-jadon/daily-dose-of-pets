import json
from django.contrib import admin
from .models import PushInformation
from .utils import _send_notification


class PushInfoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "user", "subscription", "group")
    actions = ("send_message_to_device",)

    def send_message_to_device(self, request, queryset):
        payload = {"head": "Hey",
                   "body": "Hello World"}

        for device in queryset:
            notification = _send_notification(device.subscription, json.dumps(payload), 0)
            if notification:
                self.message_user(request, "message sent successfully")
            else:
                self.message_user(request, "deprecated subscription deleted")


admin.site.register(PushInformation, PushInfoAdmin)
