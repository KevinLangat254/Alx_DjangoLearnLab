from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# ----- Custom Permission -----
class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author
        return obj.author == request.user


# ----- POST VIEWSET -----
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    # Add filtering + searching + ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["author"]   # allow ?author=1
    search_fields = ["title", "content"]  # allow ?search=hello
    ordering_fields = ["created_at", "updated_at"]  # allow ?ordering=created_at

    def perform_create(self, serializer):
        # Automatically set the logged-in user as the author
        serializer.save(author=self.request.user)


# ----- COMMENT VIEWSET -----
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["post", "author"]  # allow ?post=1
    ordering_fields = ["created_at"]

    def perform_create(self, serializer):
        # Automatically set the logged-in user as the author
        serializer.save(author=self.request.user)

class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset for the user's feed, showing posts from followed users.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied("You must be logged in to view the feed.")
        # Get posts from users this user is following
        following = user.following.all()
        return Post.objects.filter(author__in=following).order_by("-created_at")
    