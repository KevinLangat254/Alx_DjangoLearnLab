from datetime import date
from rest_framework import serializers
from .models import Book, Author

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    # Custom validation to ensure the publication year is not in the future
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        # Automatically include all fields from the Book model
        fields = '__all__'


# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer: includes all books written by this author.
    # 'many=True' since one author can have multiple books.
    # 'read_only=True' because books are not created/updated from within the AuthorSerializer.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        # Include only the author's name and the list of their books
        fields = ['name', 'books']
