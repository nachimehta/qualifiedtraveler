from django.conf.urls import patterns, include, url
from qualifiedtraveler.views import *
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),

    #mainpage
    (r'^$', main_page),

    #login/logout
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),

    # Web portal.
    (r'^account/', include('researcher.urls')),

    #temp
    (r'^register/', include('tempreg.urls'))

)