# Generated by Django 5.1.3 on 2024-11-27 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("newbuilding", "0017_newbuildings_created_at_newbuildings_is_active_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="NewBuildingsProjecrts",
            new_name="NewBuildingsProjects",
        ),
    ]
