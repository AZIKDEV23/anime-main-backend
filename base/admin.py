from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Genre)
# admin.site.register(Anime)
# admin.site.register(Review)

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'rating', 'slug')

admin.site.register(Genre)
admin.site.register(Review)
