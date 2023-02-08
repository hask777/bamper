import requests
from bs4 import BeautifulSoup
import json
from bot.utils import get_brands


token = '5927159558:AAFslDjCx3gFsP9lUFtpoQFDVDw8ZdmPxzc';
base_url = f'https://api.telegram.org/bot{token}/'

brands = get_brands()

keyboard = []

for brand in brands:
    model = [{
        'text': brand
    }]
    keyboard.append(model)
    
params = {
    'chat_id':'5650732610',
    'text': 'sdfgddfdgdffg',
    'reply_markup': json.dumps({
        'keyboard': keyboard   
    })
}

url = base_url+'sendMessage?'

req = requests.get(url, params=params).json()

with open('get_updates.json', 'w', encoding='utf-8') as f:
    json.dump(keyboard, f, indent=4, ensure_ascii=False)

