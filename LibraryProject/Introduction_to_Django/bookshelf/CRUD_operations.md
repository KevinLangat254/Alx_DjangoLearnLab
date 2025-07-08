

---

### **Final `CRUD_operations.md` File Structure**
```markdown
# Django Book Model CRUD Operations Documentation

## 1. Create Operation
```python
from bookshelf.models import Book
new_book = Book.objects.create(
    title="1984", 
    author="George Orwell", 
    publication_year=1949
)
print(new_book)  # Verify creation
```
**Output:**
```
1984 by George Orwell (1949)
```

---

## 2. Retrieve Operation
```python
# Get single book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}\nAuthor: {book.author}\nYear: {book.publication_year}")

# Get all books (verify exists)
all_books = Book.objects.all()
print("All books:", list(all_books))
```
**Output:**
```
Title: 1984
Author: George Orwell
Year: 1949
All books: [<Book: 1984 by George Orwell (1949)>]
```

---

## 3. Update Operation
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()  # Persist changes

# Verify update
updated = Book.objects.get(id=book.id)
print("Updated title:", updated.title)
```
**Output:**
```
Updated title: Nineteen Eighty-Four
```

---

## 4. Delete Operation
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
deleted = Book.objects.filter(title="Nineteen Eighty-Four").exists()
print("Book exists after deletion:", deleted)
```
**Output:**
```
Book exists after deletion: False
```

---

## 5. Bulk Operations (Bonus)
```python
# Create multiple books
Book.objects.bulk_create([
    Book(title="Animal Farm", author="George Orwell", publication_year=1945),
    Book(title="Brave New World", author="Aldous Huxley", publication_year=1932),
])

# Count all books
print("Total books:", Book.objects.count())
```
**Output:**
```
Total books: 2
```
```

---

### Key Requirements Met:
1. **Single File Submission**: All operations are documented in `CRUD_operations.md`
2. **Complete Examples**: Each CRUD operation includes:
   - The exact Python command to run in Django shell
   - Expected output with verification steps
3. **Ready for Automated Checking**: Clear formatting with code blocks and outputs
4. **Bonus**: Includes bulk operations as