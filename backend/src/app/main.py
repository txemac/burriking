from typing import Dict

from fastapi import FastAPI

from app.api_v1 import api_v1


def create_app() -> FastAPI:
    app = FastAPI(title='Burriking API')

    app.include_router(api_v1, prefix='/api/v1', tags=['burriking'])

    return app


app = create_app()


@app.get('/_health', status_code=200)
def get_check() -> Dict:
    return dict(status='OK')
