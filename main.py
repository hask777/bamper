from fastapi import FastAPI
from schemas import Book

from utils.utils import *

models = []

app = FastAPI()


@app.post('/brand')
def get_brand(item: Book):
    models.append(item)
    return models


@app.get('/models')
def get_models_list():
    print(models[0].title)
    modelss = get_models(models[0].title)
    models.append(modelss)
    return modelss


@app.get('/details')
def get_details_list_():
    details = get_detail('acura-cl')
    models.append(details)
    return details


@app.get('/detail')
def get_details_list_():
    detail = get_type("/catalog/acura-cl/group_audio-video-media/")
    models.append(detail)
    return detail

@app.get('/result')
def get_result():
    sup = get_suplies()
    models.append(sup)
    return sup

