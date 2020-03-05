from application.service.application_service import ApplicationService
from domain.model.order import Order
from domain.model.repository.order_writer_repository import OrderWriterRepository


class AddOrderAppService(ApplicationService):

    def __init__(
            self,
            order_write_repository: OrderWriterRepository
    ):
        self._order_write_repository = order_write_repository

    def execute(
            self,
            order: Order
    ) -> Order:
        return self._order_write_repository.add(order=order)
