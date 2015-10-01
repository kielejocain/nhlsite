# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('first_name', models.CharField(max_length=255, blank=True)),
                ('last_name', models.CharField(max_length=255, blank=True)),
                ('nhl_num', models.IntegerField(serialize=False, primary_key=True)),
                ('player_position', models.CharField(max_length=1, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('draft_year', models.IntegerField(null=True, blank=True)),
                ('draft_position', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'db_table': 'players',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayerTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season', models.IntegerField(null=True, blank=True)),
                ('order', models.IntegerField(null=True, blank=True)),
                ('team', models.CharField(max_length=255, blank=True)),
                ('current', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['nhl_num', 'season', 'order'],
                'db_table': 'playerteams',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='skaterstats',
            options={'ordering': ['season'], 'managed': False},
        ),
        migrations.AlterModelTable(
            name='skaterpredictions',
            table='newskatpred15',
        ),
    ]
