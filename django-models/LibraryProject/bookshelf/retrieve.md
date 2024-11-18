# Retrieve the Book Instance

## Command
```python
book = Book.objects.get(id=new_book.id)
print(book.title, book.author, book.publication_year)

Expected Output
1984 George Orwell 1949