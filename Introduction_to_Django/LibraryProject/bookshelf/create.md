# Create a Book instance with title "1984", author "George Orwell", and publication year 1949

from bookshelf.models import Book


# Python command:
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected output (example):
# <Book: 1984>

