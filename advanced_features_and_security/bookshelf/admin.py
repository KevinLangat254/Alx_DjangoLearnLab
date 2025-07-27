from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list
    search_fields = ('title', 'author')                     # Adds search bar
    list_filter = ('publication_year', 'author')            # Filters in sidebar

admin.site.register(Book, BookAdmin)



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
