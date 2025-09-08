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


class Alert(models.Model):
    INDIAN_STATES = [
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    ]

    incident = models.CharField(max_length=255)
    description = models.TextField()
    state = models.CharField(max_length=100, choices=INDIAN_STATES, blank=True, null=True)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    google_maps_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="alert_images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.incident} - {self.user.username}"
