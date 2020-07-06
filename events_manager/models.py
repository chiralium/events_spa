from django.db import models
from django.conf import settings
from datetime import datetime

class Event(models.Model):
    """Model `events`"""
    event_date = models.DateField()
    event_time = models.CharField(max_length=8, default="00:00")
    event_type = models.CharField(max_length=50)
    event_description = models.CharField(max_length=512)
    event_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_reminder_date = models.DateTimeField(default=datetime.now(), blank=True)