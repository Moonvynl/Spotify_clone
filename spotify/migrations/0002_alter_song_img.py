# Generated by Django 5.0.4 on 2024-05-09 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='img',
            field=models.ImageField(blank=True, default='playlist_default.png', upload_to='song_img/'),
        ),
    ]
