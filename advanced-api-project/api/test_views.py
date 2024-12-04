from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author
from rest_framework.test import APIClient
from django.contrib.auth.models import User



class BookListViewTest(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(title="Fantastic Beasts", publication_year=2001, author=self.author)

    def test_list_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if "Harry Potter" exists in the response data
        self.assertTrue(any(book['title'] == "Harry Potter" for book in response.data))


class BookDetailViewTest(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)

    def test_retrieve_book(self):
        # Send a GET request to the detail endpoint
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the response contains the correct book data
        self.assertEqual(response.data['title'], "Harry Potter")
        self.assertEqual(response.data['author'], self.author.id)


class BookCreateViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)  # Authenticate user
        self.author = Author.objects.create(name="J.K. Rowling")

    def test_create_book(self):
        # Data for the new book
        data = {
            "title": "Harry Potter",
            "publication_year": 1997,
            "author": self.author.id
        }

        # Send a POST request to create a new book
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the book was created
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, "Harry Potter")


class BookUpdateViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)

    def test_update_book(self):
        # Data to update the book
        data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 1998,
            "author": self.author.id
        }

        # Send a PUT request to update the book
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the book was updated
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter and the Chamber of Secrets")


class BookDeleteViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login()
        self.client.force_authenticate(user=self.user)  # Authenticate user
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)

    def test_delete_book(self):
        # Send a DELETE request to delete the book
        response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify the book was deleted
        self.assertEqual(Book.objects.count(), 0)


class BookFilterSearchOrderTest(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(title="Fantastic Beasts", publication_year=2001, author=self.author)

    def test_filter_books_by_title(self):
        response = self.client.get('/api/books/?title=Harry Potter')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    def test_search_books(self):
        response = self.client.get('/api/books/?search=Rowling')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_year(self):
        response = self.client.get('/api/books/?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2001)

