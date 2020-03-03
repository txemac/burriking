from database.promotions.promotion import Promotion
from database.schemas import Order


class PromotionBurrimenu(Promotion):

    def is_applicable(
            self,
            order: Order
    ) -> bool:
        """
        Check if the promotion 15% burrimenu is applicable.
        The same number of hamburgers, drinks and chips.

        :param Order order: order
        :return boolean: is promotion applicable
        """
        return len(order.hamburgers) == len(order.chips) == len(order.drinks)

    def apply(
            self,
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
