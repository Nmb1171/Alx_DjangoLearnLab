from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'blog/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'home'), name = 'logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    #Blog-related URLs
    path('', views.PostListView.as_view(), name='home'),  # List all posts
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # View post details
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Delete a post
]