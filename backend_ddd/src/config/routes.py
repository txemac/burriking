from flask import Blueprint

from config.di_container import container

api_orders_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1/orders')


@api_orders_v1.route(rule='', methods=['POST'])
def add_order():
    return container.get('get_add_order_action').handle()


@api_orders_v1.route(rule='', methods=['GET'])
def get_orders():
    return container.get('get_list_orders_action').handle()
