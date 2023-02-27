from fastapi import FastAPI
from schemas import Car
from utils.utils import *

m_dict = {}

app = FastAPI()


@app.post('/models')
def get_brand(item: Car):
    m_dict['brand'] = item.title
    return m_dict


@app.get('/models')
def get_models_list():
    models = get_models(m_dict['brand'])
    return models


@app.post('/details')
def post_details(item: Car):
    m_dict['model'] = item.title
    return m_dict


@app.get('/details')
def get_details_list_():
    details = get_detail(m_dict['model'])
    return details


@app.post('/suplies')
def post_suplies(item: Car):
    print(item)
    m_dict['suplies'] = item.title
    return m_dict


@app.get('/suplies')
def get_suplies_list():

    sup_arr = []
    sup_d = {}
    suplies = get_suplies(m_dict['suplies'])

    for sup in suplies:

        try:
            if len(sup['text'].encode('utf-8')) < 64:
                sup['text'] = sup['text']  

        except:

            if len(sup['text'].encode('utf-8')) > 64: 
                sup['text'] = sup['text'].split()
                sup['text'] = sup['text'][0] + ' ' + sup['text'][1]
            else:
                sup['text'] = sup['text'][0]


        sup['link'] = sup['link'].split('/')
        sup['link'] = sup['link'][2]
        # sup['marka'] = sup['link'][3]
        # sup['model'] = sup['link'][4]

    return suplies

@app.post('/zapchast')
def post_items_list(item: Car):
    # print(item.title)
    m_dict['zapchast'] = item.title
    return m_dict

@app.get('/zapchast')
def get_items_list():
    # print(m_dict['brand'])
    # print(m_dict['model'])
    items = get_items(m_dict)

    return items
