import pytest
from freezegun import freeze_time

from database import mongo_db_client


def test_get_mongo_db_client():
    assert mongo_db_client._get_mongo_db_client() is not None


def test_add_order(mongo_db_drop, order_1):
    order = mongo_db_client.add_order(order=order_1)
    assert order is not None


@freeze_time('2020-02-10')
@pytest.mark.parametrize('barista, expected_1',
                         [(None, 1),
                          ('txema', 1),
                          ('non_exists', 0)])
@pytest.mark.parametrize('start_date, end_date, expected_2',
                         [(None, '2020-10-01', 1),
                          ('2020-01-01', None, 1),
                          (None, '2020-01-01', 0),
                          ('2020-10-01', None, 0),
                          ('2020-01-01', '2020-10-01', 1),
                          ('2020-10-01', '2020-10-01', 1)])
def test_get_orders_filters(mongo_db_drop, order_1, barista, start_date, end_date, expected_1, expected_2):
    mongo_db_client.add_order(order=order_1)
    orders = mongo_db_client.get_orders_filters(barista=barista, start_date=start_date, end_date=end_date)
    assert len(list(orders)) == expected_1 * expected_2
