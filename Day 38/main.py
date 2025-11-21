import requests
from datetime import datetime

API_KEY = "Your API KEY"
APP_ID = 'Application ID'

nutrix_params = {
    'query' : input("What did you do?"),
    'weight_kg': 62,
    'height_cm' : 178,
    'age' : 23
}

nutrix_headers = {
    'x-app-id':APP_ID,
    'x-app-key':API_KEY,
}

today = datetime.now()
today_date = today.strftime("%x")
today_time = today.strftime("%X")

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                        json=nutrix_params, headers=nutrix_headers)

data = response.json()

sheety_link = "Your Sheety Link"

for exercise in data["exercises"]:
    sheety_params = {
        "workout" :{
            "date":today_date,
            "time":today_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }
    responsed = requests.post(url=sheety_link, json=sheety_params)
    print(responsed.text)