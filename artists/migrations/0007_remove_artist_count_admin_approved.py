# Generated by Django 4.1.2 on 2022-10-14 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0006_alter_artist_count_admin_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='count_admin_approved',
        ),
    ]
