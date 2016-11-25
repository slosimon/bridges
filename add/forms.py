# -*- coding: utf-8 -*-
from django import forms
from datetime import datetime
class Dodaj(forms.Form):
	ime = forms.TextField(max_length=255, help_text="npr. Most čez Savo")
	slika_od_spredaj=forms.ImageField()
	slika_od_strani=forms.ImageField()
	lokacija_sirina=forms.FloatField(default=46,validators=[MinValueValidator(42),MaxValueValidator(50)],verbose_name='Lokacija širina',help_text="Kopiraj iz Google maps prvo število (N) npr. 46.0000000")
	lokacija_dolzina=forms.FloatField(default=14,validators=[MinValueValidator(12),MaxValueValidator(20)],help_text="npr. 14.0000000",verbose_name='Lokacija dolžina')
	LJ='Ljubljana'
	CE='Celje'
	MB='Maribor'
	CE_LJ='Celje (Ljubljana)'
	LJ_NM='Ljubljana (Novo Mesto)'
	LJ_NG='Ljubljana (Nova Gorica)'
	PO ='Postojna'
	PO_NG='Postojna (Nova Gorica)'
	obmocje_choices =((LJ,'Ljubljana'),(CE,'Celje'),(MB,'Maribor'),(PO,'Postojna'),(CE_LJ,'Celje (Ljubljana)'),(LJ_NM,'Ljubljana (Novo mesto)'),(LJ_NG,'Ljubljana (Nova Gorica)'),(PO_NG,'Postojna (Nova Gorica)'))
	obmocje_SVP = forms.CharField(max_length=25,widget=forms.Select(choices=obmocje_choices),default=LJ,verbose_name='Območje SVP')
	G='Glavna'
	R='Regionalna'
	tip_proge_choices=((G,'Glavna'),(R,'Regionalna'))
	stevilka_proge = forms.IntegerField(default=10,help_text='npr. 31',verbose_name='Številka proge')
	proga = forms.TextField(max_length=255,help_text='npr. p. Celje')
	tip_proge = forms.CharField(max_length=15,widget=forms.Select(choices=tip_proge_choices),default=G)
	odsek=forms.TextField(max_length=255, help_text='npr. 510+010.10')
	km_posameznega_dela_objekta = forms.FloatField(help_text='npr.1')
	objekt_krizanja=forms.TextField(max_length=255, help_text='npr. reka Sava',verbose_name='Objekt križanja')
	obremenjevanje_data = forms.FloatField(required=False,verbose_name='Podatki o obremenjevanju')
	dokumentacija = forms.TextField(max_length=1000,required=False,help_text='npr. Glavni projekt')
	dokumentacija_datoteke = forms.FileField(required=False)
	Most='Most'
	Viadukt='Viadukt'
	Prepust='Prepust'
	tip_objekta_choices = ((Most,'Most'),(Viadukt,'Viadukt'),(Prepust,'Prepust'))
	tip_objekta=forms.CharField(max_length=10,widget=forms.Select(choices=tip_objekta_choices),default=Most)
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
        tip_krizanja= forms.CharField(max_length=100,widget=forms.Select(choices=tip_krizanja_choices),default=v,verbose_name='Tip križanja')
	a= 2015
#	leto_gradne2=forms.IntegerField(blank=True)
	leto_gradnje = forms.IntegerField(required=False,validators=[MinValueValidator(1799), MaxValueValidator(a)])
	b=(leto_gradnje)
	leto_rekonstrukcije = forms.TextField(required=False)
	bn='Branasti nosilec'
	dgpn='Dvojni glavni polnostenski nosilec'
	jn='Jeklen nosilec'
	pn='Painer nosilec'
	pk='Palicna konstrukcija'
	plk='Palicna ločna konstrukcija'
	pan='Palicni nosilec'
	ppn='Palicni parabolicni nosilec'
	pvn='Plosca z vgrajenimi nosilci'
	psn='Polnostenski nosilec'
	ppsn='Parabolicen polnostenski nosilec'
	pp='Prostolezeca plosca'
	sn='Skatlasti nosilec'
	spvn='Sovprezna plosca z vgrajenimi nosilci'
	spk='Sovprezna prednapeta konstrukcija'
	tip_konstrukcije_choices=((bn,'Branasti nosilec'),(dgpn,'Dvojni glavni polnostenski nosilec'),(jn,'Jeklen nosilec'),(pn,'Painer nosilec'),(pk,'Palična konstrukcija'),(plk,'Palična ločna konstrukcija'),(pan,u'Palični nosilec'),(ppn,u'Palični parabolični nosilec'),(pvn,u'Plošča z vgrajenimi nosilci'),(psn,'Polnostenski nosilec'),(ppsn,u'Paraboličen polnostenski nosilec'),(pp,'Prostoležeča plošča'),(sn,'Škatlasti nosilec'),(spvn,'Sovprežna plošča z vgrajenimi nosilci'),(spk,'Sovprežna prednapeta konstrukcija'))
	tip_konstrukcije = forms.CharField(max_length=255,widget=forms.Select(choices=tip_konstrukcije_choices),default=pn)
	b='Brana'
	kn='Kontinuiran nosilec'
	pno='Prostolezeci nosilec'
	pko='Prostolezeca konstrukcija'
	ppl='Prostolezeca plosca'
	psp='Prostolezeca sovprezna plosca'
	pppn='Prostolezeci polnostenski parabolicni nosilec'
	psno='Prostolezeci sovprezni nosilec'
	staticni_sistem_choices=((b,'Brana'),(kn,'Kontinuiran nosilec'),(pno,'Prostoležeči nosilec'),(pko,'Prostoležeča konstrukcija'),(ppl,'Prostoležeča plošča'),(psp,'Prostoležeča sovprežna plošča'),(pppn,'Prostoležeči polnostenski parabolični nosilec'),(psno,'Prostoležeči sovprežni nosilec'))
	staticni_sistem = forms.CharField(max_length=255, widget=forms.Select(choices=staticni_sistem_choices),default=pno,verbose_name='Statični sistem')
	razpon = forms.FloatField(default =0,help_text='v metrih!! npr. 165.10')
	staticna_razpetina_po_odprtinah = forms.TextField(max_length=255,help_text='v metrih!!! npr 2*5',required=False,verbose_name='Statična razpetina po odprtinah')
	staticna_razpetina_po_poljih= forms.TextField(max_length=255,help_text='v metrih!!! npr. 2*5,5',required=False,verbose_name='Statična razpetina po poljih')
	jeklo='Jeklo'
	jeklobeton='Jeklo in beton'
	jekloarmatura='Jeklo in armirani beton'
	material_choices=((jeklo,'Jeklo'),(jekloarmatura,'Jeklo in armirani beton'),(jeklobeton,'Jeklo in beton'))
	material = forms.CharField(max_length=255, widget=forms.Select(choices=material_choices), default=jeklo)
	preostala_doba=forms.TextField(required=False)
		
