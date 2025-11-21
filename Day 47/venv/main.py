from Scraper import AmazonScrape
from Mail import Mailing

TARGET_PRICE = 500.0

scraper = AmazonScrape()
price = scraper.scrape()

mails = Mailing()

if price < TARGET_PRICE:
    mails.mail()
    print(f"Email sent! Price dropped to {price}")
else:
    print(f"No email sent. Current price: {price}")
