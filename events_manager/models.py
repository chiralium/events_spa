from django.db import models
from django.conf import settings

class Event(models.Model):
    """Model `events`"""
    event_date = models.DateField()
    event_type = models.CharField(max_length=50)
    event_description = models.CharField(max_length=512)
    event_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)