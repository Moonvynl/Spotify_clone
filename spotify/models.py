from django.db import models
from django.conf import settings


class Song(models.Model):
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    url = models.FileField(upload_to='song/', blank=False, null=False)
    img = models.ImageField(upload_to='song_img/', blank=True, null=False, default='playlist_default.png')

    def __str__(self):
        return self.title


class Playlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)

    img = models.ImageField(upload_to='playlist_img/', blank=True, default='playlist_default.png')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']


