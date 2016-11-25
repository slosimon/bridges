# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0006_most_besedilo_za_izkaznico'),
    ]

    operations = [
        migrations.AddField(
            model_name='most',
            name='valid',
            field=models.BooleanField(default=0, verbose_name=b'Podatki so preverjeni'),
            preserve_default=False,
        ),
    ]
