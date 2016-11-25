# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150517_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novica',
            name='ime',
            field=models.TextField(max_length=500),
            preserve_default=True,
        ),
    ]
