# Delete the book "Nineteen Eighty-Four" and confirm deletion

from bookshelf.models import Book

# Retrieve the book by title
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
print(Book.objects.all())

# Expected Output:
# <QuerySet []>
# This confirms the book has been deleted (empty result set).
