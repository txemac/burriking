from freezegun import freeze_time

from database import orders
from database.promotions.promotion_burrimenu import PromotionBurrimenu
from database.schemas import Chips
from database.schemas import Drink
from database.schemas import ExtraCheese
from database.schemas import ExtraTomato
from database.schemas import Hamburger
from database.schemas import Meat
from database.schemas import Order
from tests.utils import assert_dicts


@freeze_time('2020-02-10')
def test_calculate_prices_promotion_burrimenu(order_promotion_menu):
    expected = Order(
        barista='txema',
        hamburgers=[
            Hamburger(
                meats=[
                    Meat(
                        type='pollo',
                        size='250g',
                        cooked='al punto',
                        price=2.5,
                    )
                ],
                extra_cheese=ExtraCheese(
                    type='cheddar',
                    price=1.5,
                ),
                extra_tomato=ExtraTomato(
                    type='normal',
                    price=1.0,
                ),
                price=10.0 * (100 - 15) / 100,
            ),
        ],
        chips=[
            Chips(
                type='gajo',
                size='pequeñas',
                price=2.5,
            ),
        ],
        drinks=[
            Drink(
                type='burribeer',
                price=2.5,
            ),
        ],
        price=13.5,
        promotions=['burrimenu'],
    )
    assert PromotionBurrimenu().is_applicable(order=order_promotion_menu) is True
    result = orders.calculate_prices(order=order_promotion_menu)
    assert_dicts(original=result.dict(), expected=expected.dict())
