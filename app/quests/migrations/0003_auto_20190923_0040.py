# Generated by Django 2.2.3 on 2019-09-23 00:40

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kudos', '0006_token_override_display_name'),
        ('quests', '0002_auto_20190922_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='kudos_reward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quests_reward', to='kudos.Token'),
        ),
        migrations.AddField(
            model_name='quest',
            name='questions',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='quest',
            name='unlocked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unblocks', to='quests.Quest'),
        ),
        migrations.AlterField(
            model_name='questattempt',
            name='quest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attempts', to='quests.Quest'),
        ),
    ]