# Generated by Django 5.1.2 on 2024-10-28 19:36

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('malId', models.IntegerField()),
                ('russian', models.TextField(blank=True, null=True)),
                ('english', models.TextField(blank=True, null=True)),
                ('japanese', models.TextField(blank=True, null=True)),
                ('licenseNameRu', models.TextField(blank=True, max_length=255, null=True)),
                ('synonyms', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, max_length=255, null=True), default=django.db.models.deletion.SET_NULL, null=True, size=None)),
                ('kind', models.CharField(choices=[('tv', 'Tv'), ('movie', 'Movie'), ('ova', 'Ova'), ('ona', 'Ona'), ('special', 'Special'), ('tv_special', 'Tv Special'), ('music', 'Music'), ('pv', 'Pv'), ('cm', 'Cm')], max_length=10)),
            ],
        ),
    ]