from typing import Dict

from domain.model.hamburger import Hamburger
from infrastructure.hydration.mongo_db_extra_cheese_hydration import MongoDBExtraCheeseHydration
from infrastructure.hydration.mongo_db_extra_tomato_hydration import MongoDBExtraTomatoHydration
from infrastructure.hydration.mongo_db_meat_hydration import MongoDBMeatHydration


class MongoDBHamburgerHydration:

    @staticmethod
    def hydrate(
            hamburger: Dict
    ) -> Hamburger:
        return Hamburger(
            bread_type=hamburger.get('bread_type'),
            meats=[MongoDBMeatHydration.hydrate(meat=meat)
                   for meat in hamburger.get('meats') if hamburger.get('meats')],
            extra_tomato=MongoDBExtraTomatoHydration.hydrate(extra_tomato=hamburger.get('extra_tomato')),
            extra_cheese=MongoDBExtraCheeseHydration.hydrate(extra_cheese=hamburger.get('extra_cheese')),
            price=hamburger.get('price'),
        )
