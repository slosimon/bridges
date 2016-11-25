# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_grafi'),
        ('baza', '0004_auto_20150527_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='most',
            name='grafi',
            field=models.ManyToManyField(to='home.Grafi', blank=True),
            preserve_default=True,
        ),
    ]
