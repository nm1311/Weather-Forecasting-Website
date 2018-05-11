import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=cdb1e35038472e39973e973e466d553e'


    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()


    form = CityForm()



    weather_data = []
    cities = City.objects.all()
    print(cities)

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']

        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/WeatherTemplate.html', context)

