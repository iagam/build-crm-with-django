# Generated by Django 4.1.5 on 2023-01-26 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lead",
            old_name="agent_id",
            new_name="agent",
        ),
    ]