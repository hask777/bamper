import requests
from bs4 import BeautifulSoup
import json

def get_brands():
    with open('json/br_list.json', 'r', encoding='utf-8') as f:
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

def get_type(detail=None, model=None):
    dt_ = []

    url = f"https://bamper.by/catalog/{model}/{detail}/"

    req = requests.get(url).text

    soup = BeautifulSoup(req, 'lxml')
    uls = soup.select('ul.cat-list.col-sm-6')
    for ul in uls:
        links  = ul.find_all('li', class_='list-header')

        for a in links:
            dt_.append(a.text)
    # print(dt_)

    return dt_

"""
KeyBoards
"""

def get_keyboard(func=None, models=None):
    keyboard = []

    if func is not None:
        for item in func():
            res = [{
                'text': item
            }]
            keyboard.append(res)
        return keyboard

    if models is not None:
        for model in models:
            res = [{
                'text': model
            }]
            keyboard.append(res)
        return keyboard



def get_inline_keyboard(func=None, models=None):
    inl = []

    if func is not None:
        for item in func():
            res = [{
                'text': item,
                'callback_data': item
            }]
            inl.append(res)
        return inl

    if models is not None:
        for model in models:
            res = [{
                'text': model,
                'callback_data': model
            }]
            inl.append(res)
        return inl

