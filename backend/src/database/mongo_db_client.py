import os
from datetime import datetime

from pymongo import MongoClient
from pymongo.cursor import Cursor

from database.schemas import Order

_mongo_db_client = None


def _get_mongo_db_client():
    """
    Singleton to get a mongoDB client.

    :return MongoClient: client
    """
    global _mongo_db_client
    if _mongo_db_client is None:
        client = MongoClient(os.getenv('MONGODB_URL'))
        _mongo_db_client = client[os.getenv('MONGODB_DB_NAME')]
    return _mongo_db_client


def add_order(
        order: Order,
) -> Order:
    """
    Add a new document at mongoDB.

    :param Order order: order
    :return Order: order inserted
    """
    collection = _get_mongo_db_client()[os.getenv('MONGODB_COLLECTION')]
    order.dt_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    collection.insert_one(document=order.dict())
    return order


def get_orders_filters(
        barista: str,
) -> Cursor:
    """
    Get all order from a barista.

    :param str barista: barista
    :return Cursor: pymongo cursor
    """
    collection = _get_mongo_db_client()[os.getenv('MONGODB_COLLECTION')]
    filters = dict()
    if barista is not None:
        filters['barista'] = barista
    result = collection.find(filters)
    return result
