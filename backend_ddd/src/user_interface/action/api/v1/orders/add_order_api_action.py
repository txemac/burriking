from application.interaction.transformer.add_order_command_transformer import AddOrderCommandTransformer
from application.presentation.normalizer.order_normalizer import OrderNormalizer
from infrastructure.user_interface.responder import generate_post
from user_interface.api_action import ApiAction


class AddOrderApiAction(ApiAction):

    def execution(
            self
    ):
        server_request = self._get_server_request()

        command_add_order = AddOrderCommandTransformer().transform_request(request=server_request)

        result = self._service.execute(command_add_order)

        return generate_post(data=OrderNormalizer.normalize(order=result))
