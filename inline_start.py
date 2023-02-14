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
        with open('update.json', 'w', encoding='utf-8') as f:
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

    get_brands_butttons(getUp)



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

            with open('callback.json', 'w', encoding='utf-8') as f:
                json.dump(send_brands, f, indent=4, ensure_ascii=False)

            try:
                get_models_buttons(update['callback_query'])
            except:
                return

def get_models_buttons(update):
    print(update)
    with open('last.json', 'w', encoding='utf-8') as f:
        json.dump(update, f, indent=4, ensure_ascii=False)
#     try:
#         print(update['callback_query']['message']['text'])
#         brand = update['callback_query']['message']['text'].lower()
#         brand = brand.replace(' ', '')
#         lats_update = update['update_id']
#         send_message_url = base_url+'sendMessage?'

#         models = get_models(brand)

#         params = {
#                 'chat_id':'5650732610',
#                 'text': 'Выберете модель',
#                 'reply_markup': json.dumps({
#                 'inline_keyboard': get_inline_keyboard(None, models)
#                 # 'resize_keyboard': True 
#             })
#         }
        
#         send_brands = requests.get(send_message_url, params=params).json()
#     except:
#         return



def main():
    get_updates()


while True:
    if __name__ == '__main__':
        main()
        time.sleep(3)