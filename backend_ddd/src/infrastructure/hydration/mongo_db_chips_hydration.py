from typing import Dict

from domain.model.chips import Chips


class MongoDBChipsHydration:

    @staticmethod
    def hydrate(
            chips: Dict
    ) -> Chips:
        return Chips(
            type=chips.get('type'),
            size=chips.get('size'),
            price=chips.get('price'),
        )
