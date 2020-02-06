import pytest

from database import Barista
from database.schemas import BaristaPost


def test_create_ok(session):
    count1 = session.query(Barista).count()
    data = BaristaPost(
        username='test_create',
    )
    Barista.create(
        db_session=session,
        data=data
    )
    count2 = session.query(Barista).count()
    assert count1 + 1 == count2


def test_get_all_empty(session):
    assert len(Barista.get_all(db_session=session)) == 0


def test_get_all_ok(session, new_barista):
    assert len(Barista.get_all(db_session=session)) == 1


@pytest.mark.parametrize('username', [None, ''])
def test_get_by_username_wrong(session, username):
    assert Barista.get_by_username(db_session=session, username=username) is None


def test_get_by_username_ok(session, new_barista):
    assert Barista.get_by_username(db_session=session, username=new_barista.username) is not None
