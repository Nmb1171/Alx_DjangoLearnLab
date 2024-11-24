from django.shortcuts import render
from django.contrib.auth.decorators import permission_required


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request):
    pass 

# Create your views here.
