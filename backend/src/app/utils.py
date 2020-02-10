from datetime import date
from datetime import datetime
from typing import Union

from database.schemas import Chips
from database.schemas import Drink
from database.schemas import ExtraCheese
from database.schemas import ExtraTomato
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
    for item in order.items:
        if isinstance(item, Drink):
            item.price = calculate_price_drink(item)

        elif isinstance(item, Chips):
            item.price = calculate_price_chips(item)

        elif isinstance(item, Hamburger):
            item.price = calculate_price_hamburger(item)

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
    else:
        for item in order.items:
            total += item.price
    return total


def calculate_price_drink(
        item: Drink
) -> float:
    """
    Calculate price for order drink.

    :param Drink item: item
    :return float: price
    """
    result = 0.0
    if item.type == 'burricola':
        result = 2.3
    elif item.type == 'burribeer':
        result = 2.5
    elif item.type == 'brawndo':
        result = 7.5
    return result


def calculate_price_chips(
        item: Chips
) -> float:
    """
    Calculate price for order chips.

    :param Chips item: item
    :return float: price
    """
    result = 0.0
    if item.size == 'pequeñas':
        result = 2.5
    elif item.size == 'grandes':
        result = 3.5
    return result


def calculate_price_hamburger(
        item: Hamburger
) -> float:
    """
    Calculate price for order hamburger.
    Calculate and adding prices for meats and extra ingredients.

    :param Hamburger item: item
    :return float: price
    """
    result = 5.0
    for meat in item.meats:
        result += calculate_price_meat(meat)
    for extra in item.extras:
        result += calculate_price_extra(extra)
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


def calculate_price_extra(
        extra: Union[ExtraCheese, ExtraTomato]
) -> float:
    """
    Calculate price for a extra ingredient.

    :param Union[ExtraCheese, ExtraTomato] extra: extra
    :return float: price
    """
    result = 0.0
    if isinstance(extra, ExtraCheese):
        result = 1.5
    elif isinstance(extra, ExtraTomato):
        result = 1.0
    extra.price = result
    return result


def check_promotion_menu_completed(order):
    """
    Check if the promotion 15% menu completed is applicable.
    Menu completed is minimum 1 hamburger, 1 drink and 1 chips.

    :param Order order: order
    :return boolean: is promotion applicable
    """
    hamburger = 0
    drink = 0
    chips = 0
    for item in order.items:
        if isinstance(item, Hamburger):
            hamburger += 1
        elif isinstance(item, Drink):
            drink += 1
        elif isinstance(item, Chips):
            chips += 1
    return hamburger == drink == chips == 1


def apply_promotion_menu_completed(
        order: Order
):
    """
    Apply the promotion menu completed.
    15% hamburgers.

    :param Order order: order
    :return order: order with promotion applied
    """
    for item in order.items:
        if isinstance(item, Hamburger):
            item.price = item.price * (100 - 15) / 100


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
    for item in order.items:
        if isinstance(item, Chips):
            item.price = 1.0


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
    if not len(order.items) == 3:
        return False

    burribeer = 0
    chips = 0
    for item in order.items:
        if isinstance(item, Drink) and item.type == 'burribeer':
            burribeer += 1
        if isinstance(item, Chips):
            chips += 1
    if not (burribeer == 2 and chips == 1):
        return False

    day_before = datetime.utcnow() <= datetime.strptime('2020-09-30', '%Y-%m-%d')
    hour_between = datetime.strptime('16:00:00', '%H:%M:%S').time() <= \
                   datetime.now().time() <= \
                   datetime.strptime('19:30:00', '%H:%M:%S').time()
    return day_before is True and hour_between is True
