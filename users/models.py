from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    last_jwt_login = models.DateTimeField(blank=True, null=True, default=None)

    def update_last_jwt_login(self):
        self.last_jwt_login = timezone.now()
        self.save(update_fields=['last_jwt_login'])
