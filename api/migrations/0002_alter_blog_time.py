# Generated by Django 4.1 on 2023-10-10 22:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 23, 55, 10, 48866)),
        ),
    ]
