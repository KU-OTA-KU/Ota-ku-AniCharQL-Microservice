# Generated by Django 5.1.2 on 2024-11-02 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_anime_description_anime_descriptionhtml_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='createdAt',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='updatedAt',
        ),
    ]
