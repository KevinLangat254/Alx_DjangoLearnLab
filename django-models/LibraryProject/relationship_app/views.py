from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Library App")

def list_books(request):
    from .models import Book
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

                  

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books related to this library
        context['books'] = self.object.books.all()
        return context



# Register
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # After registration, go to login
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')  # redirect to any page, e.g., book list
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
