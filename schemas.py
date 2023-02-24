from pydantic import BaseModel
from datetime import date

class Car(BaseModel):
    title: str
