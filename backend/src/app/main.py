from typing import Dict

from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(title='Burriking API')

    return app


app = create_app()


@app.get('/_health', status_code=200)
def get_check() -> Dict:
    return dict(status='OK')
