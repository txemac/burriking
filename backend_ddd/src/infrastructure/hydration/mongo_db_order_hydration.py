from typing import Dict

from domain.model.order import Order
from infrastructure.hydration.mongo_db_chips_hydration import MongoDBChipsHydration
from infrastructure.hydration.mongo_db_drink_hydration import MongoDBDrinkHydration
from infrastructure.hydration.mongo_db_hamburger_hydration import MongoDBHamburgerHydration


class MongoDBOrderHydration:

    @staticmethod
    def hydrate(
            order: Dict
    ) -> Order:
        return Order(
            barista=order.get('barista'),
            hamburgers=[MongoDBHamburgerHydration.hydrate(hamburger=hamburger)
                        for hamburger in order.get('hamburgers') if order.get('hamburgers')],
            chips=[MongoDBChipsHydration.hydrate(chips=chips)
                   for chips in order.get('chips') if order.get('chips')],
            drinks=[MongoDBDrinkHydration.hydrate(drink=drink)
                    for drink in order.get('drinks') if order.get('drinks')],
            price=order.get('price'),
            dt_created=order.get('dt_created'),
            is_ready=order.get('is_ready'),
            promotions=order.get('promotions'),
        )
