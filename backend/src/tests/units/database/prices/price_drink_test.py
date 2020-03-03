from database.prices.price_drink import PriceDrink


def test_calculate_price_drink(order_2, order_3):
    assert PriceDrink().calculate(order_2.drinks[0]) == 2.5
    assert PriceDrink().calculate(order_3.drinks[0]) == 2.5
