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


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Currskaterstats(models.Model):
    nhl_num = models.IntegerField(blank=True, null=True)
    season = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=-1, blank=True)
    team2 = models.CharField(max_length=-1, blank=True)
    team3 = models.CharField(max_length=-1, blank=True)
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

    class Meta:
        managed = False
        db_table = 'currskaterstats'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Goalies(models.Model):
    first_name = models.CharField(max_length=-1, blank=True)
    last_name = models.CharField(max_length=-1, blank=True)
    nhl_num = models.IntegerField(primary_key=True)
    player_position = models.CharField(max_length=-1, blank=True)
    birthday = models.DateField(blank=True, null=True)
    draft_year = models.IntegerField(blank=True, null=True)
    draft_position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goalies'


class Goaliestats(models.Model):
    nhl_num = models.IntegerField(blank=True, null=True)
    season = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=-1, blank=True)
    team2 = models.CharField(max_length=-1, blank=True)
    team3 = models.CharField(max_length=-1, blank=True)
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


class PollsChoice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion')

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class Skaters(models.Model):
    first_name = models.CharField(max_length=-1, blank=True)
    last_name = models.CharField(max_length=-1, blank=True)
    nhl_num = models.IntegerField(primary_key=True)
    player_position = models.CharField(max_length=-1, blank=True)
    birthday = models.DateField(blank=True, null=True)
    draft_year = models.IntegerField(blank=True, null=True)
    draft_position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skaters'


class Skaterstats(models.Model):
    nhl_num = models.ForeignKey(Skaters, db_column='nhl_num', blank=True, null=True)
    season = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=-1, blank=True)
    team2 = models.CharField(max_length=-1, blank=True)
    team3 = models.CharField(max_length=-1, blank=True)
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
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'skaterstats'


class Skatpred15(models.Model):
    nhl_num = models.IntegerField(blank=True, null=True)
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
    es_assists = models.FloatField(blank=True, null=True)
    pp_assists = models.FloatField(blank=True, null=True)
    sh_assists = models.FloatField(blank=True, null=True)
    shots = models.FloatField(blank=True, null=True)
    shot_pct = models.FloatField(blank=True, null=True)
    points = models.FloatField(blank=True, null=True)
    assists = models.FloatField(blank=True, null=True)
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
