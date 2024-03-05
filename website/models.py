from django.db import models
from datetime import date


# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.category_name

class Playlist(models.Model):
    playlist_name=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.playlist_name

class Content(models.Model):
    title=models.CharField(max_length=200,blank=False)
    description=models.TextField()
    date=models.DateField(default=date.today())
    thumbnail=models.FileField()
    video_link=models.CharField(max_length=1000)
    playlist=models.ForeignKey(Playlist,on_delete=models.SET_NULL, null=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.id} - video - Title: {self.title}"
    
