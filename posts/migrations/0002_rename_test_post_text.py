# Generated by Django 4.2.9 on 2024-01-10 04:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="test",
            new_name="text",
        ),
    ]
