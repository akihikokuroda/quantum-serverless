# Generated by Django 4.2.2 on 2023-10-10 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_job_version"),
    ]

    operations = [
        migrations.AddField(
            model_name="program",
            name="config",
            field=models.TextField(blank=True, default="[]"),
        ),
    ]