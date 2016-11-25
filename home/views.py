from django.shortcuts import get_object_or_404, render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from home.models import Novica
from baza.models import Most
from django.template import RequestContext  
import random
# Create your views here.
#def index(request):
#       latest_most=Most.objects.order_by('-ime')[:5]
#       template=loader.get_tempate('baza/idenx.html')
#       context = RequestContext(request,{'latest_most':latest_most,})
#       output=', '.join([p.tip_proge for p in latest_most])
#       return HttpResponse(template.render(context))
import datetime

def index(request):
    novice=Novica.objects.order_by('pub_date')[:10]
    slikce=Most.objects.order_by('?')
    context = {'novice':novice, 'slikce':slikce}
#    try:
#    	news=Novica.objects.get(pk=ime)	
    return render(request, 'home/index.html',context)

def lj(request):
    mostovi=Most.objects.filter(obmocje_SVP="Ljubljana")
    context = {'mostovi':mostovi}
    return render(request, 'home/pop123.html',context)

def ce(request):
    mostovi=Most.objects.filter(obmocje_SVP="Celje")
    context = {'mostovi':mostovi}
    return render(request, 'home/pop.html',context)

def mb(request):
    mostovi=Most.objects.filter(obmocje_SVP="Maribor")
    context = {'mostovi':mostovi}
    return render(request, 'home/pop13.html',context)

def po(request):
    mostovi=Most.objects.filter(obmocje_SVP="Postojna")
    context = {'mostovi':mostovi}
    return render(request, 'home/pop2.html',context)

def ce_lj(request):
    mostovi=Most.objects.filter(obmocje_SVP="Celje (Ljubljana)")
    context = {'mostovi':mostovi}
    return render(request, 'home/pop13.html',context)

def lj_ng(request):
    mostovi=Most.objects.filter(obmocje_SVP="Ljubljana (Nova Gorica)")
    context = {'mostovi':mostovi}
    return render(request, 'home/pop.html',context)

def lj_nm(request):
    mostovi=Most.objects.filter(obmocje_SVP="Ljubljana (Novo Mesto)")
    context = {'mostovi':mostovi}
    return render(request, 'home/pop.html',context)

def po_ng(request):
    mostovi=Most.objects.filter(obmocje_SVP="Postojna (Nova Gorica)")
    context = {'mostovi':mostovi}
    return render(request, 'home/pop.html',context)

def glavne(request):
	return render(request, 'home/glavne.html',{})

def regionalne(request):
	return render(request, 'home/regionalne.html',{})
