from django.contrib import admin
from events_manager.models import Event

events_manager_models = [Event]
admin.site.register(events_manager_models)