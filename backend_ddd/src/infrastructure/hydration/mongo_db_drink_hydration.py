from typing import Dict

from domain.model.drink import Drink


class MongoDBDrinkHydration:

    @staticmethod
    def hydrate(
            drink: Dict
    ) -> Drink:
        return Drink(
            type=drink.get('type'),
            price=drink.get('price'),
        )
