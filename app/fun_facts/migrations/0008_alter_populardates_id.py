# Generated by Django 4.2.4 on 2023-08-13 16:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fun_facts", "0007_alter_datesfact_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="populardates",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
