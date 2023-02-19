import requests
from bs4 import BeautifulSoup
import json
from utils.utils import get_brands, get_keyboard, get_models, get_detail, get_type, get_inline_keyboard
from env import *
import time

arr = []

main_dict = {}


def get_updates(arr, main_dict):
    url = base_url+'getUpdates'
    getUp = requests.get(url).json()
    
    try:
        lats_update = getUp['result'][-2]['update_id']
    except:
        return

    params = {
        'offset': lats_update + 1
    }

    url = base_url+'getUpdates?'
    getUp = requests.get(url, params=params).json()

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
            get_models_buttons(update , main_dict)

        else:
            get_details_button(update, main_dict) 

  


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

def get_models_buttons(update, main_dict):
    if update is not None:
        with open('json/last.json', 'w', encoding='utf-8') as f:
            json.dump(update, f, indent=4, ensure_ascii=False)

        brand = update['callback_query']['data'].lower()
        brand = brand.replace(' ', '')

        main_dict['brand'] = brand


        # print(main_dict)

        lats_update = update['update_id']

        send_message_url = base_url+'sendMessage?'
        models = get_models(brand)

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

def get_details_button(update, main_dict):  
    m_list =[]

    for upd in update['callback_query']['message']['reply_markup']['inline_keyboard']:
        for up in upd:
            m_list.append(up['text'])
    # print(m_list)

    if update['callback_query']['data'] in m_list:
        model = update['callback_query']['data']

        main_dict['model'] = model.split()[-1].lower()
        main_dict['detail'] = update['callback_query']['data']
        m_list.append(main_dict)

        # print(main_dict)

        dt = get_detail(model)

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
    
    else:
        # print(update['callback_query']['data'])
        return update['callback_query']['data']



def main():
    get_updates(main, main_dict)

while True:
    if __name__ == '__main__':
        main()
        time.sleep(3)