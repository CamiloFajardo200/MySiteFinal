# Generated by Django 3.2 on 2021-05-03 19:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 3, 19, 11, 13, 73260, tzinfo=utc)),
        ),
    ]
