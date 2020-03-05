from typing import Literal


class Drink:
    def __init__(
            self,
            type: Literal['burricola', 'burribeer', 'brawndo'],
            price: float = None,
    ):
        self.__type = type
        self.__price = price

    def type(self):
        return self.__type

    def price(self):
        return self.__price

    def set_price(
            self,
            price: float,
    ):
        self.__price = price
