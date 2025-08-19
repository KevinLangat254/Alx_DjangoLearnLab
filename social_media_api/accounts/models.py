from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # followers = models.ManyToManyField(
    #     "self",
    #     symmetrical=False,
    #     related_name="following",
    #     blank=True
    # )
    following = models.ManyToManyField(
        "self", 
        symmetrical=False,   # ensures one-way follow
        related_name="followers",  # reverse access: user.followers.all()
        blank=True
    )


    def __str__(self):
        return self.username
