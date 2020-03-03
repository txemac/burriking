from database.prices.price_chips import PriceChips


def test_calculate_price_chips(order_1, order_2, order_3):
    assert PriceChips().calculate(order_1.chips[0]) == 2.5
    assert PriceChips().calculate(order_2.chips[0]) == 3.5
    assert PriceChips().calculate(order_3.chips[0]) == 3.5
    assert PriceChips().calculate(order_3.chips[1]) == 3.5
