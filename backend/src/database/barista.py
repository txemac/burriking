from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import Session

import database
from database.schemas import BaristaPost


class Barista(database.Base):
    __tablename__ = "baristas"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    dt_created = Column(DateTime, default=func.now(), nullable=False)

    def __init__(
            self,
            username: str,
    ):
        self.username = username

    @classmethod
    def create(
            cls,
            db_session: Session,
            data: BaristaPost,
    ):
        """
        Create a new barista.

        :param Session db_session: database session
        :param BaristaPost data: data
        :return BaristaGet: barista
        """
        barista = Barista(username=data.username)

        db_session.add(barista)
        db_session.commit()
        db_session.refresh(barista)

        return barista

    @classmethod
    def get_all(
            cls,
            db_session: Session,
    ):
        """
        Get all.

        :param Session db_session: database session
        :return List[BaristaGet]: list of baristas
        """
        return db_session.query(Barista).all()

    @classmethod
    def get_by_username(
            cls,
            db_session: Session,
            username: str,
    ):
        """
        Get an barista by username.

        :param Session db_session: database session
        :param str username: username of the barista
        :return User: user
        """
        return db_session.query(cls).filter(Barista.username == username).first()
