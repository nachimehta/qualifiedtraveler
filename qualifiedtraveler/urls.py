from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qualifiedtraveler.views.home', name='home'),
    # url(r'^qualifiedtraveler/', include('qualifiedtraveler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'$', TemplateView.as_view(template_name='researcher/login.html'), name="login"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create/', 'researcher.views.create'),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'researcher/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^account/', include('researcher.urls')),
)
