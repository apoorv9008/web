# Generated by Django 2.2.4 on 2020-07-28 11:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0131_auto_20200727_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribessubscription',
            name='expires_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 28, 11, 12, 38, 779169, tzinfo=utc), null=True),
        ),
    ]
