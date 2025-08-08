from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.admin = User.objects.create_superuser(username='admin', password='adminpass')
        self.author = Author.objects.create(name='John Doe')
        self.book = Book.objects.create(title='Test Book', author=self.author, publication_year=2022)

        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', args=[self.book.id])
        self.book_create_url = reverse('book-create')
        self.book_delete_url = reverse('book-delete', args=[self.book.id])
        self.book_update_url = reverse('book-update', args=[self.book.id])

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Book.objects.count())

    def test_create_book_unauthenticated(self):
        data = {'title': 'New Book', 'author': self.author.id, 'publication_year': 2023}
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        self.client.login(username='admin', password='adminpass')
        data = {'title': 'New Book', 'author': self.author.id, 'publication_year': 2023}
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Book.objects.filter(title='New Book').exists())

    def test_update_book_authenticated(self):
        self.client.login(username='admin', password='adminpass')
        data = {'title': 'Updated Title', 'author': self.author.id, 'publication_year': 2024}
        response = self.client.put(self.book_update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book_authenticated(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
