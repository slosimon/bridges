from __future__ import print_function
from django.shortcuts import get_object_or_404, render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from baza.models import Most, Dokumentacija_vsa
from django.contrib.auth.decorators import login_required
from baza.forms import MostForm
from django.forms.models import modelformset_factory
from django.template import RequestContext
from django.db.models import Avg
from math import ceil
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from subprocess import Popen, PIPE
import tempfile
import urllib
import subprocess
import datetime
import warnings as _warnings
import os 
from tempfile import mkdtemp
import shutil
import tempfile
from django.template.loader import render_to_string
from django.shortcuts import redirect

class TemporaryDirectory(object):
    def __enter__(self):
        self.name = tempfile.mkdtemp()
        return self.name

    def __exit__(self, exc_type, exc_value, traceback):
        shutil.rmtree(self.name)
        
def index(request):
    mostovi=Most.objects.order_by('obmocje_SVP')
    context = {'mostovi':mostovi}
    return render(request, 'baza/index.html',context)

@login_required    
def dodaj_most(request):
	context=RequestContext(request)
	if request.method=='POST':
		formset=MostForm(request.POST)
		if formset.is_valid():
			formset.save(commit=True)
			return index(request)
	else:
		formset=MostForm()
	return render_to_response("baza/dodaj_most.html",{'formset':formset},context)

def most(request, most_id):
    most = get_object_or_404(Most, pk=most_id)
    docs=most.dokumentacija.all()
    leta=most.leto_rekonstrukcije_nov.all()
    return render(request, 'baza/most.html', {'most': most,'docs':docs,'leta':leta})
    
@login_required
def spremeni(request, most_id):
	element=get_object_or_404(Most, pk=most_id)
	if request.method=='POST':
		form=MostForm(request.POST,instance=element)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
	else:
		form=MostForm(instance=element)
	return render_to_response("baza/spremeni_most.html", {'form': form,}, context_instance=RequestContext(request))
@login_required	
def brisi(request, most_id):
	element=get_object_or_404(Most, pk=most_id).delete()
	if request.method=='POST':
		form=MostForm(request.POST,instance=element)
		if form.is_valid():
			Most.objects.filter(pk=most_id).delete()
			return index(request)
	else:
		form=MostForm(instance=element)
	return render_to_response("baza/brisi.html", {'form': form,}, context_instance=RequestContext(request))
	
def main(request):
	mostovi=Most.objects.order_by('obmocje_SVP')
	context = {'mostovi':mostovi}
	return render(request, 'baza/main.html',context)
	
def stats(request):
	mostovi=Most.objects.order_by('obmocje_SVP')
	lj=Most.objects.filter(obmocje_SVP="Ljubljana")
	mb=Most.objects.filter(obmocje_SVP="Maribor")
	ce=Most.objects.filter(obmocje_SVP="Celje")
	po=Most.objects.filter(obmocje_SVP="Postojna")
	celj=Most.objects.filter(obmocje_SVP="Celje (Ljubljana)")
	ljnm=Most.objects.filter(obmocje_SVP="Ljubljana (Novo Mesto)")
	ljng=Most.objects.filter(obmocje_SVP="Ljubljana (Nova Gorica)")
	pong=Most.objects.filter(obmocje_SVP="Postojna (Nova Gorica)")
	gl=Most.objects.filter(tip_proge="Glavna")
	reg=Most.objects.filter(tip_proge="Regionalna")
	va=Most.objects.filter(tip_krizanja="Vodotok")
	vpa=Most.objects.filter(tip_krizanja="Vodotok in podvoz")
	pota=Most.objects.filter(tip_krizanja="Potok")
	poda=Most.objects.filter(tip_krizanja="Podvoz")
	pvka=Most.objects.filter(tip_krizanja="Podvoz, vodotok in krizni objekt")
	mva=Most.objects.filter(tip_krizanja="Meteorna voda")
	inua=Most.objects.filter(tip_krizanja="Inudacija")
	iva=Most.objects.filter(tip_krizanja="Inudacija in vodotok")
	ipva=Most.objects.filter(tip_krizanja="Inudacija, podvoz in vodotok")
	ave_age=(Most.objects.all().aggregate(Avg('leto_gradnje')))
	bna=Most.objects.filter(tip_konstrukcije='Branasti nosilec')
	dgpna=Most.objects.filter(tip_konstrukcije='Dvojni glavni polnostenski nosilec')
	jna=Most.objects.filter(tip_konstrukcije='Jeklen nosilec')
	pna=Most.objects.filter(tip_konstrukcije='Painer nosilec')
	pkka=Most.objects.filter(tip_konstrukcije='Palicna konstrukcija')
	plka=Most.objects.filter(tip_konstrukcije='Palicna locna konstrukcija')
	pana=Most.objects.filter(tip_konstrukcije='Palicni nosilec')
	ppna=Most.objects.filter(tip_konstrukcije='Palicni parabolicni nosilec')
	pvna=Most.objects.filter(tip_konstrukcije='Plosca z vgrajenimi nosilci')
	psna=Most.objects.filter(tip_konstrukcije='Polnostenski nosilec')
	ppsna=Most.objects.filter(tip_konstrukcije='Parabolicen polnostenski nosilec')
	ppa=Most.objects.filter(tip_konstrukcije='Prostolezeca plosca')
	sna=Most.objects.filter(tip_konstrukcije='Skatlasti nosilec')
	spvna=Most.objects.filter(tip_konstrukcije='Sovprezna plosca z vgrajenimi nosilci')
	spka=Most.objects.filter(tip_konstrukcije='Sovprezna prednapeta konstrukcija')
	predaa=Most.objects.filter(tip_konstrukcije='Predalcje')
	ba=Most.objects.filter(staticni_sistem='Brana')
	kna=Most.objects.filter(staticni_sistem='Kontinuiran nosilec')
	pnoa=Most.objects.filter(staticni_sistem='Prostolezeci nosilec')
	pkoa=Most.objects.filter(staticni_sistem='Prostolezeca konstrukcija')
	ppla=Most.objects.filter(staticni_sistem='Prostolezeca plosca')
	pspa=Most.objects.filter(staticni_sistem='Prostolezeca sovprezna plosca')
	pppna=Most.objects.filter(staticni_sistem='Prostolezeci polnostenski parabolicni nosilec')
	psnoa=Most.objects.filter(staticni_sistem='Prostolezeci sovprezni nosilec')
	ave_razpon=(Most.objects.all().aggregate(Avg('razpon')))
	context = {'ave_razpon':ave_razpon, 'ba':ba, 'kna':kna, 'pnoa':pnoa, 'pkoa':pkoa, 'ppla':ppla, 'pspa':pspa, 'pppna':pppna, 'psnoa':psnoa,'sna':sna, 'spvna':spvna, 'spka':spka, 'predaa':predaa, 'bna':bna, 'dgpna':dgpna, 'jna':jna, 'pna':pna, 'pkka':pkka, 'plka':plka, 'pana':pana, 'ppna':ppna, 'pvna':pvna, 'psna':psna, 'ppsna':ppsna, 'ppa':ppa, 'mostovi':mostovi, 'ave_age':ave_age, 'lj':lj, 'mb':mb, 'ce':ce, 'po':po, 'celj':celj, 'ljnm':ljnm, 'ljng':ljng, 'pong':pong, 'gl':gl, 'reg':reg, 'va':va, 'vpa':vpa, 'pota':pota, 'poda':poda, 'pvka':pvka, 'mva':mva, 'inua':inua, 'iva':iva, 'ipva':ipva}
	return render(request, 'baza/statistika.html',context)

def izkaznica(request, most_id):
	process=subprocess.call(['sudo', 'rmdir', '-r', '/var/www/media/izkaznica/tmp*'])
	entry = get_object_or_404(Most, pk=most_id)
	leta=entry.leto_rekonstrukcije_nov.all()
	context = Context({
			'entry': entry, 'leta':leta
		})
	if entry.glavna_slika:
		if ((entry.glavna_slika.width*1.0)/(entry.glavna_slika.height*1.0)<(0.5)):
			template = get_template('baza/izkaznica.tex')
		else:
			template = get_template('baza/izkaznicav.tex')
	else:
		template = get_template('baza/izkaznicav.tex')
	tempor="/var/www/media/izkaznica"
	if not os.path.exists(tempor):
		os.makedirs(tempor)
	tempdir=tempfile.mkdtemp(dir=tempor)
	os.chmod(tempdir,0777)
	urllib.urlretrieve("http://pokreativnipoti.fgg.uni-lj.si/media/faks.png", tempdir+"/faks.png")
	urllib.urlretrieve("http://pokreativnipoti.fgg.uni-lj.si/media/logo-sklad.jpg", tempdir+"/logo-sklad.jpg")
	urllib.urlretrieve("http://pokreativnipoti.fgg.uni-lj.si/media/logo-fgg.jpg", tempdir+"/logo-fgg.jpg")
	if entry.glavna_slika:
		urllib.urlretrieve(entry.glavna_slika.url, tempdir+"/most.jpg")
	else:
		urllib.urlretrieve("http://pokreativnipoti.fgg.uni-lj.si/media/slike-ni.jpg", tempdir+"/most.jpg")
	link="https://maps.googleapis.com/maps/api/staticmap?center=Slovenija=13&size=600x300&maptype=roadmap&markers=color:red|label:Most|"
	link+=str(entry.lokacija_sirina)
	link+=","
	link+=str(entry.lokacija_dolzina)
	urllib.urlretrieve(link, tempdir+"/mapa.png")
	os.chmod(tempdir+"/faks.png",0777)
	os.chmod(tempdir+"/logo-sklad.jpg",0777)
	os.chmod(tempdir+"/logo-fgg.jpg",0777)
	os.chmod(tempdir+"/most.jpg",0777)
	os.chmod(tempdir+"/mapa.png",0777)
	rendered_tpl = template.render(context).encode('utf-8')
	f = open(tempdir+"/izkaznica.tex","w")
	f.write(rendered_tpl)
	f.close()
	os.chmod(tempdir+"/izkaznica.tex",0777)
	open(tempdir+"/izkaznica.aux","w").close()
	open(tempdir+"/izkaznica.log","w").close()
	open(tempdir+"/izkaznica.out","w").close()
	open(tempdir+"/izkaznica.pdf","w").close()
	open(tempdir+"/missfont.log","w").close()
	for i in range(2):
		cmd1 = 'cd '+tempdir 
		cmd2 = 'pdflatex izkaznica.tex -output-directory='+tempdir
		process = subprocess.Popen("{}; {}".format(cmd1, cmd2), shell=True, stdout=subprocess.PIPE)
		#process.communicate(rendered_tpl)
		os.chmod(tempdir+"/izkaznica.aux",0777)
		os.chmod(tempdir+"/izkaznica.out",0777)
		os.chmod(tempdir+"/izkaznica.log",0777)
		os.chmod(tempdir+"/missfont.log",0777)
		os.chmod(tempdir+"/izkaznica.pdf",0777)
	os.chmod(tempdir+"/izkaznica.pdf",0777)
	with open(os.path.join(tempdir, 'izkaznica.pdf'), 'rb') as f:
		pdf = f.read()
	r = HttpResponse(content_type='application/pdf')
	r.write(pdf)
	s="http://pokreativnipoti.fgg.uni-lj.si/media/izkaznica"
	for j in range(len(tempdir)-len(tempor)):
		s=s+tempdir[len(tempor)+j]
	s+="/izkaznica.pdf"
	return render(request, 'baza/redir.html',{'link':s})

	

