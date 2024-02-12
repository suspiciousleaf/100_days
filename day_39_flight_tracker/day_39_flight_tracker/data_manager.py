import requests

from credentials import *


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = [
            {"city": "Paris", "iataCode": "PAR", "id": 2, "lowestPrice": 500},
            {"city": "Berlin", "iataCode": "BER", "id": 3, "lowestPrice": 500},
            {"city": "Tokyo", "iataCode": "TYO", "id": 4, "lowestPrice": 5000},
            {"city": "Sydney", "iataCode": "SYD", "id": 5, "lowestPrice": 5000},
        ]

    def get_destination_data(self, use_dummy_data=False):
        if not use_dummy_data:
            response = requests.get(SHEETY_ENDPOINT)
            data = response.json()
            self.destination_data = data["prices"]

    def update_iata(self, destination):
        data_to_update = {"price": {"iataCode": destination["iataCode"]}}
        url = f"{SHEETY_ENDPOINT}/{destination['id']}"

        try:
            response = requests.put(url, json=data_to_update)
            response.raise_for_status()

        except Exception as e:
            print(f"An error occurred: {e}")
            print(f"{response.status_code = }")
            print(f"{response.text = }")
