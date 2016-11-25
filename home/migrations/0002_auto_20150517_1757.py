# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novica',
            name='novica',
            field=models.TextField(max_length=25500),
            preserve_default=True,
        ),
    ]
