# Generated by Django 3.0 on 2020-10-20 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20201001_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryproduct',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
    ]
