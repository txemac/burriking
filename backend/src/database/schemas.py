from datetime import datetime
from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import Field


class Meat(BaseModel):
    type: Literal['wagyu', 'pollo', 'cerdo', 'pescado', 'veggie', 'cebra', 'angus']
    size: Literal['125g', '250g', '380g']
    cooked: Literal['poco hecha', 'al punto', 'hecha']
    price: float = None


class ExtraTomato(BaseModel):
    type: Literal['cherry', 'normal']
    price: float = None


class ExtraCheese(BaseModel):
    type: Literal['cheddar']
    price: float = None


class Hamburger(BaseModel):
    bread_type: Literal['chapata', 'molde', 'deluxe'] = None
    meats: List[Meat]
    extra_tomato: ExtraTomato = None
    extra_cheese: ExtraCheese = None
    price: float = None


class Drink(BaseModel):
    type: Literal['burricola', 'burribeer', 'brawndo']
    price: float = None


class Chips(BaseModel):
    type: Literal['deluxe', 'gajo', 'de la abuela']
    size: Literal['pequeñas', 'grandes']
    price: float = None


class Order(BaseModel):
    barista: str = Field(..., min_length=3, max_length=150)
    hamburgers: List[Hamburger] = []
    chips: List[Chips] = []
    drinks: List[Drink] = []
    price: float = None
    dt_created: datetime = None
    is_ready: Literal['listo', 'en cocina'] = None


class OrderOnDB(Order):
    _id: str
