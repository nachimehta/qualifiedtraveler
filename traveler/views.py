from django.http import HttpResponse
from django.shortcuts import render_to_response
from xml.etree import ElementTree as ET
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
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
            if (len(month) < 2):
                month = '0' + month
            if (len(day) < 2):
                day = '0' + day
            if (len(hour) < 2):
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

        xmlstr = '<administrator adminIdent="' + fdict['administrator'][0] + '"><survey XFormID="' + fdict['survey'][
            0] + '"><trigger><timeTrigger><time datetime="'
        xmlstr = xmlstr + dateformat(fdict) + '/><recur><freq count="' + fdict['repeats'][0] + '"><DAILY>"' + weekdays(fdict)
        xmlstr = xmlstr + '</DAILY></freq></recur></timeTrigger></trigger>' + users(fdict) + '</survey></administrator>'

        print xmlstr

        tree = ET.XML(xmlstr)

        with open("XLM.xml", "w") as f:
            f.write(ET.tostring(tree))

    return HttpResponse("Data Submitted")
