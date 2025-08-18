from rest_framework import serializers
from .models import Post, Comment
from accounts.serializers import UserSerializer  # import your custom user serializer


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # nested user details

    class Meta:
        model = Post
        fields = ["id", "author", "title", "content", "created_at", "updated_at"]


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # nested user details
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())  # only post ID

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "content", "created_at", "updated_at"]
