# 📚 LibraryProject – Permissions and Groups Setup

This Django application manages books and uses role-based access control to enforce what users can do (view, create, edit, delete). It uses Django's group and permission system along with custom-defined permissions.

---

## ✅ Custom Permissions

Permissions are defined on the `Book` model (in `bookshelf/models.py`) using Django’s `Meta.permissions`:

```python
permissions = [
    ("can_view", "Can view book"),
    ("can_create", "Can create book"),
    ("can_edit", "Can edit book"),
    ("can_delete", "Can delete book"),
]
