# Generated by Django 3.1.2 on 2020-10-30 01:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20201030_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 1, 1, 32, 22, 504772, tzinfo=utc)),
        ),
    ]
