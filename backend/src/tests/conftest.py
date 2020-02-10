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
        items=[
            Hamburger(
                meats=[
                    Meat(
                        type='pollo',
                        size='250g',
                        cooked='al punto',
                    )
                ],
                extras=[
                    ExtraCheese(
                        type='cheddar',
                    ),
                    ExtraTomato(
                        type='normal',
                    ),
                ],
            ),
            Chips(
                type='gajo',
                size='pequeñas',
            )
        ]
    )


@pytest.fixture
def order_2():
    return Order(
        barista='txema',
        items=[
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
                extras=[
                    ExtraTomato(
                        type='normal',
                    )
                ],
            ),
            Chips(
                type='de la abuela',
                size='grandes',
            ),
            Drink(
                type='burribeer',
            ),
        ],
    )


@pytest.fixture
def order_3():
    return Order(
        barista='txema',
        items=[
            Chips(
                type='deluxe',
                size='grandes',
            ),
            Chips(
                type='gajo',
                size='grandes',
            ),
            Drink(
                type='burribeer',
            ),
        ],
    )


@pytest.fixture
def order_promotion_menu():
    return Order(
        barista='txema',
        items=[
            Hamburger(
                meats=[
                    Meat(
                        type='pollo',
                        size='250g',
                        cooked='al punto',
                    )
                ],
                extras=[
                    ExtraCheese(
                        type='cheddar',
                    ),
                    ExtraTomato(
                        type='normal',
                    ),
                ],
            ),
            Chips(
                type='gajo',
                size='pequeñas',
            ),
            Drink(
                type='burribeer',
            ),
        ]
    )


@pytest.fixture
def order_promotion_jarramania():
    return Order(
        barista='txema',
        items=[
            Chips(
                type='deluxe',
                size='grandes',
            ),
            Drink(
                type='burribeer',
            ),
            Drink(
                type='burribeer',
            ),
        ],
    )
