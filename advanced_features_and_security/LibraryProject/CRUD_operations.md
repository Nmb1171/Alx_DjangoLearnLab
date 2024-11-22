# CRUD Operations for the Book Model

## 1. Create a Book Instance

### Command
```python
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(new_book)

Expected Output
1984 by George Orwell

book = Book.objects.get(id=new_book.id)
print(book.title, book.author, book.publication_year)

Expected Output
1984 George Orwell 1949

book.title = "Nineteen Eighty-Four"
book.save()  # Save the changes
print(book.title)

Expected Output
Nineteen Eighty-Four

book.delete()  # Delete the book instance
print(Book.objects.all())

Expected Output
<QuerySet []>