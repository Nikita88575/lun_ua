# Generated by Django 5.1.3 on 2024-11-29 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("newbuilding", "0024_alter_newbuildingsphoto_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newbuildingsprojects",
            old_name="address",
            new_name="district",
        ),
    ]
