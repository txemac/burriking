from datetime import datetime

from database.promotions.promotion import Promotion
from database.schemas import Order


class PromotionJarramania(Promotion):

    def is_applicable(
            self,
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
        hour_between = datetime.strptime('16:00:00', '%H:%M:%S').time() \
                       <= datetime.now().time() \
                       <= datetime.strptime('19:30:00', '%H:%M:%S').time()
        return day_before is True and hour_between is True

    def apply(
            self,
            order: Order
    ):
        order.promotions.append('jarramania')
