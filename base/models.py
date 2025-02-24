from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Anime(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.PositiveIntegerField()
    genres = models.ManyToManyField(Genre)
    rating = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='anime_images/', blank=True, null=True)
    video = models.FileField(upload_to='anime_videos/', blank=True, null=True)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.anime.title}'
