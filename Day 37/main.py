import requests
from datetime import datetime

USERNAME = "vivekbharu25"
TOKEN = "qwert67890dytrh"
GRAPHID = "tst1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id":GRAPHID,
    "name":"Daily_Code",
    "unit":"Day",
    "type":"int",
    "color":"sora"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pix_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime.now()

pixel_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("Did you code? If yes type 1 else 0"),
}

response = requests.post(url=pix_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime("%Y%m%d")}"

update_params = {
    "quantity" : "4",
}

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)