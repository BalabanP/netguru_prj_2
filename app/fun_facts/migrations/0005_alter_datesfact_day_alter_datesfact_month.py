# Generated by Django 4.2.4 on 2023-08-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fun_facts", "0004_rename_day_populardates_days_checked"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datesfact",
            name="day",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="datesfact",
            name="month",
            field=models.IntegerField(),
        ),
    ]
