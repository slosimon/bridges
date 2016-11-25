from django.contrib import admin
from baza.models import Most, Dokumentacija_vsa, Leto
#from related_m2m.models import Most, Dokumentacija_vsa

# Register your models here.
admin.site.register(Dokumentacija_vsa)
admin.site.register(Leto)
admin.site.register(Most)

