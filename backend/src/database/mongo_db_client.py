import os
from datetime import date
from datetime import datetime

from bson import ObjectId
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
    now = datetime.now()
    order.dt_created = now.strftime("%Y-%m-%d %H:%M:%S")
    collection.insert_one(
        document=dict(
            _id=ObjectId.from_datetime(now),
            **order.dict()
        )
    )
    return order


def get_orders_filters(
        barista: str,
        start_date: date = None,
        end_date: date = None,
) -> Cursor:
    """
    Get all order from a barista.

    :param str barista: barista
    :param date start_date: date start
    :param date end_date: date end
    :return Cursor: pymongo cursor
    """
    collection = _get_mongo_db_client()[os.getenv('MONGODB_COLLECTION')]

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
        filters['_id'] = {'$lte': object_id_end}

    result = collection.find(filters)
    return result
