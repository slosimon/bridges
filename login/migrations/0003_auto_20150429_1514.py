# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20150428_2004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'User profiles'},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='slika',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='spletna_stran',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='activation_key',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 15, 14, 8, 609857)),
            preserve_default=True,
        ),
    ]
