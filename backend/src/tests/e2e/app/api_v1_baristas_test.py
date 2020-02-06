from starlette.status import HTTP_200_OK


def test_get_baristas_empty(client):
    response = client.get("/api/v1/baristas/")
    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 0


def test_get_baristas_ok(client, new_barista):
    response = client.get("/api/v1/baristas/")
    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 1
    response_json = response.json()[0]
    assert response_json['username'] == new_barista.username
