# Generated by Django 5.0.6 on 2024-05-21 03:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_faculty_faculty_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="faculty",
            name="id",
        ),
        migrations.AlterField(
            model_name="faculty",
            name="Faculty_id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
