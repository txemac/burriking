from typing import Dict
from typing import Union

from domain.model.extra_tomato import ExtraTomato


class ExtraTomatoNormalizer:

    @staticmethod
    def normalize(
            extra_tomato: ExtraTomato
    ) -> Dict[str, Union[str, int]]:
        return dict(
            type=extra_tomato.type(),
            price=extra_tomato.price(),
        )
