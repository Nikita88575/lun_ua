# Generated by Django 5.1.3 on 2024-11-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newbuilding", "0020_remove_newbuildings_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="newbuildings",
            name="images",
            field=models.ImageField(blank=True, null=True, upload_to="project_images/"),
        ),
    ]
