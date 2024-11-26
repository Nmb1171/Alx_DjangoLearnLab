from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .forms import CustomUserForm
from .forms import ExampleForm

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request, 'bookshelf/form_success.html', {'name': name})
    else:
        form = ExampleForm()  # Render an empty form for GET requests
    return render(request, 'bookshelf/example_form.html', {'form': form})

def custom_user_form_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('form_success')  # Redirect to a success page
    else:
        form = CustomUserForm()  # Render an empty form for GET requests
    return render(request, 'bookshelf/user_form.html', {'form': form})



@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request):
    pass 

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View to display a list of books/articles.
    Requires the user to have the 'can_view' permission.
    """
    books = Article.objects.all()  # Replace Article with your actual model name
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Create your views here.
