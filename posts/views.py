from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Make sure currently logged in user will be an author of the post."""
        serializer.save(user=self.request.user)
