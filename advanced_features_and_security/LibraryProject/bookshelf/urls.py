from django.urls import path
from . import views 
from django.shortcuts import render

urlpatterns = [
    path('user-form/', views.custom_user_form_view, name='user_form'),
    path('form-success/', lambda request: render(request, 'bookshelf/success.html'), name='form_success'),  # Simple success page
]
