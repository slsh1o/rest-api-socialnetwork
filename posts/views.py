from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from posts.models import Post
from posts.serializers import PostSerializer


User = get_user_model()


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Make sure currently logged in user will be an author of the post."""
        serializer.save(user=self.request.user)


class PostLikeAPIToggle(APIView):
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
