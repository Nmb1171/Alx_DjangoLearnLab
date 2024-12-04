from django.urls import path
from .views import *


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'), # List View
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), # Detail View
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create view
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),  # Update view
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),  # Delete view
]

