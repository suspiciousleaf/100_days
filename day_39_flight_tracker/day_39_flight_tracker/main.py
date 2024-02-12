# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# c:/Users/David/Documents/Programming/Python/Code_list/Projects/100_days/day_39_flight_tracker/day_39_flight_tracker_env/Scripts/Activate.ps1
import datetime

from pprint import pprint

from flight_search import FlightSearch
from data_manager import DataManager

from notification_manager import NotificationManager

flight_search = FlightSearch()

notification_manager = NotificationManager()

data_manager = DataManager()
data_manager.get_destination_data(use_dummy_data=True)

for destination in data_manager.destination_data:
    if not destination["iataCode"]:
        try:
            destination["iataCode"] = flight_search.get_iata(destination["city"])
            data_manager.update_iata(destination)
        except:
            print(f"Cannot add IATA Code for {destination['city']}")


for destination in data_manager.destination_data:
    response = flight_search.find_flights(destination)
    if response["_results"]:
        # pprint(response)
        dep_date = datetime.datetime.fromtimestamp(
            response["data"][0]["route"][0]["dTimeUTC"]
        )
        ret_date = datetime.datetime.fromtimestamp(
            response["data"][0]["route"][1]["dTimeUTC"]
        )
        duration_raw = ret_date - dep_date
        duration = int(duration_raw.days + (duration_raw.seconds / 86400) + 0.5)
        print(
            f'{response["data"][0]["cityFrom"]} to {response["data"][0]["cityTo"]}: € {response["data"][0]["price"]}. {dep_date.strftime("%d/%m/%y")} - {ret_date.strftime("%d/%m/%y")}, {duration} days'
        )
        # notification_manager.send_sms(response)
        break


# pprint(data_manager.destination_data)
