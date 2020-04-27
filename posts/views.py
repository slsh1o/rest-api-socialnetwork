from datetime import timedelta
from dateutil.parser import parse

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models.functions import TruncDay
from django.db.models import Count

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post, Like
from posts.serializers import PostSerializer, AnalyticsUserSerializer, AnalyticsTotalLikesSerializer
from posts.mixins import RequestTimeAPIMixin


User = get_user_model()


class PostViewSet(RequestTimeAPIMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Make sure currently logged in user will be an author of the post."""
        serializer.save(user=self.request.user)


class PostLikeAPIToggle(RequestTimeAPIMixin, APIView):
    """
    Like toggle endpoint.

    Create like object if user haven't liked post yet
    and vice versa remove it if did
    """
    def get(self, request, post_id, format=None):
        post = get_object_or_404(Post, id=post_id)
        user = self.request.user
        info = 'You are not authenticated!'
        if user and user.is_authenticated:
            if user.id in [post.user.id for post in post.likes.all()]:
                info = f'Unlike post: {post}'
                post.likes.get(user=user).delete()
            else:
                info = f'Like post: {post}'
                post.likes.create(user=user, post=post)
        data = {
            'info': info
        }
        return Response(data)


class AnalyticsUserActivityView(RequestTimeAPIMixin, RetrieveAPIView):
    """Return analytics about user activity like last time login and last request."""
    queryset = User.objects.all()
    serializer_class = AnalyticsUserSerializer


class AnalyticsTotalLikesView(RequestTimeAPIMixin, ListAPIView):
    """
    Count and list all likes to all posts aggregated by day.

    If `date_from` & `date_to` passed days in their range will returned.
    """
    serializer_class = AnalyticsTotalLikesSerializer

    def get_queryset(self):
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        if date_from and date_to:
            # Kinda sht but still I am not sure if it's really matter in context of the task.
            #
            # Because dates will be passed in format '%Y-%m-%d'
            # to include `date to` day `timedelta` used.
            date_from = parse(date_from)
            date_to = parse(date_to)
            date_to += timedelta(days=1)

            queryset = Like.objects\
                .filter(liked_at__range=[date_from, date_to])\
                .annotate(date=TruncDay('liked_at'))\
                .values('date')\
                .annotate(likes_number=Count('id'))
        else:
            queryset = Like.objects.annotate(date=TruncDay('liked_at')).values('date').annotate(likes_number=Count('id'))

        return queryset
