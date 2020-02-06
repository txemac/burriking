from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK
from starlette.status import HTTP_201_CREATED
from starlette.status import HTTP_400_BAD_REQUEST

from app import messages
from database import Barista
from database import get_db
from database.schemas import BaristaGet
from database.schemas import BaristaPost

api_v1_baristas = APIRouter()


@api_v1_baristas.get('/', response_model=List[BaristaGet], status_code=HTTP_200_OK)
def get_baristas(
        db_session: Session = Depends(get_db)
) -> BaristaGet:
    return Barista.get_all(db_session=db_session)


@api_v1_baristas.post('/', response_model=BaristaGet, status_code=HTTP_201_CREATED)
def post_user(
        *,
        db_session: Session = Depends(get_db),
        data: BaristaPost
) -> BaristaGet:
    if Barista.get_by_username(db_session=db_session, username=data.username) is not None:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=messages.USERNAME_ALREADY_EXISTS)

    return Barista.create(db_session=db_session, data=data)
