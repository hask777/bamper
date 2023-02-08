import requests
from bs4 import BeautifulSoup
import json

def get_detail(model):
    dt_ = []

    model = model.split()
    model = model[-1].lower()

    url = f"https://bamper.by/catalog/{model}/"

    req = requests.get(url).text

    soup = BeautifulSoup(req, 'lxml')
    uls = soup.select('ul.cat-list.col-sm-6')
    for ul in uls:
        links  = ul.find_all('li', class_='list-header')

        for a in links:
            dt_.append(a.text)
    # print(dt_)

    return dt_

# get_detail('acura-cl')

