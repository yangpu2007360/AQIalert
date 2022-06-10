import requests
import lxml
from bs4 import BeautifulSoup
import smtplib


url = "https://www.accuweather.com/en/us/burlingame/94010/air-quality-index/332055"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

# print(soup.prettify())

aqi = soup.select(
    "#current > div > div > div.content-wrapper > div.particle-chart > div > div > div > div.aq-number")[0].get_text()

curr_air_quality = int(aqi)

print("curr AQI is", curr_air_quality)

if curr_air_quality < 30:
    print("price for this product is low. I am going to send you an email")
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user="xxx@gmail.com", password="xxx")
    connection.sendmail(from_addr="xxx@gmail.com", to_addrs="xxx@gmail.com",
                        msg=f"Subject: Low Price Alert \n\n The price for {url} is low. The current price is {product_price}")
    connection.close()
    print("email sent successfully")
