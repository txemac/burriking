import pytest
from freezegun import freeze_time
from starlette.status import HTTP_200_OK
from starlette.status import HTTP_201_CREATED

from database import mongo_db_client


def test_add_order_ok(client, mongo_db_drop, order_data):
    response = client.post("/api/v1/orders", json=order_data)
    assert response.status_code == HTTP_201_CREATED
    assert response.json()['barista'] == order_data['barista']


@freeze_time('2020-02-10')
@pytest.mark.parametrize('start_date, end_date, expected',
                         [('2020-01-01', '2020-10-01', 1),
                          ('2020-01-01', '2020-01-01', 0),
                          ('2020-10-01', '2020-01-01', 0)])
def test_get_orders_ok(client, mongo_db_drop, order_1, start_date, end_date, expected):
    mongo_db_client.add_order(order=order_1)
    response = client.get(f"/api/v1/orders?barista={order_1.barista}&start_date={start_date}&end_date={end_date}")
    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == expected


def test_get_orders_empty(client, mongo_db_drop):
    response = client.get(f"/api/v1/orders?barista=non_exists")
    assert response.status_code == HTTP_200_OK
    assert response.json() == []
