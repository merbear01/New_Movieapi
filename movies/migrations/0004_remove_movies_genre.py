# Generated by Django 5.1.3 on 2024-11-25 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movies_poster_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='genre',
        ),
    ]
