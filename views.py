from django.shortcuts import get_object_or_404, render_to_response
#from django.shortcuts import render
from django.http import HttpResponseRedirect
from baza.models import Most
# Create your views here.
#def index(request):
#	latest_most=Most.objects.order_by('-ime')[:5]
#	template=loader.get_tempate('baza/idenx.html')
#	context = RequestContext(request,{'latest_most':latest_most,})
#	output=', '.join([p.tip_proge for p in latest_most])
#	return HttpResponse(template.render(context))
import datetime

def index(request):
    mostovi=Most.objects.all()[:5]
    return render_to_response('baza/index.html',{'mostovi':mostovi})
