from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.
def home(request):
    return render(request, 'blog/base.html')

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'


class CustomLogoutView(LogoutView):
    next_page = 'home'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "blog/register.html", {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        if username and email:
            request.user.username = username
            request.user.email = email
            request.user.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid data. Please try again.')

    return render(request, 'blog/profile.html')

