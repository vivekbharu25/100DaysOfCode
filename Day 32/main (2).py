import smtplib
import datetime as dt
import random

my_email = "yourmail@gmail.com"
password = "app_password_from_google"

now = dt.datetime.now()
current_day = now.weekday()

with open("quotes.txt","r") as quote:
    quotes = quote.readlines()

if current_day == 0:
    one_quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                from_addr=my_email,
                to_addrs="1stopfest@gmail.com",
                msg=f"Subject:Yo!\n\n{one_quote}"
            )


