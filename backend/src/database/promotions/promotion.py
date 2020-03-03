from abc import ABC
from abc import abstractmethod

from database.schemas import Order


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
