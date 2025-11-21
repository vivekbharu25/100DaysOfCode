import requests
from bs4 import BeautifulSoup

class AmazonScrape:
    def __init__(self):
        self.url = "https://www.amazon.com/Sony-Disc-Gaming-Console-Bluetooth/dp/B09QX9WHRS/ref=sr_1_7_mod_primary_new?_encoding=UTF8&brr=1&content-id=amzn1.sym.ed470844-7314-4717-8e3f-b384c77cdbd8&dib=eyJ2IjoiMSJ9.PBbJB_okDl5l3PtYaiAeFCK2cWGPf5NCceO2UouURX9rtQ68IG2hipXtEjKkamBg-PSxfFTAk4IOiuNs98Nj5YTPWSUjX4086Jziy3wpGP3liPaQE_5O_AzC-1VTTcqHz2dOQfiyc6ifg9PsmazpN6vkEcYtzbhiDQXLhY1EkSelH5xd4JPWNy7-fvwVtuAYQ1TtdHjl54sx3jDAkc0TeoDcQ4OIc2TSzgX5Ilq2t84.75A_qdQhJDOWkd9aD3KIAWaClAoVfVpb64XuUAArlyM&dib_tag=se&pd_rd_r=77e149a9-b0d4-4b75-8259-f5aa80be32de&pd_rd_w=1ZV6m&pd_rd_wg=RVotS&qid=1757601771&rd=1&s=videogames&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=1-7"
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
            ), "Accept-Language" : "en-US"
        }

    def scrape(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")

        container = soup.find("div", class_="a-section a-spacing-none aok-align-center aok-relative")

        whole = container.find("span", class_="a-price-whole").get_text(strip=True)
        fraction = container.find("span", class_="a-price-fraction").get_text(strip=True)

        price = f"{whole}{fraction}"
        return float(price)