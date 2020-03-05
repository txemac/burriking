from application.src.interaction.transformer.command_transformer import CommandTransformer
from domain.model.chips import Chips
from domain.model.drink import Drink
from domain.model.extra_cheese import ExtraCheese
from domain.model.extra_tomato import ExtraTomato
from domain.model.hamburger import Hamburger
from domain.model.meat import Meat
from domain.model.order import Order
from user_interface.server_request_interface import ServerRequestInterface


class AddOrderCommandTransformer(CommandTransformer):

    def transform_request(
            self,
            request: ServerRequestInterface
    ) -> Order:
        return Order(
            barista=request.parsed_body().get('barista'),
            hamburgers=[Hamburger(
                bread_type=hamburger.get('bread_type'),
                meats=[Meat(
                    type=meat.get('type'),
                    size=meat.get('size'),
                    cooked=meat.get('cooked'),
                ) for meat in hamburger.get('meats') if hamburger.get('meats')],
                extra_tomato=ExtraTomato(
                    type=hamburger.get('extra_tomato').get('type')
                    if (hamburger.get('extra_tomato') and hamburger.get('extra_tomato').get('type')) else None,
                    price=hamburger.get('extra_tomato').get('price')
                    if (hamburger.get('extra_tomato') and hamburger.get('extra_tomato').get('price')) else None,
                ),
                extra_cheese=ExtraCheese(
                    type=hamburger.get('extra_cheese').get('type')
                    if (hamburger.get('extra_cheese') and hamburger.get('extra_cheese').get('type')) else None,
                    price=hamburger.get('extra_cheese').get('price')
                    if (hamburger.get('extra_cheese') and hamburger.get('extra_cheese').get('price')) else None,
                ),
            ) for hamburger in request.parsed_body().get('hamburgers') if request.parsed_body().get('hamburgers')],
            chips=[Chips(
                type=chips.get('type'),
                size=chips.get('size'),
            ) for chips in request.parsed_body().get('chips') if request.parsed_body().get('chips')],
            drinks=[Drink(
                type=drink.get('type'),
            ) for drink in request.parsed_body().get('drinks') if request.parsed_body().get('drinks')],
        )
