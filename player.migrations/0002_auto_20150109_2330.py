# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skater',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='skaterstats',
            options={'ordering': ['season']},
        ),
    ]
