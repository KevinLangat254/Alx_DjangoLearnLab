# notifications/serializers.py
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source="actor.username", read_only=True)
    target_repr = serializers.StringRelatedField(source="target")

    class Meta:
        model = Notification
        fields = [
            "id",
            "actor_username",
            "verb",
            "target_repr",
            "timestamp",
            "is_read"
        ]
