# Generated by Django 5.2.3 on 2025-06-21 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registration",
            name="confirm_password",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="registration",
            name="password",
            field=models.CharField(max_length=128),
        ),
    ]
