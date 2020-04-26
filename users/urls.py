from django.urls import path
from rest_framework_simplejwt.views import token_refresh, token_obtain_pair

from users.views import registration


urlpatterns = [
    path('login/', token_obtain_pair, name='token_obtain_pair'),
    path('refresh/', token_refresh, name='token_refresh'),
    path('register/', registration, name='register'),
]
