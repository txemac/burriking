from database.prices.price import Price
from database.schemas import Drink


class PriceDrink(Price):

    def calculate(
            self,
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
