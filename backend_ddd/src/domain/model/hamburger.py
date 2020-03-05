from typing import List
from typing import Literal

from domain.model.extra_cheese import ExtraCheese
from domain.model.extra_tomato import ExtraTomato
from domain.model.meat import Meat


class Hamburger:
    def __init__(
            self,
            bread_type: Literal['chapata', 'molde', 'deluxe'] = None,
            meats: List[Meat] = [],
            extra_tomato: ExtraTomato = None,
            extra_cheese: ExtraCheese = None,
            price: float = None,
    ):
        self.__bread_type = bread_type
        self.__meats = meats
        self.__extra_tomato = extra_tomato
        self.__extra_cheese = extra_cheese
        self.__price = price

    def bread_type(self):
        return self.__bread_type

    def meats(self):
        return self.__meats

    def extra_tomato(self):
        return self.__extra_tomato

    def extra_cheese(self):
        return self.__extra_cheese

    def price(self):
        return self.__price

    def set_price(
            self,
            price: float = None,
    ):
        self.__price = price
