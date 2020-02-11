from typing import List

from fastapi import APIRouter
from starlette.status import HTTP_200_OK
from starlette.status import HTTP_201_CREATED

from app.utils import calculate_prices
from app.utils import order_is_ready
from database import mongo_db_client
from database.schemas import Order

api_v1 = APIRouter()


@api_v1.post('/orders/', response_model=Order, status_code=HTTP_201_CREATED)
def add_order(
        payload: Order
):
    order = calculate_prices(order=payload)
    return mongo_db_client.add_order(order=order)


@api_v1.get('/orders/', response_model=List[Order], status_code=HTTP_200_OK)
def get_orders(
        barista: str = None,
):
    orders = list(mongo_db_client.get_orders_by_barista(barista=barista))
    for order in orders:
        order['is_ready'] = order_is_ready(order=order)
    return orders
