from datetime import date

from database.promotions.promotion import Promotion
from database.schemas import Order


class PromotionEuromania(Promotion):

    def is_applicable(
            self,
            order: Order
    ) -> bool:
        """
        Check if the promotion euromania is applicable.
        If today is Wednesday or Sunday.

        :return boolean: is promotion is applicable.
        """
        return date.today().weekday() in [2, 6]

    def apply(
            self,
            order: Order
    ):
        """
        Apply the promotion euromania.

        :param Order order: order
        """
        for chips in order.chips:
            chips.price = 1.0
        order.promotions.append('euromania')
