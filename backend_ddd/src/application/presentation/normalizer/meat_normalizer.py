from typing import Dict
from typing import Union

from domain.model.meat import Meat


class MeatNormalizer:

    @staticmethod
    def normalize(
            meat: Meat
    ) -> Dict[str, Union[str, int]]:
        return dict(
            type=meat.type(),
            size=meat.size(),
            cooked=meat.cooked(),
            price=meat.price(),
        )
