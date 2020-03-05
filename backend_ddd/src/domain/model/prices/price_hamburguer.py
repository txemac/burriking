from domain.model.hamburger import Hamburger
from domain.model.prices.price import Price
from domain.model.prices.price_meat import PriceMeat


class PriceHamburger(Price):

    def calculate(
            self,
            hamburger: Hamburger
    ) -> float:
        """
        Calculate price for order hamburger.
        Calculate and adding prices for meats and extra ingredients.

        :param Hamburger hamburger: hamburger
        :return float: price
        """
        result = 5.0
        for meat in hamburger.meats():
            result += PriceMeat().calculate(meat=meat)
        if hamburger.extra_cheese():
            result += 1.5
            hamburger.extra_cheese().set_price(price=1.5)
        if hamburger.extra_tomato():
            result += 1.0
            hamburger.extra_tomato().set_price(price=1.0)
        return result
