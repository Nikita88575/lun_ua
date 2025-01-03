# Generated by Django 5.1.3 on 2024-11-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newbuilding", "0011_alter_newbuildingsprojecrts_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newbuildingsprojecrts",
            name="apartament_count",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="newbuildingsprojecrts",
            name="bacup_power_supply",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="newbuildingsprojecrts",
            name="ceiling_height",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="newbuildingsprojecrts",
            name="construction_tec",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="newbuildingsprojecrts",
            name="houses_count",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="newbuildingsprojecrts",
            name="parking",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="newbuildingsprojecrts",
            name="project_heating",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="newbuildingsprojecrts",
            name="sewerage",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="newbuildingsprojecrts",
            name="shelter",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="newbuildingsprojecrts",
            name="walls",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="newbuildingsprojecrts",
            name="walls_insulation",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="newbuildingsprojecrts",
            name="water_supply",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
