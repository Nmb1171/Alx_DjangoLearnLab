# Delete the Book Instance

## Command
```python
from bookshelf.models import Book
book.delete()
print(Book.objects.all())

Expected Output
<QuerySet []>