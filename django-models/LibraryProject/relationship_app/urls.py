from django.contrib.auth import views as auth_views
from django.urls import path
from .views import list_books, LibraryDetailView
from .views import admin_view, librarian_view, member_view 
from .views import add_book, edit_book, delete_book
from django.contrib.auth.views import LogoutView, LoginView
from .views import register_view
from . import views

# views.register


urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:pk>/', edit_book, name='edit_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book')
]