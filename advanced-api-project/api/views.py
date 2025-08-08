# views.py - API view configurations for Book model
#
# This file defines API views for listing, creating, retrieving, updating, and deleting Book instances.
# Each view is configured with appropriate permissions, filtering, and custom logic where needed.
#
# Custom hooks and settings are documented inline for clarity.
#

from datetime import datetime
from django.forms import ValidationError
from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters import rest_framework 


# Custom permission class to allow read-only access for all users,
# but restrict write operations to admin users only.
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit objects.
    Read-only permissions are allowed for any request.
    """
    def has_permission(self, request, view):
        # Allow read-only for any user, but write only for admin
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
    
class BookListView(generics.ListAPIView):
    """
    API view to retrieve list of books.
    - Open to all users (AllowAny permission).
    - Supports filtering by 'author' and 'publication_year' via query params.
    - Uses DjangoFilterBackend for filtering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # No authentication required
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]      # Enables filtering
    filterset_fields = ['title','author', 'publication_year']  # Fields available for filtering
    search_fields = ['title', 'author']  # Fields available for search
    ordering_fields = ['publication_year', 'title']  # Fields available for ordering

class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    - Requires authentication (IsAuthenticatedOrReadOnly permission).
    - Custom validation: publication_year cannot be in the future.
    - Custom save logic is implemented in perform_create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Authenticated users can create; others read-only

    def perform_create(self, serializer):
        # Custom hook: validate publication_year is not in the future
        if serializer.validated_data['publication_year'] > datetime.now().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single book by ID.
    - Open to all users (AllowAny permission).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    - Requires authentication (IsAuthenticatedOrReadOnly permission).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.
    - Requires authentication (IsAuthenticatedOrReadOnly permission).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]        

class APIRootView(APIView):
    """
    Root API landing page view. Returns a welcome message and basic API info.
    """
    def get(self, request, format=None):
        return Response({
            'message': 'Welcome to the Advanced API Project!',
            'endpoints': {
                'books_list': '/api/books/',
                'book_detail': '/api/books/<id>/',
                'book_create': '/api/books/create/',
                'book_update': '/api/books/update/<id>/',
                'book_delete': '/api/books/delete/<id>/',
            }
        })        