# Generated by Django 5.1.3 on 2024-11-27 08:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newbuilding", "0008_alter_companyprojects_townhouse_type"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="NewBuilding",
            new_name="NewBuildings",
        ),
        migrations.CreateModel(
            name="NewBuildingsCompaniesProjects",
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
                ("location", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=256)),
                ("station", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "project_type",
                    models.CharField(
                        choices=[
                            ("Cottage", "Cottage"),
                            ("Duplex", "Duplex"),
                            ("Quadrex", "Quadrex"),
                            ("Townhouse", "Townhouse"),
                        ]
                    ),
                ),
                ("project_var", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "project_state",
                    models.CharField(
                        choices=[("Builded", "Builded"), ("Builded", "Build")]
                    ),
                ),
                ("min_price_per_sqrm", models.IntegerField(blank=True, null=True)),
                ("price_per_sqrm", models.IntegerField(blank=True, null=True)),
                ("max_price_per_sqrm", models.IntegerField(blank=True, null=True)),
                ("solded", models.BooleanField(default=False)),
                ("min_area", models.FloatField(blank=True, null=True)),
                ("project_area", models.FloatField(blank=True, null=True)),
                ("max_area", models.FloatField(blank=True, null=True)),
                ("bedrooms_count", models.IntegerField(blank=True, null=True)),
                ("floors_count", models.IntegerField(blank=True, null=True)),
                ("walls", models.CharField(max_length=50)),
                ("walls_insulation", models.CharField(max_length=100)),
                ("project_heating", models.CharField(max_length=100)),
                ("water_supply", models.CharField(max_length=100)),
                ("sewerage", models.CharField(max_length=50)),
                ("territory", models.CharField()),
                ("housing_condition", models.CharField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rieltor_offer",
                        to="newbuilding.newbuildings",
                    ),
                ),
            ],
            options={
                "verbose_name": "New Building Company Project",
                "verbose_name_plural": "New Buildings Companies Projects",
                "db_table": "new_buildings_companies_projects",
            },
        ),
        migrations.DeleteModel(
            name="CompanyProjects",
        ),
    ]