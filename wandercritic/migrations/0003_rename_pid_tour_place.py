# Generated by Django 5.1.6 on 2025-02-17 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wandercritic', '0002_place_remove_page_category_tour_delete_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='PID',
            new_name='place',
        ),
    ]
