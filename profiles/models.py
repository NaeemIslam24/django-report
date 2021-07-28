from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='No bio....')
    created = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatar')

    def __str__(self):
        return f"profile of {self.user.username}"
