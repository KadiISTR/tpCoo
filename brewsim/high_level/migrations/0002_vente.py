# Generated by Django 4.2.7 on 2023-11-30 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("high_level", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vente",
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
                ("benefices", models.IntegerField()),
                (
                    "departement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="high_level.departement",
                    ),
                ),
            ],
        ),
    ]
