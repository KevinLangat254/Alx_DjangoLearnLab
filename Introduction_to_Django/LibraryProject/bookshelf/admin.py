from django.contrib import admin

# Register your models here.
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list
    search_fields = ('title', 'author')                     # Adds search bar
    list_filter = ('publication_year', 'author')            # Filters in sidebar

admin.site.register(Book, BookAdmin)
