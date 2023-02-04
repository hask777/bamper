import requests
from bs4 import BeautifulSoup
import json

brand ='acura-cl'
url = f'https://bamper.by/catalog/{brand}/'

req = requests.get(url).text

soup = BeautifulSoup(req, 'lxml')
uls = soup.select('ul.cat-list.col-sm-6')

cat_links = []

for ul in uls:
    links  = ul.find_all('a')
    for a in links:
        link = a.get('href')
        # title = a.text
        # print(title)
        cat_links.append(link)
   
with open('catalog.json', 'w', encoding='utf-8') as f:
    json.dump(cat_links, f, indent=4, ensure_ascii=False)
# print(req)