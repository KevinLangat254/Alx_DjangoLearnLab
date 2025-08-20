from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action    
from rest_framework.exceptions import PermissionDenied
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import get_object_or_404
from accounts.models import CustomUser
from accounts.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from notifications.models import Notification
from .models import Like
from rest_framework import status

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
    
    @staticmethod
    def create_comment_notification(user, comment):
        # Don’t notify if the author comments on their own post
        if comment.post.author == user:
            return

        Notification.objects.create(
            recipient=comment.post.author,   # post owner
            actor=user,                      # the commenter
            verb="commented on your post",
            target=comment                   # GenericForeignKey handles this
        )

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        self.create_comment_notification(self.request.user, comment)

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
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by("-created_at")

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            # create notification for the post owner
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb="liked your post",
                    target=post
                )
            return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "You already liked this post."}, status=status.HTTP_200_OK)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def delete(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)