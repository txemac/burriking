from abc import ABC
from abc import abstractmethod

from domain.model.order import Order


class Promotion(ABC):
    @abstractmethod
    def is_applicable(
            self,
            order: Order
    ) -> bool:
        pass

    @abstractmethod
    def apply(
            self,
            order: Order
    ):
        pass
