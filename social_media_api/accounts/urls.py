from django.urls import path
from .views import LoginView, RegistrationView, ProfileView, FollowView, UnfollowView, FollowersListView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', UnfollowView.as_view(), name='unfollow'),
    path('followers/<int:user_id>/', FollowersListView.as_view(), name='followers'),
]