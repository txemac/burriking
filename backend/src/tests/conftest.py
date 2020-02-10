import os

import pytest
from starlette.testclient import TestClient

from app.main import app
from database import mongo_db_client
from database.schemas import Chips
from database.schemas import Drink
from database.schemas import ExtraCheese
from database.schemas import ExtraTomato
from database.schemas import Hamburger
from database.schemas import Meat
from database.schemas import Order


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture
def mongodb_drop():
    mongo_db_client._get_mongo_db_client().drop_collection(name_or_collection=os.getenv('MONGODB_COLLECTION_TEST'))


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
        ]
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
