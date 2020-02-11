from starlette.status import HTTP_201_CREATED


def test_add_order_ok(client, mongo_db_drop, order_data):
    response = client.post("/api/v1/orders/", json=order_data)
    assert response.status_code == HTTP_201_CREATED
    assert response.json()['barista'] == order_data['barista']
