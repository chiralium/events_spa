from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Event

class EventSerializer(serializers.ModelSerializer):
    event_date = serializers.CharField()
    event_description = serializers.CharField()
    event_author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)

    class Meta:
        model = Event
        fields = ('id', 'event_date', 'event_time', 'event_type', 'event_description', 'event_author')

    def update(self, instance, validated_data):
        instance.event_type = validated_data.get('event_type', instance.event_type)
        instance.event_date = validated_data.get('event_date', instance.event_date)
        instance.event_time = validated_data.get('event_time', instance.event_time)
        instance.event_description = validated_data.get('event_description', instance.event_description)

        instance.save()
        return instance