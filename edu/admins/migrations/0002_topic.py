# Generated by Django 4.1.7 on 2023-04-16 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("admins", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
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
                ("name", models.CharField(max_length=64)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                ("date_updated", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admins.category",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admins.subject",
                    ),
                ),
            ],
            options={
                "db_table": "admins_topic",
                "ordering": ["name", "date_created", "date_updated"],
                "abstract": False,
            },
        ),
    ]
