from typing import Dict

from domain.model.extra_cheese import ExtraCheese


class MongoDBExtraCheeseHydration:

    @staticmethod
    def hydrate(
            extra_cheese: Dict
    ) -> ExtraCheese:
        return ExtraCheese(
            type=extra_cheese.get('type'),
            price=extra_cheese.get('price'),
        )
