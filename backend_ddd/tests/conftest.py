import os
from datetime import datetime

import pytest

from domain.model.chips import Chips
from domain.model.drink import Drink
from domain.model.extra_cheese import ExtraCheese
from domain.model.extra_tomato import ExtraTomato
from domain.model.hamburger import Hamburger
from domain.model.meat import Meat
from domain.model.order import Order
from infrastructure.persistence.mongo_db import mongo_db
from main import create_app

os.environ['MONGODB_COLLECTION'] = 'test'


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def mongo_db_drop():
    mongo_db.drop_collection(name_or_collection=os.getenv('MONGODB_COLLECTION'))


@pytest.fixture
def order_1():
    return Order(
        barista='txema',
        hamburgers=[
            Hamburger(
                meats=[
                    Meat(
                        type='pollo',
                        size='250g',
                        cooked='al punto',
                    )
                ],
                extra_cheese=ExtraCheese(
                    type='cheddar',
                ),
                extra_tomato=ExtraTomato(
                    type='normal',
                ),
            ),
        ],
        chips=[
            Chips(
                type='gajo',
                size='pequeñas',
            ),
        ],
        promotions=[],
    )


@pytest.fixture
def order_2():
    return Order(
        barista='txema',
        hamburgers=[
            Hamburger(
                meats=[
                    Meat(
                        type='cerdo',
                        size='250g',
                        cooked='al punto',
                    ),
                    Meat(
                        type='cerdo',
                        size='380g',
                        cooked='al punto',
                    ),
                ],
                extra_tomato=ExtraTomato(
                    type='normal',
                ),
            ),
        ],
        chips=[
            Chips(
                type='de la abuela',
                size='grandes',
            ),
        ],
        drinks=[
            Drink(
                type='burribeer',
            ),
        ],
    )


@pytest.fixture
def order_3():
    return Order(
        barista='txema',
        chips=[
            Chips(
                type='deluxe',
                size='grandes',
            ),
            Chips(
                type='gajo',
                size='grandes',
            ),
        ],
        drinks=[
            Drink(
                type='burribeer',
            ),
        ],
    )


@pytest.fixture
def order_promotion_menu():
    return Order(
        barista='txema',
        hamburgers=[
            Hamburger(
                meats=[
                    Meat(
                        type='pollo',
                        size='250g',
                        cooked='al punto',
                    )
                ],
                extra_cheese=ExtraCheese(
                    type='cheddar',
                ),
                extra_tomato=ExtraTomato(
                    type='normal',
                ),
            ),
        ],
        chips=[
            Chips(
                type='gajo',
                size='pequeñas',
            ),
        ],
        drinks=[
            Drink(
                type='burribeer',
            ),
        ],
    )


@pytest.fixture
def order_promotion_jarramania():
    return Order(
        barista='txema',
        chips=[
            Chips(
                type='deluxe',
                size='grandes',
            ),
        ],
        drinks=[
            Drink(
                type='burribeer',
            ),
            Drink(
                type='burribeer',
            ),
        ],
    )


@pytest.fixture
def order_data():
    return dict(
        barista='txema',
        hamburgers=[],
        chips=[dict(type='deluxe', size='grandes')],
        drinks=[dict(type='burricola')],
        dt_created=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
