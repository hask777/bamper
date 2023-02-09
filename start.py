import requests
from bs4 import BeautifulSoup
import json
from utils.utils import get_brands, get_keyboard, get_models
from env import *
import time

def main():

    url = base_url+'getUpdates'
    getUp = requests.get(url).json()
    try:
        lats_update = getUp['result'][-2]['update_id']
        print(lats_update)

        with open('logs.json', 'w', encoding='utf-8') as f:
            json.dump(getUp, f, indent=4, ensure_ascii=False)
    except:
        return

    params = {
        'offset': lats_update + 1
    }
    # print(params['offset'])
    url = base_url+'getUpdates?'

    getUp = requests.get(url, params=params).json()
    print(getUp)

    if len(getUp['result']) > 0:

        # with open('logs.json', 'w', encoding='utf-8') as f:
        #     json.dump(getUp, f, indent=4, ensure_ascii=False)

        for update in getUp['result']:
            print(update['message']['text'])
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

        




            # params = {
            #         'chat_id':'5650732610',
            #         'text': 'Выберете марку',
            #         'reply_markup': json.dumps({
            #         'keyboard': get_keyboard(get_brands),
            #         # 'resize_keyboard': True 
            #         })
            #     }

            #  if command equals /start

            # send_message_url = base_url+'sendMessage?'
            # send_brands = requests.get(send_message_url, params=params).json()

        # print(update['message']['text'].replace(' ', '').lower())
        # model = update['message']['text'].replace(' ', '').lower()

        # models = get_models(model)
        # print(models)

# def main():
#     url = base_url+'getUpdates'
#     getUp = requests.get(url).json()

#     with open('get_updates.json', 'w', encoding='utf-8') as f:
#         json.dump(getUp, f, indent=4, ensure_ascii=False)

#     last_update = 0
#     # print(last_update)

#     get_update(getUp)


while True:
    if __name__ == '__main__':
        main()
        time.sleep(3)
