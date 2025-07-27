from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    """
    Form for creating and updating Book instances.
    This uses Django’s ModelForm for automatic validation and ORM safety.
    """

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Book Title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author Name'}),
            'publication_year': forms.NumberInput(attrs={'min': 0}),
        }

    def clean_publication_year(self):
        """
        Ensure the publication year is not in the future.
        """
        year = self.cleaned_data['publication_year']
        from datetime import date
        current_year = date.today().year
        if year > current_year:
            raise forms.ValidationError("Publication year cannot be in the future.")
        return year
