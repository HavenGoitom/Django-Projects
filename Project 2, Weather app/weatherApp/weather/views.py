from django.shortcuts import render
import datetime
import requests
# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indore'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=11e926b77a1697b196e80114f7f636c3'
    PARAMS = {'units': 'metric'}
    
    data = requests.get(url, PARAMS).json()
    print(data)

    # 🛑 error check
    if 'weather' not in data:
        context = {'error': data.get('message', 'Something went wrong')}
        return render(request, 'index.html', context)

    descripion = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    day = datetime.date.today()

    context = {
        'city': city,
        'descripion': descripion,
        'icon': icon,
        'temp': temp,
        'day': day,
    }
    return render(request, 'index.html', context)
