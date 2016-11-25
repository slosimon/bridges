# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20150429_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slika',
            name='slika',
            field=models.ImageField(upload_to=b''),
            preserve_default=True,
        ),
    ]
