# Generated by Django 5.1.3 on 2024-12-02 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("newbuilding", "0028_remove_newbuildingsprojects_max_area_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newbuildings",
            old_name="bacup_power_supply",
            new_name="backup_power_supply",
        ),
    ]
