from domain.model.meat import Meat
from domain.model.prices.price import Price


class PriceMeat(Price):

    def calculate(
            self,
            meat: Meat
    ) -> float:

        """
        Calculate price for a meat.

        :param Meat meat: meat
        :return float: price
        """
        result = 0.0
        if meat.size() == '125g':
            result = 2.0
        elif meat.size() == '250g':
            result = 2.5
        elif meat.size() == '380g':
            result = 3.5
        meat.set_price(price=result)
        return result
