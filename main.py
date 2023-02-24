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


# @app.get('/detail')
# def get_details_list_():
#     detail = get_type("/catalog/acura-cl/group_audio-video-media/")
#     models.append(detail)
#     return detail


# @app.get('/detail')
# def get_result():
#     sup = get_suplies()
#     models.append(sup)
#     return sup

