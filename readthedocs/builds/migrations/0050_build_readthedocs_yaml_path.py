# Generated by Django 3.2.18 on 2023-04-04 13:03
from django.db import migrations
from django.db import models
from django_safemigrate import Safe

import readthedocs.projects.validators


class Migration(migrations.Migration):
    safe = Safe.after_deploy()
    dependencies = [
        ("builds", "0049_automation_rule_copy"),
    ]

    operations = [
        migrations.AddField(
            model_name="build",
            name="readthedocs_yaml_path",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=1024,
                null=True,
                validators=[readthedocs.projects.validators.validate_build_config_file],
                verbose_name="Custom build configuration file path used in this build",
            ),
        ),
    ]
