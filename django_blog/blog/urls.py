# urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from blog import views



urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Post URLs
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs (more RESTful structure)
    path("post/<int:pk>/comments/new/", views.CommentCreateView.as_view(), name='comment-create'),
    path("comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name='comment-update'),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name='comment-delete'),

    path('', views.home, name='home'),
]
