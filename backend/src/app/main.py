from typing import Dict

from fastapi import FastAPI

from app.api_v1_baristas import api_v1_baristas
from database import Base
from database import engine

Base.metadata.create_all(bind=engine)


def create_app() -> FastAPI:
    app = FastAPI(title='Burriking API')

    app.include_router(api_v1_baristas, prefix='/api/v1/baristas', tags=['baristas'])

    return app


app = create_app()


@app.get('/_health', status_code=200)
def get_check() -> Dict:
    return dict(status='OK')
