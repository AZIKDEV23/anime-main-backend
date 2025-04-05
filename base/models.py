from django.db import models
from django.utils.text import slugify
from .forms import *
from django.conf import settings

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
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def image_tag(self):
        if self.image:
            return f'<img src="{self.image.url}" height="325" style="object-fit: cover;" />'
        return 'No Image Found'
    
    image_tag.allow_tags = True
    image_tag.short_description = 'Image'

class review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.anime.title}'
