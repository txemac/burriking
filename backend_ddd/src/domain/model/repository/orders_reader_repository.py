from abc import ABC
from abc import abstractmethod
from datetime import date
from typing import List

from domain.model.order import Order


class OrdersReaderRepository(ABC):

    @abstractmethod
    def list_orders(
            self,
            barista: str,
            start_date: date = None,
            end_date: date = None,
    ) -> List[Order]:
        pass
