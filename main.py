import requests
from api import api_key

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 39.799358,
    "long": -89.643623,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

print(weather_data)
