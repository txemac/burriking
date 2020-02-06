from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK

from database import Barista
from database import get_db
from database.schemas import BaristaGet

api_v1_baristas = APIRouter()


@api_v1_baristas.get('/', response_model=List[BaristaGet], status_code=HTTP_200_OK)
def get_baristas(
        db_session: Session = Depends(get_db)
) -> BaristaGet:
    return Barista.get_all(db_session=db_session)
