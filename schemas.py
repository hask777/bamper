from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class Car(BaseModel):
    title: str
    model: Optional[str] = None
    brand: Optional[str] = None
