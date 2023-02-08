import requests
from bs4 import BeautifulSoup
import json
from utils.utils import get_brands, get_keyboard
from env import *
import time

def main():
    url = base_url+'getUpdates'
    getUp = requests.get(url).json()

    with open('get_updates.json', 'w', encoding='utf-8') as f:
        json.dump(getUp, f, indent=4, ensure_ascii=False)

    
    last_update = " "
    print(last_update)

    for update in getUp['result']:

        text = f"Your write: {update['message']['text']}"
        print(text)

        last_update = update['update_id']
        print(last_update)
        params = {
                'offset': last_update + 1
            }

        url = base_url+'getUpdates'
        getUp = requests.get(url, params=params).json()

        with open('new_updates.json', 'w', encoding='utf-8') as f:
            json.dump(getUp, f, indent=4, ensure_ascii=False)

        


        # for update in getUp['result']:
        #     text = f"Your write: {update['message']['text']}"
        #     print(text)

        #     last_update = update['update_id']

        #     params = {
        #         'chat_id':'5650732610',
        #         'text': 'Выберете марку',
        #         'reply_markup': json.dumps({
        #         'keyboard': get_keyboard(get_brands),
        #         # 'resize_keyboard': True 
        #         })
        #     }

        #     send_message_url = base_url+'sendMessage?'
        #     send_brands = requests.get(send_message_url, params=params).json()
        #     print(send_brands)


while True:
    if __name__ == '__main__':
        main()
        time.sleep(3)
