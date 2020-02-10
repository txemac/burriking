import os

from pymongo import MongoClient

_mongo_db_client = None


def _get_mongo_db_client():
    """
    Singleton to get a mongoDB client.

    :return MongoClient: client
    """
    global _mongo_db_client
    if _mongo_db_client is None:
        client = MongoClient(os.getenv('MONGODB_URL'))
        _mongo_db_client = client[os.getenv('MONGODB_DB_NAME')]
    return _mongo_db_client
