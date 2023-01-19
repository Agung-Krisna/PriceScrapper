from pymongo import MongoClient

def connectToDb(url="mongodb://202.83.122.66:33611/", db_name = "agungsurya", collection_name = "items"):
    client = MongoClient(url)
    db = client[db_name]
    collection = db[collection_name]
    return collection

def insertToCollection(data: dict):
    collection = connectToDb()
    collection.insert_one(data)