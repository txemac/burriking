from freezegun import freeze_time

from database import orders
from database.schemas import Chips
from database.schemas import Drink
from database.schemas import ExtraCheese
from database.schemas import ExtraTomato
from database.schemas import Hamburger
from database.schemas import Meat
from database.schemas import Order
from tests.utils import assert_dicts


@freeze_time('2020-02-10')
def test_calculate_prices_1(order_1):
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
                price=10.0,
            ),
        ],
        chips=[
            Chips(
                type='gajo',
                size='pequeñas',
                price=2.5,
            ),
        ],
        price=12.5,
        promotions=[],
    )
    result = orders.calculate_prices(order=order_1)
    assert_dicts(original=result.dict(), expected=expected.dict())


@freeze_time('2020-02-10')
def test_calculate_prices_2(order_2):
    expected = Order(
        barista='txema',
        hamburgers=[
            Hamburger(
                meats=[
                    Meat(
                        type='cerdo',
                        size='250g',
                        cooked='al punto',
                        price=2.5,
                    ),
                    Meat(
                        type='cerdo',
                        size='380g',
                        cooked='al punto',
                        price=3.5,
                    ),
                ],
                extra_tomato=ExtraTomato(
                    type='normal',
                    price=1.0,
                ),
                price=12.0 * (100 - 15) / 100,
            ),
        ],
        chips=[
            Chips(
                type='de la abuela',
                size='grandes',
                price=3.5,
            ),
        ],
        drinks=[
            Drink(
                type='burribeer',
                price=2.5,
            ),
        ],
        price=16.2,
        promotions=['burrimenu'],
    )
    result = orders.calculate_prices(order=order_2)
    assert_dicts(original=result.dict(), expected=expected.dict())


@freeze_time('2020-02-10')
def test_calculate_prices_3(order_3):
    expected = Order(
        barista='txema',
        chips=[
            Chips(
                type='deluxe',
                size='grandes',
                price=3.5,
            ),
            Chips(
                type='gajo',
                size='grandes',
                price=3.5,
            ),
        ],
        drinks=[
            Drink(
                type='burribeer',
                price=2.5,
            ),
        ],
        price=9.5,
        promotions=[],
    )
    result = orders.calculate_prices(order=order_3)
    assert_dicts(original=result.dict(), expected=expected.dict())


@freeze_time('2020-10-01 17:00:00')
def test_order_is_ready_listo(order_data):
    assert orders.order_is_ready(order=order_data) == 'listo'
