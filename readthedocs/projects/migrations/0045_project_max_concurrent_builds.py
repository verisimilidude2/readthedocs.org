# Generated by Django 2.2.11 on 2020-04-18 11:22
from django.db import migrations
from django.db import models
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.after_deploy()
    dependencies = [
        ("projects", "0044_auto_20190703_1300"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="max_concurrent_builds",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Maximum concurrent builds allowed for this project",
            ),
        ),
    ]
