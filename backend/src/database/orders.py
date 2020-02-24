from datetime import date
from datetime import datetime
from datetime import timedelta
from typing import Dict
from typing import List

from database import mongo_db_client
from database.schemas import Chips
from database.schemas import Drink
from database.schemas import Hamburger
from database.schemas import Meat
from database.schemas import Order


class Orders(Order):

    @staticmethod
    def create_order(
            payload: Order
    ) -> Order:
        """
        Create a new order and add to database.

        :param Order payload: payload
        :return Order: order
        """
        order = Orders.calculate_prices(order=payload)
        mongo_db_client.add_order(order=order)
        return order

    @staticmethod
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
            order['is_ready'] = Orders.order_is_ready(order=order)

        return orders

    @staticmethod
    def calculate_prices(
            order: Order,
    ) -> Order:
        """
        This method calculates and add the prices of all items and total.

        :param Order order: list of order.
        """
        for drink in order.drinks:
            drink.price = Orders.calculate_price_drink(drink=drink)

        for chips in order.chips:
            chips.price = Orders.calculate_price_chips(chips=chips)

        for hamburger in order.hamburgers:
            hamburger.price = Orders.calculate_price_hamburger(hamburger=hamburger)

        if Orders.check_promotion_burrimenu(order=order):
            Orders.apply_promotion_burrimenu(order=order)

        if Orders.check_promotion_euromania():
            Orders.apply_promotion_euromania(order=order)

        order.price = Orders.calculate_total_price(order=order)

        return order

    @staticmethod
    def calculate_total_price(
            order: Order,
    ) -> float:
        """
        Calculate the total price of all items.

        :param Order order: order
        :return float: price
        """
        total = 0.0
        if Orders.check_promotion_jarramania(order=order):
            total = 3.0
            order.promotions.append('jarramania')
        else:
            for item in order.hamburgers + order.drinks + order.chips:
                total += item.price
        return total

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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
            result += Orders.calculate_price_meat(meat)
        if hamburger.extra_cheese:
            result += 1.5
            hamburger.extra_cheese.price = 1.5
        if hamburger.extra_tomato:
            result += 1.0
            hamburger.extra_tomato.price = 1.0
        return result

    @staticmethod
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

    @staticmethod
    def check_promotion_burrimenu(
            order: Order
    ) -> bool:
        """
        Check if the promotion 15% burrimenu is applicable.
        The same number of hamburgers, drinks and chips.

        :param Order order: order
        :return boolean: is promotion applicable
        """
        return len(order.hamburgers) == len(order.chips) == len(order.drinks)

    @staticmethod
    def apply_promotion_burrimenu(
            order: Order
    ):
        """
        Apply the promotion burrimenu.
        15% hamburgers.

        :param Order order: order
        :return order: order with promotion applied
        """
        for hamburger in order.hamburgers:
            hamburger.price = hamburger.price * (100 - 15) / 100
        order.promotions.append('burrimenu')

    @staticmethod
    def check_promotion_euromania() -> bool:
        """
        Check if the promotion euromania is applicable.
        If today is Wednesday or Sunday.

        :return boolean: is promotion is applicable.
        """
        return date.today().weekday() in [2, 6]

    @staticmethod
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

    @staticmethod
    def check_promotion_jarramania(
            order: Order
    ) -> bool:
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

    @staticmethod
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
