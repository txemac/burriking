from typing import Dict
from typing import List
from typing import Union

from application.presentation.normalizer.extra_cheese_normalizer import ExtraCheeseNormalizer
from application.presentation.normalizer.extra_tomato_normalizer import ExtraTomatoNormalizer
from application.presentation.normalizer.meat_normalizer import MeatNormalizer
from domain.model.extra_cheese import ExtraCheese
from domain.model.extra_tomato import ExtraTomato
from domain.model.hamburger import Hamburger
from domain.model.meat import Meat


class HamburgerNormalizer:

    @staticmethod
    def normalize(
            hamburger: Hamburger
    ) -> Dict[str, Union[str, float, List[Meat], ExtraTomato, ExtraCheese]]:
        return dict(
            bread_type=hamburger.bread_type(),
            meats=[MeatNormalizer.normalize(meat=meat) for meat in hamburger.meats()],
            extra_tomato=ExtraTomatoNormalizer.normalize(extra_tomato=hamburger.extra_tomato()),
            extra_cheese=ExtraCheeseNormalizer.normalize(extra_cheese=hamburger.extra_cheese()),
            price=hamburger.price(),
        )
