from typing import Dict

from domain.model.extra_tomato import ExtraTomato


class MongoDBExtraTomatoHydration:

    @staticmethod
    def hydrate(
            extra_tomato: Dict
    ) -> ExtraTomato:
        return ExtraTomato(
            type=extra_tomato.get('type'),
            price=extra_tomato.get('price'),
        )
