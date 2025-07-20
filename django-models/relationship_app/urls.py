from django.urls import path
from .views import LibraryDetailView, list_books

urlpatterns = [
    path('', list_books, name='home'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('books/', list_books, name='list-books'),
]
