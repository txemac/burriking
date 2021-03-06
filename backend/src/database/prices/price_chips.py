from database.prices.price import Price
from database.schemas import Chips


class PriceChips(Price):

    def calculate(
            self,
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
