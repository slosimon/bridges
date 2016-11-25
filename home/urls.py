from django.conf.urls import patterns,url

from home import views

urlpatterns = patterns('',
				url(r'^SVP/ljubljana/$',views.lj, name='Ljubljana'),
				url(r'^SVP/maribor/$',views.mb, name='Maribor'),
				url(r'^SVP/celje/$',views.ce, name='Celje'),
				url(r'^SVP/postojna/$',views.po, name='Postojna'),
				url(r'^SVP/ljubljana-novo_mesto/$',views.lj_nm, name='Ljubljana (Novo Mesto)'),
				url(r'^SVP/ljubljana-nova_gorica/$',views.lj_ng, name='Ljubljana (Nova Gorica)'),
				url(r'^SVP/celje-ljubljana/$',views.ce_lj, name='Celje (Ljubljana)'),
				url(r'^SVP/postojna-nova_gorica/$',views.po_ng, name='Postojna (Nova Gorica)'),
				url(r'^glavne/$',views.glavne, name='Glavne proge'),
				url(r'^regionalne/$',views.regionalne, name='Regionalne proge'),
        url(r'^$',views.index, name='Baza mostov'),
)

