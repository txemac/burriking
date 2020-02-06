import pytest
from pydantic import ValidationError

from database.schemas import BaristaPost


def test_barista_post_ok():
    assert BaristaPost(username='username') is not None


@pytest.mark.parametrize('username', ['a', None, 12, 'a' * 151])
def test_barista_post_username_wrong(username):
    with pytest.raises(ValidationError):
        BaristaPost(username=username)
