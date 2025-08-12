# Django Blog Project

A modern, feature-rich blog application built with Django 5.2.4, featuring user authentication, profile management, and a clean, responsive design.

## 🚀 Features

- **User Authentication**: Complete registration and login system
- **Profile Management**: User profiles with bio and avatar uploads
- **Responsive Design**: Modern, mobile-friendly interface
- **File Uploads**: Profile picture upload functionality
- **Message System**: Success/error notifications
- **Security**: CSRF protection, password validation, and secure sessions

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4
- **Database**: MySQL 8.0
- **Frontend**: HTML5, CSS3, JavaScript
- **File Storage**: Local file system (configurable for production)
- **Authentication**: Django's built-in authentication system

## 📋 Prerequisites

Before running this project, ensure you have:

- Python 3.8+ installed
- MySQL 8.0+ installed and running
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd django_blog
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django mysqlclient pillow
   ```

4. **Configure the database**
   - Create a MySQL database named `BlogDB`
   - Update database settings in `django_blog/settings.py` if needed:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'BlogDB',
           'USER': 'root',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`

## 🔐 Authentication System Documentation

### Overview

The authentication system is built using Django's built-in authentication framework, providing secure user registration, login, logout, and profile management functionality.

### Components

#### 1. User Registration (`/register/`)

**Purpose**: Allows new users to create accounts

**Process**:
1. User visits `/register/`
2. Fills out registration form with:
   - Username (required, unique)
   - Email (required, unique)
   - Password (required, with validation)
   - Password confirmation (required)
3. Form validation checks:
   - Username uniqueness
   - Email format and uniqueness
   - Password strength requirements
   - Password confirmation match
4. If valid, creates User and Profile objects
5. Automatically logs in the new user
6. Redirects to home page with success message

**Files Involved**:
- `blog/forms.py`: `RegisterForm` class
- `blog/views.py`: `register` view function
- `templates/register.html`: Registration form template

#### 2. User Login (`/login/`)

**Purpose**: Authenticates existing users

**Process**:
1. User visits `/login/`
2. Enters username and password
3. Django validates credentials against database
4. If valid, creates session and redirects to home
5. If invalid, displays error message

**Files Involved**:
- `blog/urls.py`: Login URL pattern using Django's `LoginView`
- `templates/login.html`: Login form template
- `django_blog/settings.py`: Login redirect configuration

#### 3. User Logout (`/logout/`)

**Purpose**: Securely ends user sessions

**Process**:
1. User clicks logout link
2. Django destroys the session
3. Redirects to login page

**Files Involved**:
- `blog/urls.py`: Logout URL pattern using Django's `LogoutView`
- `django_blog/settings.py`: Logout redirect configuration

#### 4. Profile Management (`/profile/`)

**Purpose**: Allows users to view and edit their profile information

**Process**:
1. User visits `/profile/` (requires authentication)
2. System checks if Profile exists, creates one if needed
3. Displays current profile information
4. User can edit bio and upload avatar
5. Form submission validates and saves changes
6. Shows success message

**Files Involved**:
- `blog/models.py`: `Profile` model and signals
- `blog/forms.py`: `ProfileForm` class
- `blog/views.py`: `profile` view function
- `templates/profile.html`: Profile management template

### Security Features

1. **CSRF Protection**: All forms include CSRF tokens
2. **Password Validation**: Django's built-in password strength requirements
3. **Session Security**: Secure session management
4. **Login Required**: Profile page requires authentication
5. **File Upload Security**: Validated file uploads for avatars

### Database Models

#### User Model (Django Built-in)
- `username`: Unique username
- `email`: User's email address
- `password`: Hashed password
- `date_joined`: Account creation timestamp

#### Profile Model (Custom)
- `user`: One-to-one relationship with User
- `bio`: Text field for user biography (max 500 characters)
- `avatar`: Image field for profile picture
- `created_at`: Profile creation timestamp
- `updated_at`: Last update timestamp

### Signals

The system uses Django signals to automatically create Profile objects when User objects are created:

```python
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

## 🧪 Testing Instructions

### 1. User Registration Testing

**Test Case 1: Successful Registration**
1. Navigate to `http://127.0.0.1:8000/register/`
2. Fill out the form with valid data:
   - Username: `testuser`
   - Email: `test@example.com`
   - Password: `TestPass123!`
   - Password confirmation: `TestPass123!`
3. Click "Register"
4. **Expected Result**: Redirected to home page with success message

**Test Case 2: Registration with Existing Username**
1. Try to register with the same username as above
2. **Expected Result**: Form error indicating username already exists

**Test Case 3: Registration with Weak Password**
1. Try to register with a weak password like `123`
2. **Expected Result**: Form error indicating password requirements not met

**Test Case 4: Registration with Mismatched Passwords**
1. Enter different passwords in password and confirmation fields
2. **Expected Result**: Form error indicating passwords don't match

### 2. User Login Testing

**Test Case 1: Successful Login**
1. Navigate to `http://127.0.0.1:8000/login/`
2. Enter credentials from successful registration
3. Click "Login"
4. **Expected Result**: Redirected to home page, navigation shows "Profile" and "Logout"

**Test Case 2: Failed Login**
1. Try to login with incorrect credentials
2. **Expected Result**: Error message displayed

### 3. User Logout Testing

**Test Case 1: Successful Logout**
1. While logged in, click "Logout" in navigation
2. **Expected Result**: Redirected to login page, navigation shows "Login" and "Register"

### 4. Profile Management Testing

**Test Case 1: View Profile**
1. Login to the system
2. Navigate to `http://127.0.0.1:8000/profile/`
3. **Expected Result**: Profile page displays with user information and edit form

**Test Case 2: Edit Bio**
1. In profile page, enter text in the bio field
2. Click "Save Changes"
3. **Expected Result**: Success message displayed, bio updated

**Test Case 3: Upload Avatar**
1. In profile page, select an image file for avatar
2. Click "Save Changes"
3. **Expected Result**: Avatar uploaded and displayed

**Test Case 4: Access Profile Without Login**
1. Logout from the system
2. Try to access `http://127.0.0.1:8000/profile/`
3. **Expected Result**: Redirected to login page

### 5. Navigation Testing

**Test Case 1: Authenticated User Navigation**
1. Login to the system
2. **Expected Result**: Navigation shows "Home", "Profile", "Logout"

**Test Case 2: Unauthenticated User Navigation**
1. Logout from the system
2. **Expected Result**: Navigation shows "Home", "Login", "Register"

## 📁 Project Structure

```
django_blog/
├── blog/                          # Main application
│   ├── migrations/                # Database migrations
│   ├── __init__.py
│   ├── admin.py                   # Admin interface configuration
│   ├── apps.py                    # App configuration
│   ├── forms.py                   # Form definitions
│   ├── models.py                  # Database models
│   ├── urls.py                    # URL routing
│   └── views.py                   # View functions
├── django_blog/                   # Project settings
│   ├── __init__.py
│   ├── settings.py                # Project configuration
│   ├── urls.py                    # Main URL configuration
│   └── wsgi.py                    # WSGI configuration
├── templates/                     # HTML templates
│   ├── base.html                  # Base template
│   ├── home.html                  # Home page
│   ├── login.html                 # Login page
│   ├── profile.html               # Profile page
│   └── register.html              # Registration page
├── static/                        # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── media/                         # User uploaded files
│   └── avatars/                   # Profile pictures
├── manage.py                      # Django management script
└── README.md                      # This file
```

## 🔧 Configuration

### Environment Variables

For production deployment, consider setting these environment variables:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: List of allowed hostnames
- `DATABASE_URL`: Database connection string

### Production Deployment

1. Set `DEBUG = False` in settings
2. Configure a production database
3. Set up static file serving
4. Configure media file storage (e.g., AWS S3)
5. Set up HTTPS
6. Configure proper logging

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure MySQL is running
   - Check database credentials in settings.py
   - Verify database exists

2. **Migration Errors**
   - Run `python manage.py makemigrations`
   - Run `python manage.py migrate`

3. **Static Files Not Loading**
   - Run `python manage.py collectstatic`
   - Check STATIC_URL and STATICFILES_DIRS settings

4. **Media Files Not Uploading**
   - Ensure media directory exists
   - Check MEDIA_URL and MEDIA_ROOT settings
   - Verify file permissions

### Getting Help

If you encounter issues not covered in this documentation:

1. Check the Django documentation
2. Review the error logs
3. Create an issue in the project repository

---

**Happy Blogging! 🎉** 

## 📝 Blog Posts Feature Documentation

### Overview
The blog module lets authenticated users create, view, edit, and delete posts. Public users can browse and read posts. Author-only permissions are enforced for editing and deleting posts.

### Data Model
- **Post**
  - `title` (CharField, 200)
  - `content` (TextField)
  - `published_date` (DateTime, auto_now_add)
  - `author` (ForeignKey to `User`)

- **Comment**
  - `post` (ForeignKey to `Post`, related_name='comments')
  - `author` (ForeignKey to `User`)
  - `content` (TextField)
  - `created_at` (DateTime, auto_now_add)
  - `updated_at` (DateTime, auto_now)

Posts are ordered by `published_date` (newest first). After creating or editing a post, users are redirected to the post detail page via `get_absolute_url`.

### URLs
- `GET /posts/` → List all posts
- `GET /posts/new/` → Create form (login required)
- `POST /posts/new/` → Create post (login required)
- `GET /posts/<id>/` → Post detail
- `GET /posts/<id>/edit/` → Edit form (author only)
- `POST /posts/<id>/edit/` → Update post (author only)
- `GET /posts/<id>/delete/` → Delete confirmation (author only)
- `POST /posts/<id>/delete/` → Delete post (author only)

**Comment URLs:**
- `GET /posts/<post_id>/comments/new/` → Create comment form (login required)
- `POST /posts/<post_id>/comments/new/` → Create comment (login required)
- `GET /comments/<id>/edit/` → Edit comment form (author only)
- `POST /comments/<id>/edit/` → Update comment (author only)
- `GET /comments/<id>/delete/` → Delete comment confirmation (author only)
- `POST /comments/<id>/delete/` → Delete comment (author only)

### Permissions & Security
- **Create**: Login required.
- **Edit/Delete**: Only the post author can edit or delete (enforced with `LoginRequiredMixin` and `UserPassesTestMixin`).
- **Comments**: Login required to create; only comment author can edit/delete.
- **CSRF**: All forms include CSRF tokens.
- **Passwords/Sessions**: Handled by Django's built-in authentication.
- **Output escaping**: Post content is rendered with Django's default auto-escaping (no raw HTML rendered by default).

### Forms & Validation
- `PostForm`: fields `title`, `content`.
- `CommentForm`: field `content` with validation for non-empty content.
- Server-side validation via Django forms; client-side enhancements provided by `static/js/script.js` for general form UX.

### Views
- `PostListView` (list)
- `PostDetailView` (detail, handles comment submission)
- `PostCreateView` (create, login required)
- `PostUpdateView` (update, login required, author check)
- `PostDeleteView` (delete, login required, author check)
- `CommentCreateView` (create comment, login required)
- `CommentUpdateView` (update comment, login required, author check)
- `CommentDeleteView` (delete comment, login required, author check)

### Templates (styled with existing CSS)
- `templates/blog/post_list.html`
- `templates/blog/post_detail.html` (includes comments section)
- `templates/blog/post_form.html`
- `templates/blog/post_confirm_delete.html`
- `templates/blog/comment_form.html`
- `templates/blog/comment_confirm_delete.html`

All templates extend `base.html` and use the existing classes: `.form-container`, `.form-group`, `.submit-btn`, `.home-container`, `.feature-grid`, `.feature-card`, etc.

### Admin
- `Post`, `Profile`, and `Comment` are registered in the Django admin. Admins can manage posts, profiles, and comments via `/admin/`.

### How to Use
1. Navigate to `http://127.0.0.1:8000/posts/` to view posts.
2. Login and click "New Post" to create one.
3. On a post detail page, authors can "Edit" or "Delete" their own posts.
4. **Comments**: Login users can add comments on any post. Comment authors can edit/delete their own comments.
5. Use the navigation to move between list, detail, create, and edit screens.

### Testing Blog Posts
- **Create Post (Authenticated)**
  1. Login → go to `/posts/new/` → enter title and content → Save.
  2. Expected: Redirect to detail page; new post appears in `/posts/` at the top.
- **Edit Post (Author Only)**
  1. As the author, visit `/posts/<id>/edit/` → change fields → Save.
  2. Expected: Redirect to detail page with updated content.
- **Delete Post (Author Only)**
  1. As the author, visit `/posts/<id>/delete/` → confirm delete.
  2. Expected: Redirect to `/posts/`; post removed.
- **Permission Check (Not Author)**
  1. Login as a different user → try `/posts/<id>/edit/` or `/posts/<id>/delete/`.
  2. Expected: Access denied (author check fails).
- **Public Access**
  - `/posts/` and `/posts/<id>/` are accessible without login.

### Testing Comments
- **Add Comment (Authenticated)**
  1. Login → visit any post detail page → fill comment form → Submit.
  2. Expected: Comment appears in comments list; form resets.
- **Edit Comment (Author Only)**
  1. As comment author, click "Edit" → modify content → Save.
  2. Expected: Comment updated; redirect to post detail.
- **Delete Comment (Author Only)**
  1. As comment author, click "Delete" → confirm deletion.
  2. Expected: Comment removed; redirect to post detail.
- **Comment Permissions**
  1. Try to edit/delete another user's comment.
  2. Expected: Access denied (author check fails). 