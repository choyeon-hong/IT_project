# Generated by Django 5.1.6 on 2025-02-22 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wandercritic', '0002_user_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
    ]
