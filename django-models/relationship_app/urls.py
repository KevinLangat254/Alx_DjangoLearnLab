from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='home'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('books/', views.list_books, name='list-books'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
     path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian-role/', views.librarian_view, name='librarian_view'),
    path('member-role/', views.member_view, name='member_view'),
]
