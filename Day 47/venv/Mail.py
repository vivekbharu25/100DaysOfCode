import os
from dotenv import load_dotenv
import smtplib

load_dotenv()
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

print(EMAIL_ADDRESS)
print(SMTP_ADDRESS)

class Mailing:
    def mail(self):
        with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_ADDRESS,
                to_addrs="vivekbharu25@gmail.com",
                msg="Subject: New Price!\n\nThe PS5 is now below $500! Check it online."
            )