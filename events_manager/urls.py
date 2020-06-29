from django.urls import path
from .views import Home, Register

urlpatterns = [
    path('', Home.as_view()),
    path('register/', Register.as_view())
]