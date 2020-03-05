from dependency_injector import containers
from dependency_injector import providers

from application.service.add_order_app_service import AddOrderAppService
from application.service.list_orders_app_service import ListOrdersAppService
from config.burriking_container import BurrikingContainer
from infrastructure.persistence import mongo_db
from infrastructure.persistence.mongo_db.repository.mongo_db_order_writer_repository import MongoDBOrderWriterRepository
from infrastructure.persistence.mongo_db.repository.mongo_db_orders_reader_repository import MongoDBOrdersReaderRepository
from user_interface.action.api.health import HealthAction
from user_interface.action.api.v1.orders.add_order_api_action import AddOrderApiAction
from user_interface.action.api.v1.orders.list_orders_api_action import ListOrdersApiAction


class RepositoryContainer(containers.DeclarativeContainer):
    order_writer_repository = providers.Factory(
        MongoDBOrderWriterRepository,
        collection=mongo_db.collection
    )
    order_reader_repository = providers.Factory(
        MongoDBOrdersReaderRepository,
        collection=mongo_db.collection
    )


class ServicesContainer(containers.DeclarativeContainer):
    get_add_order_service = providers.Factory(
        AddOrderAppService,
        order_write_repository=RepositoryContainer.order_writer_repository(),
    )
    get_list_orders_service = providers.Factory(
        ListOrdersAppService,
        orders_reader_repository=RepositoryContainer.order_reader_repository(),
    )


class ActionsContainer(containers.DeclarativeContainer):
    health_check_action = providers.Factory(
        HealthAction,
    )
    add_order_action = providers.Factory(
        AddOrderApiAction,
        service=ServicesContainer.get_add_order_service,
    )
    list_orders_action = providers.Factory(
        ListOrdersApiAction,
        service=ServicesContainer.get_list_orders_service,
    )


container = BurrikingContainer.get_instance()
container.bind('get_health_check_action', ActionsContainer.health_check_action())
container.bind('get_add_order_action', ActionsContainer.add_order_action())
container.bind('get_list_orders_action', ActionsContainer.list_orders_action())
