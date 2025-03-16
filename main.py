from bs4 import BeautifulSoup as bs
import requests

url = 'https://appbrewery.github.io/instant_pot/'

response = requests.get(url)
soup = bs(response.text, 'html.parser')

# price_html_whole = soup.find(class_='a-price-whole')
# price_whole = price_html_whole.getText()
# price_htm_fraction = soup.find(class_='a-price-fraction')
# price_fraction = price_htm_fraction.getText()
# whole_price = float(f'{price_whole}{price_fraction}')
# print(whole_price)

price_html_whole = soup.find(class_='a-offscreen')
price = price_html_whole.getText().split('$')[1]


