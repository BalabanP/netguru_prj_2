# Generated by Django 4.2.4 on 2023-08-11 10:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fun_facts", "0003_populardates"),
    ]

    operations = [
        migrations.RenameField(
            model_name="populardates",
            old_name="day",
            new_name="days_checked",
        ),
    ]