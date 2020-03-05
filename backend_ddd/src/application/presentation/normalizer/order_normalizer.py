from typing import Dict
from typing import Union

from application.presentation.normalizer.chips_normalizer import ChipsNormalizer
from application.presentation.normalizer.drinks_normalizer import DrinkNormalizer
from application.presentation.normalizer.hamburger_normalizer import HamburgerNormalizer
from domain.model.order import Order


class OrderNormalizer:

    @staticmethod
    def normalize(
            order: Order
    ) -> Dict[str, Union[str, int]]:
        return dict(
            barista=order.barista() or None,
            hamburgers=[HamburgerNormalizer.normalize(hamburger=hamburger) for hamburger in order.hamburgers()],
            chips=[ChipsNormalizer.normalize(chips=chips) for chips in order.chips()],
            drinks=[DrinkNormalizer.normalize(drink=drink) for drink in order.drinks()],
            price=order.price(),
            dt_created=order.dt_created(),
            is_ready=order.is_ready(),
            promotions=order.promotions(),
        )
