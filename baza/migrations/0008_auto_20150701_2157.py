# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0007_most_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='most',
            name='obmocje_SVP',
            field=models.CharField(default=b'Ljubljana', max_length=25, verbose_name=b'Obmo\xc4\x8dje SVP', choices=[(b'Ljubljana', b'Ljubljana'), (b'Celje', b'Celje'), (b'Maribor', b'Maribor'), (b'Postojna', b'Postojna'), (b'Celje (Ljubljana)', b'Celje (Ljubljana)'), (b'Ljubljana (Novo mesto)', b'Ljubljana (Novo mesto)'), (b'Ljubljana (Nova Gorica)', b'Ljubljana (Nova Gorica)'), (b'Postojna (Nova Gorica)', b'Postojna (Nova Gorica)')]),
            preserve_default=True,
        ),
    ]
