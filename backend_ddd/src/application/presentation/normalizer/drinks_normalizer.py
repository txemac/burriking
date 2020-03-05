from typing import Dict
from typing import Union

from domain.model.drink import Drink


class DrinkNormalizer:

    @staticmethod
    def normalize(
            drink: Drink
    ) -> Dict[str, Union[str, int]]:
        return dict(
            type=drink.type(),
            price=drink.price(),
        )
