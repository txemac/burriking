from database.prices.price_hamburguer import PriceHamburger


def test_calculate_price_hamburger(order_1, order_2):
    assert PriceHamburger().calculate(order_1.hamburgers[0]) == 10.0
    assert PriceHamburger().calculate(order_2.hamburgers[0]) == 12.0
