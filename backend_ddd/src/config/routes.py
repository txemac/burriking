from flask import Blueprint

from config.di_container import container

api_orders_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1/orders')


@api_orders_v1.route(rule='', methods=['POST'])
def add_order():
    """
    Add a new order.
    ---
    tags:
      - Orders
    definitions:
      Meat_add:
        type: object
        properties:
          type:
            description: type
            type: string
            example: wagyu
          size:
            description: size
            type: string
            example: 250g
          cooked:
            description: cooked
            type: string
            example: poco hecha
      Hamburger_add:
        type: object
        properties:
          bread_type:
            description: bread_type
            type: string
            example: chapata
          meats:
            description: meats
            type: array
            items:
              $ref: '#/definitions/Meat_add'
          extra_tomato:
            description: extra_tomato
            type: object
            properties:
              type:
                description: type
                type: string
                example: cherry
          extra_cheese:
            description: extra_cheese
            type: object
            properties:
              type:
                description: type
                type: string
                example: cheddar
      Drink_add:
        type: object
        properties:
          type:
            description: type
            type: string
            example: burricola
      Chips_add:
        type: object
        properties:
          type:
            description: type
            type: string
            example: deluxe
          size:
            description: size
            type: string
            example: grandes
    parameters:
      - name: barista
        description: barista
        in: body
        required: true
        type: string
        example: txema
      - name: hamburgers
        description: list of hamburgers
        in: body
        required: true
        type: array
        items:
          $ref: '#/definitions/Hamburger_add'
      - name: drinks
        description: drinks
        in: body
        required: true
        type: array
        items:
          $ref: '#/definitions/Drink_add'
      - name: chips
        description: chips
        in: body
        required: true
        type: array
        items:
          $ref: '#/definitions/Chips_add'
    responses:
      200:
        description: orders details
        schema:
          type: object
          properties:
            status:
              description: status with text
              type: object
              properties:
                text:
                  description: message of the status
                  type: string
                  example: ok.
            meta:
              description: meta
              type: object
              properties:
                page:
                  description: page
                  type: int
                  example: 1
                pages:
                  description: pages
                  type: int
                  example: 1
                results:
                  description: results
                  type: int
                  example: 10
                showing:
                  description: showing
                  type: int
                  example: 10
            data:
              description: orders detail
              type: array
              items:
                $ref: '#/definitions/Order_get'
    """
    return container.get('get_add_order_action').handle()


@api_orders_v1.route(rule='', methods=['GET'])
def get_orders():
    """
    Get orders.
    ---
    tags:
      - Orders
    definitions:
      Meat_get:
        type: object
        properties:
          type:
            description: type
            type: string
            example: wagyu
          size:
            description: size
            type: string
            example: 250g
          cooked:
            description: cooked
            type: string
            example: poco hecha
          price:
            description: price
            type: float
            example: 2.50
      Hamburger_get:
        type: object
        properties:
          bread_type:
            description: bread_type
            type: string
            example: chapata
          meats:
            description: meats
            type: array
            items:
              $ref: '#/definitions/Meat_get'
          extra_tomato:
            description: extra_tomato
            type: object
            properties:
              type:
                description: type
                type: string
                example: cherry
              price:
                description: price
                type: float
                example: 2.50
          extra_cheese:
            description: extra_cheese
            type: object
            properties:
              type:
                description: type
                type: string
                example: cheddar
              price:
                description: price
                type: float
                example: 3.50
          price:
            description: price
            type: float
            example: 3.50
      Drink_get:
        type: object
        properties:
          type:
            description: type
            type: string
            example: burricola
          price:
            description: price
            type: float
            example: 3.50
      Chips_get:
        type: object
        properties:
          type:
            description: type
            type: string
            example: burricola
          size:
            description: size
            type: string
            example: grandes
          price:
            description: price
            type: float
            example: 3.50
      Order_get:
        type: object
        properties:
          hamburgers:
            description: hamburgers
            type: array
            items:
              $ref: '#/definitions/Hamburger_get'
          chips:
            description: chips
            type: array
            items:
              $ref: '#/definitions/Chips_get'
          drinks:
            description: drinks
            type: array
            items:
              $ref: '#/definitions/Drink_get'
          promotions:
            description: promotions
            type: array
            items:
              type: string
              example: burrimenu
          price:
            description: price
            type: float
            example: 14.50
    parameters:
      - name: barista
        description: barista
        in: query
        required: false
        type: string
        example: txema
      - name: start_date
        description: start date
        in: query
        required: false
        type: string
        example: 2019-01-25
      - name: end_date
        description: end date
        in: query
        required: false
        type: string
        example: 2019-01-25
    responses:
      201:
        description: orders details
        schema:
          type: object
          properties:
            status:
              description: status with text
              type: object
              properties:
                text:
                  description: message of the status
                  type: string
                  example: ok.
            meta:
              description: meta
              type: object
              properties:
                page:
                  description: page
                  type: int
                  example: 1
                pages:
                  description: pages
                  type: int
                  example: 1
                results:
                  description: results
                  type: int
                  example: 10
                showing:
                  description: showing
                  type: int
                  example: 10
            data:
              description: orders detail
              type: array
              items:
                $ref: '#/definitions/Order_get'
    """
    return container.get('get_list_orders_action').handle()
