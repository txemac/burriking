from datetime import date
from datetime import datetime
from datetime import timedelta
from typing import Dict
from typing import List

from bson import ObjectId
from pymongo.collection import Collection

from domain.model.order import Order
from domain.model.repository.orders_reader_repository import OrdersReaderRepository
from infrastructure.hydration.mongo_db_order_hydration import MongoDBOrderHydration


class MongoDBOrdersReaderRepository(OrdersReaderRepository):

    def __init__(
            self,
            collection: Collection
    ):
        self._collection = collection

    def list_orders(
            self,
            barista: str,
            start_date: date = None,
            end_date: date = None,
    ) -> List[Order]:
        filters = dict()
        if barista is not None:
            filters['barista'] = barista

        if start_date is not None:
            start_dt = datetime.strptime(f'{start_date} 00:00:00', "%Y-%m-%d %H:%M:%S")
            object_id_start = ObjectId.from_datetime(start_dt)
            filters['_id'] = {'$gte': object_id_start}

        if end_date is not None:
            end_dt = datetime.strptime(f'{end_date} 00:00:00', "%Y-%m-%d %H:%M:%S")
            object_id_end = ObjectId.from_datetime(end_dt)
            if filters.get('_id'):
                filters['_id']['$lte'] = object_id_end
            else:
                filters['_id'] = {'$lte': object_id_end}

        result = self._collection.find(filters)

        orders = list(result)

        for order in orders:
            order['is_ready'] = self.__order_is_ready(order=order)

        return [MongoDBOrderHydration().hydrate(order=order) for order in orders]

    @staticmethod
    def __order_is_ready(
            order: Dict
    ) -> str:
        """
        Check if the order is ready.

        :param Order order: order
        :return str: 'listo' or 'en cocina'
        """
        minutes = 2
        if len(order['hamburgers']) > 1:
            minutes = 7

        dt_created = datetime.strptime(order['dt_created'], '%Y-%m-%d %H:%M:%S')
        return 'listo' if dt_created + timedelta(minutes=minutes) < datetime.now() else 'en cocina'
