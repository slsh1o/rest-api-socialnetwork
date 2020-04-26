from django.urls import path, include
from rest_framework.routers import SimpleRouter

from posts.views import PostViewSet


router = SimpleRouter()
router.register('posts', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
