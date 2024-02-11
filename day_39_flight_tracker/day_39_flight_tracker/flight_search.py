import requests
from pprint import pprint
import datetime

from credentials import *

FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        pass

    def get_iata(self, city_name):
        search_slug = "locations/query"

        headers = {"apikey": FLIGHT_SEARCH_API_KEY}

        params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
            "limit": 1,
        }
        try:
            response = requests.get(
                url=f"{FLIGHT_SEARCH_ENDPOINT}{search_slug}",
                params=params,
                headers=headers,
            )
            response.raise_for_status()

            return response.json()["locations"][0]["code"]

        except Exception as e:
            print(f"An error occurred: {e}")
            print(f"{response.status_code = }")
            print(f"{response.text = }")

    def find_flights(self, destination):
        search_slug = "search"

        headers = {"apikey": FLIGHT_SEARCH_API_KEY}

        """You can also search using a radius. It needs to be in form lat-lon-xkm. The number of decimal places for radius is limited to 6.  E.g.-23.24--47.86-500km for places around Sao Paulo."""

        date_from = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime(
            "%d/%m/%Y"
        )
        date_to = (datetime.datetime.now() + datetime.timedelta(days=181)).strftime(
            "%d/%m/%Y"
        )

        params = {
            "fly_from": "LON",
            "fly_to": destination["iataCode"],
            "date_from": date_from,
            "date_to": date_to,
            "price_to": destination["lowestPrice"],
            "max_stopovers": 0,
            "locale": "en",
            "curr": "EUR",
            "limit": 2,
            "sort": "price",
        }
        try:
            response = requests.get(
                url=f"{FLIGHT_SEARCH_ENDPOINT}{search_slug}",
                params=params,
                headers=headers,
            )
            response.raise_for_status()

            return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")
            print(f"{response.status_code = }")
            print(f"{response.text = }")
