from datetime import datetime
from typing import List
from typing import Literal

from pydantic import Field

from domain.model.chips import Chips
from domain.model.drink import Drink
from domain.model.hamburger import Hamburger


class Order:
    def __init__(
            self,
            barista: str = Field(..., min_length=3, max_length=150),
            hamburgers: List[Hamburger] = [],
            chips: List[Chips] = [],
            drinks: List[Drink] = [],
            price: float = None,
            dt_created: datetime = None,
            is_ready: Literal['listo', 'en cocina'] = None,
            promotions: List[Literal['burrimenu', 'euromania', 'jarramania']] = [],
    ):
        self.__barista = barista
        self.__hamburgers = hamburgers
        self.__chips = chips
        self.__drinks = drinks
        self.__price = price
        self.__dt_created = dt_created
        self.__is_ready = is_ready
        self.__promotions = promotions

    def barista(self):
        return self.__barista

    def hamburgers(self):
        return self.__hamburgers

    def chips(self):
        return self.__chips

    def drinks(self):
        return self.__drinks

    def price(self):
        return self.__price

    def dt_created(self):
        return self.__dt_created

    def is_ready(self):
        return self.__is_ready

    def promotions(self):
        return self.__promotions

    def set_dt_created(
            self,
            str_created: str
    ):
        self.__dt_created = str_created

    def set_price(
            self,
            price: float
    ):
        self.__price = price

    def set_promotions(
            self,
            promotions: List[Literal['burrimenu', 'euromania', 'jarramania']],
    ):
        self.__promotions = promotions
