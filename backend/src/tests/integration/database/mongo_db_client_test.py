import pytest

from database import mongo_db_client


def test_get_mongo_db_client():
    assert mongo_db_client._get_mongo_db_client() is not None


def test_add_order(mongo_db_drop, order_1):
    order = mongo_db_client.add_order(order=order_1)
    assert order is not None


@pytest.mark.parametrize('barista, expected',
                         [(None, 1),
                          ('txema', 1),
                          ('nont_exists', 0)])
def test_get_order_by_barista(mongo_db_drop, order_1, barista, expected):
    mongo_db_client.add_order(order=order_1)
    orders = mongo_db_client.get_orders_by_barista(barista=barista)
    assert orders is not None
    assert len(list(orders)) == expected
