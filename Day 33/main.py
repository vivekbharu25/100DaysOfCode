import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 39.757457
MY_LONG = -89.678668
TIMEZONE = "America/Chicago"

EMAIL = "yourmail@gmail.com"
PASSWORD = "app_password_from_google"



response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()["iss_position"]

iss_longitude = float(data["longitude"])
iss_latitude = float(data["latitude"])

def check_position():
    if abs(MY_LAT - iss_latitude)<=5 and abs(MY_LONG - iss_longitude)<=5:
        return True
    else:
        return False

def check_time(ctime,srtime, sstime):
    if ctime < srtime or ctime > sstime:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
    "tzid":TIMEZONE
}

response_here =requests.get(url = "http://api.sunrise-sunset.org/json", params=parameters)
response_here.raise_for_status()
data_here = response_here.json()
sunrise_here = int(data_here["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_here = int(data_here["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise_here, sunset_here)

current_now = datetime.now()
time_now = current_now.hour


while True:
    time.sleep(60)
    if check_position():
        if check_time(time_now,sunrise_here,sunset_here):
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=PASSWORD,
                    to_addrs="vivekbharu25@gmail.com",
                    msg=f"Subject:Check_Outside!\n\nISS is near you, Go Outside and Look Up!"
                )