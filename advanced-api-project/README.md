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