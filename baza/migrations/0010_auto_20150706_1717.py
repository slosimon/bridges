# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0009_auto_20150701_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='most',
            name='razpon',
            field=models.FloatField(default=0, help_text=b'v metrih!! npr. 165.10', verbose_name=b'Dol\xc5\xbeina mostu'),
            preserve_default=True,
        ),
    ]
