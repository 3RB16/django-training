# Generated by Django 4.1.2 on 2022-10-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_alter_artist_count_admin_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='count_admin_approved',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
