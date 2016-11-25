from django.conf.urls import patterns,url

from baza import views

urlpatterns = patterns('',
	url(r'^$',views.main, name='Mostovi'),
	url(r'^statistika/$',views.stats, name='Statistika'),
	url(r'^seznam/$',views.index, name='Baza mostov'),
	url(r'^dodaj_most/$',views.dodaj_most,name='Dodaj Most'),
   url(r'^most/(?P<most_id>[0-9]+)/$', views.most, name='Most'),
   url(r'^most/(?P<most_id>[0-9]+)/spremeni/$', views.spremeni, name='Spremeni most'),
   url(r'^most/(?P<most_id>[0-9]+)/izbrisi/$', views.brisi, name='Izbrisi most'),
   url(r'^most/(?P<most_id>[0-9]+)/izkaznica.pdf$', views.izkaznica, name='Izkaznica')
)
