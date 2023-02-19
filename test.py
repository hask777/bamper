import requests
from bs4 import BeautifulSoup
import json
from utils.utils import get_brands, get_keyboard, get_models, get_detail, get_type, get_inline_keyboard
from env import *
import time


def get_items():
    # print(update['callback_query']['data'])

    url = f'https://bamper.by/zchbu/zapchast_blok-abs/marka_skoda/model_scala/'
    print(url)
    try:
        req = requests.get(url).text

        soup = BeautifulSoup(req, 'lxml')
        items = soup.find_all("div", class_="item-list")
        print(items)
    except:
        return

get_items()