# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0002_auto_20150527_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='most',
            name='leto_rekonstrukcije',
        ),
    ]
