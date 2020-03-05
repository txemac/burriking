from typing import Dict

from flask import Flask

from config import routes
from config.di_container import container


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(routes.api_orders_v1)

    return app


app = create_app()


@app.route(rule='/_health')
def get_health() -> Dict:
    return container.get('get_health_check_action').handle()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
