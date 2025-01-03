# Generated by Django 5.1.3 on 2024-11-25 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newbuilding", "0006_alter_companyprojects_project_state_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="companyprojects",
            old_name="cottage_area",
            new_name="townhouse_area",
        ),
        migrations.RenameField(
            model_name="companyprojects",
            old_name="cottage_type",
            new_name="townhouse_type",
        ),
        migrations.AlterField(
            model_name="companyprojects",
            name="project_type",
            field=models.CharField(
                choices=[
                    ("1-room", "1-room"),
                    ("2-room", "2-room"),
                    ("3-room", "3-room"),
                    ("4-room", "4-room"),
                    ("5-room", "5-room"),
                    ("Comorer", "Comorer"),
                    ("Commerce", "Commerce"),
                    ("Cottage", "Cottage"),
                    ("Duplex", "Duplex"),
                    ("Townhouse", "Townhouse"),
                ]
            ),
        ),
    ]
