from django.db import models

from cumulus.storage import SwiftclientStorage

from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.alias import aliases


if not aliases.get('thingthumb'):
    aliases.set('thingthumb', {'size': (150, 80), 'crop': True})


class Thing(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = ThumbnailerImageField(
        upload_to='things', thumbnail_storage=SwiftclientStorage())
