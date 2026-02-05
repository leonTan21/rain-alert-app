import requests
from config import api_key, client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 39.799358,
    "lon": -89.643623,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
        break

if will_rain:
    message = client.messages.create(
        to="+12172802180",
        from_="+18445042644",
        body="It will rain ☔"
    )
