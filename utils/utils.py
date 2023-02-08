import requests
from bs4 import BeautifulSoup
import json

def get_brands():
    with open('br_list.json', 'r', encoding='utf-8') as f:
        mds = json.load(f)
        # print(mds)
    return mds

def get_models(brand):
    md_ = []

    url = f"https://bamper.by/catalog/marka/{brand}/"

    req = requests.get(url).text

    soup = BeautifulSoup(req, 'lxml')
    uls = soup.select('ul.cat-list.col-sm-6')
    for ul in uls:
        links  = ul.find_all('a')

        for a in links:
            md_.append(a.text.strip())
    # print(md_)

    return md_


def get_keyboard(func):
    keyboard = []

    for item in func():
        res = [{
            'text': item
        }]
        keyboard.append(res)
    return keyboard