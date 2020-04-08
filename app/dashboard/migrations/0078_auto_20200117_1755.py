# Generated by Django 2.2.4 on 2020-01-17 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kudos', '0011_auto_20191106_0237'),
        ('dashboard', '0077_remove_activity_kudos'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='kudos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='kudos.Token'),
        ),
        migrations.AddField(
            model_name='activity',
            name='kudos_transfer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='kudos.KudosTransfer'),
        ),
    ]