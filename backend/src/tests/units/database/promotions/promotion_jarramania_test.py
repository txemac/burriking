from freezegun import freeze_time

from database import orders
from database.promotions.promotion_jarramania import PromotionJarramania
from database.schemas import Chips
from database.schemas import Drink
from database.schemas import Order
from tests.utils import assert_dicts


@freeze_time('2020-02-10 17:00:00')
def test_calculate_prices_promotion_jarramania_1(order_promotion_jarramania):
    expected = Order(
        barista='txema',
        chips=[
            Chips(
                type='deluxe',
                size='grandes',
                price=3.5,
            ),
        ],
        drinks=[
            Drink(
                type='burribeer',
                price=2.5,
            ),
            Drink(
                type='burribeer',
                price=2.5,
            ),
        ],
        price=3.0,
        promotions=['jarramania'],
    )
    assert PromotionJarramania().is_applicable(order_promotion_jarramania) is True
    result = orders.calculate_prices(order=order_promotion_jarramania)
    assert_dicts(original=result.dict(), expected=expected.dict())


@freeze_time('2020-02-10 20:00:00')
def test_calculate_prices_promotion_jarramania_2(order_promotion_jarramania):
    expected = Order(
        barista='txema',
        chips=[
            Chips(
                type='deluxe',
                size='grandes',
                price=3.5,
            ),
        ],
        drinks=[
            Drink(
                type='burribeer',
                price=2.5,
            ),
            Drink(
                type='burribeer',
                price=2.5,
            ),
        ],
        price=8.5,
        promotions=[],
    )
    assert PromotionJarramania().is_applicable(order_promotion_jarramania) is False
    result = orders.calculate_prices(order=order_promotion_jarramania)
    assert_dicts(original=result.dict(), expected=expected.dict())


@freeze_time('2020-10-01 17:00:00')
def test_calculate_prices_promotion_jarramania_3(order_promotion_jarramania):
    expected = Order(
        barista='txema',
        chips=[
            Chips(
                type='deluxe',
                size='grandes',
                price=3.5,
            ),
        ],
        drinks=[
            Drink(
                type='burribeer',
                price=2.5,
            ),
            Drink(
                type='burribeer',
                price=2.5,
            ),
        ],
        price=8.5,
        promotions=[],
    )
    assert PromotionJarramania().is_applicable(order_promotion_jarramania) is False
    result = orders.calculate_prices(order=order_promotion_jarramania)
    assert_dicts(original=result.dict(), expected=expected.dict())
