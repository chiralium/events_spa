from django.urls import path
from .views import Home, registration_handler

urlpatterns = [
    path('', Home.as_view()),
    path('register/', registration_handler)
]