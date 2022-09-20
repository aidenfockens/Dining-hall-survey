from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib.request

breakfast = []
lunch = []
dinner = []

URL = 'https://www.bu.edu/dining/location/marciano/#menu'
webpage = requests.get(URL)
soup = BeautifulSoup(webpage.text, 'html.parser')
titles = soup.find_all('h4', {'class': 'js-nutrition-open-alias menu-item-title'})
for i in titles:
    print(i.text.strip())