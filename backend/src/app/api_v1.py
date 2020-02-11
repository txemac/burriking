from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED

from app.utils import calculate_prices
from database import mongo_db_client
from database.schemas import Order

api_v1 = APIRouter()


@api_v1.post('/orders/', response_model=Order, status_code=HTTP_201_CREATED)
def add_order(
        payload: Order
):
    order = calculate_prices(order=payload)
    return mongo_db_client.add_order(order=order)
