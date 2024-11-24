from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import permission_required


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
