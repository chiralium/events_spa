from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view()),
    path('register/', registration_handler),
    path('login/', login_handler),
    path('login/is_auth/', is_logged_in),
    path('login/credentials/', get_user_credentials),
    path('logout/', logout_handler)
]