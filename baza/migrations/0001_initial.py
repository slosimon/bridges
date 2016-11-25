# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dokumentacija_vsa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ime_dokumenta', models.CharField(help_text=b'Javno ime dokumenta npr. Tloris', max_length=255)),
                ('dokument', models.FileField(upload_to=b'')),
                ('je_javni', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Most',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ime', models.CharField(help_text=b'npr. Most \xc4\x8dez Savo', max_length=255)),
                ('slike', models.FileField(help_text=b"Slike spravite v arhiv (ZIP, 7Z, TAR.GZ ali kaj podobnega), sliko, katero pa \xc5\xbeelite na izkaznici pa poimenujte v main.jpg ali katerakoli druga kon\xc4\x8dnica, nobena druga slika pa ne sme imeti imena main in karkoli drugo naprej (It's temporary)", upload_to=b'', null=True, verbose_name=b'Slike stisnjene v eno datoteko', blank=True)),
                ('glavna_slika', models.ImageField(help_text=b'Slika, katero \xc5\xbeelite, da bodo obiskovalci videli na strani in na izkaznici, ostale pa bodo lahko dobili z downloadom, zaradi velikosti strani (po\xc4\x8dasno nalaganje)', null=True, upload_to=b'', blank=True)),
                ('lokacija_sirina', models.FloatField(default=46, help_text=b'Kopiraj iz Google maps prvo \xc5\xa1tevilo (N) npr. 46.0000000', verbose_name=b'Lokacija \xc5\xa1irina', validators=[django.core.validators.MinValueValidator(42), django.core.validators.MaxValueValidator(50)])),
                ('lokacija_dolzina', models.FloatField(default=14, help_text=b'npr. 14.0000000', verbose_name=b'Lokacija dol\xc5\xbeina', validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(20)])),
                ('obmocje_SVP', models.CharField(default=b'Ljubljana', max_length=25, verbose_name=b'Obmo\xc4\x8dje SVP', choices=[(b'Ljubljana', b'Ljubljana'), (b'Celje', b'Celje'), (b'Maribor', b'Maribor'), (b'Postojna', b'Postojna'), (b'Celje (Ljubljana)', b'Celje (Ljubljana)'), (b'Ljubljana (Novo Mesto)', b'Ljubljana (Novo mesto)'), (b'Ljubljana (Nova Gorica)', b'Ljubljana (Nova Gorica)'), (b'Postojna (Nova Gorica)', b'Postojna (Nova Gorica)')])),
                ('stevilka_proge', models.IntegerField(default=10, help_text=b'npr. 31', verbose_name=b'\xc5\xa0tevilka proge')),
                ('proga', models.CharField(help_text=b'npr. p. Celje', max_length=255)),
                ('tip_proge', models.CharField(default=b'Glavna', max_length=15, choices=[(b'Glavna', b'Glavna'), (b'Regionalna', b'Regionalna')])),
                ('odsek', models.CharField(help_text=b'npr. 510+010.10', max_length=255)),
                ('objekt_krizanja', models.CharField(help_text=b'npr. reka Sava', max_length=255, verbose_name=b'Objekt kri\xc5\xbeanja')),
                ('obremenjevanje_data', models.FloatField(null=True, verbose_name=b'Podatki o obremenjevanju', blank=True)),
                ('tip_objekta', models.CharField(default=b'Most', max_length=10, choices=[(b'Most', b'Most'), (b'Viadukt', b'Viadukt'), (b'Prepust', b'Prepust')])),
                ('tip_krizanja', models.CharField(default=b'Vodotok', max_length=100, verbose_name=b'Tip kri\xc5\xbeanja', choices=[(b'Vodotok', b'Vodotok'), (b'Vodotok in podvoz', b'Vodotok in podvoz'), (b'Potok', b'Potok'), (b'Podvoz', b'Podvoz'), (b'Podvoz, vodotok in krizni objekt', b'Podvoz, vodotok in kri\xc5\xbeni objekt'), (b'Meteorna voda', b'Meteorna voda'), (b'Inudacija', b'Inudacija'), (b'Inudacija in vodotok', b'Inudacija in vodotok'), (b'Inudacija, podvoz in vodotok', b'Inudacija, podvoz in vodotok')])),
                ('leto_gradnje', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1799), django.core.validators.MaxValueValidator(2015)])),
                ('leto_rekonstrukcije', models.CharField(help_text=b'1905, 1982', max_length=255, null=True, blank=True)),
                ('tip_konstrukcije', models.CharField(default=b'Painer nosilec', max_length=255, choices=[(b'Branasti nosilec', b'Branasti nosilec'), (b'Dvojni glavni polnostenski nosilec', b'Dvojni glavni polnostenski nosilec'), (b'Jeklen nosilec', b'Jeklen nosilec'), (b'Painer nosilec', b'Painer nosilec'), (b'Palicna konstrukcija', b'Pali\xc4\x8dna konstrukcija'), (b'Palicna locna konstrukcija', b'Pali\xc4\x8dna lo\xc4\x8dna konstrukcija'), (b'Palicni nosilec', 'Pali\u010dni nosilec'), (b'Palicni parabolicni nosilec', 'Pali\u010dni paraboli\u010dni nosilec'), (b'Plosca z vgrajenimi nosilci', 'Plo\u0161\u010da z vgrajenimi nosilci'), (b'Polnostenski nosilec', b'Polnostenski nosilec'), (b'Parabolicen polnostenski nosilec', 'Paraboli\u010den polnostenski nosilec'), (b'Prostolezeca plosca', b'Prostole\xc5\xbee\xc4\x8da plo\xc5\xa1\xc4\x8da'), (b'Skatlasti nosilec', b'\xc5\xa0katlasti nosilec'), (b'Sovprezna plosca z vgrajenimi nosilci', b'Sovpre\xc5\xbena plo\xc5\xa1\xc4\x8da z vgrajenimi nosilci'), (b'Sovprezna prednapeta konstrukcija', b'Sovpre\xc5\xbena prednapeta konstrukcija'), (b'Predalcje', b'Predal\xc4\x8dje')])),
                ('staticni_sistem', models.CharField(default=b'Prostolezeci nosilec', max_length=255, verbose_name=b'Stati\xc4\x8dni sistem', choices=[(b'Brana', b'Brana'), (b'Kontinuiran nosilec', b'Kontinuiran nosilec'), (b'Prostolezeci nosilec', b'Prostole\xc5\xbee\xc4\x8di nosilec'), (b'Prostolezeca konstrukcija', b'Prostole\xc5\xbee\xc4\x8da konstrukcija'), (b'Prostolezeca plosca', b'Prostole\xc5\xbee\xc4\x8da plo\xc5\xa1\xc4\x8da'), (b'Prostolezeca sovprezna plosca', b'Prostole\xc5\xbee\xc4\x8da sovpre\xc5\xbena plo\xc5\xa1\xc4\x8da'), (b'Prostolezeci polnostenski parabolicni nosilec', b'Prostole\xc5\xbee\xc4\x8di polnostenski paraboli\xc4\x8dni nosilec'), (b'Prostolezeci sovprezni nosilec', b'Prostole\xc5\xbee\xc4\x8di sovpre\xc5\xbeni nosilec')])),
                ('razpon', models.FloatField(default=0, help_text=b'v metrih!! npr. 165.10')),
                ('staticna_razpetina_po_odprtinah', models.CharField(help_text=b'v metrih!!! npr 2*5', max_length=255, null=True, verbose_name=b'Stati\xc4\x8dna razpetina po odprtinah', blank=True)),
                ('staticna_razpetina_po_poljih', models.CharField(help_text=b'v metrih!!! npr. 2*5,5', max_length=255, null=True, verbose_name=b'Stati\xc4\x8dna razpetina po poljih', blank=True)),
                ('material', models.CharField(default=b'Jeklo', max_length=255, choices=[(b'Jeklo', b'Jeklo'), (b'Jeklo in armirani beton', b'Jeklo in armirani beton'), (b'Jeklo in beton', b'Jeklo in beton')])),
                ('preostala_doba', models.CharField(max_length=255, null=True, blank=True)),
                ('dokumentacija', models.ManyToManyField(to='baza.Dokumentacija_vsa', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
