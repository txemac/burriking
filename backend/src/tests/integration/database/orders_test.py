from database import orders


def test_create_order(mongo_db_drop, order_1):
    assert order_1.price is None
    orders.create_order(payload=order_1)
    assert order_1.price > 0.0


def test_get_orders_empty(mongo_db_drop):
    assert len(orders.get_orders()) == 0


def test_get_orders_ok(mongo_db_drop, order_1):
    orders.create_order(payload=order_1)
    assert len(orders.get_orders()) == 1
