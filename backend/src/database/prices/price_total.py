from database.prices.price import Price
from database.promotions.promotion_jarramania import PromotionJarramania
from database.schemas import Order


class PriceTotal(Price):

    def calculate(
            self,
            order: Order
    ) -> float:
        """
        Calculate the total price of all items.

        :param Order order: order
        :return float: price
        """
        total = 0.0
        if PromotionJarramania().is_applicable(order=order):
            total = 3.0
            PromotionJarramania().apply(order=order)
        else:
            for item in order.hamburgers + order.drinks + order.chips:
                total += item.price
        return total
