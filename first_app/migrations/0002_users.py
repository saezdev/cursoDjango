# Generated by Django 4.1 on 2023-07-24 02:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("first_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Users",
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
                ("f_name", models.CharField(max_length=30)),
                ("l_name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=50, unique=True)),
            ],
        ),
    ]
