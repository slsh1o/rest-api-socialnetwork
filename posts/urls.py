from django.urls import path, include
from rest_framework.routers import SimpleRouter

from posts.views import PostViewSet, PostLikeAPIToggle


router = SimpleRouter()
router.register('posts', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/like/', PostLikeAPIToggle.as_view(), name='like_post'),
]
