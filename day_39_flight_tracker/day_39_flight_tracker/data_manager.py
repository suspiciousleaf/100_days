import requests

from credentials import *


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        self.destination_data

    def update_iata(self, destination):
        # for destination in self.destination_data:
        data_to_update = {"price": {"iataCode": destination["iataCode"]}}
        url = f"{SHEETY_ENDPOINT}/{destination['id']}"

        try:
            response = requests.put(url, json=data_to_update)
            response.raise_for_status()

        except Exception as e:
            print(f"An error occurred: {e}")
            print(f"{response.status_code = }")
            print(f"{response.text = }")
