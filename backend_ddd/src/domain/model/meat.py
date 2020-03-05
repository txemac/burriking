from typing import Literal


class Meat:
    def __init__(
            self,
            type: Literal['wagyu', 'pollo', 'cerdo', 'pescado', 'veggie', 'cebra', 'angus'],
            size: Literal['125g', '250g', '380g'],
            cooked: Literal['poco hecha', 'al punto', 'hecha'],
            price: float = None,
    ):
        self.__type = type
        self.__size = size
        self.__cooked = cooked
        self.__price = price

    def type(self):
        return self.__type

    def size(self):
        return self.__size

    def cooked(self):
        return self.__cooked

    def price(self):
        return self.__price

    def set_price(
            self,
            price: float,
    ):
        self.__price = price
