# Generated by Django 5.1.2 on 2024-11-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_rename_scorestats_anime_scoresstats'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='descriptionHtml',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='descriptionSource',
            field=models.TextField(blank=True, null=True),
        ),
    ]