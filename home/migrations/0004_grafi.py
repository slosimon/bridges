# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20150517_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grafi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('graf', models.ImageField(upload_to=b'')),
                ('opis', models.TextField(max_length=10000)),
                ('po_vrsti', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
