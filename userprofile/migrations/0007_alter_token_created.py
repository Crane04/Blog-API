# Generated by Django 4.1 on 2023-11-05 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0006_alter_token_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="token",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 5, 17, 40, 33, 929939),
                editable=False,
            ),
        ),
    ]
