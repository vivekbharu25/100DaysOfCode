import requests

SHEETY_ENDPOINT = "https://api.sheety.co/b165a2a2d6a075603ea70fcb087b77ad/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url = f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)