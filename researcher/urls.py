from django.conf.urls import *
from researcher.views import *

urlpatterns = patterns('',
                      url(r'$', create),
                      url(r'^create', create)
                      )