# Generated by Django 4.1.2 on 2022-10-14 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=100, unique=True)),
                ('social_link', models.URLField(blank=True)),
                ('num_admin_approved', models.IntegerField(editable=False, null=True)),
            ],
            options={
                'db_table': 'artists',
                'ordering': ['stage_name'],
            },
        ),
    ]
