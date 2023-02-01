# Generated by Django 4.1.5 on 2023-01-29 11:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0002_rename_agent_id_lead_agent"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="created",
            field=models.DateTimeField(
                default=django.utils.timezone.now, editable=False
            ),
        ),
    ]