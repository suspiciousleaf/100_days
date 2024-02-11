# c:/Users/David/Documents/Programming/Python/Code_list/Projects/100_days/day_35/day_35_env/Scripts/Activate.ps1

import requests
from twilio.rest import Client
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

will_rain = False

for hour in weather["hourly"][:12]:
    if hour["weather"][0]["id"] < 700:
        will_rain = True


if will_rain:
    print("Rain incoming!")

    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Remember to pack an umbrella!",
        from_=twilio_number,
        to=my_number,
    )
else:
    print("No rain today")

    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="No rain today",
        from_=twilio_number,
        to=my_number,
    )


print(message.status)
