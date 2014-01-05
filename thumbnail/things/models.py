from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="things")
