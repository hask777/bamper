from pydantic import BaseModel
from datetime import date

class Car(BaseModel):
    title: str

class Zap(BaseModel):
    zapchast: str
    model: str