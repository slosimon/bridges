from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from haystack.views import SearchView, search_view_factory
from haystack.forms import HighlightedModelSearchForm
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mostovi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#   admin.site.site_header = 'Admin stran mostov'
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^baza/',include('baza.urls')),
    url(r'^login/',include('login.urls')),
    url(r'^admin_hidden/',include(admin.site.urls)),
    url(r'^baza/',include('baza.urls')),
#    url(r'^',include('home.urls')),
    url(r'^about/',TemplateView.as_view(template_name='about/index.html'),name='O nas'),
    url(r'^baza/iskanje/$', search_view_factory(view_class=SearchView, form_class=HighlightedModelSearchForm), name='Iskanje'),
    url(r'^',include('home.urls')),
#	url(r'^$','index',name='index'),
#    url(r'static/',name='static'),
#    url(r'media/',name='media'),
#    url(r'^/','mostovi.views.home',name='home'),
)

handler404='mostovi.views.handler404'
handler500='mostovi.views.handler500'
