# Generated by Django 5.0.6 on 2024-05-20 06:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_alter_faculty_faculty_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="faculty",
            name="Faculty_id",
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
