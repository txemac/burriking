from domain.model.order import Order
from domain.model.prices.price import Price
from domain.model.prices.price_chips import PriceChips
from domain.model.prices.price_drink import PriceDrink
from domain.model.prices.price_hamburguer import PriceHamburger
from domain.model.promotions.promotion_burrimenu import PromotionBurrimenu
from domain.model.promotions.promotion_euromania import PromotionEuromania
from domain.model.promotions.promotion_jarramania import PromotionJarramania


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
        for drink in order.drinks():
            drink.set_price(price=PriceDrink().calculate(drink=drink))

        for chips in order.chips():
            chips.set_price(price=PriceChips().calculate(chips=chips))

        for hamburger in order.hamburgers():
            hamburger.set_price(price=PriceHamburger().calculate(hamburger=hamburger))

        if PromotionBurrimenu().is_applicable(order=order):
            PromotionBurrimenu().apply(order=order)

        if PromotionEuromania().is_applicable(order=order):
            PromotionEuromania().apply(order=order)

        total = 0.0
        if PromotionJarramania().is_applicable(order=order):
            total = 3.0
            PromotionJarramania().apply(order=order)
        else:
            for item in order.hamburgers() + order.drinks() + order.chips():
                total += item.price()

        order.set_price(price=total)

        return total
