from relationship_app.models import Author, Book, Library, Librarian

author_name = "Jane Austen"

author = Author.objects.get(name=author_name)

books_by_author = Book.objects.filter(author=author)

print(f"Books by {author_name}: {[book.title for book in books_by_author]}")


library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

librarian = library.librarian
print(f"Librarian for {library_name}: {librarian.name}")