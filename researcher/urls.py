from django.conf.urls import *
from researcher.views import *

urlpatterns = patterns('',

                      #researcher main page is the create experiment page for now
                      url(r'^$', researcher_main_page),
                      url(r'^exp', create_experiment),
                      )