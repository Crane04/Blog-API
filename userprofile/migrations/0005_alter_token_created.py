# Generated by Django 4.1 on 2023-10-28 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0004_alter_token_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="token",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 28, 18, 35, 22, 617024),
                editable=False,
            ),
        ),
    ]
