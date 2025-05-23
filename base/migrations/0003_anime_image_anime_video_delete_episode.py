# Generated by Django 5.1.6 on 2025-03-29 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_anime_image_remove_anime_video_episode'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='anime_images/'),
        ),
        migrations.AddField(
            model_name='anime',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='anime_videos/'),
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
    ]
