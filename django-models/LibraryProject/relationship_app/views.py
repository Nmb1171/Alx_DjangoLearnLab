from django.shortcuts import render
from .models import Book, Library
# Create your views here.

def list_books(request):
    book = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
