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
    suplies = get_suplies(m_dict['suplies'])
    return suplies

