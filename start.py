import requests
from bs4 import BeautifulSoup
import json
from utils.utils import get_brands, get_keyboard, get_models, get_detail, get_type
from env import *
import time

def get_updates():
    url = base_url+'getUpdates'
    
    getUp = requests.get(url).json()
    try:
        lats_update = getUp['result'][-2]['update_id']
        # print(lats_update)
        with open('json/logs.json', 'w', encoding='utf-8') as f:
            json.dump(getUp, f, indent=4, ensure_ascii=False)
    except:
        return

    params = {
        'offset': lats_update + 1
    }

    url = base_url+'getUpdates?'
    getUp = requests.get(url, params=params).json()

    with open('update.json', 'w', encoding='utf-8') as f:
        json.dump(getUp, f, indent=4, ensure_ascii=False)

    print(getUp)
    get_brands_butttons(getUp)
    

def get_brands_butttons(request):
    if len(request['result']) > 0:

        for update in request['result']:
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

            # print(get_brands())
            # brand = request['result'][-1]['message']['text']
            # print(brand)

            # if brand in get_brands():
            send_brands = requests.get(send_message_url, params=params).json()
            get_models_buttons(update)
            # print('this is get brands')


def get_models_buttons(update):
    # function get all models
    # print(update['message']['text'])
    brand = update['message']['text'].lower()
    brand = brand.replace(' ', '')
    # print(brand)
    lats_update = update['update_id']
    send_message_url = base_url+'sendMessage?'

    models = get_models(brand)
    # mdls = []

    # for model in models:
    #     model = model.split()
    #     model = model[-1].lower()
    #     mdls.append(model)

    # print(mdls)

    params = {
            'chat_id':'5650732610',
            'text': 'Выберете модель',
            'reply_markup': json.dumps({
            'keyboard': get_keyboard(None, models),
            # 'resize_keyboard': True 
        })
    }
    
    # print(get_brands())
    # brand = update['message']['text']
    # print(brand)



    send_brands = requests.get(send_message_url, params=params).json()
    get_details_buttons(update)
    # print('this is get models')

def get_details_buttons(update):
    model = update['message']['text']
    # print(model)

    dt = get_detail(model)
    # print(dt)

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
    # print(update['message']['text'])
    get_single(update)
    print('this is get details')

def get_single(update):

    detail = update['message']['text']
    # print(detail)

    dt = get_type(detail)
    print(dt)

    # lats_update = update['update_id']
    # send_message_url = base_url+'sendMessage?'

    # params = {
    #             'chat_id':'5650732610',
    #             'text': 'Выберете деталь',
    #             'reply_markup': json.dumps({
    #             'keyboard': get_keyboard(None, dt),
    #             # 'resize_keyboard': True 
    #         })
    #     }

    # send_brands = requests.get(send_message_url, params=params).json()



def main():
    get_updates()


while True:
    if __name__ == '__main__':
        main()
        time.sleep(3)