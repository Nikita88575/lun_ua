# Generated by Django 5.1.3 on 2024-11-28 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("newbuilding", "0023_alter_newbuildings_company_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="newbuildingsphoto",
            options={
                "verbose_name": "New Building Photo",
                "verbose_name_plural": "New Buildings Photos",
            },
        ),
        migrations.AlterModelTable(
            name="newbuildingsphoto",
            table="new_buildings_photos",
        ),
    ]