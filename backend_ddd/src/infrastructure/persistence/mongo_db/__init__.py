import os

from pymongo import MongoClient

client = MongoClient(os.getenv('MONGODB_URL'))
mongo_db = client[os.getenv('MONGODB_DB_NAME')]
collection = mongo_db[os.getenv('MONGODB_COLLECTION')]
