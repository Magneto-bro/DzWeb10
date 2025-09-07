import json
from bson.objectid import ObjectId
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.hw

with open(r'my_project\utils\quotes.json', 'r',encoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname':quote['author']})
    if author:
        db.quotes.insert_one({
            'quote':quote['quote'],
            'tags':quote['tags'],
            'author':ObjectId(author['_id'])
        })
print("готово")
print(client.list_database_names())  # перевір бази
print(db.list_collection_names()) 
a = db.authors.find_one()
print(a)
print(db.command("usersInfo")) 
