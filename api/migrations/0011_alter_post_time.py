# Generated by Django 4.1 on 2023-10-17 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_post_body_alter_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 17, 7, 41, 48, 211202)),
        ),
    ]
