import requests
from bs4 import BeautifulSoup
import json
from utils.utils import get_brands, get_keyboard, get_models, get_detail
from env import *
import time

def main():
    url = base_url+'getUpdates'
    getUp = requests.get(url).json()
    try:
        lats_update = getUp['result'][-2]['update_id']
        print(lats_update)
        with open('json/logs.json', 'w', encoding='utf-8') as f:
            json.dump(getUp, f, indent=4, ensure_ascii=False)
    except:
        return

    params = {
        'offset': lats_update + 1
    }

    url = base_url+'getUpdates?'
    getUp = requests.get(url, params=params).json()
    # print(getUp)

    if len(getUp['result']) > 0:

        for update in getUp['result']:
            # print(update['message']['text'])
            lats_update = update['update_id']
            send_message_url = base_url+'sendMessage?'

            params = {
                'chat_id':'5650732610',
                'text': 'Выберете марку',
                'reply_markup': json.dumps({
                'keyboard': get_keyboard(get_brands),
                # 'resize_keyboard': True 
                })
            }

            send_brands = requests.get(send_message_url, params=params).json()

            # function get all models
            print(update['message']['text'])
            brand = update['message']['text'].lower()
            brand = brand.replace(' ', '')
            print(brand)
            lats_update = update['update_id']
            send_message_url = base_url+'sendMessage?'

            models = get_models(brand)
            print(models)

            params = {
                'chat_id':'5650732610',
                'text': 'Выберете модель',
                'reply_markup': json.dumps({
                'keyboard': get_keyboard(None, models),
                # 'resize_keyboard': True 
                })
            }

            send_brands = requests.get(send_message_url, params=params).json()
            model = update['message']['text']
            print(model)

            dt = get_detail(model)
            print(dt)

            lats_update = update['update_id']
            send_message_url = base_url+'sendMessage?'

            params = {
                'chat_id':'5650732610',
                'text': 'Выберете деталь',
                'reply_markup': json.dumps({
                'keyboard': get_keyboard(None, dt),
                # 'resize_keyboard': True 
                })
            }

            send_brands = requests.get(send_message_url, params=params).json()


while True:
    if __name__ == '__main__':
        main()
        time.sleep(3)
