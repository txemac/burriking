from freezegun import freeze_time

from app.utils import calculate_price_chips
from app.utils import calculate_price_drink
from app.utils import calculate_price_hamburger
from app.utils import calculate_price_meat
from app.utils import calculate_prices
from app.utils import check_promotion_burrimenu
from app.utils import check_promotion_euromania
from app.utils import check_promotion_jarramania
from app.utils import order_is_ready
from database.schemas import Chips
from database.schemas import Drink
from database.schemas import ExtraCheese
from database.schemas import ExtraTomato
from database.schemas import Hamburger
from database.schemas import Meat
from database.schemas import Order
from tests.utils import assert_dicts


def test_calculate_price_meat(order_1, order_2):
    assert calculate_price_meat(order_1.hamburgers[0].meats[0]) == 2.5
    assert calculate_price_meat(order_2.hamburgers[0].meats[0]) == 2.5
    assert calculate_price_meat(order_2.hamburgers[0].meats[1]) == 3.5


def test_calculate_price_hamburger(order_1, order_2):
    assert calculate_price_hamburger(order_1.hamburgers[0]) == 10.0
    assert calculate_price_hamburger(order_2.hamburgers[0]) == 12.0


def test_calculate_price_chips(order_1, order_2, order_3):
    assert calculate_price_chips(order_1.chips[0]) == 2.5
    assert calculate_price_chips(order_2.chips[0]) == 3.5
    assert calculate_price_chips(order_3.chips[0]) == 3.5
    assert calculate_price_chips(order_3.chips[1]) == 3.5


def test_calculate_price_drink(order_2, order_3):
    assert calculate_price_drink(order_2.drinks[0]) == 2.5
    assert calculate_price_drink(order_3.drinks[0]) == 2.5


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
    result = calculate_prices(order=order_1)
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
    result = calculate_prices(order=order_2)
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
    result = calculate_prices(order=order_3)
    assert_dicts(original=result.dict(), expected=expected.dict())


@freeze_time('2020-02-10')
def test_calculate_prices_promotion_menu(order_promotion_menu):
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
    assert check_promotion_burrimenu(order=order_promotion_menu) is True
    result = calculate_prices(order=order_promotion_menu)
    assert_dicts(original=result.dict(), expected=expected.dict())


@freeze_time('1982-04-25')  # sunday
def test_calculate_prices_promotion_euromania(order_promotion_menu):
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
                price=1.0,
            ),
        ],
        drinks=[
            Drink(
                type='burribeer',
                price=2.5,
            ),
        ],
        price=12.0,
        promotions=['burrimenu', 'euromania'],
    )
    assert check_promotion_euromania() is True
    result = calculate_prices(order=order_promotion_menu)
    assert_dicts(original=result.dict(), expected=expected.dict())


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
    assert check_promotion_jarramania(order_promotion_jarramania) is True
    result = calculate_prices(order=order_promotion_jarramania)
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
    assert check_promotion_jarramania(order_promotion_jarramania) is False
    result = calculate_prices(order=order_promotion_jarramania)
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
    assert check_promotion_jarramania(order_promotion_jarramania) is False
    result = calculate_prices(order=order_promotion_jarramania)
    assert_dicts(original=result.dict(), expected=expected.dict())


@freeze_time('2020-10-01 17:00:00')
def test_order_is_ready_listo(order_data):
    assert order_is_ready(order=order_data) == 'listo'
