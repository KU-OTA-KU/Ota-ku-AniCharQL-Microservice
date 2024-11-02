# Generated by Django 5.1.2 on 2024-10-30 19:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_poster_anime_season_anime_url_anime_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='fandubbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, max_length=255, null=True), default=list, null=True, size=None),
        ),
        migrations.AddField(
            model_name='anime',
            name='fansubbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, max_length=255, null=True), default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='anime',
            name='synonyms',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, max_length=255, null=True), default=list, null=True, size=None),
        ),
    ]