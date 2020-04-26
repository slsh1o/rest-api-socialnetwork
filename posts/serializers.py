from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'content', 'total_likes')
        extra_kwargs = {'user': {'read_only': True}}


class AnalyticsUserSerializer(serializers.ModelSerializer):
    """Serialize data about user activity."""
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'last_jwt_login', 'request_last_time')


class AnalyticsTotalLikesSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    likes_number = serializers.IntegerField()
