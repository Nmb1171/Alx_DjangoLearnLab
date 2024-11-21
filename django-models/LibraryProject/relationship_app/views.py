from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from .models import Book
from .models import Library
from .forms import BookForm
# Create your views here.


@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})


@permission_required ('relationship-app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            login(request, user)  # Log in the user after registration
            return redirect('list_books')  # Redirect to a post-login page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def is_admin(user):
    return user.is_authenticated and user.profile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.profile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.profile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')




def list_books(request):
    books = Book.objects.all()
    #return render(request, 'relationship_app/list_books.html', {'books': books})
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = '/library_detail.html'
    context_object_name = 'library'
    #template_name = 'relationship_app/library_detail.html'
   
    
