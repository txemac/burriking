from abc import ABC
from abc import abstractmethod


class Extra(ABC):

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def set_price(
            self,
            price: float,
    ):
        pass
