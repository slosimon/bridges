# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0003_remove_most_leto_rekonstrukcije'),
    ]

    operations = [
        migrations.AlterField(
            model_name='most',
            name='leto_rekonstrukcije_nov',
            field=models.ManyToManyField(help_text=b'Leta rekonstrukcije', to='baza.Leto', blank=True),
            preserve_default=True,
        ),
    ]
