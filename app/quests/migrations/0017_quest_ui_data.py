# Generated by Django 2.2.3 on 2019-10-24 20:42

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0016_auto_20191023_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='ui_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
