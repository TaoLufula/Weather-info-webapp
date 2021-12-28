from django.shortcuts import render
import urllib.request
import json
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        #'http://history.openweathermap.org/data/2.5/history/city?q=' +city+ 'CA&type=hour&start={start}&end={end}&appid={API key}
        source = urllib.request.urlopen('http://history.openweathermap.org/data/2.5/history/city?q=' + city + 
        'CA&appid=93248baefaecb815a9686b3b21d118af').read()

        data_list = json.loads(source)

        data = {
            "country_code": str(data_list['sys']['country']),
            "temp": str(data_list['main']['temp'])+ '°C',
            "main": str(data_list['weather'][0]['main']),
            "icon": data_list['weather'][0]['icon']
        }
        print(data)
    else:
        data = {}
    
    return render(request, "index.html", data)
