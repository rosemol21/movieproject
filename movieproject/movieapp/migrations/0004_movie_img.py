# Generated by Django 4.2.4 on 2023-09-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_remove_movie_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='kkkppp', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
