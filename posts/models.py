from django.conf import settings
from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'"{self.title}" by {self.user}'

    @property
    def total_likes(self):
        return self.likes.count()


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='liked_posts',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name='likes',
        on_delete=models.CASCADE
    )
    liked_at = models.DateTimeField(default=now())

    def __str__(self):
        return f'{self.user} like {self.post}'
