from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Thing(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="things")
    thumb = ImageSpecField(source="image", processors=[ResizeToFill(50, 50)], options={"quality": 100})
