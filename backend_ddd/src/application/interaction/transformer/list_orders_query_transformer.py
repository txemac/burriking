from application.interaction.query.list_orders_query import ListOrdersQuery
from application.src.interaction.transformer.query_transformer import QueryTransformer
from user_interface.server_request_interface import ServerRequestInterface


class ListOrdersQueryTransformer(QueryTransformer):

    def transform_request(
            self,
            request: ServerRequestInterface
    ) -> ListOrdersQuery:
        return ListOrdersQuery(
            barista=request.query_params().get('barista'),
            start_date=request.query_params().get('start_date'),
            end_date=request.query_params().get('end_date'),
        )
