import os

import pytest
from starlette.testclient import TestClient

from app.main import app
from database import mongo_db_client


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture
def mongodb_drop():
    mongo_db_client._get_mongo_db_client().drop_collection(name_or_collection=os.getenv('MONGODB_COLLECTION_TEST'))
