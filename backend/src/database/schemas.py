from typing import List
from typing import Literal
from typing import Union

from pydantic import BaseModel
from pydantic import validator


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
    meats: List[Meat] = None
    extras: List[Union[ExtraTomato, ExtraCheese]] = None
    price: float = None


class Drink(BaseModel):
    type: Literal['burricola', 'burribeer', 'brawndo']
    price: float = None


class Chips(BaseModel):
    type: Literal['deluxe', 'gajo', 'de la abuela']
    size: Literal['pequeñas', 'grandes']
    price: float = None


class OrderPost(BaseModel):
    barista: str = None
    items: List

    @validator('items')
    def item_type(cls, items):
        if not all(isinstance(item, (Hamburger, Drink, Chips)) for item in items):
            raise ValueError('Not valid type.')
        return items


class Order(OrderPost):
    price: float = None
    is_ready: Literal['listo', 'en cocina'] = None


class OrderOnDB(Order):
    _id: str
