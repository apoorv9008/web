# Generated by Django 2.0.4 on 2018-04-16 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0054_bountyfulfillment_fulfiller_github_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bounty',
            name='avatar_url',
        ),
    ]
