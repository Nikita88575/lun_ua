# Generated by Django 5.1.3 on 2024-11-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newbuilding", "0014_remove_newbuildingsprojecrts_sewerage_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="newbuildingsprojecrts",
            name="fixed_price_per_sqrm",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
