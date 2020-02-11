import os

from database import mongo_db_client


def test_get_mongo_db_client():
    assert mongo_db_client._get_mongo_db_client() is not None


def test_add_order(mongo_db_drop, order_1):
    order = mongo_db_client.add_order(order=order_1, collection_name=os.getenv('MONGODB_COLLECTION_TEST'))
    assert order is not None


def test_get_order_by_barista(mongo_db_drop, order_1):
    mongo_db_client.add_order(order=order_1, collection_name=os.getenv('MONGODB_COLLECTION_TEST'))
    order = mongo_db_client.get_orders_by_barista(
        barista='txema',
        collection_name=os.getenv('MONGODB_COLLECTION_TEST')
    )
    assert order is not None
