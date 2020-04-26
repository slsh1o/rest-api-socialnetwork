from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """
    Custom user model.

    last_jwt_login - save time when user logged in last time via `login/` route
    request_last_time - save time when user made last request to the api routes
    """
    last_jwt_login = models.DateTimeField(blank=True, null=True, default=None)
    request_last_time = models.DateTimeField(blank=True, null=True, default=None)

    def update_last_jwt_login(self):
        self.last_jwt_login = timezone.now()
        self.save(update_fields=['last_jwt_login'])
