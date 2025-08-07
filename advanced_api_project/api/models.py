from django.db import models

# Author model represents a writer who can have multiple books.
class Author(models.Model):
    # The name of the author (e.g., "Chinua Achebe")
    name = models.CharField(max_length=100)

    def __str__(self):
        # String representation of the author instance
        return self.name  # Fixed: should return name, not title


# Book model represents a single book written by an author.
class Book(models.Model):
    # Title of the book (e.g., "Things Fall Apart")
    title = models.CharField(max_length=200)

    # Year the book was published
    publication_year = models.IntegerField()

    # ForeignKey creates a one-to-many relationship:
    # Each Book is linked to a single Author, but an Author can have many Books.
    author = models.ForeignKey(
        Author,
        related_name='books',  # Allows reverse access: author.books.all()
        on_delete=models.CASCADE  # If the author is deleted, all their books are also deleted
    )

    def __str__(self):
        # String representation of the book instance
        return self.title
