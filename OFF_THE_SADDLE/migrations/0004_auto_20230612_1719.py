# Generated by Django 3.2.16 on 2023-06-12 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OFF_THE_SADDLE', '0003_auto_20230611_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='ridetime',
            name='time',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]
