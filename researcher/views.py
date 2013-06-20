from django.http import HttpResponse
from django.shortcuts import render_to_response
from xml.etree import ElementTree as ET
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User
from researcher.forms import ExperimentForm


@login_required
def researcher_main_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    variables = RequestContext(request, {'user': request.user})
    return render_to_response('researcher/index.html', variables)


@login_required
#show survey page
def create(request):
    variables = RequestContext(request, {'user': request.user})
    return render_to_response('researcher/create.html', variables)

@login_required
def create2(request):
    form = ExperimentForm()
    variables = RequestContext(request, {'user': request.user, 'form': form})
    return render_to_response('researcher/create2.html', variables)

#create xml file from survey
@csrf_exempt
def create_experiment(request):
    if request.method == 'POST':

        def dateformat(datadict):
            month = datadict['month'][0]
            day = datadict['day'][0]
            year = datadict['year'][0]
            hour = datadict['hour'][0]

            if datadict['ampm'][0] == 'pm':
                hourint = int(hour) + 12
                if (hourint == 24):
                    hourint = 12
                hour = str(hourint)

            elif datadict['ampm'][0] == 'am' and hour == '12':
                hour = '0'

            datetime = '20' + year + '-'
            if len(month) < 2:
                month = '0' + month
            if len(day) < 2:
                day = '0' + day
            if len(hour) < 2:
                hour = '0' + hour

            datetime = datetime + month + '-' + day + 'T' + hour + ':00:00"'

            return datetime

        def weekdays(datadict):
            result = ''
            for w in datadict['weekdays']:
                result += '<byweekday weekdays="' + w + '"/>'

            return result

        def users(datadict):
            result = ''
            for u in datadict['user']:
                result += '<user id="' + u + '"/>'

            return result

        formdata = request.POST['data']
        fdict = dict()

        for u in formdata.split('&'):
            k = u.split('=')[0]
            v = u.split('=')[1]
            if k in fdict:
                fdict[k].append(v)
            else:
                fdict[k] = [v]

        xmlstr = '<researcher adminIdent="' + fdict['researcher'][0] + '"><survey XFormID="' + fdict['survey'][
            0] + '"><trigger><timeTrigger><time datetime="'
        xmlstr = xmlstr + dateformat(fdict) + '/><recur><freq count="' + fdict['repeats'][0] + '"><DAILY>"' + weekdays(fdict)
        xmlstr = xmlstr + '</DAILY></freq></recur></timeTrigger></trigger>' + users(fdict) + '</survey></researcher>'

        tree = ET.XML(xmlstr)

        #This is where Hoang takes over
        with open("XLM.xml", "w") as f:
            f.write(ET.tostring(tree))

    return HttpResponse("Data Submitted")
