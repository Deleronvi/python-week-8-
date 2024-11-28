from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

def get_weather(request):
    if request.method == "POST":
        city = request.POST['city']
        api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != "404":
            main_data = data["main"]
            weather_data = data["weather"][0]
            context = {
                "city": city,
                "temperature": main_data["temp"],
                "description": weather_data["description"],
                "icon": weather_data["icon"],
            }
        else:
            context = {
                "error": "City not found"
            }

        return render(request, 'weather/index.html', context)

    return render(request, 'weather/index.html')
