from django.contrib import admin
from django.utils.html import format_html
from .models import *
# Register your models here.

# admin.site.register(Genre)
# admin.site.register(Anime)
# admin.site.register(Review)

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'slug', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img id="image-preview" src="{}" height="325" style="object-fit: cover;" />', obj.image.url)
        return format_html('<img id="image-preview" src="" height="325" style="display: none;" />')
    
    image_preview.short_description = 'Image Preview'

    class Media:
        js = ('admin/js/image_preview.js',)

admin.site.register(Genre)
admin.site.register(review)
# admin.site.register(CustomUser)