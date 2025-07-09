# Retrieve a specific book instance using Django ORM

# Python command:
book = Book.objects.get(title="1984")

# Expected output:
# <Book: 1984>

print(book)

# Expected Output:
# <QuerySet [<Book: 1984>, <Book: Another Book>, ...]>
# This shows a list of all books stored in the database.
