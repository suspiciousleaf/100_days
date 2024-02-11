# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# c:/Users/David/Documents/Programming/Python/Code_list/Projects/100_days/day_39_flight_tracker/day_39_flight_tracker_env/Scripts/Activate.ps1

from pprint import pprint

from flight_search import FlightSearch
from data_manager import DataManager

from notification_manager import NotificationManager

flight_search = FlightSearch()

notification_manager = NotificationManager()

data_manager = DataManager()
data_manager.get_destination_data()

for destination in data_manager.destination_data:
    if not destination["iataCode"]:
        try:
            destination["iataCode"] = flight_search.get_iata(destination["city"])
            data_manager.update_iata(destination)
        except:
            print(f"Cannot add IATA Code for {destination['city']}")

# destinations = [
#     {"city": "Paris", "iataCode": "PAR", "id": 2, "lowestPrice": 500},
#     {"city": "Berlin", "iataCode": "BER", "id": 3, "lowestPrice": 500},
#     {"city": "Tokyo", "iataCode": "TYO", "id": 4, "lowestPrice": 5000},
#     {"city": "Sydney", "iataCode": "SYD", "id": 5, "lowestPrice": 5000},
# ]

for destination in data_manager.destination_data:
    response = flight_search.find_flights(destination)
    if response["_results"]:
        # pprint(response)
        print(
            f'{response["data"][0]["cityFrom"]} to {response["data"][0]["cityTo"]}: € {response["data"][0]["price"]}'
        )
        notification_manager.send_sms(response)
        # break


# pprint(data_manager.destination_data)