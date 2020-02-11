import os

from starlette.status import HTTP_200_OK
from starlette.status import HTTP_201_CREATED

from database import mongo_db_client
from tests.utils import assert_dicts


def test_add_order_ok(client, mongo_db_drop, order_data):
    response = client.post("/api/v1/orders/", json=order_data)
    assert response.status_code == HTTP_201_CREATED
    assert response.json()['barista'] == order_data['barista']


def test_get_orders_barista_ok(client, mongo_db_drop, order_1):
    mongo_db_client.add_order(order=order_1, collection_name=os.getenv('MONGODB_COLLECTION_TEST'))
    response = client.get(f"/api/v1/orders/{order_1.barista}")
    assert response.status_code == HTTP_200_OK
    assert response.json() is not None
    assert_dicts(original=response.json()[0], expected=order_1.dict())


def test_get_orders_barista_empty(client, mongo_db_drop):
    response = client.get(f"/api/v1/orders/non_exist")
    assert response.status_code == HTTP_200_OK
    assert response.json() == []
