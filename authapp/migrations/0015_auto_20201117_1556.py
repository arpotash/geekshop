# Generated by Django 3.1.2 on 2020-11-17 12:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0014_auto_20201113_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 12, 56, 48, 158901, tzinfo=utc)),
        ),
    ]
