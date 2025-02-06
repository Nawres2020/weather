from django.shortcuts import render, redirect

from datetime import time, datetime

import requests


def index(request):
    return render(request, 'index.html')
def get_data(request):
    API_key = "3381b7db57c359dc59c051deb63a7a58"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Get the city name from the form
    city = request.GET.get("nawres", "")
    print(f"City entered: {city}")

    if not city:
        return render(request, 'index.html', {'error': 'Please enter a city name.'})

    print(f"City entered: {city}")  # Debugging

    # Build the API URL
    result_url = f"{base_url}appid={API_key}&q={city}&units=metric"
    print(f"API URL: {result_url}")  # Debugging

    # Fetch weather data
    weather_data = requests.get(result_url).json()

    print(f"API Response: {weather_data}")  # Debugging

    # Check for errors in the API response
    if weather_data.get("cod") != 200:
        return render(request, 'index.html', {'error': 'City not found or invalid API key.'})

    # Prepare context for the template
    context = {
        'main_temp': weather_data["main"]["temp"],
        'region': city,
        'country': weather_data["sys"]["country"],
        'min_temp': weather_data["main"]["temp_min"],
        'max_temp': weather_data["main"]["temp_max"],
        'wind': weather_data["wind"]["speed"],
        'updated_time': time(datetime.now().hour, datetime.now().minute),
    }
    return render(request, 'index.html', context)
