import datetime
from haystack import indexes
from baza.models import Most


class MostIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	ime = indexes.CharField(model_attr='ime')
	obmocje_SVP = indexes.CharField(model_attr='obmocje_SVP')
	stevilka_proge = indexes.CharField(model_attr='stevilka_proge')
	proga = indexes.CharField(model_attr='proga')
	tip_proge = indexes.CharField(model_attr='tip_proge')
	odsek=indexes.CharField(model_attr='odsek')
	objekt_krizanja=indexes.CharField(model_attr='objekt_krizanja')
	tip_objekta=indexes.CharField(model_attr='tip_objekta')
	tip_krizanja= indexes.CharField(model_attr='tip_krizanja')
	leto_gradnje = indexes.CharField(model_attr='leto_gradnje')
	tip_konstrukcije = indexes.CharField(model_attr='tip_konstrukcije')
	staticni_sistem = indexes.CharField(model_attr='staticni_sistem')
	razpon = indexes.CharField(model_attr='razpon')
	material = indexes.CharField(model_attr='material')
	
	def get_model(self):
		return Most

	def index_queryset(self, using=None):
		return self.get_model().objects.order_by('ime')
