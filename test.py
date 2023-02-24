import requests
import json



def get_items():
  
    url = f'http://127.0.0.1:8000/brand'

    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    params = {
        "title": "acura"
    }

    req = requests.post(url,  data = json.dumps(params)).text
    print(req)

    return req

get_items()
    