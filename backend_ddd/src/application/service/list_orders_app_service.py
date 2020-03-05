from application.interaction.query.list_orders_query import ListOrdersQuery
from application.service.application_service import ApplicationService
from application.src.interaction.query.query_response import QueryResponse
from domain.model.repository.orders_reader_repository import OrdersReaderRepository


class ListOrdersAppService(ApplicationService):

    def __init__(
            self,
            orders_reader_repository: OrdersReaderRepository
    ):
        self._orders_reader_repository = orders_reader_repository

    def execute(
            self,
            query_list_orders: ListOrdersQuery
    ) -> QueryResponse:
        result = self._orders_reader_repository.list_orders(
            barista=query_list_orders.barista(),
            start_date=query_list_orders.start_date(),
            end_date=query_list_orders.end_date(),
        )

        return QueryResponse(
            data=result
        )
