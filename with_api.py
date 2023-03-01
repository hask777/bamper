import requests
from bs4 import BeautifulSoup
import json
from utils.utils import *
from env import *
import time


arr = []
main_dict = {}

items_arr = []

# make start
# make delete message


def get_updates():
    url = base_url+'getUpdates'
    getUp = requests.get(url).json()

    try:
        chat_id = getUp['result'][0]['message']['chat']['id']
    except:
        chat_id = getUp['result'][0]['callback_query']['message']['chat']['id']

    

    with open('up.json', 'w', encoding='utf-8') as f:
        json.dump(getUp, f, indent=4, ensure_ascii=False)

    # print(getUp)
    
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

            send_message_url = base_url+'sendMessage?'

            params = {
                    'chat_id':chat_id,
                    'text': 'Начинаем поиск ...',

            }
            
            start_search = requests.get(send_message_url, params=params).json()

            get_brands_buttons(getUp, chat_id) 
    except:
        if getUp['result'][0]['callback_query']['data'] in get_brands():
            get_models_buttons(update, chat_id)

        else:
            get_details_list_button(update, chat_id)

            if update['callback_query']['data'] is not None:
                get_items_list(update, chat_id)

            try:     
                while True:
                    check_items(items_arr, chat_id)

                    print('update')
                    time.sleep(30)
                    
            except:
                return
            

            
            

def get_brands_buttons(request, chat_id):
    
    if len(request['result']) > 0:
       
        for update in request['result']:
            # print(update['message']['text'])
            lats_update = update['update_id']
            send_message_url = base_url+'sendMessage?'

            params = {
                    'chat_id': chat_id,
                    'text': 'Chose brand',
                    'reply_markup': json.dumps({
                    'inline_keyboard': get_inline_keyboard(get_brands)
                    # 'resize_keyboard': True 
                })
            }

            send_brands = requests.get(send_message_url, params=params).json()

            return update

def get_models_buttons(update, chat_id):
    if update is not None:

        brand = update['callback_query']['data'].lower()
        brand = brand.replace(' ', '')

        main_dict['brand'] = brand

        url = f'http://127.0.0.1:8000/models'

        params = {
            "title": brand
        }

        req = requests.post(url,  data = json.dumps(params)).text

        lats_update = update['update_id']

        send_message_url = base_url+'sendMessage?'

        # models = get_models(brand)
        models = requests.get('http://127.0.0.1:8000/models').json()

        params = {
                    'chat_id': chat_id,
                    'text': 'Выберете модель',
                    'reply_markup': json.dumps({
                    'inline_keyboard': get_inline_keyboard(None, models)
                    # 'resize_keyboard': True 
            })
        }
            
        send_models = requests.get(send_message_url, params=params).json()
    else:
        return

def get_details_list_button(update, chat_id):  
    m_list =[]

    for upd in update['callback_query']['message']['reply_markup']['inline_keyboard']:
        for up in upd:
            m_list.append(up['text'])
    # print(m_list)

    if update['callback_query']['data'] in m_list:
        model = update['callback_query']['data']

        model = model.split()
        model = model[-1].lower()

        url = f'http://127.0.0.1:8000/details'

        params = {
            "title": model
        }

        req = requests.post(url,  data = json.dumps(params)).text
        # print(req)

        dt =  requests.get('http://127.0.0.1:8000/details').json()

        lats_update = update['update_id']
        send_message_url = base_url+'sendMessage?'

        params = {
                    'chat_id': chat_id,
                    'text': 'Выберете систему',
                    'reply_markup': json.dumps({
                    'inline_keyboard': get_inline_keyboard(None, dt),
                    # 'resize_keyboard': True 
            })
        }

        send_details = requests.get(send_message_url, params=params).json()

    else:
        get_suplies(update, chat_id)
        return update['callback_query']['data']

def get_suplies(update, chat_id):
    # print(update['callback_query']['data'])

    suplies = update['callback_query']['data']

    url = 'http://127.0.0.1:8000/suplies'

    params = {
        'title': suplies
    }

    req = requests.post(url,  data = json.dumps(params)).text
    
    try:
        spl =  requests.get('http://127.0.0.1:8000/suplies').json()

        # print(spl)

        lats_update = update['update_id']
        send_message_url = base_url+'sendMessage?'

        params = {
                        'chat_id': chat_id,
                        'text': 'Выберете деталь',
                        'reply_markup': json.dumps({
                        'inline_keyboard': get_inline_keyboard(None, spl),
                        # 'resize_keyboard': True 
            })
        }

        send_suplies = requests.get(send_message_url, params=params).json()

    except:
        return
   
def get_items_list(update, chat_id):
    # print(update['callback_query']['data'])
    all_items = []

    zapchast = update['callback_query']['data']

    url = 'http://127.0.0.1:8000/zapchast'

    params = {
        'title': zapchast
    }

    req = requests.post(url,  data = json.dumps(params)).text


    # get items
    try:
        url = 'http://127.0.0.1:8000/zapchast'

        items = requests.get(url).json()
    except:
        return

    try:

        for item in items:
            img = item['img']
            link = item['link']
            title = item['title']

            lats_update = update['update_id']
            send_message_url = base_url+'sendMessage?'

            params = {
                        'chat_id': chat_id,
                        'text': f'{title}\n{link}\nhttps://bamper.by/{img}',
                    }
            
            send_items = requests.get(send_message_url, params=params).json()

            items_arr.append(items)

    except:
        return
       

def check_items(items, chat_id):            

    its = []
    if items is not None:
        
        check_items = requests.get('http://127.0.0.1:8000/zapchast').json()

        for it in items[0]:
            it['title']
            its.append(it['title'])
        # print(its)

        for item in check_items:
            # print(item['title'])
            if item['title'] not in its:
                # print(item)

                img = item['img']
                link = item['link']
                title = item['title']

                send_message_url = base_url+'sendMessage?'

                params = {
                            'chat_id': chat_id,
                            'text': f'{title}\n{link}\nhttps://bamper.by/{img}',
                        }
                
                send_items = requests.get(send_message_url, params=params).json()


            else:
                print('not new details')
    

def main():
    get_updates()

while True:
    if __name__ == '__main__':
        main()
        time.sleep(3)