from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikeView, UnlikeView
from django.urls import path
# <int:pk>/like/", "<int:pk>/unlike/

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls + [
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:post_id>/like/', LikeView.as_view(), name='like'),
    path('posts/<int:post_id>/unlike/', UnlikeView.as_view(), name='unlike'),
]

