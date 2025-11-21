##################### Extra Hard Starting Project ######################
import os
import smtplib
import datetime as dt
import random
import pandas as pd


EMAIL = "yourmail@gmail.com"
PASSWORD = "app_password_from_google"

# 1. Update the birthdays.csv
birthdays = pd.read_csv("birthdays.csv")
entry_name = input("Their Name: ")
if len(entry_name)>0:
    entry_email = input("their email: ")
    entry_bday = input("their Birthday(in YYYYMMDD): ")

    new_data = {"name":entry_name, "email":entry_email,
                "year":int(entry_bday[0:4]), "month":int(entry_bday[4:6]),
                "day":int(entry_bday[6:8])}
    birthdays = birthdays.append(new_data, ignore_index = True)
    birthdays.to_csv("birthdays.csv", index = False)
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_day = now.day
current_month = now.month

indicess = birthdays[(birthdays["month"]==current_month) & (birthdays["day"]==current_day)].index.tolist()

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

folder_path = "letter_templates"
files = os.listdir(folder_path)

files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

if files:
    random_file = random.choice(files)
    with open(os.path.join(folder_path, random_file), "r") as greeting:
        content = greeting.read()
    for i in indicess:
        new_file = content.replace("[NAME]",birthdays.loc[i,"name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=PASSWORD,
                to_addrs=birthdays.loc[i,"email"],
                msg=f"Subject:Greetings!\n\n{new_file}"
            )
# 4. Send the letter generated in step 3 to that person's email address.