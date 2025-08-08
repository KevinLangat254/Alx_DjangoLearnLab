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

## Testing Strategy and Guidelines

### Testing Approach
This project uses Django's built-in testing framework along with Django REST Framework's test utilities to ensure API functionality, data integrity, and security.

### Test Categories

#### 1. Model Tests
- **Purpose:** Validate model field constraints, methods, and data integrity
- **Coverage:** Book model validation, field types, and custom methods
- **Examples:** Publication year validation, required fields, string representations

#### 2. API View Tests
- **Purpose:** Test API endpoints for correct responses, permissions, and data handling
- **Coverage:** All CRUD operations (Create, Read, Update, Delete)
- **Examples:** 
  - List view returns correct data
  - Create view validates input and saves data
  - Update view modifies existing records
  - Delete view removes records
  - Permission checks for authenticated vs unauthenticated users

#### 3. Serializer Tests
- **Purpose:** Validate data serialization/deserialization
- **Coverage:** Field validation, custom validation logic
- **Examples:** Publication year validation, required field validation

#### 4. Permission Tests
- **Purpose:** Ensure proper access control
- **Coverage:** Custom permission classes, role-based access
- **Examples:** Admin-only operations, authenticated user restrictions

### Running Tests

#### Run All Tests
```bash
python manage.py test
```

#### Run Specific Test Module
```bash
python manage.py test api.tests
```

#### Run Specific Test Class
```bash
python manage.py test api.tests.BookModelTestCase
```

#### Run Specific Test Method
```bash
python manage.py test api.tests.BookModelTestCase.test_book_creation
```

#### Run Tests with Verbose Output
```bash
python manage.py test --verbosity=2
```

#### Run Tests with Coverage Report
```bash
# Install coverage if not already installed
pip install coverage

# Run tests with coverage
coverage run --source='.' manage.py test

# Generate coverage report
coverage report

# Generate HTML coverage report
coverage html
```

### Test Structure Guidelines

#### Test Class Naming Convention
- `BookModelTestCase` - for model tests
- `BookAPITestCase` - for API view tests
- `BookSerializerTestCase` - for serializer tests
- `BookPermissionTestCase` - for permission tests

#### Test Method Naming Convention
- `test_<functionality>_<expected_behavior>`
- Examples:
  - `test_book_creation_with_valid_data`
  - `test_book_creation_with_invalid_publication_year`
  - `test_list_view_returns_all_books`
  - `test_create_view_requires_authentication`

### Interpreting Test Results

#### Test Output Interpretation
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.123s

OK
```
- **Dots (.)** indicate passed tests
- **F** indicates failed tests
- **E** indicates errors
- **s** indicates skipped tests
- **x** indicates expected failures

#### Common Test Failure Scenarios
1. **AssertionError:** Expected vs actual values don't match
2. **ValidationError:** Data validation failed
3. **PermissionDenied:** Authentication/authorization issues
4. **Http404:** URL routing problems
5. **DatabaseError:** Model or database issues

### Test Data Management
- Use `setUp()` method to create test data
- Use `tearDown()` method to clean up after tests
- Use factories or fixtures for complex test data
- Avoid hardcoded test data in assertions

### Best Practices
1. **Test Isolation:** Each test should be independent
2. **Descriptive Names:** Test methods should clearly describe what they test
3. **Arrange-Act-Assert:** Structure tests with setup, execution, and verification
4. **Edge Cases:** Test boundary conditions and error scenarios
5. **Performance:** Keep tests fast and efficient
6. **Coverage:** Aim for high test coverage (80%+ recommended)

### Example Test Case Structure
```python
class BookAPITestCase(TestCase):
    def setUp(self):
        """Set up test data before each test method."""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass123'
        )
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': 2020
        }
    
    def test_create_book_authenticated_user(self):
        """Test that authenticated users can create books."""
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/books/create/', self.book_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 1)
    
    def test_create_book_unauthenticated_user(self):
        """Test that unauthenticated users cannot create books."""
        response = self.client.post('/api/books/create/', self.book_data)
        self.assertEqual(response.status_code, 401)
```

### Continuous Integration
- Run tests automatically on code changes
- Include test coverage reports in CI/CD pipeline
- Set minimum coverage thresholds
- Use pre-commit hooks to run tests before commits

---

**Note:** The current test file (`api/tests.py`) contains only a basic template. Implement comprehensive tests following the guidelines above for full test coverage of your API functionality. 