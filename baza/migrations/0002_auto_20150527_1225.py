# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leto', models.IntegerField(help_text=b'Leto rekonstrukcije')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='most',
            name='leto_rekonstrukcije_nov',
            field=models.ManyToManyField(to='baza.Leto', blank=True),
            preserve_default=True,
        ),
    ]
