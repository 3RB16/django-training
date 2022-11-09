# Generated by Django 4.1.2 on 2022-11-03 10:39

import albums.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_alter_song_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(upload_to='musics/', validators=[albums.validators.audio_file_validator]),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterModelTable(
            name='song',
            table=None,
        ),
    ]