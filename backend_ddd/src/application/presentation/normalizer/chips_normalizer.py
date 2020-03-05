from typing import Dict
from typing import Union

from domain.model.chips import Chips


class ChipsNormalizer:

    @staticmethod
    def normalize(
            chips: Chips
    ) -> Dict[str, Union[str, int]]:
        return dict(
            type=chips.type(),
            size=chips.size(),
            price=chips.price(),
        )
