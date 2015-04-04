# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_auto_20150109_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standings',
            fields=[
                ('team', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('division', models.CharField(max_length=1, null=True, blank=True)),
                ('games_played', models.IntegerField(null=True, blank=True)),
                ('wins', models.IntegerField(null=True, blank=True)),
                ('losses', models.IntegerField(null=True, blank=True)),
                ('ot_losses', models.IntegerField(null=True, blank=True)),
                ('points', models.IntegerField(null=True, blank=True)),
                ('row', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'standings',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
