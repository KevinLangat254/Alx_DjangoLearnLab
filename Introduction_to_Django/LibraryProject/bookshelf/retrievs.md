# Retrieve all Book instances from the database

from bookshelf.models import Book

# Get all books
books = Book.objects.all()

# Display the result
print(books)

# Expected Output:
# <QuerySet [<Book: 1984>, <Book: Another Book>, ...]>
# This shows a list of all books stored in the database.
