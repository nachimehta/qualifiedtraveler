from django.conf.urls import *
from researcher.views import *

urlpatterns = patterns('',

    #researcher main page is the create experiment page for now
    (r'^$', researcher_main_page),
    #(r'^create', create),
    (r'^create2', create2),
    (r'^exp', create_experiment),
    )