from datetime import datetime

from bson import ObjectId
from pymongo.collection import Collection

from application.presentation.normalizer.order_normalizer import OrderNormalizer
from domain.model.order import Order
from domain.model.prices.price_total import PriceTotal
from domain.model.repository.order_writer_repository import OrderWriterRepository


class MongoDBOrderWriterRepository(OrderWriterRepository):

    def __init__(
            self,
            collection: Collection
    ):
        self._collection = collection

    def add(
            self,
            order: Order,
    ):
        now = datetime.now()
        order.set_dt_created(str_created=now.strftime("%Y-%m-%d %H:%M:%S"))
        order.set_price(price=PriceTotal().calculate(order=order))

        self._collection.insert_one(
            document=dict(
                _id=ObjectId.from_datetime(now),
                **OrderNormalizer.normalize(order=order)
            )
        )
        return order
