# Generated by Django 4.1 on 2023-10-29 06:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0005_alter_token_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="token",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 29, 7, 28, 2, 857362),
                editable=False,
            ),
        ),
    ]
