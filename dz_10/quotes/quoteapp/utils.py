from pymongo import MongoClient

def get_mongodb():
    client = MongoClient("mongodb+srv://sturenko4:31122014@sturenko4.e02me8x.mongodb.net/?retryWrites=true&w=majority&appName=sturenko4")
    db = client.base
    return db