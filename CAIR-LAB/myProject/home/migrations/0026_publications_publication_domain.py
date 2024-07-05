# Generated by Django 5.0.6 on 2024-06-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0025_alter_contact_desc_alter_contact_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="publications",
            name="Publication_domain",
            field=models.CharField(
                choices=[
                    ("EDGE-AI", "EDGE-AI"),
                    ("DATA SCIENCE", "DATA SCIENCE"),
                    ("CLOUD", "CLOUD"),
                    ("HPC", "HPC"),
                ],
                default="EDGE-AI",
                max_length=50,
            ),
        ),
    ]
