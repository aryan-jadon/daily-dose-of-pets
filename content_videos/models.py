from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class VideoEntry(models.Model):
    video_text = models.CharField(default='', max_length=999)
    video_image = models.URLField(default='', max_length=999)
    video_link = models.URLField(default='', max_length=999)
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=999
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.video_text

    def save(self, *args, **kwargs):
        value = self.video_text
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('video_shared_link', args=[self.slug])
