from django.conf.urls import patterns,url

from login import views
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
	url(r'^register/$',views.register, name='Registracija'),
	url(r'^$',views.user_login,name='Prijava'),
	url(r'^logout/$',views.user_logout, name='Odjava'),
	url(r'^sign_up/', views.register, name='Registriraj'),
    url(r'^register_success/', views.register, name='Uspesna registracija'),
    url(r'^confirm/(?P<activation_key>\w+)/', views.register_confirm, name='Potrditev registracije'),
)
