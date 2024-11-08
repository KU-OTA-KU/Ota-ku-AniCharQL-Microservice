# Generated by Django 5.1.2 on 2024-10-30 23:11

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_topic_character_anime_characterroles'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolesEn', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None)),
                ('rolesRu', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.character')),
            ],
        ),
        migrations.AlterField(
            model_name='anime',
            name='characterRoles',
            field=models.ManyToManyField(blank=True, default=dict, to='api.characterrole'),
        ),
    ]
