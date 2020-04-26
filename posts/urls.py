from django.urls import path, include
from rest_framework.routers import SimpleRouter

from posts.views import PostViewSet, PostLikeAPIToggle, AnalyticsUserActivityView, AnalyticsTotalLikesView


router = SimpleRouter()
router.register('posts', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/like/', PostLikeAPIToggle.as_view(), name='like_post'),
    path('analytics/user/<int:pk>/', AnalyticsUserActivityView.as_view(), name='user_activity'),
    path('analytics/likes/', AnalyticsTotalLikesView.as_view(), name='total_likes'),
]
