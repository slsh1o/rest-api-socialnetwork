from django.urls import path
from rest_framework_simplejwt.views import token_refresh

from users.views import registration, AuthTokenObtainPairView


urlpatterns = [
    path('login/', AuthTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', token_refresh, name='token_refresh'),
    path('register/', registration, name='register'),
]
