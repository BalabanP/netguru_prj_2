# Generated by Django 4.2.4 on 2023-08-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fun_facts", "0005_alter_datesfact_day_alter_datesfact_month"),
    ]

    operations = [
        migrations.AlterField(
            model_name="populardates",
            name="days_checked",
            field=models.IntegerField(),
        ),
    ]
