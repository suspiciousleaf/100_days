# c:/Users/David/Documents/Programming/Python/Code_list/Projects/100_days/day_35/day_35_env/Scripts/Activate.ps1

import requests
from credentials import *
from pprint import pprint

OWM_endpoint = f"https://api.openweathermap.org/data/3.0/onecall"

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

weather_raw = requests.get(OWM_endpoint, params=weather_params)

try:
    weather_raw.raise_for_status()
except Exception as e:
    print("\n", e, "\n", sep="")

weather = weather_raw.json()

for i, hour in enumerate(weather["hourly"]):
    if i < 12:
        if hour["weather"][0]["id"] < 700:
            print("Rain incoming!")
            break

# Video 4, 7:45
