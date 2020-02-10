from datetime import datetime
from typing import List
from typing import Literal
from typing import Union

from pydantic import BaseModel


class Meet(BaseModel):
    name: str = 'carne'
    type: Literal['wagyu', 'pollo', 'cerdo', 'pescado', 'veggie', 'cebra', 'angus']
    size: Literal['125g', '250g', '380g']
    cooked: Literal['poco hecha', 'al punto', 'hecha']
    price: float = None


class ExtraTomato(BaseModel):
    name: str = 'toamte'
    type: Literal['cherry', 'normal']
    price: float = None


class ExtraCheese(BaseModel):
    name: str = 'queso'
    type: Literal['cheddar']
    price: float = None


class Hamburger(BaseModel):
    name: str = 'hamburguesa'
    bread_type: Literal['chapata', 'molde', 'deluxe'] = None
    meets: List[Meet] = None
    extras: List[Union[ExtraTomato, ExtraCheese]] = None
    price: float = None


class Drink(BaseModel):
    name: str = 'refresco'
    type: Literal['burricola', 'burribeer', 'brawndo']
    price: float = None


class Chips(BaseModel):
    name: str = 'patatas'
    type: Literal['deluxe', 'gajo', 'de la abuela']
    size: Literal['pequeñas', 'grandes']
    price: float = None


class Items(BaseModel):
    items: List[Union[Hamburger, Chips, Drink]]
    price: float = None


class Order(Items):
    barista: str
    dt_created: datetime = None
    is_ready: Literal['listo', 'en cocina'] = None


class OrderOnDB(Order):
    _id: str
