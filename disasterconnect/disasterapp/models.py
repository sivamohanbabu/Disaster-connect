from django.db import models
from django.contrib.auth.models import AbstractUser


# Extend Django's User model
class CustomUser(AbstractUser):
    USER_TYPES = [
        ("volunteer", "Volunteer"),
        ("supervisor", "Supervisor"),
        ("adminuser", "Admin"),
    ]

    mobile = models.CharField(max_length=15, unique=True)
    picture = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    state = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default="volunteer")

    def __str__(self):
        return f"{self.username} ({self.user_type})"
