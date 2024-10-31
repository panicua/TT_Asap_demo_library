from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from books_app.models import Book

User = get_user_model()


class BaseBookAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = reverse('books_app:book-list')
        self.detail_url = lambda id_: reverse('books_app:book-detail', args=[id_])

    def _create_book(self, data):
        return Book.objects.create(**data)

    def _assert_response_status(self, response, status_code):
        self.assertEqual(response.status_code, status_code)


class AdminUserBookAPITests(BaseBookAPITests):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create_superuser(
            username='admin@test.com',
            password='adminpassword'
        )
        token = self.client.post(reverse('token_obtain_pair'), data={
            'username': self.user.username,
            'password': 'adminpassword'
        }).data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_create_book(self):
        """Test that admin users can create books."""
        data = {
            'title': 'The Master and Margarita',
            'author': 'Mikhail Bulgakov',
            'isbn': '9780679760801',
            'language': 'Russian'
        }
        self.client.post(self.list_url, data)

    def test_list_books(self):
        """Test that admin users can retrieve a list of books."""
        response = self.client.get(self.list_url)
        self._assert_response_status(response, status.HTTP_200_OK)

    def test_retrieve_book(self):
        """Test that admin users can retrieve a book."""
        data = {
            'title': 'The Master and Margarita',
            'author': 'Mikhail Bulgakov',
            'isbn': '9780679760801',
            'language': 'Russian'
        }
        book = self._create_book(data)
        response = self.client.get(self.detail_url(book.id))
        self._assert_response_status(response, status.HTTP_200_OK)

    def test_update_book(self):
        """Test that admin users can update a book."""
        data = {
            'title': 'The Master and Margarita',
            'author': 'Mikhail Bulgakov',
            'isbn': '9780679760801',
            'language': 'Russian'
        }
        book = self._create_book(data)
        new_title = 'The Master and Margarita (Updated)'
        updated_data = {**data, 'title': new_title}
        self.client.put(self.detail_url(book.id), updated_data)

    def test_delete_book(self):
        """Test that admin users can delete a book."""
        data = {
            'title': 'The Master and Margarita',
            'author': 'Mikhail Bulgakov',
            'isbn': '9780679760801',
            'language': 'Russian'
        }
        book = self._create_book(data)
        self.client.delete(self.detail_url(book.id))


class DefaultUserBookAPITests(BaseBookAPITests):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user(
            username='user@test.com',
            password='userpassword'
        )
        response = self.client.post(reverse('token_obtain_pair'), data={
            'username': self.user.username,
            'password': 'userpassword'
        })
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_create_book(self):
        """Test that default users cannot create books."""
        response = self.client.post(self.list_url, {'title': 'The Master and Margarita'})
        self._assert_response_status(response, status.HTTP_403_FORBIDDEN)

    def test_list_books(self):
        """Test that default users can retrieve a list of books."""
        response = self.client.get(self.list_url)
        self._assert_response_status(response, status.HTTP_200_OK)

    def test_retrieve_book(self):
        """Test that default users can retrieve a book."""
        data = {
            'title': 'The Master and Margarita',
            'author': 'Mikhail Bulgakov',
            'isbn': '9780679760801',
            'language': 'Russian'
        }
        book = self._create_book(data)
        response = self.client.get(self.detail_url(book.id))
        self._assert_response_status(response, status.HTTP_200_OK)

    def test_update_book(self):
        """Test that default users cannot update a book."""
        data = {
            'title': 'The Master and Margarita',
            'author': 'Mikhail Bulgakov',
            'isbn': '9780679760801',
            'language': 'Russian'
        }
        book = self._create_book(data)
        new_title = 'The Master and Margarita (Updated)'
        updated_data = {**data, 'title': new_title}
        response = self.client.put(self.detail_url(book.id), updated_data)
        self._assert_response_status(response, status.HTTP_403_FORBIDDEN)

    def test_delete_book(self):
        """Test that default users cannot delete a book."""
        data = {
            'title': 'The Master and Margarita',
            'author': 'Mikhail Bulgakov',
            'isbn': '9780679760801',
            'language': 'Russian'
        }
        book = self._create_book(data)
        response = self.client.delete(self.detail_url(book.id))
        self._assert_response_status(response, status.HTTP_403_FORBIDDEN)
