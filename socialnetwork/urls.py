"""URL Configuration for socialnetwork project."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/jwtauth/', include('users.urls')),
]
