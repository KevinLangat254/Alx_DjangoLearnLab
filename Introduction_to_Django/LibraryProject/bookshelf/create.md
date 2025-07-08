# Create a Book instance with title "1984", author "George Orwell", and publication year 1949

from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()  # Saves the book instance to the database

# Expected Output:
# The book is saved successfully in the database.
# You can verify by running: Book.objects.all()
# <QuerySet [<Book: 1984>]>
