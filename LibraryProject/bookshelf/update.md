# Update the title of the book "1984" to "Nineteen Eighty-Four"

from bookshelf.models import Book

# Retrieve the book by title
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output:
# The book's title is successfully updated.
# You can verify by checking:
# print(Book.objects.get(id=book.id).title)
# Output: Nineteen Eighty-Four
