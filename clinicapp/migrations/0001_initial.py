# Generated by Django 5.0.3 on 2024-03-30 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("lastName", models.CharField(max_length=20)),
                ("firstName", models.CharField(max_length=20)),
                ("age", models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="ClinicalData",
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
                (
                    "componentName",
                    models.CharField(
                        choices=[
                            ("hw", "height/weight"),
                            ("bp", "Blood Pressure"),
                            ("heartrate", "Heart Rate"),
                        ],
                        max_length=20,
                    ),
                ),
                ("componentValue", models.CharField(max_length=20)),
                ("measuredDateTime", models.DateTimeField(auto_now_add=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clinicapp.patient",
                    ),
                ),
            ],
        ),
    ]
