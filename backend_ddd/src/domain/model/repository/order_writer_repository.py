from abc import ABC
from abc import abstractmethod

from domain.model.order import Order


class OrderWriterRepository(ABC):

    @abstractmethod
    def add(
            self,
            order: Order,
    ) -> Order:
        pass
