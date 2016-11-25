# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from time import gmtime, strftime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
from django.template.defaultfilters import slugify
from home.models import Grafi

# Create your models here.
class Dokumentacija_vsa(models.Model):
	ime_dokumenta=models.CharField(help_text="Javno ime dokumenta npr. Tloris", max_length=255)
	dokument=models.FileField()
	je_javni=models.BooleanField(default=True)
	def __unicode__(self):
		return self.ime_dokumenta

class Leto(models.Model):
	leto=models.IntegerField(help_text="Leto rekonstrukcije")
	def __unicode__(self):
		return unicode(self.leto)

class Most(models.Model):
	ime = models.CharField(max_length=255, help_text="npr. Most čez Savo")
#	slika_od_spredaj=models.ImageField(blank=True)
#	slika_od_strani=models.ImageField(blank=True)
	slike=models.FileField(null=True,help_text="Slike spravite v arhiv (ZIP, 7Z, TAR.GZ ali kaj podobnega), sliko, katero pa želite na izkaznici pa poimenujte v main.jpg ali katerakoli druga končnica, nobena druga slika pa ne sme imeti imena main in karkoli drugo naprej (It's temporary)", verbose_name='Slike stisnjene v eno datoteko', blank=True)
	glavna_slika=models.ImageField(null=True, blank=True,help_text="Slika, katero želite, da bodo obiskovalci videli na strani in na izkaznici, ostale pa bodo lahko dobili z downloadom, zaradi velikosti strani (počasno nalaganje)")
	lokacija_sirina=models.FloatField(default=46,validators=[MinValueValidator(42),MaxValueValidator(50)],verbose_name='Lokacija širina',help_text="Kopiraj iz Google maps prvo število (N) npr. 46.0000000")
	lokacija_dolzina=models.FloatField(default=14,validators=[MinValueValidator(12),MaxValueValidator(20)],help_text="npr. 14.0000000",verbose_name='Lokacija dolžina')
	LJ='Ljubljana'
	CE='Celje'
	MB='Maribor'
	CE_LJ='Celje (Ljubljana)'
	LJ_NM='Ljubljana (Novo mesto)'
	LJ_NG='Ljubljana (Nova Gorica)'
	PO ='Postojna'
	PO_NG='Postojna (Nova Gorica)'
	obmocje_choices =((LJ,'Ljubljana'),(CE,'Celje'),(MB,'Maribor'),(PO,'Postojna'),(CE_LJ,'Celje (Ljubljana)'),(LJ_NM,'Ljubljana (Novo mesto)'),(LJ_NG,'Ljubljana (Nova Gorica)'),(PO_NG,'Postojna (Nova Gorica)'))
	obmocje_SVP = models.CharField(max_length=25,choices=obmocje_choices,default=LJ,verbose_name='Območje SVP')
	G='Glavna'
	R='Regionalna'
	tip_proge_choices=((G,'Glavna'),(R,'Regionalna'))
	stevilka_proge = models.IntegerField(default=10,help_text='npr. 31',verbose_name='Številka proge')
	proga = models.CharField(max_length=255,help_text='npr. p. Celje')
	tip_proge = models.CharField(max_length=15,choices=tip_proge_choices,default=G)
	odsek=models.CharField(max_length=255, help_text='npr. 510+010.10')
#	km_posameznega_dela_objekta = models.FloatField(blank=True,help_text='npr.1',null=True)
	objekt_krizanja=models.CharField(max_length=255, help_text='npr. reka Sava',verbose_name='Objekt križanja')
	obremenjevanje_data = models.FloatField(blank=True,verbose_name='Podatki o obremenjevanju',null=True)
	Most='Most'
	Viadukt='Viadukt'
	Prepust='Prepust'
	tip_objekta_choices = ((Most,'Most'),(Viadukt,'Viadukt'),(Prepust,'Prepust'))
	tip_objekta=models.CharField(max_length=10,choices=tip_objekta_choices,default=Most)
	v='Vodotok'
	vp='Vodotok in podvoz'
	pot='Potok'
	pod ='Podvoz'
	pvk='Podvoz, vodotok in krizni objekt'
        mv='Meteorna voda'
        i='Inudacija'
        iv ='Inudacija in vodotok'
	ipv = 'Inudacija, podvoz in vodotok'
        tip_krizanja_choices=((v,'Vodotok'),(vp,'Vodotok in podvoz'),(pot,'Potok'),(pod,'Podvoz'),(pvk,'Podvoz, vodotok in križni objekt'),(mv,'Meteorna voda'),(i,'Inudacija'),(iv,'Inudacija in vodotok'),(ipv,'Inudacija, podvoz in vodotok'))
        tip_krizanja= models.CharField(max_length=100,choices=tip_krizanja_choices,default=v,verbose_name='Tip križanja')
	a= 2015
#	leto_gradne2=models.IntegerField(blank=True)
	leto_gradnje = models.IntegerField(blank= True,validators=[MinValueValidator(1799), MaxValueValidator(a)],null=True)
	b=(leto_gradnje)
#	leto_rekonstrukcije = models.CharField(max_length=255,blank=True,help_text='1905, 1982',null=True)
	leto_rekonstrukcije_nov = models.ManyToManyField(Leto, blank=True, help_text="Leta rekonstrukcije")
	bn='Branasti nosilec'
	dgpn='Dvojni glavni polnostenski nosilec'
	jn='Jeklen nosilec'
	pn='Painer nosilec'
	pkk='Palicna konstrukcija'
	plk='Palicna locna konstrukcija'
	pan='Palicni nosilec'
	ppn='Palicni parabolicni nosilec'
	pvn='Plosca z vgrajenimi nosilci'
	psn='Polnostenski nosilec'
	ppsn='Parabolicen polnostenski nosilec'
	pp='Prostolezeca plosca'
	sn='Skatlasti nosilec'
	spvn='Sovprezna plosca z vgrajenimi nosilci'
	spk='Sovprezna prednapeta konstrukcija'
	preda='Predalcje'
	tip_konstrukcije_choices=((bn,'Branasti nosilec'),(dgpn,'Dvojni glavni polnostenski nosilec'),(jn,'Jeklen nosilec'),(pn,'Painer nosilec'),(pkk,'Palična konstrukcija'),(plk,'Palična ločna konstrukcija'),(pan,u'Palični nosilec'),(ppn,u'Palični parabolični nosilec'),(pvn,u'Plošča z vgrajenimi nosilci'),(psn,'Polnostenski nosilec'),(ppsn,u'Paraboličen polnostenski nosilec'),(pp,'Prostoležeča plošča'),(sn,'Škatlasti nosilec'),(spvn,'Sovprežna plošča z vgrajenimi nosilci'),(spk,'Sovprežna prednapeta konstrukcija'),(preda,'Predalčje'))
	tip_konstrukcije = models.CharField(max_length=255,choices=tip_konstrukcije_choices,default=pn)
	b='Brana'
	kn='Kontinuiran nosilec'
	pno='Prostolezeci nosilec'
	pko='Prostolezeca konstrukcija'
	ppl='Prostolezeca plosca'
	psp='Prostolezeca sovprezna plosca'
	pppn='Prostolezeci polnostenski parabolicni nosilec'
	psno='Prostolezeci sovprezni nosilec'
	staticni_sistem_choices=((b,'Brana'),(kn,'Kontinuiran nosilec'),(pno,'Prostoležeči nosilec'),(pko,'Prostoležeča konstrukcija'),(ppl,'Prostoležeča plošča'),(psp,'Prostoležeča sovprežna plošča'),(pppn,'Prostoležeči polnostenski parabolični nosilec'),(psno,'Prostoležeči sovprežni nosilec'))
	staticni_sistem = models.CharField(max_length=255, choices=staticni_sistem_choices,default=pno,verbose_name='Statični sistem')
	razpon = models.FloatField(default =0,help_text='v metrih!! npr. 165.10', verbose_name="Dolžina mostu")
	staticna_razpetina_po_odprtinah = models.CharField(max_length=255,help_text='v metrih!!! npr 2*5',blank=True,null=True,verbose_name='Statična razpetina po odprtinah')
	staticna_razpetina_po_poljih= models.CharField(max_length=255,help_text='v metrih!!! npr. 2*5,5',blank=True,null=True,verbose_name='Statična razpetina po poljih')
	jeklo='Jeklo'
	jeklobeton='Jeklo in beton'
	jekloarmatura='Jeklo in armirani beton'
	material_choices=((jeklo,'Jeklo'),(jekloarmatura,'Jeklo in armirani beton'),(jeklobeton,'Jeklo in beton'))
	material = models.CharField(max_length=255, choices=material_choices, default=jeklo)
	preostala_doba=models.CharField(max_length=255,blank=True,null=True)
	dokumentacija=models.ManyToManyField(Dokumentacija_vsa,blank=True)
	grafi=models.ManyToManyField(Grafi,blank=True)
	besedilo_za_izkaznico=models.CharField(max_length=1000,blank=True, null=True)
	valid=models.BooleanField(verbose_name="Podatki so preverjeni", default=False)
	def __unicode__(self):
		return self.ime
