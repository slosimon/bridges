# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Novica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField()),
                ('ime', models.TextField(max_length=50)),
                ('novica', models.TextField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
