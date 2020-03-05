from typing import Literal

from domain.model.extra import Extra


class ExtraCheese(Extra):
    def __init__(
            self,
            type: Literal['cheddar'],
            price: float = None,
    ):
        super().__init__()
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
