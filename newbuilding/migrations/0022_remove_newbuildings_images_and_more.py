# Generated by Django 5.1.3 on 2024-11-28 23:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newbuilding", "0021_newbuildings_images"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newbuildings",
            name="images",
        ),
        migrations.AddField(
            model_name="newbuildings",
            name="company_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="companies_images/"
            ),
        ),
        migrations.CreateModel(
            name="NewBuildingsPhoto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="company_project/"
                    ),
                ),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="newbuilding.newbuildings",
                    ),
                ),
            ],
        ),
    ]
