from datetime import date
from typing import List

from fastapi import APIRouter
from starlette.status import HTTP_200_OK
from starlette.status import HTTP_201_CREATED

from database import orders
from database.schemas import Order

api_v1 = APIRouter()


@api_v1.post('/orders', response_model=Order, status_code=HTTP_201_CREATED)
def add_order(
        payload: Order
):
    return orders.create_order(payload=payload)


@api_v1.get('/orders', response_model=List[Order], status_code=HTTP_200_OK)
def get_orders(
        barista: str = None,
        start_date: date = None,
        end_date: date = None,
):
    return orders.get_orders(barista=barista, start_date=start_date, end_date=end_date)
