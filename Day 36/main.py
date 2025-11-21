import requests
import datetime
from twilio.rest import Client

today = datetime.date.today()

UP = "🔺"
DOWN = "🔻"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc."
STOCK_API_KEY = 'IBSGOVCZU3AP1LPD'
NEWS_API_KEY = 'STOCK_API_KEY '
account_sid = "account_sid"
auth_token = "auth_token"


stock_parameters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':STOCK_API_KEY
}

news_parameters = {
    'q':COMPANY_NAME,
    'from':'2025-02-10',
    # or 'from':today
    'sortBy':'popularity',
    'apiKey':NEWS_API_KEY
}


stock_response = requests.get(url='https://www.alphavantage.co/query',
                              params=stock_parameters)
print(stock_response.status_code)
stock_response.raise_for_status()
stock_data = stock_response.json()
print(stock_data)
present = int(list(stock_data['Time Series (Daily)'].values())[0]['4. close'])
past = int(list(stock_data['Time Series (Daily)'].values())[1]['4. close'])

percent_change = str(int((abs(present-past)/present)*100))

news_response = requests.get(url = 'https://newsapi.org/v2/everything',
                             params = news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
news_title = news_data['articles'][0]['title']
news_description = news_data['articles'][0]['description']
if present-past<0:
    start_word = percent_change + DOWN
else:
    start_word = percent_change + UP


final_news = (f"{STOCK}: {start_word}%\n"
              f"Headline: {news_title},\n"
              f"Brief: {news_description[0:100]}...")

client = Client(account_sid, auth_token)
message = client.messages.create(
        body=final_news,
        from_="contact_number",
        to="number",
)
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

