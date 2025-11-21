import requests
from twilio.rest import Client

ws_api_key = 'YOUR_OWN_API_KEY'
account_sid = 'YOUR_ACC_ID'
auth_token = "YOUR_OWN_AUTH_TOKEN"


parameters = {
    'access_key': ws_api_key,
    'query':'39.7579,-89.67971'
}

response = requests.get(url = "https://api.weatherstack.com/current", params=parameters)
print(response.status_code)
response.raise_for_status()

data = response.json()
current = data['current']
weather_id = current['weather_code']
weather_forecast = current['weather_descriptions']

if int(weather_id)>175:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Weak your Jackets, Have a Nice Day!",
        from_="your_number",
        to="your_number",
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:your_number',
        body="Weak your Jackets, Have a Nice Day!",
        to='whatsapp:your_number'
    )

    print(message.status)



