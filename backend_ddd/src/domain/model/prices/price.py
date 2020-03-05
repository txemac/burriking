from abc import ABC
from abc import abstractmethod

from domain.model.order import Order


class Price(ABC):
    @abstractmethod
    def calculate(
            self,
            order: Order
    ) -> float:
        pass
