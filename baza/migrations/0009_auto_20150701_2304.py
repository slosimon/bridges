# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0008_auto_20150701_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='most',
            name='valid',
            field=models.BooleanField(default=False, verbose_name=b'Podatki so preverjeni'),
            preserve_default=True,
        ),
    ]
