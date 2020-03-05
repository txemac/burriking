from typing import Dict
from typing import Union

from domain.model.extra_cheese import ExtraCheese


class ExtraCheeseNormalizer:

    @staticmethod
    def normalize(
            extra_cheese: ExtraCheese
    ) -> Dict[str, Union[str, int]]:
        return dict(
            type=extra_cheese.type(),
            price=extra_cheese.price(),
        )
