# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goalie',
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
                'db_table': 'goalies',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goaliestats',
            fields=[
                ('nhl_num', models.IntegerField(serialize=False, primary_key=True)),
                ('season', models.IntegerField(null=True, blank=True)),
                ('team', models.CharField(max_length=3, blank=True)),
                ('team2', models.CharField(max_length=3, blank=True)),
                ('team3', models.CharField(max_length=3, blank=True)),
                ('games_played', models.IntegerField(null=True, blank=True)),
                ('games_started', models.IntegerField(null=True, blank=True)),
                ('wins', models.IntegerField(null=True, blank=True)),
                ('losses', models.IntegerField(null=True, blank=True)),
                ('ties', models.IntegerField(null=True, blank=True)),
                ('overtime_losses', models.IntegerField(null=True, blank=True)),
                ('shots_against', models.IntegerField(null=True, blank=True)),
                ('goals_against', models.IntegerField(null=True, blank=True)),
                ('gaa', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('saves', models.IntegerField(null=True, blank=True)),
                ('save_pct', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('shutouts', models.IntegerField(null=True, blank=True)),
                ('goals', models.IntegerField(null=True, blank=True)),
                ('assists', models.IntegerField(null=True, blank=True)),
                ('penalty_minutes', models.IntegerField(null=True, blank=True)),
                ('toi', models.IntegerField(null=True, blank=True)),
                ('ps_attempts', models.IntegerField(null=True, blank=True)),
                ('ps_goals_against', models.IntegerField(null=True, blank=True)),
                ('ps_saves', models.IntegerField(null=True, blank=True)),
                ('so_wins', models.IntegerField(null=True, blank=True)),
                ('so_losses', models.IntegerField(null=True, blank=True)),
                ('so_shots_against', models.IntegerField(null=True, blank=True)),
                ('so_goals_against', models.IntegerField(null=True, blank=True)),
                ('es_shots_against', models.IntegerField(null=True, blank=True)),
                ('es_goals_against', models.IntegerField(null=True, blank=True)),
                ('es_saves', models.IntegerField(null=True, blank=True)),
                ('es_save_pct', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('pp_shots_against', models.IntegerField(null=True, blank=True)),
                ('pp_goals_against', models.IntegerField(null=True, blank=True)),
                ('pp_saves', models.IntegerField(null=True, blank=True)),
                ('pp_save_pct', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('sh_shots_against', models.IntegerField(null=True, blank=True)),
                ('sh_goals_against', models.IntegerField(null=True, blank=True)),
                ('sh_saves', models.IntegerField(null=True, blank=True)),
                ('sh_save_pct', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ],
            options={
                'db_table': 'goaliestats',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skater',
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
                'db_table': 'skaters',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkaterPredictions',
            fields=[
                ('games_played', models.FloatField(null=True, blank=True)),
                ('es_toi', models.FloatField(null=True, blank=True)),
                ('sh_toi', models.FloatField(null=True, blank=True)),
                ('pp_toi', models.FloatField(null=True, blank=True)),
                ('toi', models.FloatField(null=True, blank=True)),
                ('es_goals', models.FloatField(null=True, blank=True)),
                ('sh_goals', models.FloatField(null=True, blank=True)),
                ('pp_goals', models.FloatField(null=True, blank=True)),
                ('goals', models.FloatField(null=True, blank=True)),
                ('pp_points', models.FloatField(null=True, blank=True)),
                ('sh_points', models.FloatField(null=True, blank=True)),
                ('es_points', models.FloatField(null=True, blank=True)),
                ('points', models.FloatField(null=True, blank=True)),
                ('es_assists', models.FloatField(null=True, blank=True)),
                ('pp_assists', models.FloatField(null=True, blank=True)),
                ('sh_assists', models.FloatField(null=True, blank=True)),
                ('assists', models.FloatField(null=True, blank=True)),
                ('shots', models.FloatField(null=True, blank=True)),
                ('shot_pct', models.FloatField(null=True, blank=True)),
                ('minors', models.FloatField(null=True, blank=True)),
                ('majors', models.FloatField(null=True, blank=True)),
                ('misconducts', models.FloatField(null=True, blank=True)),
                ('game_misconducts', models.FloatField(null=True, blank=True)),
                ('penalty_minutes', models.FloatField(null=True, blank=True)),
                ('team_goals_for', models.FloatField(null=True, blank=True)),
                ('team_pp_goals_for', models.FloatField(null=True, blank=True)),
                ('team_goals_against', models.FloatField(null=True, blank=True)),
                ('team_pp_goals_against', models.FloatField(null=True, blank=True)),
                ('plus_minus', models.FloatField(null=True, blank=True)),
                ('faceoff_wins', models.FloatField(null=True, blank=True)),
                ('faceoff_losses', models.FloatField(null=True, blank=True)),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'skatpred15',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkaterStats',
            fields=[
                ('season', models.IntegerField(null=True, blank=True)),
                ('team', models.CharField(max_length=3, blank=True)),
                ('team2', models.CharField(max_length=3, blank=True)),
                ('team3', models.CharField(max_length=3, blank=True)),
                ('games_played', models.IntegerField(null=True, blank=True)),
                ('goals', models.IntegerField(null=True, blank=True)),
                ('assists', models.IntegerField(null=True, blank=True)),
                ('points', models.IntegerField(null=True, blank=True)),
                ('plus_minus', models.IntegerField(null=True, blank=True)),
                ('penalty_minutes', models.IntegerField(null=True, blank=True)),
                ('pp_goals', models.IntegerField(null=True, blank=True)),
                ('pp_points', models.IntegerField(null=True, blank=True)),
                ('sh_goals', models.IntegerField(null=True, blank=True)),
                ('sh_points', models.IntegerField(null=True, blank=True)),
                ('gw_goals', models.IntegerField(null=True, blank=True)),
                ('ot_goals', models.IntegerField(null=True, blank=True)),
                ('shots', models.IntegerField(null=True, blank=True)),
                ('shot_pct', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('en_goals', models.IntegerField(null=True, blank=True)),
                ('ps_goals', models.IntegerField(null=True, blank=True)),
                ('minors', models.IntegerField(null=True, blank=True)),
                ('majors', models.IntegerField(null=True, blank=True)),
                ('misconducts', models.IntegerField(null=True, blank=True)),
                ('game_misconducts', models.IntegerField(null=True, blank=True)),
                ('matches', models.IntegerField(null=True, blank=True)),
                ('team_goals_for', models.IntegerField(null=True, blank=True)),
                ('team_pp_goals_for', models.IntegerField(null=True, blank=True)),
                ('team_goals_against', models.IntegerField(null=True, blank=True)),
                ('team_pp_goals_against', models.IntegerField(null=True, blank=True)),
                ('hits', models.IntegerField(null=True, blank=True)),
                ('blocked_shots', models.IntegerField(null=True, blank=True)),
                ('missed_shots', models.IntegerField(null=True, blank=True)),
                ('giveaways', models.IntegerField(null=True, blank=True)),
                ('takeaways', models.IntegerField(null=True, blank=True)),
                ('faceoff_wins', models.IntegerField(null=True, blank=True)),
                ('faceoff_losses', models.IntegerField(null=True, blank=True)),
                ('so_shots', models.IntegerField(null=True, blank=True)),
                ('so_goals', models.IntegerField(null=True, blank=True)),
                ('so_pct', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('game_deciding_goals', models.IntegerField(null=True, blank=True)),
                ('ot_games_played', models.IntegerField(null=True, blank=True)),
                ('ot_assists', models.IntegerField(null=True, blank=True)),
                ('ot_points', models.IntegerField(null=True, blank=True)),
                ('es_toi', models.IntegerField(null=True, blank=True)),
                ('sh_toi', models.IntegerField(null=True, blank=True)),
                ('pp_toi', models.IntegerField(null=True, blank=True)),
                ('toi', models.IntegerField(null=True, blank=True)),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['nhl_num'],
                'db_table': 'skaterstats',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
