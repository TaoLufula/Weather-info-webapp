import json
from django.shortcuts import render
import urllib.request
# Create your views here.

def index(request):
    if request.method == 'POST':
        dt = request.POST['dt']

        # Users will have to provide the unix timestamps for the 5 previous days. five calls will be perfomed, one for each timestamp.
        #API key can be obtained from https://openweathermap.org/api

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=75.69&lon=45.42&dt='+ dt + '&units=metric&appid=???????').read()         
        data_list = json.loads(source)
        data = {
            "temp": str(data_list['hourly'][0]['temp'])+ '°C',
            "timezone":str(data_list['timezone']), 
        }
        print(data)
    else:
        data = {}
    return render(request, "index.html", data)
