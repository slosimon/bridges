# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='picture',
            new_name='slika',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='website',
            new_name='spletna_stran',
        ),
    ]
