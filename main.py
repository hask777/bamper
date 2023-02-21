from fastapi import FastAPI
from schemas import Book

from utils.utils import *
models = []

app = FastAPI()


@app.post('/book')
def create_book(item: Book):
    models.append(item)
    return models


@app.get('/')
def mdss():
    print(models)
    return models