# Generated by Django 5.1.3 on 2024-11-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newbuilding", "0019_remove_newbuildingsprojects_address_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newbuildings",
            name="address",
        ),
        migrations.RemoveField(
            model_name="newbuildings",
            name="location",
        ),
        migrations.RemoveField(
            model_name="newbuildings",
            name="metro_station",
        ),
        migrations.AddField(
            model_name="newbuildingsprojects",
            name="address",
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="newbuildingsprojects",
            name="location",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="newbuildingsprojects",
            name="metro_station",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
