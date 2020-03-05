from typing import Dict

from domain.model.meat import Meat


class MongoDBMeatHydration:

    @staticmethod
    def hydrate(
            meat: Dict
    ) -> Meat:
        return Meat(
            type=meat.get('type'),
            size=meat.get('size'),
            cooked=meat.get('cooked'),
            price=meat.get('price'),
        )
