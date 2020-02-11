import os

from pymongo import MongoClient

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
        collection_name: str = os.getenv('MONGODB_COLLECTION'),
) -> Order:
    """
    Add a new document at mongoDB.

    :param Order order: order
    :param str collection_name: name of the collection
    :return Order: order inserted
    """
    collection = _get_mongo_db_client()[collection_name]
    collection.insert_one(document=order.dict())
    return order
