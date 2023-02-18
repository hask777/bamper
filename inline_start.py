import requests
from bs4 import BeautifulSoup
import json
from utils.utils import get_brands, get_keyboard, get_models, get_detail, get_type, get_inline_keyboard
from env import *
import time

def get_updates():
    url = base_url+'getUpdates'
    getUp = requests.get(url).json()
    
    try:
        lats_update = getUp['result'][-2]['update_id']
        # print(lats_update)
        # with open('update.json', 'w', encoding='utf-8') as f:
        #     json.dump(getUp, f, indent=4, ensure_ascii=False)
    except:
        return

    params = {
        'offset': lats_update + 1
    }

    url = base_url+'getUpdates?'
    getUp = requests.get(url, params=params).json()

    # with open('json/update.json', 'w', encoding='utf-8') as f:
    #     json.dump(getUp, f, indent=4, ensure_ascii=False)
        
    try:
        if getUp['result'][0]['callback_query'] is not None:
            update = getUp['result'][0]
            
    except:
        update = None

    try:
        if getUp['result'][0]['message']['text'] is not None:
            get_brands_butttons(getUp) 
         
    except:
        if getUp['result'][0]['callback_query']['data'] in get_brands():
            get_models_buttons(update)

        else:
           get_details_button(update) 
  


def get_brands_butttons(request):
    if len(request['result']) > 0:

        for update in request['result']:
            # print(update['message']['text'])
            lats_update = update['update_id']
            send_message_url = base_url+'sendMessage?'

            params = {
                    'chat_id':'5650732610',
                    'text': 'Chose brand',
                    'reply_markup': json.dumps({
                    'inline_keyboard': get_inline_keyboard(get_brands)
                    # 'resize_keyboard': True 
                })
            }

            send_brands = requests.get(send_message_url, params=params).json()

            with open('json/callback.json', 'w', encoding='utf-8') as f:
                json.dump(send_brands, f, indent=4, ensure_ascii=False)

            return update

def get_models_buttons(update):
    if update is not None:
        print(update['callback_query']['data'])
        with open('json/last.json', 'w', encoding='utf-8') as f:
            json.dump(update, f, indent=4, ensure_ascii=False)

        brand = update['callback_query']['data'].lower()
        brand = brand.replace(' ', '')
        print(brand)

        lats_update = update['update_id']

        send_message_url = base_url+'sendMessage?'
        print(send_message_url)


        models = get_models(brand)
        # print(get_models(brand))

        params = {
                    'chat_id':'5650732610',
                    'text': 'Выберете модель',
                    'reply_markup': json.dumps({
                    'inline_keyboard': get_inline_keyboard(None, models)
                    # 'resize_keyboard': True 
            })
        }
            
        send_models = requests.get(send_message_url, params=params).json()
    else:
        return

def get_details_button(update):   
    print(update['callback_query']['data'].lower())

    model = update['callback_query']['data']

    dt = get_detail(model)
    print(dt)

    lats_update = update['update_id']
    send_message_url = base_url+'sendMessage?'

    params = {
                'chat_id':'5650732610',
                'text': 'Выберете деталь',
                'reply_markup': json.dumps({
                'inline_keyboard': get_inline_keyboard(None, dt),
                # 'resize_keyboard': True 
        })
    }

    send_details = requests.get(send_message_url, params=params).json()

    print('this is get details')



def main():
    get_updates()

while True:
    if __name__ == '__main__':
        main()
        time.sleep(3)