# Generated by Django 5.0.6 on 2024-06-06 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_generator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='yt_link',
            new_name='youtube_link',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='yt_title',
            new_name='youtube_title',
        ),
    ]
