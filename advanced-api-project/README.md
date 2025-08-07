# API View Configuration Documentation

This document describes how each API view in `api/views.py` is configured and intended to operate, including any custom settings or hooks.

## Book API Views

### 1. BookListView
- **Type:** ListAPIView
- **Purpose:** Retrieve a list of all books.
- **Permissions:** Open to all users (`AllowAny`).
- **Filtering:** Supports filtering by `author` and `publication_year` via query parameters (e.g., `/api/books/?author=John&publication_year=2020`).
- **Filter Backend:** Uses `DjangoFilterBackend` for flexible filtering.

### 2. BookCreateView
- **Type:** CreateAPIView
- **Purpose:** Create a new book entry.
- **Permissions:** Only authenticated users can create (`IsAuthenticated`).
- **Custom Hook:** Implements a custom validation in `perform_create` to ensure the `publication_year` is not in the future. If the year is invalid, a validation error is raised.

### 3. BookDetailView
- **Type:** RetrieveAPIView
- **Purpose:** Retrieve details of a single book by its ID.
- **Permissions:** Open to all users (`AllowAny`).

### 4. BookUpdateView
- **Type:** UpdateAPIView
- **Purpose:** Update an existing book entry.
- **Permissions:** Only authenticated users can update (`IsAuthenticated`).

### 5. BookDeleteView
- **Type:** DestroyAPIView
- **Purpose:** Delete a book entry.
- **Permissions:** Only authenticated users can delete (`IsAuthenticated`).

## Custom Permissions

### IsAdminOrReadOnly
- **Purpose:** Allows read-only access for all users, but restricts write operations (create, update, delete) to admin users only.
- **Usage:** This class is defined for potential use but is not currently applied to the views above. It can be used by setting `permission_classes = [IsAdminOrReadOnly]` in any view.

## Summary
- All views use Django REST Framework generic views for standard CRUD operations.
- Permissions are set per view to control access.
- Filtering is enabled for list views using DjangoFilterBackend.
- Custom validation logic is implemented in the create view to enforce business rules.

For further customization or to apply the custom permission, update the `permission_classes` attribute in the relevant view. 

## Filtering, Searching, and Ordering

### Filtering
Filtering is enabled on the `BookListView` using DjangoFilterBackend. You can filter books by `author` and `publication_year` using query parameters.

**Example:**
```
GET /api/books/?author=John&publication_year=2020
```
This returns all books authored by John and published in 2020.

### Searching
Currently, full-text search is not implemented in the provided views. To add search functionality, you can use Django REST Framework's `SearchFilter` and specify `search_fields` in the view.

**Example Implementation (not yet in code):**
```python
from rest_framework.filters import SearchFilter

class BookListView(generics.ListAPIView):
    ...
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'author']
```
**Example Request:**
```
GET /api/books/?search=python
```
This would return books with 'python' in the title or author fields.

### Ordering
Ordering is not currently enabled in the provided views. To add ordering, use Django REST Framework's `OrderingFilter` and specify `ordering_fields`.

**Example Implementation (not yet in code):**
```python
from rest_framework.filters import OrderingFilter

class BookListView(generics.ListAPIView):
    ...
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['title', 'publication_year']
```
**Example Request:**
```
GET /api/books/?ordering=title
GET /api/books/?ordering=-publication_year
```
This would return books ordered by title (ascending) or by publication year (descending).

---

**Note:**
- Filtering by `author` and `publication_year` is available out of the box.
- Searching and ordering are not yet implemented, but code examples above show how to add them if needed. 