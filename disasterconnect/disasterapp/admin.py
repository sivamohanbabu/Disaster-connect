from django.contrib import admin
from .models import CustomUser, Alert

admin.site.register(CustomUser)
admin.site.register(Alert)


