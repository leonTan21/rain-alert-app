import requests
from datetime import datetime
from config import api_key, client, TO_NUMBER, FROM_NUMBER

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# Coordinates for your location
weather_params = {
    "lat": 39.799358,
    "lon": -89.643623,
    "appid": api_key,
    "cnt": 8,  # 8 * 3h = 24h forecast
    "units": "metric",  # or 'imperial' for °F
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

rain_hours = []

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:  # anything under 700 = rain, snow, drizzle, etc.
        # Get hour in local time (HH:MM)
        dt = datetime.fromtimestamp(hour_data["dt"])
        rain_hours.append(dt.strftime("%-I %p"))  # e.g., '3 PM'

# Build the message
if not rain_hours:
    summary = "It will not rain or snow today ☀️"
else:
    summary = f"It will rain or snow at {', '.join(rain_hours)} today ☔"

# Send via Twilio WhatsApp
message = client.messages.create(
    to=TO_NUMBER,
    from_=FROM_NUMBER,
    body=summary
)
