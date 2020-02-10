from database import mongo_db_client


def test_get_mongo_db_client():
    assert mongo_db_client._get_mongo_db_client() is not None
