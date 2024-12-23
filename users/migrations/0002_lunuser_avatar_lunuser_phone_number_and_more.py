# Generated by Django 5.1.3 on 2024-11-29 16:13

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lunuser",
            name="avatar",
            field=django_resized.forms.ResizedImageField(
                blank=True,
                crop=None,
                force_format=None,
                keep_meta=True,
                null=True,
                quality=-1,
                scale=None,
                size=[256, 256],
                upload_to="avatars/",
            ),
        ),
        migrations.AddField(
            model_name="lunuser",
            name="phone_number",
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="lunuser",
            name="work_ends_at",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="lunuser",
            name="work_starts_at",
            field=models.TimeField(blank=True, null=True),
        ),
    ]