# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Goalie(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    nhl_num = models.IntegerField(primary_key=True)
    player_position = models.CharField(max_length=1, blank=True)
    birthday = models.DateField(blank=True, null=True)
    draft_year = models.IntegerField(blank=True, null=True)
    draft_position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goalies'


class Goaliestats(models.Model):
    nhl_num = models.IntegerField(primary_key=True)
    season = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=3, blank=True)
    team2 = models.CharField(max_length=3, blank=True)
    team3 = models.CharField(max_length=3, blank=True)
    games_played = models.IntegerField(blank=True, null=True)
    games_started = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    ties = models.IntegerField(blank=True, null=True)
    overtime_losses = models.IntegerField(blank=True, null=True)
    shots_against = models.IntegerField(blank=True, null=True)
    goals_against = models.IntegerField(blank=True, null=True)
    gaa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    saves = models.IntegerField(blank=True, null=True)
    save_pct = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shutouts = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    penalty_minutes = models.IntegerField(blank=True, null=True)
    toi = models.IntegerField(blank=True, null=True)
    ps_attempts = models.IntegerField(blank=True, null=True)
    ps_goals_against = models.IntegerField(blank=True, null=True)
    ps_saves = models.IntegerField(blank=True, null=True)
    so_wins = models.IntegerField(blank=True, null=True)
    so_losses = models.IntegerField(blank=True, null=True)
    so_shots_against = models.IntegerField(blank=True, null=True)
    so_goals_against = models.IntegerField(blank=True, null=True)
    es_shots_against = models.IntegerField(blank=True, null=True)
    es_goals_against = models.IntegerField(blank=True, null=True)
    es_saves = models.IntegerField(blank=True, null=True)
    es_save_pct = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pp_shots_against = models.IntegerField(blank=True, null=True)
    pp_goals_against = models.IntegerField(blank=True, null=True)
    pp_saves = models.IntegerField(blank=True, null=True)
    pp_save_pct = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sh_shots_against = models.IntegerField(blank=True, null=True)
    sh_goals_against = models.IntegerField(blank=True, null=True)
    sh_saves = models.IntegerField(blank=True, null=True)
    sh_save_pct = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goaliestats'


@python_2_unicode_compatible
class Skater(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    nhl_num = models.IntegerField(primary_key=True)
    player_position = models.CharField(max_length=1, blank=True)
    birthday = models.DateField(blank=True, null=True)
    draft_year = models.IntegerField(blank=True, null=True)
    draft_position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skaters'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return ' '.join([self.first_name,
                         self.last_name,
                         ])


class CurrSkaterStats(models.Model):
    nhl_num = models.ForeignKey(Skater, db_column='nhl_num')
    season = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=3, blank=True)
    team2 = models.CharField(max_length=3, blank=True)
    team3 = models.CharField(max_length=3, blank=True)
    games_played = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    plus_minus = models.IntegerField(blank=True, null=True)
    penalty_minutes = models.IntegerField(blank=True, null=True)
    pp_goals = models.IntegerField(blank=True, null=True)
    pp_points = models.IntegerField(blank=True, null=True)
    sh_goals = models.IntegerField(blank=True, null=True)
    sh_points = models.IntegerField(blank=True, null=True)
    gw_goals = models.IntegerField(blank=True, null=True)
    ot_goals = models.IntegerField(blank=True, null=True)
    shots = models.IntegerField(blank=True, null=True)
    shot_pct = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    en_goals = models.IntegerField(blank=True, null=True)
    ps_goals = models.IntegerField(blank=True, null=True)
    minors = models.IntegerField(blank=True, null=True)
    majors = models.IntegerField(blank=True, null=True)
    misconducts = models.IntegerField(blank=True, null=True)
    game_misconducts = models.IntegerField(blank=True, null=True)
    matches = models.IntegerField(blank=True, null=True)
    team_goals_for = models.IntegerField(blank=True, null=True)
    team_pp_goals_for = models.IntegerField(blank=True, null=True)
    team_goals_against = models.IntegerField(blank=True, null=True)
    team_pp_goals_against = models.IntegerField(blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    blocked_shots = models.IntegerField(blank=True, null=True)
    missed_shots = models.IntegerField(blank=True, null=True)
    giveaways = models.IntegerField(blank=True, null=True)
    takeaways = models.IntegerField(blank=True, null=True)
    faceoff_wins = models.IntegerField(blank=True, null=True)
    faceoff_losses = models.IntegerField(blank=True, null=True)
    so_shots = models.IntegerField(blank=True, null=True)
    so_goals = models.IntegerField(blank=True, null=True)
    so_pct = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    game_deciding_goals = models.IntegerField(blank=True, null=True)
    ot_games_played = models.IntegerField(blank=True, null=True)
    ot_assists = models.IntegerField(blank=True, null=True)
    ot_points = models.IntegerField(blank=True, null=True)
    es_toi = models.IntegerField(blank=True, null=True)
    sh_toi = models.IntegerField(blank=True, null=True)
    pp_toi = models.IntegerField(blank=True, null=True)
    toi = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'currskaterstats'
        ordering = ['nhl_num']
        def __str__(self):
            return ' '.join([str(self.nhl_num),
                         ])


class SkaterPredictions(models.Model):
    nhl_num = models.IntegerField(primary_key=True)
    games_played = models.FloatField(blank=True, null=True)
    es_toi = models.FloatField(blank=True, null=True)
    sh_toi = models.FloatField(blank=True, null=True)
    pp_toi = models.FloatField(blank=True, null=True)
    toi = models.FloatField(blank=True, null=True)
    es_goals = models.FloatField(blank=True, null=True)
    sh_goals = models.FloatField(blank=True, null=True)
    pp_goals = models.FloatField(blank=True, null=True)
    goals = models.FloatField(blank=True, null=True)
    pp_points = models.FloatField(blank=True, null=True)
    sh_points = models.FloatField(blank=True, null=True)
    es_points = models.FloatField(blank=True, null=True)
    points = models.FloatField(blank=True, null=True)
    es_assists = models.FloatField(blank=True, null=True)
    pp_assists = models.FloatField(blank=True, null=True)
    sh_assists = models.FloatField(blank=True, null=True)
    assists = models.FloatField(blank=True, null=True)
    shots = models.FloatField(blank=True, null=True)
    shot_pct = models.FloatField(blank=True, null=True)
    minors = models.FloatField(blank=True, null=True)
    majors = models.FloatField(blank=True, null=True)
    misconducts = models.FloatField(blank=True, null=True)
    game_misconducts = models.FloatField(blank=True, null=True)
    penalty_minutes = models.FloatField(blank=True, null=True)
    team_goals_for = models.FloatField(blank=True, null=True)
    team_pp_goals_for = models.FloatField(blank=True, null=True)
    team_goals_against = models.FloatField(blank=True, null=True)
    team_pp_goals_against = models.FloatField(blank=True, null=True)
    plus_minus = models.FloatField(blank=True, null=True)
    faceoff_wins = models.FloatField(blank=True, null=True)
    faceoff_losses = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skatpred15'
