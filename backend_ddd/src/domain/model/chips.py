from typing import Literal


class Chips:
    def __init__(
            self,
            type: Literal['deluxe', 'gajo', 'de la abuela'],
            size: Literal['pequeñas', 'grandes'],
            price: float = None,
    ):
        self.__type = type
        self.__size = size
        self.__price = price

    def type(self):
        return self.__type

    def size(self):
        return self.__size

    def price(self):
        return self.__price

    def set_price(
            self,
            price: float,
    ):
        self.__price = price
