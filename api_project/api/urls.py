from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
    # Include the router URLs
    path('', include(router.urls)),
]