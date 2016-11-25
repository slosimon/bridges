# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0005_most_grafi'),
    ]

    operations = [
        migrations.AddField(
            model_name='most',
            name='besedilo_za_izkaznico',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
