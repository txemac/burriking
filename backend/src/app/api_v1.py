from typing import List

from fastapi import APIRouter
from starlette.status import HTTP_200_OK
from starlette.status import HTTP_201_CREATED

from database.orders import Orders
from database.schemas import Order

api_v1 = APIRouter()


@api_v1.post('/orders/', response_model=Order, status_code=HTTP_201_CREATED)
def add_order(
        payload: Order
):
    return Orders.create_order(payload=payload)


@api_v1.get('/orders/', response_model=List[Order], status_code=HTTP_200_OK)
def get_orders(
        barista: str = None,
):
    return Orders.get_orders(barista=barista)
