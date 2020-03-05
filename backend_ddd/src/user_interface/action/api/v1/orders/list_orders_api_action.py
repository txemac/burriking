from requests import Response

from application.interaction.transformer.list_orders_query_transformer import ListOrdersQueryTransformer
from application.presentation.normalizer.order_normalizer import OrderNormalizer
from infrastructure.user_interface import responder
from user_interface.api_action import ApiAction


class ListOrdersApiAction(ApiAction):

    def execution(
            self
    ) -> Response:
        server_request = self._get_server_request()

        query_list_orders = ListOrdersQueryTransformer().transform_request(request=server_request)
        query_response = self._service.execute(query_list_orders=query_list_orders)

        data = [OrderNormalizer.normalize(order=order) for order in query_response.data()]

        return responder.generate_get(data=data)
