from datetime import date
from datetime import datetime
from datetime import timedelta
from typing import Dict

from database.schemas import Chips
from database.schemas import Drink
from database.schemas import Hamburger
from database.schemas import Meat
from database.schemas import Order


def calculate_prices(
        order: Order,
):
    """
    This method calculates and add the prices of all items and total.

    :param Order order: list of order.
    """
    for drink in order.drinks:
        drink.price = calculate_price_drink(drink=drink)

    for chips in order.chips:
        chips.price = calculate_price_chips(chips=chips)

    for hamburger in order.hamburgers:
        hamburger.price = calculate_price_hamburger(hamburger=hamburger)

    if check_promotion_menu_completed(order=order):
        apply_promotion_menu_completed(order=order)

    if check_promotion_euromania():
        apply_promotion_euromania(order=order)

    order.price = calculate_total_price(order=order)

    return order


def calculate_total_price(
        order: Order,
) -> float:
    """
    Calculate the total price of all items.

    :param Order order: order
    :return float: price
    """
    total = 0.0
    if check_promotion_jarramania(order=order):
        total = 3.0
        order.promotions.append('jarramania')
    else:
        for item in order.hamburgers + order.drinks + order.chips:
            total += item.price
    return total


def calculate_price_drink(
        drink: Drink
) -> float:
    """
    Calculate price for order drink.

    :param Drink drink: drink
    :return float: price
    """
    result = 0.0
    if drink.type == 'burricola':
        result = 2.3
    elif drink.type == 'burribeer':
        result = 2.5
    elif drink.type == 'brawndo':
        result = 7.5
    return result


def calculate_price_chips(
        chips: Chips
) -> float:
    """
    Calculate price for order chips.

    :param Chips chips: chips
    :return float: price
    """
    result = 0.0
    if chips.size == 'pequeñas':
        result = 2.5
    elif chips.size == 'grandes':
        result = 3.5
    return result


def calculate_price_hamburger(
        hamburger: Hamburger
) -> float:
    """
    Calculate price for order hamburger.
    Calculate and adding prices for meats and extra ingredients.

    :param Hamburger hamburger: hamburger
    :return float: price
    """
    result = 5.0
    for meat in hamburger.meats:
        result += calculate_price_meat(meat)
    if hamburger.extra_cheese:
        result += 1.5
        hamburger.extra_cheese.price = 1.5
    if hamburger.extra_tomato:
        result += 1.0
        hamburger.extra_tomato.price = 1.0
    return result


def calculate_price_meat(
        meat: Meat
) -> float:
    """
    Calculate price for a meat.

    :param Meat meat: meat
    :return float: price
    """
    result = 0.0
    if meat.size == '125g':
        result = 2.0
    elif meat.size == '250g':
        result = 2.5
    elif meat.size == '380g':
        result = 3.5
    meat.price = result
    return result


def check_promotion_menu_completed(order):
    """
    Check if the promotion 15% menu completed is applicable.
    Menu completed is minimum 1 hamburger, 1 drink and 1 chips.

    :param Order order: order
    :return boolean: is promotion applicable
    """
    return len(order.hamburgers) > 0 and len(order.chips) > 0 and len(order.drinks) > 0


def apply_promotion_menu_completed(
        order: Order
):
    """
    Apply the promotion menu completed.
    15% hamburgers.

    :param Order order: order
    :return order: order with promotion applied
    """
    for hamburger in order.hamburgers:
        hamburger.price = hamburger.price * (100 - 15) / 100
    order.promotions.append('menu')


def check_promotion_euromania():
    """
    Check if the promotion euromania is applicable.
    If today is Wednesday or Sunday.

    :return boolean: is promotion is applicable.
    """
    return date.today().weekday() in [2, 6]


def apply_promotion_euromania(
        order: Order
):
    """
    Apply the promotion euromania.

    :param Order order: order
    """
    for chips in order.chips:
        chips.price = 1.0
    order.promotions.append('euromania')


def check_promotion_jarramania(
        order: Order
):
    """
    Check if the promotion jarramania is applicable.
    - 2 burribeers and 1 chips.
    - Everyday to 30-09-2020. Between 16-19.30 h.

    :param Order order: order
    :return boolean: is promotion applicable
    """
    if len(order.drinks) != 2 \
            and [drink.type != 'burribeer' for drink in order.drinks] \
            and len(order.chips) != 1:
        return False

    day_before = datetime.utcnow() <= datetime.strptime('2020-09-30', '%Y-%m-%d')
    hour_between = datetime.strptime('16:00:00', '%H:%M:%S').time() <= \
                   datetime.now().time() <= \
                   datetime.strptime('19:30:00', '%H:%M:%S').time()
    return day_before is True and hour_between is True


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
