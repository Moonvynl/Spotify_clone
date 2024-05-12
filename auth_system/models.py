from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user-avatars/',  blank=True, null=False, default='playlist_default.png')

    def __str__(self):
        return self.username
    
    class Meta():
        verbose_name = 'User'

