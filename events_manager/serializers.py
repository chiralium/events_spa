from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Event

class EventSerializer(serializers.ModelSerializer):
    event_date = serializers.CharField()
    event_description = serializers.CharField()
    event_author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)

    class Meta:
        model = Event
        fields = ('id', 'event_date', 'event_type', 'event_description', 'event_author')