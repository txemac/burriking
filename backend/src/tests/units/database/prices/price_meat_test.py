from database.prices.price_meat import PriceMeat


def test_calculate_price_meat(order_1, order_2):
    assert PriceMeat().calculate(order_1.hamburgers[0].meats[0]) == 2.5
    assert PriceMeat().calculate(order_2.hamburgers[0].meats[0]) == 2.5
    assert PriceMeat().calculate(order_2.hamburgers[0].meats[1]) == 3.5
