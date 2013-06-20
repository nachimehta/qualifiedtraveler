from django.conf.urls import *
from tempreg.views import *

urlpatterns = patterns('',

    #researcher main page is the create experiment page for now
    (r'^$', create),
    (r'^exp', create_experiment),
    )