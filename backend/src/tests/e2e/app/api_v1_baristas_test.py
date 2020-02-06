from starlette.status import HTTP_200_OK
from starlette.status import HTTP_201_CREATED
from starlette.status import HTTP_400_BAD_REQUEST

from app import messages


def test_get_baristas_empty(client):
    response = client.get("/api/v1/baristas/")
    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 0


def test_get_baristas_ok(client, new_barista, data_barista):
    response = client.get("/api/v1/baristas/")
    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 1
    response_json = response.json()[0]
    assert response_json['username'] == data_barista['username']


def test_post_barista_ok(client):
    data = dict(
        username='test',
    )
    response = client.post("/api/v1/baristas/", json=data)
    assert response.status_code == HTTP_201_CREATED


def test_post_barista_username_already_exists(client, new_barista, data_barista):
    response = client.post("/api/v1/baristas/", json=data_barista)
    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.json()['detail'] == messages.USERNAME_ALREADY_EXISTS
