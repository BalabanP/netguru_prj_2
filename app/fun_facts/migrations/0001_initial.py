# Generated by Django 4.2.4 on 2023-08-10 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatesFact',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('month', models.IntegerField(max_length=2)),
                ('day', models.IntegerField(max_length=2)),
                ('fact', models.TextField(max_length=200)),
            ],
        ),
    ]
