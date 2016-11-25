from about.models import Slika
from django.shortcuts import get_object_or_404, render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
def index(request):
	testis=Slika.objects.all()
	context={'slika',slika}		
	return render(request,'about/index.html',context)

#	return render(request,'about/index.html',{{}})
#    novice=Novica.objects.order_by('pub_date')[:5]
#    context = {'novice':novice}
#    try:
#       news=Novica.objects.get(pk=ime) 
#    return render(request, 'about/index.html',context)


