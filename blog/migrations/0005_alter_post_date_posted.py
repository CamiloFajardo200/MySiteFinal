# Generated by Django 3.2.1 on 2021-05-27 17:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 27, 17, 54, 29, 22743, tzinfo=utc)),
        ),
    ]
