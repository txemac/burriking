from datetime import date
from datetime import datetime
from datetime import timedelta
from typing import Dict
from typing import List

from database import mongo_db_client
from database.prices.price_chips import PriceChips
from database.prices.price_drink import PriceDrink
from database.prices.price_hamburguer import PriceHamburger
from database.prices.price_total import PriceTotal
from database.promotions.promotion_burrimenu import PromotionBurrimenu
from database.promotions.promotion_euromania import PromotionEuromania
from database.schemas import Order


def create_order(
        payload: Order
) -> Order:
    """
    Create a new order and add to database.

    :param Order payload: payload
    :return Order: order
    """
    order = calculate_prices(order=payload)
    mongo_db_client.add_order(order=order)
    return order


def get_orders(
        barista: str = None,
        start_date: date = None,
        end_date: date = None,
) -> List[Order]:
    """
    Get all orders.
    Filters:
        - barista
        - date start
        - date end

    :param str barista: barista
    :param date start_date: date start
    :param date end_date: date end
    :return List: orders
    """
    result = mongo_db_client.get_orders_filters(barista=barista, start_date=start_date, end_date=end_date)

    orders = list(result)

    for order in orders:
        order['is_ready'] = order_is_ready(order=order)

    return orders


def calculate_prices(
        order: Order,
) -> Order:
    """
    This method calculates and add the prices of all items and total.

    :param Order order: list of order.
    """
    for drink in order.drinks:
        drink.price = PriceDrink().calculate(drink=drink)

    for chips in order.chips:
        chips.price = PriceChips().calculate(chips=chips)

    for hamburger in order.hamburgers:
        hamburger.price = PriceHamburger().calculate(hamburger=hamburger)

    if PromotionBurrimenu().is_applicable(order=order):
        PromotionBurrimenu().apply(order=order)

    if PromotionEuromania().is_applicable(order=order):
        PromotionEuromania().apply(order=order)

    order.price = PriceTotal().calculate(order=order)

    return order


def order_is_ready(
        order: Dict
) -> str:
    """
    Check if the order is ready.

    :param Order order: order
    :return str: 'listo' or 'en cocina'
    """
    minutes = 2
    if len(order['hamburgers']) > 1:
        minutes = 7

    dt_created = datetime.strptime(order['dt_created'], '%Y-%m-%d %H:%M:%S')
    return 'listo' if dt_created + timedelta(minutes=minutes) < datetime.now() else 'en cocina'
