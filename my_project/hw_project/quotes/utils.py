from pymongo import MongoClient

def get_mongdb():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.hw
    return db